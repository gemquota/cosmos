---
type: "concept"
title: "Sparse Experts"
description: "The expert modules in MoE models that activate only for a subset of tokens"
tags: ["sparse-experts", "moe", "architecture", "efficiency"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Sparse Experts

## Summary
The expert modules in MoE models that activate only for a subset of tokens

## Details
- Each expert specializes in patterns learned during training.
- Only top-k experts run per token, saving compute.
- Expert balance affects utilization and quality.
- Shared with dense layers in hybrid designs.

## Related
- [[wiki/ml-frameworks/moe-architectures|Mixture-of-Experts Architectures]] — parent architecture
- [[wiki/ml-frameworks/dense-vs-sparse-models|Dense vs Sparse Models]] — contrast
- [[wiki/ml-frameworks/tensor-parallelism|Tensor Parallelism]] — distributing experts across GPUs
- [[wiki/ml-frameworks/inference-engines|Inference Engines]] — runtime support
- [[wiki/ml-frameworks/model-composition|Model Composition]] — expert reuse ideas
