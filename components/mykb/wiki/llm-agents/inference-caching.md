---
type: "concept"
title: "Inference Caching"
description: "Reusing intermediate inference work across calls to reduce latency and cost"
tags: ["llm", "caching", "inference", "performance"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://platform.openai.com/docs/guides/prompt-caching", "https://docs.anthropic.com/en/docs/build-with-claude/prompt-caching"]
---

# Inference Caching

## Summary
Inference caching reuses expensive intermediate results — prompt prefixes, KV caches, or completed responses — across calls. It is the umbrella over prompt caching, KV-cache reuse, and semantic caching. Because decoding dominates inference cost, avoiding re-computation of shared prefixes is the biggest lever.

## Details
- **Prefix caching** — providers cache the KV state of repeated prompt prefixes; a long system prompt plus few-shot examples can be reused across requests.
- **KV-cache management** — at the engine level, paged attention and prefix trees make cache hits cheap and memory-efficient.
- **Response caching** — exact or semantic response reuse for deterministic workloads.
- **Worked example** — a fixed system prompt and tool schemas are cached by the provider; every user turn skips re-processing that prefix.
- **Tradeoffs** — cache correctness (staleness), memory pressure, and eviction policies matter.
- **mykb relevance** — RSIS3's repeated loop prompts benefit directly from provider-level prefix caching.
- **Cache layers** — prompt-level prefix caches (KV cache reuse) and response-level caches both cut cost, but only the latter serves identical answers instantly.
- **Invalidation** — TTLs, model-version keys, and content hashes keep caches from serving stale or wrong-model output.

## Related
- [[wiki/llm-agents/prompt-caching|Prompt Caching]] — provider prompt caching
- [[wiki/ml-frameworks/paged-attention|PagedAttention]] — memory for cache
- [[wiki/ai-ml/llm-latency-optimization|LLM Latency Optimization]] — latency benefits
- [[wiki/agent-systems/agent-cost-optimization|Agent Cost Optimization]] — cost benefits
- [[wiki/prompt-engineering/context-window-management|Context Window Management]] — what fills the cached prefix
- [[wiki/ml-frameworks/openrouter-prompt-caching|OpenRouter and Prompt Caching]] — provider caching options
- [[wiki/ml-frameworks/embeddings-api|Embeddings API]] — embeddings access
- [[wiki/syntheses/knowledge-system|Knowledge System Overview]] — the KB loop this work feeds
