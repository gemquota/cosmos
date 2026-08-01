---
type: "concept"
title: "Qdrant"
description: "Rust vector database with strong payload filtering and hybrid search"
tags: ["qdrant", "vector-database", "rust", "filtering"]
timestamp: "2026-07-31T00:00:00Z"
status: "stub"
---

# Qdrant

## Summary
Qdrant is a Rust-written vector database emphasizing payload filtering, approximate search, and hybrid (dense + sparse) retrieval. Its filtering-first design makes precise scoped queries natural.

## Details
- **Design** — segments of vectors with payload indexes; filtering composes with ANN search.
- **APIs** — gRPC and REST; client libraries for Python and other languages; embedded mode available.
- **Agent relevance** — Qdrant's payload filters map directly to mykb's frontmatter fields (tags, type, timestamp).

## Related
- [[wiki/data-storage/vector-databases|Vector Databases]] — the category
- [[wiki/data-storage/hnsw|HNSW]] — its default index
- [[wiki/data-storage/metadata-filtering|Metadata Filtering]] — Qdrant's signature feature
- [[wiki/data-storage/hybrid-search|Hybrid Search]] — sparse-plus-dense retrieval in Qdrant
- [[wiki/data-storage/index|Data Storage]] — vector database family
