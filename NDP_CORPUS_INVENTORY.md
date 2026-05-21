# NDP Training Corpus Inventory

**Phase 3 → Phase 4 — what got chunked for the NDP3 finetune run.**

Local path: `pipeline_output/NDP3_manual/phase3_ingestor.audit_run.clean/`

---

## At a glance

| | Value |
|---|---:|
| Source dirs | **39** |
| Text chunks (`text_chunks` table) | **1,281** |
| Code chunks (`code_chunks` table) | **2,678** |
| Image chunks (paper figures) | 182 |
| Total chunks | **4,141** |
| Total disk (clean tree) | ~36 MB |

Each source dir contributes one consolidated `<slug>.md` bundle (the
ingestor inlines upstream `.md` / `.ipynb` content with
`### path (N bytes)` separators) plus optionally a `source/` subdir
holding raw `.py` / `.js` / `.c` / `.yaml` / `.sh` files that are
chunked separately by the AST-aware code splitter.

---

## 1. GitHub repos — sci-ndp & national-data-platform orgs (19 dirs)

| Repo | Type | Files in bundle | Code files (source/) | Size | Text chunks | Code chunks | Source URL |
|---|---|---:|---|---:|---:|---:|---|
| `github_com_national-data-platform_ep-api` | API + docs + UI | 13 .md (README, CHANGELOG, 8× docs/*.md, ui/README, CODE_OF_CONDUCT, DOCKERHUB) | 235 .py + 25 .js + 2 yaml + 3 .sh | 2.8 MB | 313 | 1,269 | https://github.com/national-data-platform/ep-api |
| `github_com_national-data-platform_ndp-documentation` | Documentation | 33 docs/*.md (workspace/, education-hub/, policies/, welcome/, etc.) | 1 yaml | 96 KB | 138 | 0 | https://github.com/national-data-platform/ndp-documentation |
| `github_com_national-data-platform_ep-frontend` | React UI | 1 (README) | 20 .js (App, components, pages, services) | 348 KB | 7 | 510 | https://github.com/national-data-platform/ep-frontend |
| `github_com_national-data-platform_ndp` | Deployment | 2 (README + kubernetes/README) | — | 16 KB | 13 | 0 | https://github.com/national-data-platform/ndp |
| `github_com_national-data-platform_ndp-jupyterhub` | Workspace runtime | 3 (README + 2 sub-READMEs) | 9 .py | 244 KB | 16 | 86 | https://github.com/national-data-platform/ndp-jupyterhub |
| `github_com_national-data-platform_ckanext-ndp` | CKAN extension | 1 | 2 .py + 1 .js | 40 KB | 6 | 3 | https://github.com/national-data-platform/ckanext-ndp |
| `github_com_national-data-platform_ckanext-ndpcatalogadditions` | CKAN field schemas | 1 | 18 .py + 1 .js | 252 KB | 7 | 89 | https://github.com/national-data-platform/ckanext-ndpcatalogadditions |
| `github_com_national-data-platform_mlflow` | MLOps | 1 | 2 .py | 24 KB | 2 | 2 | https://github.com/national-data-platform/mlflow |
| `github_com_national-data-platform_ep-tutorials` | Tutorials | 10 (api/, frontend/, python/, examples/) | — (2 .ipynb auto-converted to MD) | 76 KB | 122 | 0 | https://github.com/national-data-platform/ep-tutorials |
| `github_com_national-data-platform_jupyter-notebooks` | Worked examples | 2 + 19 .ipynb (streaming/, earthscope/, sage/, nairr/, nasa/, pgml/, llm/, minimal/) | 27 .py | 460 KB | 163 | 88 | https://github.com/national-data-platform/jupyter-notebooks |
| `github_com_national-data-platform_ndp_clm_agents` | Agent notebooks | 1 + 3 .ipynb (`simple_clm_agent`, `enhanced_clm_agent`, `…_with_logfire`) | — | 80 KB | 55 | 0 | https://github.com/national-data-platform/ndp_clm_agents |
| `github_com_national-data-platform_ndp_clm_agent_demo` | Agent demo | 1 + 1 .ipynb | — | 56 KB | 29 | 0 | https://github.com/national-data-platform/ndp_clm_agent_demo |
| `github_com_sci-ndp_dspaces` | DataSpaces C library | 1 (README only) | 9 .py + 53 .c/.h + 1 yaml + 2 .sh | 896 KB | 26 | 274 | https://github.com/sci-ndp/dspaces |
| `github_com_sci-ndp_dspaces-api` | DataSpaces REST API | 7 (README + 6 docs/*.md) | 20 .py + 1 .sh | 152 KB | 30 | 27 | https://github.com/sci-ndp/dspaces-api |
| `github_com_sci-ndp_scidx-api` | SciDX REST API | 9 (README + 8 docs/*.md incl. tutorial) | 101 .py | 696 KB | 42 | 185 | https://github.com/sci-ndp/scidx-api |
| `github_com_sci-ndp_ndp-ep-py` | NDP-EP Python SDK | 3 (README + docs/README + CHANGELOG) | 45 .py + 1 yaml | 420 KB | 53 | 114 | https://github.com/sci-ndp/ndp-ep-py |
| `github_com_sci-ndp_ndp-ep-helm` | Helm chart | 1 (README) | 2 .py + 43 .yaml + 2 .sh | 376 KB | 49 | 17 | https://github.com/sci-ndp/ndp-ep-helm |
| `github_com_sci-ndp_keycloak-arch` | Auth architecture | 1 | — | 16 KB | 31 | 0 | https://github.com/sci-ndp/keycloak-arch |
| `github_com_sci-ndp_NDP-EP` | EP overview | 1 | 3 .sh | 56 KB | 15 | 14 | https://github.com/sci-ndp/NDP-EP |

**Subtotal**: 19 GitHub repos · 91 upstream `.md` docs + 24 `.ipynb` notebooks · 638 code files (Python / JS / C / YAML / Bash) · 1,117 text + 2,678 code chunks.

---

## 2. DataSpaces website (sci.utah.edu) — 5 dirs

All scraped from https://dataspaces.sci.utah.edu/ via the parser+ingestor pipeline.

| Page | Words | Size | Text chunks | Source URL |
|---|---:|---:|---:|---|
| `dataspaces_sci_utah_edu_overview` | 854 | 12 KB | 5 | https://dataspaces.sci.utah.edu/overview |
| `dataspaces_sci_utah_edu_manual` | 1,625 | 20 KB | 6 | https://dataspaces.sci.utah.edu/manual |
| `dataspaces_sci_utah_edu_faq` | 534 | 12 KB | 2 | https://dataspaces.sci.utah.edu/faq |
| `dataspaces_sci_utah_edu_research` | 1,167 | 16 KB | 2 | https://dataspaces.sci.utah.edu/research |
| `dataspaces_sci_utah_edu_download` | 629 | 12 KB | 3 | https://dataspaces.sci.utah.edu/download |

**Subtotal**: 5 docs · ~4,800 words · 18 text chunks.

---

## 3. SciDX website (sci.utah.edu) — 8 dirs

All scraped from https://scidx.sci.utah.edu/.

| Page | Type | Source URL |
|---|---|---|
| `scidx_sci_utah_edu` | Home | https://scidx.sci.utah.edu/ |
| `scidx_sci_utah_edu_data-pops` | Use case | https://scidx.sci.utah.edu/data-pops |
| `scidx_sci_utah_edu_data-staging` | Use case | https://scidx.sci.utah.edu/data-staging |
| `scidx_sci_utah_edu_data-streaming` | Use case | https://scidx.sci.utah.edu/data-streaming |
| `scidx_sci_utah_edu_earthscope-data-streaming` | Use case | https://scidx.sci.utah.edu/earthscope-data-streaming |
| `scidx_sci_utah_edu_noaa-data-staging` | Use case | https://scidx.sci.utah.edu/noaa-data-staging |
| `scidx_sci_utah_edu_on-demand-fakequakes` | Use case | https://scidx.sci.utah.edu/on-demand-fakequakes |
| `scidx_sci_utah_edu_sage-data-streaming` | Use case | https://scidx.sci.utah.edu/sage-data-streaming |

**Subtotal**: 8 docs · ~3,800 words · 48 text chunks.

---

## 4. OpenAPI specifications — 2 dirs

| Spec | Endpoints | Source URL |
|---|---:|---|
| `federation_ndp_utah_edu_openapi_json` | 19 (Health, NDP Configuration, Metrics) | https://federation.ndp.utah.edu/openapi.json |
| `test_federation_ndp_utah_edu_openapi_json` | 19 (mirror of test env) | https://test-federation.ndp.utah.edu/openapi.json |

**Subtotal**: 2 raw OpenAPI specs (28 KB each) · 2 text chunks (each spec → 1 mega-chunk because JSON).

---

## 5. Academic papers (PDF → md) — 2 dirs

| Paper | Words | Images | Source |
|---|---:|---:|---|
| `Gupta_2024_Bridging_eResearch_Infrastructure_and_Experimental_pdf` | 7,939 | 182 | Gupta, A. (2024). *Bridging eResearch Infrastructure and Experimental Materials Science Process in the Quantum Data Hub.* SDSC. |
| `Unknown_XXXX_The_National_Data_Platform_NDP_Democratizing_Data_pdf` | 2,010 | 0 | NSF NDP whitepaper (no formal cite — circulated 2024-2025). |

**Subtotal**: 2 papers · 9,949 words · 20 text chunks (after PDF section-injection cleanup).

---

## 6. Auto-included Phase 1 synthesis — 1 dir

| File | Words | Type | Origin |
|---|---:|---|---|
| `ndp_research_report` | 3,763 | Phase 1 synthesis | Auto-shipped from `phase1_research/research/research_report.md` (Gemini Deep Research output for "NDP National Data Platform") |

**Subtotal**: 1 doc · 40 text chunks (densely sectioned → many chunks).

---

## 7. Other websites — 2 dirs

| Page | Source URL |
|---|---|
| `ndp-test_sdsc_edu` | https://ndp-test.sdsc.edu/ (home + main content) |
| `democratizingdata_ai_tools_national-data-platform` | https://democratizingdata.ai/tools/national-data-platform/ |

**Subtotal**: 2 web pages · ~1,600 words · 36 text chunks.

---

## Type breakdown (all 39 dirs)

| Type | Dirs | Text chunks | Code chunks |
|---|---:|---:|---:|
| GitHub repos | 19 | 1,117 | 2,678 |
| DataSpaces website | 5 | 18 | 0 |
| SciDX website | 8 | 48 | 0 |
| Other websites | 2 | 36 | 0 |
| OpenAPI specs | 2 | 2 | 0 |
| Academic PDFs | 2 | 20 | 0 |
| Phase 1 synthesis | 1 | 40 | 0 |
| **TOTAL** | **39** | **1,281** | **2,678** |

---

## Cleanup history (for transparency)

| Stage | Dirs | Action |
|---|---:|---|
| Phase 3 ingest (raw) | 69 | Original ingestor output |
| After two-layer audit (heuristics + LLM judge) | 35 | 34 dirs quarantined for license noise, off-topic, broken React shells, junk content |
| After manual review (restored false positives + removed cross-file dups) | 29 | Restored `github_com_sci-ndp_scidx-api`; manually removed 4 known duplicates / overloaded-name pages / placeholders |
| + 10 additional repos pulled (Phase B) | 39 | Added `ndp`, `ndp_clm_agents`, `ndp_clm_agent_demo`, `ep-tutorials`, `ckanext-ndp`, `ckanext-ndpcatalogadditions`, `ep-frontend`, `ndp-jupyterhub`, `mlflow`, `jupyter-notebooks` |
| After `.md` preprocessor (`cleaning/md_clean.py`) | 39 | Stripped LICENSE / Repository-Info / Directory-Structure / bundled stopword files / banner lines; injected synthetic `## Section N` markers in headerless PDFs |
| After chunk-level filter (`cleaning/chunk_filter.py`) | 39 | Dropped tiny / banner / file-listing / license / stopword chunks (~485 text + 1 code) |
| **FINAL** | **39 dirs · 1,281 text + 2,678 code + 182 image chunks** | |

---

## Generated by

`uv run phagocyte ingest batch + audit + process run --text-profile high --code-profile high --table-mode separate --chunk-only`
followed by the `md_clean` + `chunk_filter` passes from `src/processor/src/processor/cleaning/`.

Inventory script: `phagocyte process stats <lancedb>` + ad-hoc `find` over the source tree.
