---
type: "concept"
title: "Milvus"
description: "Open-source distributed vector database for large-scale similarity search"
tags: ["milvus", "vector-database", "ann", "distributed"]
timestamp: "2026-07-31T00:00:00Z"
status: "stub"
---

# Milvus

## Summary
Milvus is an open-source vector database built for scale: distributed indexing, multiple ANN index types, and metadata filtering. It is a common backend when embedding collections outgrow a single process.

## Details
- **Architecture** — separate storage, index, and query nodes; sharded by design for billion-scale vectors.
- **Indexes** — HNSW, IVF, and disk-based indexes; consistency and durability are first-class.
- **Agent relevance** — a future mykb deployment with many users or massive corpora could host its embedding index in Milvus.

## Related
- [[wiki/data-storage/vector-databases|Vector Databases]] — the category Milvus belongs to
- [[wiki/data-storage/faiss|FAISS]] — the ANN library Milvus builds on
- [[wiki/data-storage/hnsw|HNSW]] — the graph index Milvus offers
- [[wiki/data-storage/embeddings|Embeddings]] — the vectors Milvus indexes
- [[wiki/data-storage/index|Data Storage]] — vector database family
