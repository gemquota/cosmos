---
type: "concept"
title: "Prompt Caching"
description: "Reusing cached processing of stable prompt prefixes to cut cost and latency"
tags: ["prompt-caching", "context", "cost", "llm"]
timestamp: "2026-07-31T00:00:00Z"
status: "stub"
---

# Prompt Caching

## Summary
Prompt caching stores the processed representation of stable prompt prefixes (system prompts, tool schemas, shared context) so subsequent requests with the same prefix are cheaper and faster. It matters because agent loops resend large constant prefixes constantly. Caching is a core context-management cost lever.

## Details
- Cache hits require exact prefix match; keep stable content first.
- Significant savings on long system prompts and tool definitions.
- Pairs with context management: cache the stable, retrieve the volatile.
- Open questions: invalidation strategy when schemas change.

## Related
- [[wiki/llm-agents/context-management|Context Management]] — the practice caching optimizes
- [[wiki/llm-agents/rag-agent|RAG Agent]] — caching retrieved context
- [[wiki/agent-systems/agent-loop|Agent Loop]] — the loop that resends prefixes
- [[wiki/concepts/working-memory|Working Memory]] — the cached stable part
- [[wiki/llm-agents/agentic-workflows|Agentic Workflows]] — caching across workflow steps
