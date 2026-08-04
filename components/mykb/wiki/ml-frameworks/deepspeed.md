---
type: "entity"
title: "DeepSpeed"
description: "Microsoft library for distributed training and inference of very large models"
tags: ["distributed", "training", "scaling"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# DeepSpeed

## Summary
Microsoft library for distributed training and inference of very large models

## Details
- Provides ZeRO stages, pipeline and tensor parallelism, and offloading for billion-scale training.
- Used to train many frontier open models by reducing memory per GPU.
- Also includes inference optimizations such as kernel injection and sparse attention.
- The natural choice when a fine-tuning job outgrows a single GPU.

## Related
- [[wiki/ml-frameworks/zero-stage|ZeRO Stages]] — its memory-sharding core
- [[wiki/ml-frameworks/sharding-data-parallel|Sharding and Data Parallelism]] — data-parallel variant it extends
- [[wiki/ml-frameworks/pipeline-parallelism|Pipeline Parallelism]] — layer-split strategy it supports
- [[wiki/ml-frameworks/tensor-parallelism|Tensor Parallelism]] — within-layer splitting
- [[wiki/ml-frameworks/mixed-precision-training|Mixed-Precision Training]] — memory savings it layers on
