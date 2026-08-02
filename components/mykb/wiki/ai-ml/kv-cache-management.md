---
type: "concept"
title: "KV-Cache Management"
description: "Storing and reusing the key-value attention cache to cut inference cost and latency"
tags: ["kv-cache", "inference", "attention", "memory"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://arxiv.org/abs/2309.06180", "https://arxiv.org/abs/2205.14135"]
---

# KV-Cache Management

## Summary
The KV cache stores the attention keys and values computed for earlier tokens so decode does not recompute them. It matters because the cache dominates memory and bandwidth during generation. Managing it well — reuse, eviction, and paging — is the biggest serving lever after batching.

## Details
- **Cost** — cache grows linearly with context length and batch size; memory planning is essential.
- **Techniques** — prefix caching across requests, paged allocation (PagedAttention), quantization of the cache, and windowed eviction.
- **Worked example** — a shared system prompt is cached once and reused across thousands of requests, cutting per-request prefill cost.
- **Trade-offs** — cache compression saves memory but can degrade quality; eviction policies drop old context.
- **mykb relevance** — repeated mykb system prompts are ideal prefix-cache candidates.
- **Worked example** — a shared system prompt is cached once and reused across thousands of requests, cutting per-request prefill cost.
- **Metrics** — cache hit rate and cache size per request belong in every serving dashboard.

## Related
- [[wiki/ml-frameworks/paged-attention|PagedAttention]] — paged allocation
- [[wiki/ml-frameworks/flash-attention|FlashAttention]] — efficient attention
- [[wiki/ai-ml/speculative-decoding|Speculative Decoding]] — cache-aware decode
- [[wiki/ai-ml/llm-latency-optimization|LLM Latency Optimization]] — latency impact
- [[wiki/llm-agents/inference-caching|Inference Caching]] — caching family
- [[wiki/prompt-engineering/context-window-management|Context Window Management]] — cache scope
- [[wiki/ai-ml/self-attention|Self-Attention]] — attention foundation
- [[wiki/ai-ml/multi-head-attention|Multi-Head Attention]] — attention mechanics
