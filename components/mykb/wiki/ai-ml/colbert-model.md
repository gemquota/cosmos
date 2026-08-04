---
type: "entity"
title: "ColBERT Model"
description: "Retrieval model that scores query-document pairs with token-level late interaction instead of a single vector"
tags: ["retrieval", "embeddings", "ranking"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# ColBERT Model

## Summary
Retrieval model that scores query-document pairs with token-level late interaction instead of a single vector

## Details
- Emits per-token embeddings for query and document, then computes maximal similarity sums.
- Late interaction preserves fine-grained lexical-semantic match signals.
- Produces state-of-the-art retrieval accuracy at manageable cost.
- ColBERTv2 adds compression and indexing tricks for scale.

## Related
- [[wiki/ai-ml/dense-passage-retrieval|Dense Passage Retrieval]] — single-vector baseline it outperforms
- [[wiki/ai-ml/bm25-hybrid-fusion|BM25 Hybrid Fusion]] — lexical baseline
- [[wiki/ai-ml/reranking-strategies|Reranking Strategies]] — multi-stage use of ColBERT
- [[wiki/ai-ml/embeddings-and-vector-search|Embeddings and Vector Search]] — vector search family
- [[wiki/ai-ml/multi-hop-retrieval|Multi-Hop Retrieval]] — accuracy needs it supports
