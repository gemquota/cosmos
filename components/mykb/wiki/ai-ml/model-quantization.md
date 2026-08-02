---
type: "concept"
title: "Model Quantization"
description: "Reducing model precision to cut memory and latency at some accuracy cost"
tags: ["quantization", "inference", "optimization", "llm"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://huggingface.co/docs/transformers/en/main_classes/quantization", "https://arxiv.org/abs/2305.14314"]
---

# Model Quantization

## Summary
Quantization stores weights (and activations) at lower precision — 8-bit, 4-bit, or lower — shrinking memory and speeding inference. It is how large models run on laptops and edge devices. Accuracy loss is usually small but must be measured per task; some models quantize far better than others.

## Details
- **Approaches** — post-training quantization (PTQ) converts trained weights; quantization-aware training (QAT) tunes with quantization in the loop; GPTQ, AWQ, and bitsandbytes are common implementations.
- **Tradeoffs** — 8-bit is nearly lossless for most tasks; 4-bit saves more memory with measurable degradation on reasoning-heavy workloads.
- **KV-cache quantization** — quantizing the attention cache reduces memory at long contexts.
- **Worked example** — a 7B model at 4-bit runs in ~4GB RAM on a laptop, enabling local on-device inference for a privacy-sensitive task.
- **Measurement** — run task evals before and after quantization; perplexity deltas alone miss task-specific regressions.
- **mykb relevance** — quantisation is an existing mykb topic; local inference is how RSIS3 could run models on-device.

## Related
- [[wiki/ai-ml/quantisation|Quantisation]] — existing quantization concept
- [[wiki/ml-frameworks/distillation-vs-quantization|Distillation vs Quantization]] — quantization vs distillation
- [[wiki/ml-frameworks/small-language-models|Small Language Models]] — small models needing quantization
- [[wiki/ml-frameworks/on-device-llm|On-Device LLMs]] — quantized local inference
- [[wiki/ml-frameworks/llama-cpp|llama.cpp]] — a quantized local runtime
- [[wiki/ml-frameworks/pruning-and-sparsity|Pruning and Sparsity]] — other compression methods
- [[wiki/ml-frameworks/inference-engines|Inference Engines]] — quantized serving
- [[wiki/data-storage/hnsw|HNSW]] — ANN index family
