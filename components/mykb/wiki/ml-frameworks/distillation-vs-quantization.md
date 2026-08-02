---
type: "concept"
title: "Distillation vs Quantization"
description: "Comparing two model-compression approaches: teaching a smaller model versus compressing weights"
tags: ["distill-vs-quant", "compression", "efficiency", "comparison"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Distillation vs Quantization

## Summary
Comparing two model-compression approaches: teaching a smaller model versus compressing weights

## Details
- Distillation transfers knowledge to a smaller architecture.
- Quantization shrinks precision of an existing model.
- Distillation changes weights; quantization changes representation.
- Often combined for extreme compression.

## Related
- [[wiki/meta-learning/knowledge-distillation|Knowledge Distillation]] — distillation core
- [[wiki/ai-ml/model-quantization|Model Quantization]] — quantization core
- [[wiki/ml-frameworks/pruning-and-sparsity|Pruning and Sparsity]] — third lever
- [[wiki/ml-frameworks/small-language-models|Small Language Models]] — distillation target
- [[wiki/ml-frameworks/on-device-llm|On-Device LLMs]] — compression use case
