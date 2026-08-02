---
type: "concept"
title: "Index Rebuild Strategies"
description: "Policies for when and how to rebuild vector indexes as the corpus changes"
tags: ["index", "vector-db", "operations"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Index Rebuild Strategies

## Summary
Policies for when and how to rebuild vector indexes as the corpus changes

## Details
- Full rebuilds, incremental updates, and soft-delete tombstones trade freshness for cost.
- HNSW graphs degrade without periodic rebuilds.
- Strategies include background rebuild, shadow index, and blue-green swap.
- Index freshness directly affects retrieval quality.

## Related
- [[wiki/ai-ml/hnsw-index|HNSW Index]] — graph that needs rebuilds
- [[wiki/ai-ml/vector-database-sharding|Vector Database Sharding]] — rebuilds across shards
- [[wiki/ai-ml/model-versioning-and-registry|Model Versioning and Registry]] — reindexing when embeddings change
- [[wiki/ai-ml/embedding-regression|Embedding Regression]] — detecting embedding drift
- [[wiki/ml-frameworks/data-loaders-and-pipelines|Data Loaders and Pipelines]] — feeding index updates
