---
type: "concept"
title: "Semantic Memory"
description: "General facts and abstractions, independent of the episode that produced them"
tags: ["semantic-memory", "memory", "knowledge", "facts"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://en.wikipedia.org/wiki/Semantic_memory", "https://plato.stanford.edu/entries/memory/"]
---

# Semantic Memory

## Summary
Semantic memory stores general knowledge: facts, definitions, and abstractions stripped of their original context. It matters because it lets an agent reuse distilled lessons without replaying every episode. mykb concept pages are semantic memory; episode pages are episodic.

## Details
- Built by consolidating episodes into general claims.
- Supports search and graph linking across the wiki.
- Stale semantic memories cause confident errors; they need review.
- Open questions: how to detect and update outdated facts.
- Semantic memory stores general knowledge — facts, concepts, and their relationships — independent of the episodes that produced them.
- It is what lets you know what a 'graph' is without recalling the first time you learned it.
- Semantic memory is structured and relational: concepts connect to categories, properties, and other concepts, which is exactly the shape of a knowledge graph.
- It is built by consolidation from episodic traces and can also be learned directly from study.
- **Worked example / comparison** — Worked example — the wiki's concept articles are semantic memory: 'circuit breaker' links to 'retry' and 'resilience' without recording which session first introduced them.
- For mykb, semantic memory is the model for the wiki itself: a curated graph of concepts and relations, distinct from raw session records.

## Related
- [[wiki/llm-agents/memory-augmented-agents|Memory-Augmented Agents]]
- [[wiki/llm-agents/rag-agent|RAG Agent]]
- [[wiki/concepts/episodic-memory|Episodic Memory]]
- [[wiki/concepts/procedural-memory|Procedural Memory]]
- [[wiki/concepts/declarative-memory|Declarative Memory]]
- [[wiki/concepts/promotion-readiness|Promotion Readiness]]
- [[wiki/dev-tools/global-link-check|Global Link Check]]
- [[wiki/concepts/explainers|Explainers]]
