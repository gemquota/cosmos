---
type: "concept"
title: "Paged Attention"
description: "Attention memory manager that stores KV cache in non-contiguous pages like virtual memory"
tags: ["paged-attention", "attention", "kv-cache", "memory"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# Paged Attention

## Summary

Paged attention is a memory-management technique for transformer inference that stores the key-value (KV) cache in non-contiguous pages, analogous to virtual memory in operating systems. It eliminates fragmentation and enables near-100 percent cache utilization, which is a prerequisite for high-throughput serving. The technique matters because it directly determines how many requests a serving engine can process concurrently.

## Details

- **Definition** — paged attention divides the KV cache into fixed-size blocks that can be scattered across memory, with a block table mapping logical to physical locations.
- **Fragmentation problem** — naive serving preallocates contiguous KV buffers per request, wasting memory on unused headroom and creating severe fragmentation.
- **Operating-system analogy** — like virtual memory, paged attention supports on-demand allocation, sharing, and efficient preemption of cached blocks.
- **Utilization gains** — near-100 percent cache utilization dramatically increases the number of concurrent requests an engine can serve on the same hardware.
- **Prefix sharing** — identical prompt prefixes can share KV pages across requests, cutting memory and compute for common system prompts and few-shot prefixes.
- **Preemption** — when memory is exhausted, blocks can be swapped out or recomputed, providing graceful behavior under load.
- **Implementation** — the technique powers vLLM's high-throughput serving and has been adopted by other inference engines.
- **Relation to batching** — by removing memory pressure, paged attention is a key enabler of continuous batching at scale.
- **Worked example** — a server holds hundreds of requests whose KV caches are spread across a shared pool of 16-token blocks, with the block table ensuring each request reads its own pages.
- **Failure modes** — block overhead and table lookups add minor costs, and pathological sharing patterns can reduce the benefits.

## Related

- [[wiki/ai-ml/kv-cache-management|KV-Cache Management]] — the cache family
- [[wiki/ml-frameworks/vllm|vLLM]] — the primary implementer
- [[wiki/ml-frameworks/continuous-batching|Continuous Batching]] — the throughput technique enabled
- [[wiki/ml-frameworks/flash-attention|FlashAttention]] — the complementary kernel
- [[wiki/ml-frameworks/inference-engines|Inference Engines]] — the adopting systems
- [[wiki/ml-frameworks/batching-strategies|Batching Strategies]] — scheduling context

