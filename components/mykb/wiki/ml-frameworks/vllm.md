---
type: "concept"
title: "vLLM"
description: "A high-throughput inference and serving engine for LLMs, optimized with PagedAttention"
tags: ["vllm", "inference", "serving", "llm"]
timestamp: "2026-07-31T00:00:00Z"
status: "stub"
---

# vLLM

## Summary
vLLM is a production serving engine that achieves high throughput via PagedAttention (efficient KV-cache memory) and continuous batching. It is the standard choice for self-hosted GPU inference at scale.

## Details
- PagedAttention reduces KV-cache waste; continuous batching maximizes GPU utilization.
- Serves OpenAI-compatible endpoints for chat, completions, and embeddings.
- Supports quantization, LoRA adapters, and multi-GPU tensor parallelism.
- RSIS3 relevance: vLLM is the scalable serving layer if RSIS3's L1 loop runs self-hosted models at volume.

## Related
- [[wiki/ml-frameworks/llama-cpp|llama.cpp]] — The CPU/edge alternative
- [[wiki/ai-ml/quantisation|Quantisation]] — Supported precision formats
- [[wiki/ml-frameworks/openai-api|OpenAI API]] — The compatible serving surface
- [[wiki/prompt-engineering/token-budgets|Token Budgets]] — Throughput planning
- [[wiki/ai-ml/deepseek|DeepSeek]] — Large open models commonly served with vLLM
