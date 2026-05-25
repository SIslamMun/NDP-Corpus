# Dataset A — clio-kit 3-tool surface (v2, schema-fixed)

This is the **v2** Dataset A after fixing a critical registry/API mismatch
discovered while end-to-end testing against the live NDP MCP server at
`http://155.101.6.191:8003`.

## What changed vs the v1 in `../A_clio_3tools/`

The v1 registry `ndp_tools_v3.json` used invented parameter names
(`search_terms`, `name_filter`, `dataset_identifier`, …) that don't exist on
the real NDP REST API. The trained model dutifully emitted those names — and
the live API rejected every `/search` call with HTTP 422.

The v2 registry `ndp_tools_v3_real.json` matches the actual OpenAPI:

| Tool | v2 params | API endpoint |
|---|---|---|
| `list_organizations` | `name`, `server` | `GET /organization` |
| `search_datasets`    | `terms` (array, required), `keys`, `server` | `GET /search` |
| `get_dataset_details`| `terms` (array, required), `server` | `GET /search` (no dedicated endpoint exists) |

`fix_dataset_A.py` migrates the 1004 audited v1 examples to the v2 schema by:
- renaming legacy params (`search_terms` → `terms`, `name_filter` → `name`, …)
- collapsing legacy fields into `terms` for searches (`dataset_name`, `dataset_title`,
  `dataset_description`, `owner_org`, `resource_*` all become `terms`)
- dropping non-existent params (`timestamp`, `limit`, `filter_list`, `identifier_type`)
- coercing string `terms` to array
- regex-fixing chain-of-thought text so the assistant reasoning uses the new names

Result: 1003/1004 examples survived migration (1 dropped because `filter_list`
was its only arg — no `terms` left after migration).

## Files

| File | Purpose |
|---|---|
| `ndp_tools_v3_real.json` | Corrected 3-tool registry matching the live API |
| `tool_examples_audited_fixed.json` | 1003 migrated training examples |
| `tool_train_functiongemma.jsonl`   | Re-prep'd JSONL (native-list messages + tools field) |
| `fix_dataset_A.py`     | The migration script |
| `probe_via_ollama.py`  | Real-NDP probe for ollama-served models (Qwen3) |
| `probe_fg_direct.py`   | Real-NDP probe for transformers-direct models (FunctionGemma) |
| `mcp_probe_*.json`     | Per-prompt probe traces for each model |
| `mcp_probe_summary.json` | Score summary |
| `ndp-*.Modelfile`      | Ollama Modelfiles for each trained model |

## Trained models — real-NDP MCP probe scores (12 prompts)

| Model | v1 raw | v1 + 3 fixes | v2 (this) |
|---|---:|---:|---:|
| Qwen3-4B-Instruct-2507 | 5/12 (42%) | 8/12 (67%, with shim) | **10/12 (83%)** |
| FunctionGemma-270M     | 3/12 (25%) | — | **7/12 (58%)** |

The "3 fixes" stack on v1 was: (a) training-time system prompt at inference,
(b) server-side null/cross-tool arg sanitization, (c) registry→API name shim.
v2 builds those fixes into the data itself so the shim is no longer needed.

## Remaining failure modes

**Qwen3 (2 fails):** over-eager refusal handling — "Create a new org X" and
"Rename org Y" both call `list_organizations` instead of refusing. HTTP 200,
semantically wrong but operationally safe (read where write was asked).

**FunctionGemma (5 fails):** 4 over-eager refusals (same pattern as Qwen3 plus
"weather in Tokyo" hallucination), 1 search call missing `terms` (model didn't
extract the query from "Search for CSV resources about wildfire risk owned by
usgs" — multi-keyword extraction is weak in 270M models).

## How to reproduce

```bash
# 1. Re-prep with the fixed registry
cp datasets/A_clio_3tools_v2/tool_examples_audited_fixed.json \
   example/datasets/A_clio_3tools/data/tool_examples_clean.json
uv run python -m generator.cli train-tool \
    -c example/configs/dataset_A_3tools.yaml --only prep-tool \
    --tools datasets/A_clio_3tools_v2/ndp_tools_v3_real.json

# 2. Train Qwen3 (~14 min on A100-40GB)
$REPO/.venv-ft/bin/finetuner run --backend unsloth \
    --base-model unsloth/Qwen3-4B-Instruct-2507 \
    --dataset example/datasets/A_clio_3tools/data/tool_train_functiongemma.jsonl \
    -o example/datasets/A_clio_3tools/artifacts/qwen3_4b \
    --lora-rank 128 --lora-alpha 256 --epochs 3 --batch-size 4 --grad-accum 1 \
    --lr 1e-4 --max-seq-length 4096 --bf16 --save-merged

# 3. Train FunctionGemma (~5 min)
$REPO/.venv-ft/bin/finetuner run --backend unsloth \
    --base-model unsloth/functiongemma-270m-it \
    --dataset example/datasets/A_clio_3tools/data/tool_train_functiongemma.jsonl \
    -o example/datasets/A_clio_3tools/artifacts/functiongemma_270m \
    --lora-rank 64 --lora-alpha 128 --epochs 3 --batch-size 4 --grad-accum 2 \
    --lr 2e-4 --max-seq-length 4096 --bf16 --save-merged

# 4. Probe
python probe_via_ollama.py     # Qwen3 via ollama
python probe_fg_direct.py      # FunctionGemma via transformers
```
