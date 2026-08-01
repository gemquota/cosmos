---
type: "concept"
title: "Memory Hierarchy"
description: "Three tiers with different guarantees — git (truth), knowledge graph (insight), vectors (retrieval)"
tags: [memory, hierarchy, rsis3, architecture, persistence]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: []
---

# Memory Hierarchy

## Summary
The memory hierarchy is RSIS3's three-tier persistence model: git commits are the truth, the knowledge graph is the insight layer, and vector embeddings are the retrieval layer. Each tier trades fidelity for speed, and writes flow down (code → insight → embedding) while queries flow up. This mirrors cognitive memory: episodic → semantic → procedural, with different forgetting characteristics.

## Details
| Tier | Storage | Guarantee | Written by | Read by |
|---|---|---|---|---|
| Truth | git commits / checkpoints | perfect, replayable | L2 apply, checkpoints | recovery, rollback |
| Insight | `.rsis/knowledge_graph.json` | structured, typed | L3 consolidation, record_improvement | L4/L5/L6/L7 stats |
| Retrieval | `.rsis/vectors/` | fast semantic recall | record_improvement | pattern injection |

- **Invariant**: no tier is authoritative alone; git is the arbiter, and rollback rebuilds the upper tiers.
- **Consolidation**: L3 moves durable conclusions from sessions into the graph and prunes redundancies — the "commits ▲" arrow of the hierarchy.

## Related
- [[wiki/concepts/knowledge-graph-memory|Knowledge-Graph Memory]] — the insight tier
- [[wiki/concepts/vector-memory|Vector Memory]] — the retrieval tier
- [[wiki/concepts/checkpoint-rollback|Checkpoint & Rollback]] — the git truth tier in action
- [[wiki/memory/memory-consolidation|Memory Consolidation]] — the process that feeds the hierarchy
- [[wiki/concepts/episodic-memory|Episodic Memory]] — the cognitive analogue of session history