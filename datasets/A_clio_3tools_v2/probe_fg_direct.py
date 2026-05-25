"""Probe FunctionGemma via transformers (apply_chat_template) — bypasses ollama
since ollama's gemma3 template doesn't render tools= in FunctionGemma's native
<start_function_declaration> format.

Same 12 prompts as probe_via_ollama.py. Same NDP REST forward at 155.101.6.191:8003.
"""
import json, re, time, sys, urllib.parse, urllib.request, urllib.error
from pathlib import Path
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

MERGED = Path('/home/cc/Phagocyte/example/datasets/A_clio_3tools/artifacts/functiongemma_270m/merged_16bit')
NDP    = 'http://155.101.6.191:8003'

REG = json.loads(Path('/home/cc/Phagocyte/example/configs/ndp_tools_v3_real.json').read_text())
VALID_TOOLS = {t['name'] for t in REG['tools']}
TOOL_PARAMS = {t['name']: {p['name'] for p in t.get('parameters', [])} for t in REG['tools']}
# Tools in HF format (apply_chat_template expects this)
HF_TOOLS = [{
    'type': 'function',
    'function': {
        'name': t['name'],
        'description': t['description'],
        'parameters': {
            'type': 'object',
            'properties': {p['name']: {'type': 'integer' if p.get('type') == 'integer' else 'string',
                                       'description': p.get('description','')} for p in t.get('parameters', [])},
            'required': [p['name'] for p in t.get('parameters', []) if p.get('required')]
        }
    }
} for t in REG['tools']]

PROMPTS = [
    ('single', 'list_organizations',  'List all organizations on the National Data Platform.'),
    ('single', 'search_datasets',     'Find datasets about ocean temperature on the global server, limit 5.'),
    ('single', 'get_dataset_details', 'Show me details for the dataset named "noaa-temperature-2024".'),
    ('single', 'list_organizations',  'Are there any NDP orgs with "biodiversity" in their name?'),
    ('single', 'search_datasets',     'Search for CSV resources about wildfire risk owned by usgs.'),
    ('multi',  'search_datasets',     'Find datasets about climate and then get full details for the first match.'),
    ('multi',  'list_organizations',  'List NDP orgs containing "noaa", then search their datasets about temperature.'),
    ('multi',  'search_datasets',     'Look up datasets about earthquake monitoring, then pull metadata for the most relevant one.'),
    ('refusal', None,                 'Delete the dataset "old-test-data" from the NDP catalog.'),
    ('refusal', None,                 'Create a new organization called "demo-org" on the platform.'),
    ('refusal', None,                 'What is the weather in Tokyo right now?'),
    ('refusal', None,                 'Rename the organization "noaa" to "noaa-archive".'),
]

# FunctionGemma emits tool calls as `<start_function_call>call:name{...args...}<end_function_call>` per its training.
TC_RE = re.compile(
    r'<start_function_call>\s*call:\s*(\w+)\s*(\{.*?\})\s*<end_function_call>',
    re.DOTALL,
)


_PAIR_RE = re.compile(r'^\s*([A-Za-z_]\w*)\s*:\s*(.+?)\s*$', re.DOTALL)


def _parse_fg_value(v: str):
    """Parse a single FG arg value (right-of-colon). Returns the python value or _PARSE_FAIL."""
    v = v.strip().rstrip(',')
    if not v:
        return _PARSE_FAIL
    # <escape>X<escape>
    m = re.match(r'^<escape>(.*?)<escape>$', v, re.DOTALL)
    if m:
        return m.group(1)
    if v in ('None', 'null'): return None
    if v in ('True', 'true'): return True
    if v in ('False', 'false'): return False
    # Number
    try: return int(v)
    except ValueError: pass
    try: return float(v)
    except ValueError: pass
    # Already quoted
    if (v.startswith('"') and v.endswith('"')) or (v.startswith("'") and v.endswith("'")):
        return v[1:-1]
    return _PARSE_FAIL


_PARSE_FAIL = object()


def _fg_args_to_dict(s: str) -> dict:
    """Resilient FunctionGemma args parser — split on commas, parse pairs
    individually, ignore malformed pairs (the model sometimes emits broken
    syntax like '  : value' from CoT-rewrite artifacts)."""
    if not s.startswith('{') or not s.endswith('}'):
        return {}
    body = s[1:-1].strip()
    if not body: return {}
    out = {}
    # Split on commas — but not commas INSIDE <escape>...<escape>.
    # Quick-and-dirty: replace <escape>X<escape> with placeholders, split, restore.
    placeholders = []
    def stash(m):
        placeholders.append(m.group(0))
        return f'\x00{len(placeholders)-1}\x00'
    body_p = re.sub(r'<escape>.*?<escape>', stash, body, flags=re.DOTALL)
    for chunk in body_p.split(','):
        if '\x00' in chunk:
            chunk = re.sub(r'\x00(\d+)\x00', lambda m: placeholders[int(m.group(1))], chunk)
        m = _PAIR_RE.match(chunk)
        if not m: continue
        k = m.group(1); rhs = m.group(2)
        v = _parse_fg_value(rhs)
        if v is _PARSE_FAIL: continue
        # First occurrence wins (model occasionally repeats keys)
        if k not in out:
            out[k] = v
    return out


def parse_tool_calls(text: str):
    calls = []
    for m in TC_RE.finditer(text):
        name = m.group(1)
        raw = m.group(2)
        # Try JSON first, fall back to FunctionGemma syntax
        try: args = json.loads(raw)
        except Exception: args = _fg_args_to_dict(raw)
        calls.append({'name': name, 'args': args})
    return calls


def http_get(url, params=None, timeout=30):
    if params: url = url + '?' + urllib.parse.urlencode({k: v for k, v in params.items() if v is not None})
    try:
        with urllib.request.urlopen(urllib.request.Request(url), timeout=timeout) as r:
            return r.getcode(), r.read().decode('utf-8', errors='replace')[:300]
    except urllib.error.HTTPError as e:
        return e.code, e.read().decode('utf-8', errors='replace')[:300]
    except Exception as e:
        return 0, f'EXC: {e}'

def call_ndp(name, args):
    if name == 'list_organizations':
        return http_get(f'{NDP}/organization', {'name': args.get('name'), 'server': args.get('server','global')})
    if name == 'search_datasets':
        terms = args.get('terms')
        if isinstance(terms, list): terms = ','.join(str(t) for t in terms)
        return http_get(f'{NDP}/search', {'terms': terms, 'keys': args.get('keys'), 'server': args.get('server','global')})
    if name == 'get_dataset_details':
        terms = args.get('terms')
        if isinstance(terms, list): terms = ','.join(str(t) for t in terms)
        return http_get(f'{NDP}/search', {'terms': terms, 'server': args.get('server','global')})
    return 404, 'UNKNOWN_TOOL'


def score(kind, expected, calls, text):
    names = [c['name'] for c in calls]
    tool_ok = all(n in VALID_TOOLS for n in names) if names else True
    args_ok = True
    exec_results = []
    for c in calls:
        if c['name'] not in TOOL_PARAMS:
            args_ok = False
            exec_results.append({'name': c['name'], 'args': c['args'], 'code': None, 'reason': 'bad tool'})
            continue
        # SANITIZE: drop nulls + cross-tool keys before hitting the API.
        cleaned = {k: v for k, v in c['args'].items()
                   if k in TOOL_PARAMS[c['name']] and v is not None and v != '' and v != 'null'}
        dropped = sorted(set(c['args'].keys()) - set(cleaned.keys()))
        code, body = call_ndp(c['name'], cleaned)
        exec_results.append({'name': c['name'], 'args_raw': c['args'], 'args_cleaned': cleaned,
                             'dropped': dropped, 'code': code, 'body_head': body[:200]})
        if code >= 400 or code == 0:
            args_ok = False
    if kind == 'refusal':
        intent = (len(calls) == 0)
    elif kind == 'single':
        intent = bool(names) and names[0] == expected
    else:
        intent = expected in names
    return {'ok': (tool_ok and args_ok or kind == 'refusal') and intent,
            'tool_ok': tool_ok, 'args_ok': args_ok, 'intent': intent,
            'calls': calls, 'exec': exec_results,
            'text_preview': text[:300]}


def main():
    print(f'loading {MERGED} ...', flush=True)
    t0 = time.time()
    tok = AutoTokenizer.from_pretrained(str(MERGED), trust_remote_code=True)
    if tok.pad_token is None: tok.pad_token = tok.eos_token
    model = AutoModelForCausalLM.from_pretrained(str(MERGED), torch_dtype=torch.bfloat16, device_map='cuda', trust_remote_code=True)
    model.eval()
    print(f'  loaded in {time.time()-t0:.1f}s — {sum(p.numel() for p in model.parameters())/1e6:.0f}M params')

    rows = []
    n_pass = 0
    for i, (kind, expected, prompt) in enumerate(PROMPTS):
        messages = [
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
        ]
        try:
            text_in = tok.apply_chat_template(messages, tools=HF_TOOLS, add_generation_prompt=True, tokenize=False)
        except Exception as e:
            print(f'  [{i+1}] template error: {e}')
            rows.append({'kind':kind,'expected':expected,'prompt':prompt,'error':str(e),'pass':False})
            continue
        inputs = tok(text_in, return_tensors='pt').to('cuda')
        with torch.no_grad():
            out = model.generate(**inputs, max_new_tokens=400, do_sample=False, pad_token_id=tok.pad_token_id)
        gen = tok.decode(out[0][inputs['input_ids'].shape[1]:], skip_special_tokens=False)
        calls = parse_tool_calls(gen)
        s = score(kind, expected, calls, gen)
        rows.append({'kind': kind, 'expected': expected, 'prompt': prompt, 'generated': gen[:600], **s})
        if s['ok']: n_pass += 1
        mark = '✓' if s['ok'] else '✗'
        called = ','.join(c['name'] for c in calls) or '(no call)'
        print(f'  [{i+1:2d}] {mark} {kind:7s} exp={expected!s:25s} got={called:30s}')

    pct = n_pass / len(PROMPTS) * 100
    print(f'\nSCORE: {n_pass}/{len(PROMPTS)} ({pct:.0f}%)')
    out = Path('/tmp/mcp_probe_functiongemma.json')
    out.write_text(json.dumps({'model':'functiongemma_270m','n_pass':n_pass,'n_total':len(PROMPTS),'rows':rows}, indent=2, ensure_ascii=False))
    print(f'full → {out}')


if __name__ == '__main__':
    main()
