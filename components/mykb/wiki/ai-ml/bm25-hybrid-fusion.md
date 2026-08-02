---
type: "concept"
title: "BM25 and Hybrid Fusion"
description: "Combining lexical BM25 scoring with dense vector similarity and fusing rankings for better retrieval"
tags: ["lexical", "hybrid", "retrieval"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# BM25 and Hybrid Fusion

## Summary
Combining lexical BM25 scoring with dense vector similarity and fusing rankings for better retrieval

## Details
- BM25 handles exact terms and rare keywords that embeddings miss.
- Hybrid systems merge BM25 and dense scores via weights or rank fusion.
- Covers both lexical precision and semantic recall.
- Reciprocal rank fusion is the simplest effective merge.

## Related
- [[wiki/data-storage/reciprocal-rank-fusion|Reciprocal Rank Fusion]] — rank-based fusion method
- [[wiki/ai-ml/hybrid-search-systems|Hybrid Search Systems]] — system-level pattern
- [[wiki/ai-ml/dense-passage-retrieval|Dense Passage Retrieval]] — dense half of the pair
- [[wiki/ai-ml/reranking-strategies|Reranking Strategies]] — applied after fusion
- [[wiki/ai-ml/evaluation-rag-as-a-service|Evaluating RAG as a Service]] — measuring fused pipelines
