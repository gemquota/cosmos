---
type: "concept"
title: "Paged Attention"
description: "Attention memory manager that stores KV cache in non-contiguous pages like virtual memory"
tags: ["paged-attention", "attention", "kv-cache", "memory"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Paged Attention

## Summary
Attention memory manager that stores KV cache in non-contiguous pages like virtual memory

## Details
- Eliminates fragmentation and enables near-100% cache utilization.
- Powers vLLM high-throughput serving.
- Supports prefix sharing and efficient preemption.
- The KV-cache innovation behind continuous batching at scale.

## Related
- [[wiki/ai-ml/kv-cache-management|KV-Cache Management]] — cache family
- [[wiki/ml-frameworks/vllm|vLLM]] — primary implementer
- [[wiki/ml-frameworks/continuous-batching|Continuous Batching]] — enabled throughput
- [[wiki/ml-frameworks/flash-attention|FlashAttention]] — complementary kernel
- [[wiki/ml-frameworks/inference-engines|Inference Engines]] — adoption
