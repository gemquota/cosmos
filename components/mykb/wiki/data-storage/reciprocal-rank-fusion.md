---
type: "concept"
title: "Reciprocal Rank Fusion"
description: "Rank-based method for merging multiple result lists that is robust to incomparable relevance scores"
tags: ["fusion", "ranking", "retrieval", "hybrid", "search"]
timestamp: "2026-07-31T00:00:00Z"
status: "growing"
source: ["https://www.pinecone.io/learn/hybrid-search/"]
---

# Reciprocal Rank Fusion

## Summary
Reciprocal rank fusion (RRF) merges several ranked lists by summing `1/(k + rank)` for each document, ignoring each system's raw scores. It is robust, parameter-light, and the standard way to combine BM25 and vector results in hybrid search. Cormack, Clarke and Buettcher proposed it in 2009 for data fusion.

## Details
- **Formula** — for document d at rank r in each list, add `1/(k + r)` with k about 60; sort by total. Documents ranked high in multiple lists win.
- **Why ranks, not scores** — BM25 scores and cosine similarities are incomparable; converting to ranks sidesteps normalization entirely.
- **Worked example** — hybrid query: doc A is rank 2 in lexical and rank 5 in vector; doc B is rank 1 lexical but rank 40 in vector; RRF favors A even though B's raw lexical score may be higher.
- **Variants** — weighted RRF (multiply each list's contribution), score fusion with min-max normalization, and learned fusion (reranking models).
- **Use in RAG** — RRF-stabilized hybrid retrieval improves robustness when a query is half-identifier, half-concept.

## Related
- [[wiki/data-storage/hybrid-search|Hybrid Search]] — the primary application of RRF
- [[wiki/data-storage/bm25|BM25]] — one ranking source in the fusion
- [[wiki/data-storage/semantic-search|Semantic Search]] — the other ranking source
- [[wiki/data-storage/elasticsearch|Elasticsearch]] — a production lexical source RRF can fuse
- [[wiki/data-storage/cosine-similarity|Cosine Similarity]] — the score metric RRF deliberately ignores
- [[wiki/data-storage/vector-databases|Vector Databases]] — provides the vector-ranked list
- [[wiki/syntheses/knowledge-system|Knowledge System]] — retrieval fusion supports the knowledge loop
- [[wiki/data-storage/00-index|Data Storage]] — home of ranking and fusion tech
