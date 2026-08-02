---
type: "concept"
title: "Query Transformations"
description: "Rewriting or expanding user queries before retrieval to improve matching quality"
tags: ["rag", "queries", "retrieval"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Query Transformations

## Summary
Rewriting or expanding user queries before retrieval to improve matching quality

## Details
- Common transforms: rewriting, expansion, decomposition, and hypothetical documents.
- Better query representations close the gap between user phrasing and index terms.
- Each transform adds latency and cost, so it should be applied selectively.
- A core lever in retrieval-prompting and agentic RAG.

## Related
- [[wiki/ai-ml/query-decomposition|Query Decomposition]] — splitting into sub-queries
- [[wiki/ai-ml/hypothetical-document-embeddings|Hypothetical Document Embeddings]] — generate-then-embed variant
- [[wiki/ai-ml/multi-hop-retrieval|Multi-Hop Retrieval]] — transforms enabling multi-step search
- [[wiki/ai-ml/agentic-rag|Agentic RAG]] — agent decides when to transform
- [[wiki/prompt-engineering/retrieval-prompting|Retrieval Prompting]] — prompt-level transformation
