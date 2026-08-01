---
type: "concept"
title: "Knowledge-Graph Memory"
description: "The semantic memory tier: typed nodes (improvements, insights, strategies) and edges queried by the loops"
tags: [knowledge-graph, memory, semantic, rsis3, kg]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: []
---

# Knowledge-Graph Memory

## Summary
Knowledge-graph memory is the middle tier of the memory hierarchy: a graph of typed, attributed nodes — improvements, insights, strategies, failures — with relations that encode structure, not just text. It is the "insight" layer that sits between raw git history and dense vector embeddings. RSIS3 persists it to `.rsis/knowledge_graph.json` and every improvement is recorded as a node.

## Details
- **Node types**: `improvement` (with outcome, scores, goal), `insight`, `strategy`, `failure`; strategies seed the L5 population.
- **Queries**: `get_insights(limit)` returns the most recent improvement/insight nodes in insertion order — this is the outcome stream that L4/L6/L7 aggregate into success-rate stats.
- **Write path**: `record_improvement()` adds a node and mirrors it into the vector store, so the two tiers stay consistent.
- **Why it matters for loops**: fitness scoring (L5) and success-rate signals (L4/L6) are computed *from the graph*, making it the shared read-mostly substrate.

## Related
- [[wiki/concepts/vector-memory|Vector Memory]] — the retrieval tier above the graph
- [[wiki/concepts/memory-hierarchy|Memory Hierarchy]] — where the KG sits
- [[wiki/concepts/semantic-memory|Semantic Memory]] — the cognitive analogue
- [[wiki/concepts/nine-loop-hierarchy|Nine-Loop Hierarchy]] — L3 consolidates the graph, L4/L5 read it