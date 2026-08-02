---
type: "concept"
title: "BF16 Training"
description: "Training in bfloat16, which keeps the FP32 exponent range while halving memory footprint"
tags: ["precision", "training", "memory"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# BF16 Training

## Summary
Training in bfloat16, which keeps the FP32 exponent range while halving memory footprint

## Details
- BF16 has the same 8-bit exponent as FP32 but a truncated mantissa.
- Avoids the loss-scaling complexity of FP16 for most LLM workloads.
- Widely supported on modern accelerators and the default for many frameworks.
- Small precision loss is usually acceptable at LR scales used for pretraining.

## Related
- [[wiki/ml-frameworks/mixed-precision-training|Mixed-Precision Training]] — family it belongs to
- [[wiki/ai-ml/model-quantization|Model Quantization]] — post-training counterpart
- [[wiki/ai-ml/llm-fine-tuning|LLM Fine-Tuning]] — precision choices during SFT
- [[wiki/ml-frameworks/gradient-accumulation|Gradient Accumulation]] — memory optimization stack
- [[wiki/ml-frameworks/checkpointing-training|Training Checkpointing]] — complements activation savings
