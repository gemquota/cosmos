---
type: "concept"
title: "Prompt Caching"
description: "Reusing cached processing of stable prompt prefixes to cut cost and latency"
tags: ["prompt-caching", "context", "cost", "llm"]
timestamp: "2026-07-31T00:00:00Z"
status: "growing"
---
# Prompt Caching

## Summary

Prompt caching reuses the KV-cache of a prior model call when the new prompt shares a prefix, cutting latency and cost for repeated system prompts and large context. It is the economic lever that makes long-context agents affordable — with correctness and staleness caveats.

## Details
- Mechanism: providers (OpenAI, Anthropic, Google) cache the processed prefix of a prompt; a subsequent request with the same prefix (system prompt + shared context) bills the cached portion at a steep discount and skips recomputation; caches have TTLs and eviction; cacheability requires stable ordering (static system prompt first, dynamic content last) and exact prefix match.
- Concrete example: an agent with a 5k-token system prompt + tool schema reuses the cache across every turn — 80-90% of input tokens at cache prices; a RAG loop that prepends retrieved chunks before the question changes the prefix per query and destroys cache reuse (order dynamic content consistently).
- Failure modes: assuming cache hits (prefix changes — timestamps, ordering, minor edits — invalidate silently); stale cache serving outdated context in some setups (understand provider semantics); cost leakage from non-cacheable prefixes; and debugging cost regressions that trace to prompt reordering.
- Operational tradeoffs: caching trades prompt-engineering discipline (stable prefixes) for cost and latency; the practice is static-first prompt layouts, cache-aware dynamic insertion points, and monitoring cache-hit rates and token costs per session.
- RSIS3/mykb relevance: the wiki's loop prompts keep static system/tool prefixes stable so long sessions reuse caches, and cost telemetry tracks the savings.
- Cache-aware design: order prompt sections by stability (system, tools, few-shot, then dynamic), and keep dynamic inserts at the tail to preserve the shared prefix.
- Monitoring: track cache hit ratio and token cost per session; a hit-ratio drop after a prompt edit is the signal that the layout changed.

## Related
- [[wiki/llm-agents/context-management|Context Management]] — the practice caching optimizes
- [[wiki/llm-agents/rag-agent|RAG Agent]] — caching retrieved context
- [[wiki/agent-systems/agent-loop|Agent Loop]] — the loop that resends prefixes
- [[wiki/concepts/working-memory|Working Memory]] — the cached stable part
- [[wiki/llm-agents/agentic-workflows|Agentic Workflows]] — caching across workflow steps
