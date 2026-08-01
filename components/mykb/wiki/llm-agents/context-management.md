---
type: "concept"
title: "Context Management"
description: "Keeping the right information in a finite context window"
tags: ["context", "llm", "prompting", "memory", "retrieval"]
timestamp: "2026-07-31T00:00:00Z"
status: "growing"
source: ["https://arxiv.org/abs/2307.03172"]
---

# Context Management

## Summary
Context management is the practice of deciding what goes into the model's context window, in what order, and when it should be evicted or summarized. It matters because context is finite and models attend unevenly — the Lost in the Middle result shows middle-of-context information is used worst. Good context management is the difference between a coherent long-running agent and one that forgets its own instructions.

## Details
- **Selection**: retrieval (TF-IDF, embeddings, backlinks) pulls only task-relevant memories into context.
- **Compaction**: summarization and rolling digests keep long sessions within budget.
- **Positioning**: critical instructions belong at the start or end of context, not buried mid-window.
- **Caching**: prompt caching reuses stable prefixes to cut cost and latency.
- RSIS3 uses mykb as external context: the daemon serves search results that planning queries before acting.
- Worked example: a long session compacts the full transcript into a bullet digest and keeps the task spec pinned at the top.

## Related
- [[wiki/concepts/working-memory|Working Memory]] — the active slice of context
- [[wiki/llm-agents/prompt-caching|Prompt Caching]] — reusing stable context prefixes
- [[wiki/concepts/cognitive-load|Cognitive Load]] — the cost of overloaded context
- [[wiki/llm-agents/rag-agent|RAG Agent]] — retrieval-driven context assembly
- [[wiki/concepts/mykb-analysis|Mykb Analysis]] — search and enrichment for context selection
- [[wiki/syntheses/knowledge-system|Knowledge System Overview]] — the pipeline that feeds context
