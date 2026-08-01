---
type: "concept"
title: "Hybrid Search"
description: "Retrieval that fuses lexical (BM25/TF-IDF) and semantic (vector) results into one ranked list"
tags: ["search", "hybrid", "bm25", "embeddings", "fusion"]
timestamp: "2026-07-31T00:00:00Z"
status: "growing"
source: ["https://weaviate.io/developers/weaviate/search/hybrid"]
---

# Hybrid Search

## Summary
Hybrid search runs a keyword retriever and a vector retriever in parallel, then fuses the two rankings so exact terms and semantic matches both surface. It fixes the blind spots of each approach and is the default production recipe for RAG. RSIS3-style systems benefit because memory queries mix precise identifiers with fuzzy concepts.

## Details
- **Why it wins** — BM25 nails exact names, IDs, and rare terms; embeddings handle paraphrase and conceptual queries; fusion keeps both.
- **Fusion methods** — reciprocal rank fusion (RRF) combines rank positions; score normalization (min-max or z-score) combines raw scores; weighted convex combinations tune recall vs precision.
- **Worked example** — a query for 'FAISS HNSW product quantization' gets lexical hits for 'FAISS' plus vector hits for similar ANN-index notes; RRF merges them into a single list.
- **Trade-offs** — two indexes to build and tune; score normalization is brittle across different scales, which is why rank-based fusion is popular.
- **mykb relevance** — mykb already maintains TF-IDF and embedding paths; a hybrid stage over both is the natural next step for retrieval quality.

## Related
- [[wiki/data-storage/reciprocal-rank-fusion|Reciprocal Rank Fusion]] — the standard rank-based fusion used by hybrid search
- [[wiki/data-storage/bm25|BM25]] — the lexical half of the hybrid pair
- [[wiki/data-storage/semantic-search|Semantic Search]] — the semantic half of the hybrid pair
- [[wiki/data-storage/vector-databases|Vector Databases]] — where the vector half is stored
- [[wiki/data-storage/qdrant|Qdrant]] — a vector database with built-in hybrid support
- [[wiki/data-storage/weaviate|Weaviate]] — a vector database with built-in hybrid search
- [[wiki/syntheses/knowledge-system|Knowledge System]] — the loop hybrid search makes accessible
- [[wiki/data-storage/index|Data Storage]] — home of the hybrid search stack
