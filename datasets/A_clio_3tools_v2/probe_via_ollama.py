"""Test each trained model via the local Ollama, with calls forwarded to
the LIVE NDP MCP REST API at http://155.101.6.191:8003.

For each model and each probe prompt:
  1. POST /api/chat to ollama with tools=[ndp 3-tool spec]
  2. Parse `message.tool_calls` from the response
  3. Map each tool call to the corresponding NDP REST endpoint and call it
  4. Score: tool_name_valid × args_validate_to_400-or-better × intent_ok

Outputs:
  /tmp/mcp_probe_<model>.json  — per-model full trace
  printed comparison table
"""
from __future__ import annotations
import json, time, sys, re, os
from pathlib import Path
import urllib.request, urllib.parse, urllib.error

OLLAMA = 'http://localhost:11434'
NDP    = 'http://155.101.6.191:8003'

VALID_TOOLS = {'list_organizations', 'search_datasets', 'get_dataset_details'}

REG = json.loads(Path('/home/cc/Phagocyte/example/configs/ndp_tools_v3_real.json').read_text())
TOOL_PARAMS = {t['name']: {p['name'] for p in t.get('parameters', [])} for t in REG['tools']}

# Tool definitions in Ollama tool-calling format (= OpenAI tools format)
TOOLS = [{
    'type': 'function',
    'function': {
        'name': t['name'],
        'description': t['description'],
        'parameters': {
            'type': 'object',
            'properties': {p['name']: {'type': p.get('type','string') if p.get('type') != 'integer' else 'integer', 'description': p.get('description','')} for p in t.get('parameters', [])},
            'required': [p['name'] for p in t.get('parameters', []) if p.get('required')]
        }
    }
} for t in REG['tools']]

PROMPTS = [
    ('single',  'list_organizations',  'List all organizations on the National Data Platform.'),
    ('single',  'search_datasets',     'Find datasets about ocean temperature on the global server, limit 5.'),
    ('single',  'get_dataset_details', 'Show me details for the dataset named "noaa-temperature-2024".'),
    ('single',  'list_organizations',  'Are there any NDP orgs with "biodiversity" in their name?'),
    ('single',  'search_datasets',     'Search for CSV resources about wildfire risk owned by usgs.'),
    ('multi',   'search_datasets',     'Find datasets about climate and then get full details for the first match.'),
    ('multi',   'list_organizations',  'List NDP orgs containing "noaa", then search their datasets about temperature.'),
    ('multi',   'search_datasets',     'Look up datasets about earthquake monitoring, then pull metadata for the most relevant one.'),
    ('refusal', None,                  'Delete the dataset "old-test-data" from the NDP catalog.'),
    ('refusal', None,                  'Create a new organization called "demo-org" on the platform.'),
    ('refusal', None,                  'What is the weather in Tokyo right now?'),
    ('refusal', None,                  'Rename the organization "noaa" to "noaa-archive".'),
]


def http_post(url: str, body: dict, timeout=120) -> dict:
    data = json.dumps(body).encode('utf-8')
    req = urllib.request.Request(url, data=data, headers={'Content-Type': 'application/json'})
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return json.loads(r.read())


def http_get(url: str, params: dict | None = None, timeout=30):
    if params:
        url = url + '?' + urllib.parse.urlencode({k: v for k, v in params.items() if v is not None})
    try:
        req = urllib.request.Request(url)
        with urllib.request.urlopen(req, timeout=timeout) as r:
            return r.getcode(), r.read().decode('utf-8', errors='replace')[:500]
    except urllib.error.HTTPError as e:
        return e.code, e.read().decode('utf-8', errors='replace')[:500]
    except Exception as e:
        return 0, f'EXCEPTION: {e}'


def call_ndp(name: str, args: dict) -> tuple[int, str]:
    """Forward a model tool call to the real NDP REST API. NO shim — the model
    is expected to emit the real-API names (terms/keys/name/server) directly
    after training on the fixed schema (ndp_tools_v3_real.json)."""
    if name == 'list_organizations':
        params = {'name': args.get('name'), 'server': args.get('server', 'global')}
        return http_get(f'{NDP}/organization', params)
    if name == 'search_datasets':
        terms = args.get('terms')
        if isinstance(terms, list):
            terms = ','.join(str(t) for t in terms)
        params = {'terms': terms, 'keys': args.get('keys'), 'server': args.get('server', 'global')}
        return http_get(f'{NDP}/search', params)
    if name == 'get_dataset_details':
        # The fixed schema collapses dataset_identifier into `terms`; route via /search
        terms = args.get('terms')
        if isinstance(terms, list):
            terms = ','.join(str(t) for t in terms)
        params = {'terms': terms, 'server': args.get('server', 'global')}
        return http_get(f'{NDP}/search', params)
    return 404, f'UNKNOWN_TOOL: {name}'


def call_model(model_name: str, prompt: str) -> dict:
    body = {
        'model': model_name,
        'messages': [
            # MATCH the training-time system prompt verbatim (anti arg-spam + refusal discipline)
            {'role': 'system', 'content': (
                "You are an AI assistant with access to a set of tools (function calls). "
                "When the user asks for something a tool can do, call the appropriate tool with "
                "valid arguments. Think step-by-step inside <think>...</think> tags before "
                "producing the tool call, then summarise the result for the user in plain language. "
                "If no tool fits, say so politely instead of fabricating a call.\n\n"
                "Tool-call discipline:\n"
                "- ONLY include parameters that you are actually setting to a value.\n"
                "- NEVER include parameters whose value would be None, null, empty string, or unset.\n"
                "- NEVER invent parameter names that are not in the tool's schema.\n"
                "- If a parameter is optional and you're not using it, OMIT IT ENTIRELY (do not emit it with a None placeholder)."
            )},
            {'role': 'user', 'content': prompt},
        ],
        'tools': TOOLS,
        'stream': False,
        'options': {'temperature': 0.0},
    }
    try:
        r = http_post(f'{OLLAMA}/api/chat', body, timeout=180)
        return r.get('message', {})
    except Exception as e:
        return {'error': str(e)}


def score(kind: str, expected: str | None, message: dict) -> dict:
    if 'error' in message:
        return {'ok': False, 'reason': f'ollama error: {message["error"]}',
                'intent_ok': False, 'all_valid': False, 'tool_calls': [], 'exec': [],
                'text_preview': ''}
    tool_calls = message.get('tool_calls', []) or []
    text = message.get('content', '') or ''

    # Validate tool names + args + execute via real NDP
    exec_results = []
    names_called = []
    all_valid = True
    for tc in tool_calls:
        fn = tc.get('function', {})
        name = fn.get('name')
        args = fn.get('arguments', {}) or {}
        if isinstance(args, str):
            try: args = json.loads(args)
            except Exception: args = {}
        names_called.append(name)
        if name not in VALID_TOOLS:
            all_valid = False
            exec_results.append({'name': name, 'args': args, 'code': None, 'reason': 'hallucinated tool name'})
            continue
        # SANITIZE the model's args: drop null / empty / cross-tool keys before
        # hitting the API. This isolates "did the model know what to call?"
        # from "did the model produce clean args?".
        cleaned = {k: v for k, v in args.items()
                   if k in TOOL_PARAMS[name] and v is not None and v != '' and v != 'null'}
        dropped_keys = sorted(set(args.keys()) - set(cleaned.keys()))
        code, body = call_ndp(name, cleaned)
        exec_results.append({'name': name, 'args_raw': args, 'args_cleaned': cleaned,
                             'dropped': dropped_keys, 'code': code, 'body_head': body[:200]})
        if code >= 400 or code == 0:
            all_valid = False
        exec_results.append({'name': name, 'args': args, 'code': code, 'body_head': body[:200]})
        if code >= 400 or code == 0:
            all_valid = False

    if kind == 'refusal':
        intent_ok = (len(tool_calls) == 0)
    elif kind == 'single':
        intent_ok = (len(names_called) >= 1 and names_called[0] == expected)
    else:  # multi
        intent_ok = (len(names_called) >= 1 and any(n == expected for n in names_called))

    pass_overall = (all_valid or kind == 'refusal') and intent_ok
    return {'ok': pass_overall, 'intent_ok': intent_ok, 'all_valid': all_valid,
            'tool_calls': names_called, 'exec': exec_results,
            'text_preview': text[:300] if text else ''}


def probe(model_name: str) -> dict:
    print(f'\n{"="*70}\n  PROBE: {model_name}\n{"="*70}', flush=True)
    rows = []
    n_pass = 0
    t0 = time.time()
    for i, (kind, expected, prompt) in enumerate(PROMPTS):
        msg = call_model(model_name, prompt)
        s = score(kind, expected, msg)
        rows.append({'kind': kind, 'expected': expected, 'prompt': prompt, 'message': msg, **s})
        if s['ok']: n_pass += 1
        marker = '✓' if s['ok'] else '✗'
        called = ','.join(s['tool_calls']) or '(no call)'
        print(f'  [{i+1:2d}] {marker} {kind:7s} exp={expected!s:25s} got={called:50s}', flush=True)
    wall = time.time() - t0
    pct = n_pass / len(PROMPTS) * 100
    print(f'\n  SCORE: {n_pass}/{len(PROMPTS)} = {pct:.0f}%   wall={wall:.0f}s', flush=True)
    out = Path(f'/tmp/mcp_probe_{model_name.replace("/","_")}.json')
    out.write_text(json.dumps({'model': model_name, 'n_pass': n_pass, 'n_total': len(PROMPTS),
                                'wall_s': wall, 'rows': rows}, indent=2, ensure_ascii=False))
    print(f'  full → {out}', flush=True)
    return {'model': model_name, 'n_pass': n_pass, 'n_total': len(PROMPTS), 'wall_s': wall}


def main():
    # Find the loaded ollama models
    import urllib.request
    with urllib.request.urlopen(f'{OLLAMA}/api/tags') as r:
        models = [m['name'] for m in json.load(r)['models']]
    targets = [m for m in models if m.startswith('ndp-')]
    print(f'targets in ollama: {targets}')
    if not targets:
        print('NO ndp-* MODELS LOADED — run load_to_ollama.sh first'); sys.exit(2)

    summary = []
    for m in targets:
        try:
            summary.append(probe(m))
        except Exception as e:
            import traceback; traceback.print_exc()
            summary.append({'model': m, 'error': str(e)})

    print('\n' + '═'*70)
    print('  COMPARISON — Dataset A trained models, probed via real NDP MCP')
    print('═'*70)
    print(f'{"model":<28s} {"score":>14s} {"wall":>10s}')
    for r in summary:
        if 'error' in r:
            print(f'{r["model"]:<28s} ERROR  {r["error"][:50]}')
        else:
            print(f'{r["model"]:<28s} {r["n_pass"]:>3d}/{r["n_total"]:<2d} ({100*r["n_pass"]/r["n_total"]:>4.0f}%) {r["wall_s"]:>8.0f}s')
    print('═'*70)
    Path('/tmp/mcp_probe_summary.json').write_text(json.dumps(summary, indent=2))


if __name__ == '__main__':
    main()
