# NDP-Corpus

A pre-built training corpus for the **National Data Platform (NDP)** —
cleaned Markdown sources + a LanceDB vector store of pre-computed chunks.
Pulled from 19 GitHub repos (sci-ndp + national-data-platform orgs),
the DataSpaces / SciDX websites, two academic papers, two OpenAPI specs,
and a Phase 1 deep-research synthesis. ~58 MB total.

| Folder | Contents |
|---|---|
| `ndp_docs/` | 39 source dirs — GitHub repo dumps + DataSpaces / SciDX website pages + 2 academic PDFs + 2 OpenAPI specs + the Phase 1 synthesis report. Post-cleanup (license / boilerplate / banner stripping applied). |
| `lancedb/` | Phase-4 LanceDB output: 1,281 text + 2,678 code + 182 image chunks with full metadata (`section_path`, `title`, `symbol_name`, `token_count`). Drop-in for any tool that reads LanceDB. |

## Provenance

[`NDP_CORPUS_INVENTORY.md`](NDP_CORPUS_INVENTORY.md) lists every source
(repo / page / paper), file counts by type, sizes, upstream URLs, and
chunk counts. Generated during the NDP3 finetune run.

## Quick start with Phagocyte

These artifacts are the example data set bundled with
[grc-iit/Phagocyte](https://github.com/grc-iit/Phagocyte). Use them
directly to smoke-test Phase 5 generators or Phase 6 fine-tuning
without re-running phases 1–4:

```bash
# Refusal QA over 5 chunks (no API key with claude SDK):
uv run phagocyte generate refusal ./lancedb \
    -o /tmp/refusal_smoke.json --provider claude \
    --n-per-chunk 2 --max-chunks 5

# Single-pass QA + CoT:
uv run phagocyte generate cot ./lancedb \
    -o /tmp/qa_cot_smoke.json \
    --n-pairs 1 --max-chunks 10 --provider claude
```

## Standalone use

You don't need Phagocyte to use this corpus. Any tool that reads
LanceDB tables (`text_chunks`, `code_chunks`, `image_chunks`) works:

```python
import lancedb
db = lancedb.connect("./lancedb")
df = db.open_table("text_chunks").to_pandas()
print(f"{len(df)} chunks across "
      f"{df['source_file'].str.split('/').str[0].nunique()} sources")
```

## License

Each source has its own license — see the upstream repos / pages in
`NDP_CORPUS_INVENTORY.md`. This bundle is published for research and
fine-tuning use; respect each upstream's terms when redistributing.
