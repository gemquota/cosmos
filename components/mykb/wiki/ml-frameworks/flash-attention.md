---
type: "concept"
title: "Flash Attention"
description: "IO-aware attention algorithm that avoids materializing the full attention matrix"
tags: ["flash-attention", "attention", "efficiency", "gpu"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Flash Attention

## Summary
IO-aware attention algorithm that avoids materializing the full attention matrix

## Details
- Tiles attention computation to keep data in fast on-chip memory.
- Reduces memory from O(n^2) to O(n) for the score matrix.
- Speeds training and inference with exact results.
- A standard component of modern serving stacks.

## Related
- [[wiki/ml-frameworks/paged-attention|PagedAttention]] — memory-management sibling
- [[wiki/ml-frameworks/kernels-and-inference-optimization|Kernels and Inference Optimization]] — kernel family
- [[wiki/ai-ml/transformer-architecture-attention-mechanisms|Transformer Architecture and Attention]] — algorithm base
- [[wiki/ai-ml/kv-cache-management|KV-Cache Management]] — cache interaction
- [[wiki/ai-ml/llm-latency-optimization|LLM Latency Optimization]] — speedup source
