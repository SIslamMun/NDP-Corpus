# Qwen3-4B-Instruct-2507 NDP-A GGUF (Q8_0, 4.0 GB)

NOT in git — GitHub LFS file limit is 2 GB.

Rebuild locally:
1. Apply the LoRA in `../lora/` on top of `unsloth/Qwen3-4B-Instruct-2507`.
2. Convert via `unsloth save_pretrained_gguf(..., quantization_method='q8_0')`.

Or split the existing 4 GB GGUF into ≤2 GB shards via llama.cpp's
`llama-gguf-split --split-max-size 1900M model.Q8_0.gguf shard` before pushing.
