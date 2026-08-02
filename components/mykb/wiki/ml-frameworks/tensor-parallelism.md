---
type: "concept"
title: "Tensor Parallelism"
description: "Distributed training and inference that splits individual weight tensors across multiple GPUs"
tags: ["parallelism", "gpu", "inference"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Tensor Parallelism

## Summary
Distributed training and inference that splits individual weight tensors across multiple GPUs

## Details
- Weight matrices are partitioned by row or column across devices that cooperate on each layer.
- All-reduce communication per layer keeps results consistent across devices.
- Reduces per-GPU memory for a single model layer but needs fast interconnects.
- Widely used for serving very large models that do not fit one GPU.

## Related
- [[wiki/ml-frameworks/pipeline-parallelism|Pipeline Parallelism]] — complements layer-level splitting
- [[wiki/ml-frameworks/sharding-data-parallel|Sharding and Data Parallelism]] — data-parallel counterpart
- [[wiki/ml-frameworks/inference-engines|Inference Engines]] — engines implement TP for serving
- [[wiki/ml-frameworks/moe-architectures|Mixture-of-Experts Architectures]] — experts complicate TP layouts
- [[wiki/ai-ml/model-quantization|Model Quantization]] — memory levers that combine with TP
