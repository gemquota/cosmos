---
type: "concept"
title: "Vector Memory"
description: "Dense-embedding retrieval over past improvements — semantic recall for similar-pattern reuse"
tags: [vector, embeddings, retrieval, rsis3, memory]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: []
---

# Vector Memory

## Summary
Vector memory is the top tier of the memory hierarchy: every improvement is embedded into a dense vector space so retrieval finds *semantically similar* past work, not just keyword matches. It answers "what did we do last time something like this failed?" RSIS3 persists it under `.rsis/vectors/` with an index of documents and embeddings.

## Details
- **Write path**: `record_improvement()` embeds `"<outcome>: <description>"` plus metadata (files, scores, goal) and appends to the store.
- **Read path**: `get_relevant_patterns(goal, k)` embeds the query and returns the nearest neighbors — used for context injection before code generation.
- **Design rule**: the vector store is derived from the knowledge graph, never authoritative on its own; git remains the source of truth.
- Failure mode to avoid: stale vectors after KG pruning — the tier is only as trustworthy as the consolidation that feeds it.

## Related
- [[wiki/concepts/knowledge-graph-memory|Knowledge-Graph Memory]] — the source tier it mirrors
- [[wiki/concepts/memory-hierarchy|Memory Hierarchy]] — retrieval vs. truth
- [[wiki/concepts/semantic-memory|Semantic Memory]] — the cognitive analogue of embedding recall
- [[wiki/concepts/working-memory|Working Memory]] — the small active context retrieval feeds