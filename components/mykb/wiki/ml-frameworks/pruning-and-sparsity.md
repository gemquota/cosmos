---
type: "concept"
title: "Pruning and Sparsity"
description: "Removing or zeroing model weights to reduce size and compute"
tags: ["pruning", "compression", "sparsity", "efficiency"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Pruning and Sparsity

## Summary
Removing or zeroing model weights to reduce size and compute

## Details
- Structured pruning removes units; unstructured sparsity zeros individual weights.
- Sparse models need special kernels to pay off.
- Retraining recovers much of the lost accuracy.
- A complement to quantization and distillation.

## Related
- [[wiki/ml-frameworks/distillation-vs-quantization|Distillation vs Quantization]] — compression family
- [[wiki/ml-frameworks/kernels-and-inference-optimization|Kernels and Inference Optimization]] — sparse kernel support
- [[wiki/ai-ml/model-quantization|Model Quantization]] — sibling method
- [[wiki/ml-frameworks/compiler-optimizations-llm|Compiler Optimizations for LLMs]] — sparsity-aware compilation
- [[wiki/ml-frameworks/small-language-models|Small Language Models]] — size goals
