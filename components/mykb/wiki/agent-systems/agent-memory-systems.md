---
type: "concept"
title: "Agent Memory Systems"
description: "Memory architectures that let agents persist state, experience, and knowledge across runs"
tags: ["agents", "memory", "persistence", "architecture"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://arxiv.org/abs/2307.09288", "https://arxiv.org/abs/2210.03629"]
---

# Agent Memory Systems

## Summary
Agent memory systems give an agent continuity: what it did, what it learned, and what it knows persist beyond a single context window. Memory is layered by timescale and fidelity — working, episodic, semantic, and procedural. It is the difference between an agent that repeats mistakes and one that improves.

## Details
- **Layers** — working memory holds the current task; episodic memory records past runs; semantic memory stores distilled knowledge; procedural memory encodes skills.
- **Storage** — memory can live in vector stores, structured records, or the agent's own summary notes; retrieval quality decides usefulness.
- **Consolidation** — raw experiences are summarized and merged into durable knowledge during idle or reflection cycles.
- **Worked example** — a support agent records each resolved ticket as an episodic memory, then consolidates recurring tickets into a semantic playbook.
- **Tradeoffs** — richer memory improves continuity but raises retrieval latency, cost, and the risk of stale or contradictory entries.
- **mykb relevance** — mykb is itself the semantic memory layer of the triad, and RSIS3's reflections are episodic memory records.

- **Retrieval quality decides value** — a memory store is only useful if the right memories surface at the right time; indexing, ranking, and forgetting policies matter as much as storage.
- **Forgetting is a feature** — bounded memory with decay or eviction keeps the store relevant; unbounded accumulation dilutes retrieval and raises cost.
- **Memory and identity** — a stable memory base is what lets an agent be the same entity across sessions, tying memory systems to identity and continuity.
## Related
- [[wiki/llm-agents/memory-consolidation-agents|Memory Consolidation for Agents]] — turning experience into durable knowledge
- [[wiki/llm-agents/memory-augmented-agents|Memory-Augmented Agents]] — memory as an agent capability
- [[wiki/concepts/knowledge-graph-memory|Knowledge-Graph Memory]] — graph-structured memory in mykb
- [[wiki/concepts/declarative-memory|Declarative Memory]] — the cognitive counterpart
- [[wiki/concepts/episodic-memory|Episodic Memory]] — cognitive science view
- [[wiki/llm-agents/conversation-history-management|Conversation History Management]] — related concept in this cluster
- [[wiki/concepts/semantic-memory|Semantic Memory]] — memory type it builds on
- [[wiki/llm-agents/dialog-state-tracking|Dialog State Tracking]] — related concept in this cluster
