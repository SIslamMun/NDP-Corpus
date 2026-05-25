# Dataset B — extended 14-tool NDP MCP surface (v2 schema)

`ndp_tools_v14_real.json` is the 14-tool registry built directly from the
live OpenAPI at http://155.101.6.191:8003/openapi.json (NDP-EndPoint-DEMO).
Replaces the original `example/configs/ndp_tools_v14.json` which used
invented parameter names (same registry-defect class as v3 → v3_real).

## Tools (14, real-API aligned)

**Reads (8):**
- `get_dataset_details` — emulated via `GET /search` (no `/dataset/{id}` GET endpoint)
- `get_jupyter_details` — `GET /status/jupyter` (auth required on live API)
- `get_kafka_details` — `GET /status/kafka-details` (auth required)
- `get_system_metrics` — `GET /status/metrics` (auth required)
- `get_user_info` — `GET /user/info` (auth required)
- `list_kafka_streams` — `GET /resources/search?format=kafka`
- `list_organizations` — `GET /organization`
- `search_datasets` — `GET /search` (terms required, array)
- `search_resources` — `GET /resources/search`

**Writes (5, body params from real schemas):**
- `register_dataset` — `POST /dataset` body GeneralDatasetRequest
- `register_kafka_topic` — `POST /kafka` body KafkaDataSourceRequest
- `register_derived_stream` — `POST /kafka` with `mapping` field recording source_topic + filter
- `register_s3_resource` — `POST /s3` body S3Request
- `register_url_resource` — `POST /url` body URLRequest

## Generation

Generated via `gpt-oss:120b` on local Ollama with
`tools_per_example=8`, target_pairs=1000, ratios single 0.30 / multi 0.30
/ chain 0.25 / error 0.15.

## Trained models (TBD)

This dataset will train:
1. `unsloth/Qwen3-4B-Instruct-2507` (qwen3 model_type)
2. `nvidia/Llama-3.1-Nemotron-Nano-4B-v1.1` (llama model_type)
3. `ibm-granite/granite-4.1-3b` (granite model_type)

All open / non-gated. The originally-requested `nvidia/Nemotron-3-Nano-4B-v2`
and `ibm-granite/granite-4.1-3b-instruct` are HF-gated.

Scores TBD post-train, probed against the live NDP MCP.
