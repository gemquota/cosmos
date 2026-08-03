---
type: "concept"
title: "Vector Databases"
description: "Databases purpose-built to index and search high-dimensional embedding vectors by similarity"
tags: ["vector-search", "database", "embeddings", "similarity", "indexing"]
timestamp: "2026-07-31T00:00:00Z"
status: "growing"
source: ["https://en.wikipedia.org/wiki/Vector_database"]
---

# Vector Databases

## Summary
A vector database stores embedding vectors alongside metadata and answers approximate nearest-neighbour (ANN) queries. It is the workhorse behind semantic search and RAG, returning items closest to a query embedding rather than matching keywords. mykb uses embedding-backed search to complement its TF-IDF engine.

## Details
- **Core operation** — given a query vector, return the k nearest vectors under a distance metric (cosine, dot product, Euclidean).
- **Index structures** — HNSW (graph-based), IVF (partitioned lists), and product quantization (compressed codes) trade memory, speed, and recall.
- **Metadata** — production systems store payloads (tags, timestamps, source) so results can be filtered before or after ANN search.
- **Managed vs embedded** — Pinecone, Qdrant Cloud, Weaviate, Milvus are server deployments; FAISS, ChromaDB, sqlite-vec run in-process.
- **Comparison table** — FAISS (library, no server) vs Milvus (distributed) vs Qdrant (Rust, filtering-first) vs ChromaDB (Pythonic, local) vs Pinecone (fully managed).
- **mykb relevance** — a local vector index over wiki notes enables 'recall similar memories' during RSIS3 reflection, with graceful degradation when no index exists.

## Related
- [[wiki/data-storage/faiss|FAISS]] — the foundational open-source ANN library
- [[wiki/data-storage/hnsw|HNSW]] — graph-based index that many vector databases use
- [[wiki/data-storage/milvus|Milvus]] — distributed vector database used at scale
- [[wiki/data-storage/qdrant|Qdrant]] — Rust vector database with strong filtering
- [[wiki/data-storage/embeddings|Embeddings]] — the vectors such databases index
- [[wiki/data-storage/hybrid-search|Hybrid Search]] — lexical plus vector retrieval in one system
- [[wiki/data-storage/00-index|Data Storage]] — home directory for storage technologies
- [[wiki/concepts/mykb-research-report|Mykb Research Report]] — surveys vector search options for mykb
