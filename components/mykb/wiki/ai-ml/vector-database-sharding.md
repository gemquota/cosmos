---
type: "concept"
title: "Vector Database Sharding"
description: "Partitioning a vector index across nodes to scale beyond a single machine"
tags: ["vector-db", "scaling", "sharding"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Vector Database Sharding

## Summary
Partitioning a vector index across nodes to scale beyond a single machine

## Details
- Shards split vectors by hash, cluster, or tenant and route queries to relevant nodes.
- Needed for billions of vectors or high query volume.
- Shard choice affects recall, latency, and cross-shard queries.
- Managed systems hide much of this behind a distributed index.

## Related
- [[wiki/ai-ml/hnsw-index|HNSW Index]] — graph index built per shard
- [[wiki/data-storage/vector-databases|Vector Databases]] — systems that shard
- [[wiki/ai-ml/index-rebuild-strategies|Index Rebuild Strategies]] — rebalancing shards
- [[wiki/ai-ml/hybrid-search-systems|Hybrid Search Systems]] — sharded lexical+dense search
- [[wiki/ai-ml/embeddings-and-vector-search|Embeddings and Vector Search]] — scale pressure source
