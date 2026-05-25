"""Migrate Dataset A's audited tool calls to match the REAL NDP MCP API at
http://155.101.6.191:8003. The original `ndp_tools_v3.json` used invented
parameter names (`search_terms`, `name_filter`, ...) that don't exist on the
live API. This script rewrites every training example's tool calls + tools
field + CoT text to use the real names, so a model trained on the result
needs no inference-time shim.

Run after this:
  cp tool_examples_audited_fixed.json tool_examples_clean.json
  uv run python -m generator.cli train-tool -c example/configs/dataset_A_3tools.yaml --only prep-tool
  # then retrain.
"""
from __future__ import annotations
import json, re, copy
from pathlib import Path
from collections import Counter

DATA = Path('/home/cc/Phagocyte/example/datasets/A_clio_3tools/data')
AUDITED = DATA / 'tool_examples_audited.json'
FIXED   = DATA / 'tool_examples_audited_fixed.json'
REAL_REG = Path('/home/cc/Phagocyte/example/configs/ndp_tools_v3_real.json')

# Real-API tool schema (matched against /openapi.json from 155.101.6.191:8003)
NEW_TOOLS = [
    {
        'name': 'list_organizations',
        'description': 'List organizations on the NDP catalog. Returns organization names.',
        'parameters': [
            {'name': 'name',   'type': 'string', 'description': 'Substring filter on organization name', 'required': False},
            {'name': 'server', 'type': 'string', 'description': "Server scope: 'local', 'global', or 'pre_ckan'", 'required': False},
        ],
    },
    {
        'name': 'search_datasets',
        'description': 'Search NDP datasets by free-text terms (returns matching datasets with metadata).',
        'parameters': [
            {'name': 'terms',  'type': 'array',  'description': 'Search terms — list of strings combined as OR-search', 'required': True},
            {'name': 'keys',   'type': 'string', 'description': "Optional field-restriction spec (comma-separated field names)", 'required': False},
            {'name': 'server', 'type': 'string', 'description': "Server: 'local' or 'global'", 'required': False},
        ],
    },
    {
        'name': 'get_dataset_details',
        'description': 'Look up a specific dataset by exact name or id (returns dataset metadata + resources). Uses the catalog search backend.',
        'parameters': [
            {'name': 'terms',  'type': 'array',  'description': 'Single-element array containing the dataset name or id', 'required': True},
            {'name': 'server', 'type': 'string', 'description': "Server: 'local' or 'global'", 'required': False},
        ],
    },
]
NEW_PARAMS = {t['name']: {p['name'] for p in t['parameters']} for t in NEW_TOOLS}

# Per-tool migration rules
MIGRATIONS = {
    'search_datasets': {
        # rename → new key
        'rename': {
            'search_terms': 'terms',
            'search_term':  'terms',
            'search_keys':  'keys',
            'filter_list':  'keys',
            # these all collapse to terms (search text)
            'dataset_name':         'terms',
            'dataset_title':        'terms',
            'dataset_description':  'terms',
            'resource_name':        'terms',
            'resource_description': 'terms',
            'resource_url':         'terms',
            'owner_org':            'terms',
            'resource_format':      'terms',
            'timestamp':            None,   # drop (not supported)
            'limit':                None,   # drop (not supported by /search)
        },
        'array_args': {'terms'},
        'required':   {'terms'},
    },
    'list_organizations': {
        'rename': {'name_filter': 'name'},
        'array_args': set(),
        'required':   set(),
    },
    'get_dataset_details': {
        'rename': {
            'dataset_identifier': 'terms',
            'identifier_type':    None,   # drop — single combined search field
            'name':               'terms',
            'id':                 'terms',
            'dataset_name':       'terms',
        },
        'array_args': {'terms'},
        'required':   {'terms'},
    },
}

# CoT text replacements — keep model's reasoning in sync with renamed args
COT_TEXT_REPLACEMENTS = [
    (r'\bsearch_terms?\b',    'terms'),
    (r'\bsearch_keys\b',      'keys'),
    (r'\bname_filter\b',      'name'),
    (r'\bdataset_identifier\b', 'terms'),
    (r'\bidentifier_type\b',  ''),
    (r'\bfilter_list\b',      'keys'),
]


def migrate_args(tool: str, args: dict) -> dict | None:
    """Apply the per-tool migration. Returns new args dict or None to drop the step."""
    spec = MIGRATIONS[tool]
    rename = spec['rename']
    keep = NEW_PARAMS[tool]
    new = {}
    for k, v in args.items():
        # Rename
        new_k = rename.get(k, k)
        if new_k is None:
            continue  # explicitly dropped
        if new_k not in keep:
            continue  # not in real schema — drop
        # Merge into existing (e.g. multiple legacy fields collapse to 'terms')
        if new_k in new:
            if new_k in spec['array_args']:
                # Combine as list
                existing = new[new_k] if isinstance(new[new_k], list) else [new[new_k]]
                addition = v if isinstance(v, list) else [v]
                new[new_k] = existing + [x for x in addition if x not in existing]
            # else: keep first occurrence
        else:
            new[new_k] = v
    # Coerce array args
    for arg in spec['array_args']:
        if arg in new:
            if not isinstance(new[arg], list):
                new[arg] = [new[arg]]
            new[arg] = [str(x) for x in new[arg] if x is not None and x != '']
    # Drop step if required missing
    if spec['required'] - set(new.keys()):
        return None
    return new


def fix_cot_text(s: str) -> str:
    if not isinstance(s, str): return s
    for pattern, repl in COT_TEXT_REPLACEMENTS:
        s = re.sub(pattern, repl, s)
    return s


def main():
    raw = json.loads(AUDITED.read_text())
    print(f'Input: {len(raw)} audited examples')

    fixed = []
    drops = Counter()
    drop_reasons = []
    for ex in raw:
        ex2 = copy.deepcopy(ex)
        sol = ex2['solution']
        rp = sol['reasoning_path']
        keep = True
        new_rp = []
        for step in rp:
            tool = step['tool']
            if tool not in MIGRATIONS:
                drops['unknown_tool'] += 1
                keep = False; break
            new_args = migrate_args(tool, step.get('args', {}))
            if new_args is None:
                drops['missing_required_after_migration'] += 1
                drop_reasons.append((ex2['instruction'][:60], step.get('args', {})))
                keep = False; break
            step['args'] = new_args
            # Fix CoT text in the step's thought
            if 'thought' in step:
                step['thought'] = fix_cot_text(step['thought'])
            new_rp.append(step)
        if keep:
            sol['reasoning_path'] = new_rp
            # Fix final_answer text too
            if 'final_answer' in sol:
                sol['final_answer'] = fix_cot_text(sol['final_answer'])
            fixed.append(ex2)
        else:
            drops['total_dropped_rows'] += 1

    print(f'\nFixed: {len(fixed)} / {len(raw)} examples')
    print(f'Drop reasons:')
    for k, n in drops.most_common():
        print(f'  {k}: {n}')
    if drop_reasons[:3]:
        print('\nSample drops:')
        for instr, args in drop_reasons[:3]:
            print(f'  {instr!r}: {args}')

    FIXED.write_text(json.dumps(fixed, indent=2, ensure_ascii=False))
    REAL_REG.write_text(json.dumps({'tools': NEW_TOOLS}, indent=2, ensure_ascii=False))
    print(f'\nWrote: {FIXED} ({FIXED.stat().st_size//1024} KB)')
    print(f'Wrote: {REAL_REG}')

    # Quick stats on fixed data
    tool_calls = Counter()
    for ex in fixed:
        for step in ex['solution']['reasoning_path']:
            tool_calls[step['tool']] += 1
    print(f'\nTool call distribution in fixed data:')
    for t, n in tool_calls.most_common():
        print(f'  {t}: {n}')


if __name__ == '__main__':
    main()
