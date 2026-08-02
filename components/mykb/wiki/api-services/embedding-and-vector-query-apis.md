---
type: "concept"
title: "Embedding and Vector Query APIs"
description: "Serving semantic search over vector indexes"
tags: ["embeddings", "vector-search", "api-design", "semantic-search"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Embedding and Vector Query APIs

## Summary

A stub to be expanded into a full article; frames the concept and open questions.

## Details

- Vector APIs accept an embedding or raw text and return nearest neighbors by similarity.
- Support filters, hybrid search, and metadata post-filtering.
- Index types (HNSW, IVF) trade recall, latency, and memory.
- Version embeddings: models change, so store model IDs with vectors.

## Related

- [[wiki/data-storage/embeddings|Embeddings]] — embeddings
- [[wiki/data-storage/vector-databases|Vector Databases]] — vector storage
- [[wiki/data-storage/hnsw|HNSW]] — HNSW index
- [[wiki/data-storage/vector-databases-revisited|Vector Databases Revisited]] — vector DB design
- [[wiki/data-storage/data-engineering-fundamentals|Data Engineering Fundamentals]] — core data engineering concepts
