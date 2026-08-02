---
type: "concept"
title: "Mixed Precision Training"
description: "Training that stores some tensors in low precision and others in full precision to save memory and speed up compute"
tags: ["training", "memory", "gpu"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Mixed Precision Training

## Summary
Training that stores some tensors in low precision and others in full precision to save memory and speed up compute

## Details
- Forward and backward pass in FP16/BF16 while a full-precision master copy of weights is kept.
- Loss scaling prevents underflow in FP16; BF16 avoids scaling for many LLM workloads.
- Roughly halves memory and can double throughput on tensor-core GPUs.
- The standard default for modern LLM training.

## Related
- [[wiki/ml-frameworks/bf16-training|BF16 Training]] — the preferred low-precision format for LLMs
- [[wiki/ml-frameworks/gradient-accumulation|Gradient Accumulation]] — memory strategy that combines well
- [[wiki/ml-frameworks/zero-stage|ZeRO Stages]] — sharding that builds on precision savings
- [[wiki/ai-ml/llm-fine-tuning|LLM Fine-Tuning]] — where precision matters
- [[wiki/ml-frameworks/checkpointing-training|Training Checkpointing]] — reduces activation memory
