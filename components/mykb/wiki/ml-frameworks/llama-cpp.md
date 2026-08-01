---
type: "concept"
title: "llama.cpp"
description: "A C/C++ inference engine for running quantized LLMs efficiently on CPU and GPU"
tags: ["llama-cpp", "inference", "quantisation", "llm"]
timestamp: "2026-07-31T00:00:00Z"
status: "stub"
---

# llama.cpp

## Summary
llama.cpp is the reference high-performance C/C++ runtime for LLM inference, famous for GGUF quantization and running large models on modest hardware. It underpins Ollama, LM Studio, and many embedders.

## Details
- GGUF format packages weights, tokenizer, and metadata for portable quantization.
- Supports CPU, CUDA, Metal, Vulkan, and other backends; k/v-cache optimizations.
- Server mode exposes an OpenAI-compatible HTTP API.
- RSIS3 relevance: llama.cpp is the execution engine for RSIS3's fully local inference path.

## Related
- [[wiki/ai-ml/quantisation|Quantisation]] — The technique it popularized
- [[wiki/ml-frameworks/ollama|Ollama]] — A user-friendly wrapper
- [[wiki/ai-ml/llama|Llama]] — The original target model family
- [[wiki/ml-frameworks/onnx|ONNX]] — The alternative cross-runtime format
- [[wiki/ml-frameworks/vllm|vLLM]] — The GPU-datacenter alternative
