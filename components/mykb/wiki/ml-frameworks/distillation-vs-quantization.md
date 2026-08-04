---
type: "concept"
title: "Distillation vs Quantization"
description: "Comparing two model-compression approaches: teaching a smaller model versus compressing weights"
tags: ["distill-vs-quant", "compression", "efficiency", "comparison"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# Distillation vs Quantization

## Summary

Distillation and quantization are the two dominant approaches to compressing language models, but they work differently: distillation trains a smaller model to imitate a larger teacher, while quantization compresses the weights of an existing model into fewer bits. Choosing between them depends on the target hardware, the acceptable quality loss, and whether training resources are available. The comparison matters because compression determines which models can run where.

## Details

- **Distillation definition** — knowledge distillation transfers the teacher's behavior, often through its output distributions, into a smaller student model.
- **Quantization definition** — quantization reduces the numeric precision of weights and activations, shrinking memory and accelerating arithmetic.
- **Quality tradeoffs** — distillation can produce better small models because it learns a new architecture, while quantization preserves the original model's behavior with a fixed structure.
- **Resource requirements** — distillation requires a training run and data; quantization typically needs only a calibration set and can be done in hours.
- **Hardware fit** — quantized models benefit from integer-optimized hardware, while distilled models run on any hardware suited to their size.
- **Combination** — practitioners often distill first, then quantize the student, stacking both compression strategies.
- **Worked example** — a team replaces a 70B model with a distilled 8B student for API serving, then applies 4-bit quantization so the same GPU can host more replicas.
- **Failure modes** — aggressive quantization causes outliers and perplexity degradation; aggressive distillation can collapse rare skills.
- **Practical relevance** — the choice shapes cost, latency, and deployment footprint, and both techniques feed the small-model and edge ecosystems.
- **Evaluation** — comparing the two requires measuring task performance, size, latency, and energy, not just parameter count.

## Related

- [[wiki/meta-learning/knowledge-distillation|Knowledge Distillation]] — the distillation method
- [[wiki/ai-ml/model-quantization|Model Quantization]] — the compression method
- [[wiki/ml-frameworks/pruning-and-sparsity|Pruning and Sparsity]] — the third compression route
- [[wiki/ml-frameworks/small-language-models|Small Language Models]] — the product of compression
- [[wiki/ml-frameworks/on-device-llm|On-Device LLMs]] — the deployment context

