---
type: "concept"
title: "Recursive Retrieval"
description: "Retrieval that navigates a structured document or index layer by layer to converge on relevant passages"
tags: ["rag", "retrieval", "hierarchy"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Recursive Retrieval

## Summary
Retrieval that navigates a structured document or index layer by layer to converge on relevant passages

## Details
- Starts from coarse summaries or sections and drills into finer granularity.
- Works well with hierarchical documents such as books and codebases.
- More steps than flat retrieval but higher precision on nested content.
- Often paired with query-decomposition for complex information needs.

## Related
- [[wiki/ai-ml/multi-hop-retrieval|Multi-Hop Retrieval]] — query side of multi-step retrieval
- [[wiki/ai-ml/small-to-big-retrieval|Small-to-Big Retrieval]] — granularity strategy it can use
- [[wiki/ai-ml/parent-document-retrieval|Parent Document Retrieval]] — nested structure mapping
- [[wiki/ai-ml/agentic-rag|Agentic RAG]] — agent-driven retrieval loop
- [[wiki/ai-ml/query-decomposition|Query Decomposition]] — splitting complex queries
