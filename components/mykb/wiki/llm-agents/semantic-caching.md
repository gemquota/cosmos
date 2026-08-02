---
type: "concept"
title: "Semantic Caching"
description: "Reusing prior LLM responses for semantically similar requests"
tags: ["llm", "caching", "cost", "performance"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://platform.openai.com/docs/guides/prompt-caching", "https://github.com/BerriAI/litellm"]
---

# Semantic Caching

## Summary
Semantic caching stores past LLM responses keyed by meaning rather than exact text, so similar requests reuse earlier answers. It cuts cost and latency dramatically for repetitive workloads. The challenge is deciding similarity safely: an over-eager cache returns wrong answers for subtly different requests.

## Details
- **Mechanism** — embed the request, compare against cached embeddings with a similarity threshold, and serve the cached response on a match.
- **Thresholds** — the similarity threshold trades hit rate against correctness; per-use-case calibration is required.
- **Safety** — caching is only safe for deterministic, time-insensitive outputs; personalized or fresh-data requests must bypass it.
- **Invalidation** — time-to-live, source-change invalidation, and per-session namespaces keep caches fresh.
- **Worked example** — a support bot caches answers to common troubleshooting questions; a paraphrase of a known question hits the cache and returns in milliseconds.
- **mykb relevance** — RSIS3 prompt caching and gateway caching extend the same idea to exact-prefix and semantic levels.

## Related
- [[wiki/llm-agents/prompt-caching|Prompt Caching]] — exact-prefix caching
- [[wiki/ai-ml/semantic-operator-similarity|Semantic Operator Similarity]] — similarity operators
- [[wiki/agent-systems/agent-cost-optimization|Agent Cost Optimization]] — cost impact of caching
- [[wiki/ai-ml/kv-cache-management|KV-Cache Management]] — low-level cache management
- [[wiki/prompt-engineering/context-window-management|Context Window Management]] — caching context reuse
- [[wiki/ml-frameworks/openrouter-prompt-caching|OpenRouter and Prompt Caching]] — related concept in this cluster
- [[wiki/ml-frameworks/embeddings-api|Embeddings API]] — embeddings access
- [[wiki/syntheses/knowledge-system|Knowledge System Overview]] — the KB loop this work feeds
