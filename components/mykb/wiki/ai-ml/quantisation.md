---
type: "concept"
title: "Quantisation"
description: "Reducing model weight and activation precision (e.g., FP16 to INT8/INT4) to shrink memory and speed up inference"
tags: ["quantisation", "inference", "optimization", "llm"]
timestamp: "2026-07-31T00:00:00Z"
status: "growing"
source: ["https://huggingface.co/docs/transformers/quantization", "https://github.com/ggerganov/llama.cpp"]
---

# Quantisation

## Summary
Quantization stores weights in lower-precision formats (INT8, INT4, or mixed) to cut memory footprint and often improve throughput, at the cost of small quality degradation. It is the main reason 7-70B models run on laptops and phones via tools like llama.cpp and Ollama.

## Details
- Hugging Face's quantization docs cover PTQ (post-training) methods like GPTQ, AWQ, bitsandbytes, and GGUF formats for transformers.
- llama.cpp popularized 4-bit GGUF quantizations that fit multi-billion-parameter models in a few gigabytes of RAM.
- Quality impact varies by task: perplexity usually rises slightly, but structured and code tasks can degrade more, so evals must gate quantized checkpoints.
- KV-cache quantization and activation quantization matter too — memory savings are not limited to weights.
- Quantization pairs with pruning and distillation in the broader inference-optimization toolkit.
- RSIS3 relevance: local RSIS3 runs (Ollama/llama.cpp) depend on quantized models; mykb should record which quantization each experiment used as a telemetry field.

## Related
- [[wiki/ml-frameworks/ollama|Ollama]] — Local runtime that serves quantized models
- [[wiki/ml-frameworks/llama-cpp|llama.cpp]] — The reference GGUF quantization stack
- [[wiki/ml-frameworks/vllm|vLLM]] — Server-side engine with quantization support
- [[wiki/ml-frameworks/onnx|ONNX]] — Quantized export format for cross-runtime deployment
- [[wiki/ai-ml/llama|Llama]] — Model family commonly run quantized
- [[wiki/ai-ml/mistral|Mistral]] — Model family commonly run quantized
- [[wiki/concepts/mykb-research-report|mykb Research Report: Personal LLM Wiki Systems — Methodologies, Architectures & Integration Blueprint]] — Local inference research in the mykb blueprint
