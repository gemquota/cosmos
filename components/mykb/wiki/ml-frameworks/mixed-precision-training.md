---
type: "concept"
title: "Mixed Precision Training"
description: "Training that stores some tensors in low precision and others in full precision to save memory and speed up compute"
tags: ["training", "memory", "gpu"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---
# Mixed Precision Training

## Summary

Mixed-precision training mixes FP32 with FP16/BF16 (and FP8) to halve memory, double throughput, and speed training, while loss scaling preserves accuracy. It is the standard training regime for modern models — and a source of silent divergence when misapplied.

## Details
- Mechanism: master weights stay FP32; forward/backward run in lower precision (FP16 for GPUs with loss scaling, BF16 with its wider range on newer hardware); optimizers keep FP32 states; automatic mixed precision (PyTorch autocast, TensorFlow mixed_precision) inserts casts and loss scaling automatically; FP8 pushes further on H100-class hardware.
- Concrete example: a 7B model fine-tune runs in BF16 with FP32 master weights and Adam states — VRAM roughly halves vs full FP32, throughput nearly doubles; a training run that skips loss scaling in FP16 diverges to NaN; a distributed run mixes precisions inconsistently across ranks and loses convergence.
- Failure modes: underflow in FP16 (small gradients → 0) without scaling; overflow to inf; BF16's reduced mantissa hurting fine-grained tasks (some tasks need FP32 accumulation); hardware without native FP16/BF16 support slowing down; and comparing loss curves across precision settings as if equivalent.
- Operational tradeoffs: mixed precision trades a little numerical headroom for large speed/memory wins — the default for any serious training; the discipline is using framework AMP, checking convergence parity with FP32 on a small run, and monitoring loss/NaN stats as training health signals.
- RSIS3/mykb relevance: the wiki's fine-tuning recipes pin precision settings per hardware, so the loop's training runs are reproducible and comparable.
- Loss scaling tuning: monitor scaled gradient distribution and adjust the scale factor on overflow; silent fp16 overflow appears as NaN loss only later in training.
- Distributed consistency: set precision and scaling identically across ranks; divergent settings are a classic source of hard-to-reproduce divergence in large runs.

## Related
- [[wiki/ml-frameworks/bf16-training|BF16 Training]] — the preferred low-precision format for LLMs
- [[wiki/ml-frameworks/gradient-accumulation|Gradient Accumulation]] — memory strategy that combines well
- [[wiki/ml-frameworks/zero-stage|ZeRO Stages]] — sharding that builds on precision savings
- [[wiki/ai-ml/llm-fine-tuning|LLM Fine-Tuning]] — where precision matters
- [[wiki/ml-frameworks/checkpointing-training|Training Checkpointing]] — reduces activation memory
