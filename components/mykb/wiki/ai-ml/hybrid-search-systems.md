---
type: "concept"
title: "Hybrid Search Systems"
description: "Combining lexical and semantic search to get both exact-match precision and meaning-based recall"
tags: ["hybrid", "search", "retrieval", "bm25"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://weaviate.io/blog/hybrid-search-explained", "https://arxiv.org/abs/2104.08488"]
---

# Hybrid Search Systems

## Summary
Hybrid search runs keyword (BM25) and vector (dense) retrieval in parallel and fuses the results. It matters because neither alone is enough: lexical search nails exact terms, semantic search catches paraphrase. Fusion combines their strengths with tunable weights.

## Details
- **Components** — BM25 index, embedding index, and a fusion function (weighted sum or reciprocal rank).
- **Tuning** — fusion weights balance precision and recall per domain; rerankers then refine the merged list.
- **Worked example** — a code search: BM25 finds the exact API name, dense search finds the conceptual pattern, fusion mixes both, a cross-encoder reranks.
- **Failure modes** — duplicated results, contradictory rankings, and embedding drift degrade hybrid quality.
- **mykb relevance** — a personal KB benefits doubly: exact titles via BM25, conceptual recall via embeddings.
- **Worked example** — a code search: BM25 finds the exact API name, dense search finds the conceptual pattern, fusion mixes both, a cross-encoder reranks.
- **Operational care** — monitor both indexes; embedding drift or index staleness silently degrades one leg of the hybrid.

## Related
- [[wiki/ai-ml/bm25-hybrid-fusion|BM25 Hybrid Fusion]] — fusion mechanics
- [[wiki/ai-ml/reranking-strategies|Reranking Strategies]] — post-fusion refinement
- [[wiki/ai-ml/embeddings-and-vector-search|Embeddings and Vector Search]] — dense side
- [[wiki/data-storage/reciprocal-rank-fusion|Reciprocal Rank Fusion]] — rank fusion method
- [[wiki/data-storage/vector-databases|Vector Databases]] — dense index
- [[wiki/ai-ml/vector-database-sharding|Vector Database Sharding]] — related concept in this cluster
- [[wiki/data-storage/cosine-similarity|Cosine Similarity]] — vector metric
