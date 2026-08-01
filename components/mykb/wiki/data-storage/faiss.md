---
type: "concept"
title: "FAISS"
description: "Facebook's library for efficient similarity search and clustering of dense vectors"
tags: ["faiss", "ann", "similarity-search", "library"]
timestamp: "2026-07-31T00:00:00Z"
status: "stub"
---

# FAISS

## Summary
FAISS (Facebook AI Similarity Search) is the foundational open-source library for approximate nearest-neighbour search over dense vectors, written in C++ with Python bindings. Most vector databases build on ideas it made standard.

## Details
- **Capabilities** — IVF, HNSW, PQ, and scalar/quantization indexes; GPU support; batch search and clustering.
- **Role** — a library, not a server: you manage indexes and persistence yourself.
- **Agent relevance** — a local FAISS index over mykb embeddings gives in-process semantic search with full control.

## Related
- [[wiki/data-storage/vector-databases|Vector Databases]] — FAISS is often the engine inside them
- [[wiki/data-storage/hnsw|HNSW]] — the graph index FAISS implements
- [[wiki/data-storage/ivf|IVF Index]] — the inverted-file index FAISS popularized
- [[wiki/data-storage/product-quantization|Product Quantization]] — compression FAISS supports
- [[wiki/data-storage/embeddings|Embeddings]] — the vectors FAISS searches
- [[wiki/data-storage/index|Data Storage]] — ANN libraries
