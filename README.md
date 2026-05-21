# Phagocyte example corpus + LanceDB

A working slice of the **NDP3 finetune run** — useful for smoke-testing
Phase 5 / 6 (generate + train) without re-running phases 1-4 from scratch.

| Folder | Contents |
|---|---|
| `ndp_docs/` | 39 source dirs — GitHub repo dumps + DataSpaces/SciDX website pages + 2 academic PDFs + 2 OpenAPI specs + the Phase 1 synthesis report. Post-cleanup (md_clean ran). |
| `lancedb/` | The LanceDB Phase 4 output: 1,281 text + 2,678 code + 182 image chunks. Use directly as `--lancedb ./example/lancedb` in any `phagocyte generate …` command. |

Total: ~58 MB.

## Source inventory + provenance

See [`NDP_CORPUS_INVENTORY.md`](NDP_CORPUS_INVENTORY.md) for the full
per-source breakdown — repo URL, file count, type (docs / code / paper /
web), and chunk counts.

## Quick test using the example

```bash
# Generate refusal QA over 5 chunks (smoke test, no API key needed):
uv run phagocyte generate refusal ./example/lancedb \
    -o /tmp/refusal_smoke.json \
    --provider claude \
    --n-per-chunk 2 \
    --max-chunks 5

# Single-pass QA + CoT over the same:
uv run phagocyte generate cot ./example/lancedb \
    -o /tmp/qa_cot_smoke.json \
    --n-pairs 1 --max-chunks 10 \
    --provider claude
```
# NDP-Corpus
