---
type: "concept"
title: "Query Decomposition"
description: "Splitting a complex query into simpler sub-queries that are answered separately and combined"
tags: ["rag", "queries", "multi-hop"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Query Decomposition

## Summary
Splitting a complex query into simpler sub-queries that are answered separately and combined

## Details
- Breaks multi-part questions into independent retrievals.
- Sub-answers are then fused or reasoned over for the final response.
- Improves coverage on multi-hop and comparison questions.
- Requires a planner and a merge step, adding orchestration.

## Related
- [[wiki/ai-ml/multi-hop-retrieval|Multi-Hop Retrieval]] — retrieval side of decomposed queries
- [[wiki/ai-ml/query-transformations|Query Transformations]] — family it belongs to
- [[wiki/ai-ml/recursive-retrieval|Recursive Retrieval]] — hierarchical counterpart
- [[wiki/prompt-engineering/self-ask-technique|Self-Ask Technique]] — prompting variant
- [[wiki/agent-systems/agent-planning-systems|Agent Planning Systems]] — planning the sub-queries
