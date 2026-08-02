---
type: "concept"
title: "Vector Databases Revisited"
description: "Storing embeddings and serving similarity search at scale"
tags: ["vector-databases", "embeddings", "similarity-search", "rag"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://en.wikipedia.org/wiki/Vector_database", "https://weaviate.io/developers/weaviate"]
---

# Vector Databases Revisited

## Summary

Vector databases index embeddings for fast approximate nearest-neighbor search.
They power semantic search, RAG, and recommendation systems.
Index choices (HNSW, IVF) trade recall, memory, and latency.
Vector search is a retrieval stage, not a complete answer system; pair it with reranking and filters.

## Details

- Embeddings map text/images to dense vectors; similarity uses distance metrics.
- HNSW gives high recall with memory overhead; IVF is lighter.
- Hybrid search combines vector and keyword signals.
- Metadata filters narrow candidate sets before scoring.
- Model versioning matters: embeddings from different models are incomparable.
- Benchmark recall-latency tradeoffs on your own data.
- Keep vector indexes versioned alongside embedding models.
- Vector search quality is bounded by embedding quality; invest in embeddings, not just indexes.

## Related

- [[wiki/api-services/embedding-and-vector-query-apis|Embedding And Vector Query Apis]] — serving
- [[wiki/data-storage/search-and-relevance-ranking|Search And Relevance Ranking]] — ranking
- [[wiki/data-storage/vector-databases|Vector Databases]] — existing note
- [[wiki/data-storage/hnsw|HNSW]] — HNSW
- [[wiki/data-storage/embeddings|Embeddings]] — embeddings
- [[wiki/data-storage/data-quality-dimensions|Data Quality Dimensions]] — quality dimensions

