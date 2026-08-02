---
type: "concept"
title: "Embeddings and Vector Search"
description: "Representing text as vectors and searching by semantic similarity"
tags: ["embeddings", "vector-search", "semantic", "retrieval"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://platform.openai.com/docs/guides/embeddings", "https://github.com/facebookresearch/faiss"]
---

# Embeddings and Vector Search

## Summary
Embeddings map text to dense vectors such that similar meanings sit close together; vector search finds nearest neighbors efficiently. They are the retrieval substrate for RAG, semantic memory, and deduplication. Quality depends on the embedding model, the similarity metric, and the index.

## Details
- **Embedding models** — sentence-transformers, OpenAI embeddings, and ColBERT-style late-interaction models each trade quality, cost, and speed.
- **Similarity** — cosine similarity is standard for normalized embeddings; dot product and Euclidean distance fit other geometries.
- **Indexes** — HNSW and IVF indexes trade recall, memory, and build time; quantization shrinks memory at some accuracy cost.
- **Worked example** — a support bot embeds 10,000 resolved tickets; a new question retrieves the nearest 5 by cosine similarity as grounding.
- **Pitfalls** — chunking effects, domain shift, and embedding staleness degrade search; evaluation with retrieval benchmarks keeps quality visible.
- **mykb relevance** — mykb already runs embedding-based search over its wiki; this is the same machinery behind its semantic layer.

## Related
- [[wiki/ai-ml/hybrid-search-systems|Hybrid Search Systems]] — combining lexical and semantic search
- [[wiki/data-storage/retrieval-augmented-generation|Retrieval-Augmented Generation]] — using vectors in RAG
- [[wiki/ml-frameworks/embeddings-api|Embeddings API]] — the embeddings API
- [[wiki/ai-ml/hnsw-index|HNSW Index]] — a graph index for vectors
- [[wiki/data-storage/cosine-similarity|Cosine Similarity]] — the common metric
- [[wiki/data-storage/chunking-strategies|Chunking Strategies]] — chunking for embeddings
- [[wiki/meta-learning/sentence-transformers|Sentence Transformers]] — embedding tooling
- [[wiki/ai-ml/vector-database-sharding|Vector Database Sharding]] — scaling vector stores
