---
type: "entity"
title: "Milvus"
description: "Open-source distributed vector database for large-scale similarity search"
tags: ["milvus", "vector-database", "ann", "distributed"]
timestamp: "2026-07-31T00:00:00Z"
status: "growing"
---

# Milvus

## Summary
Milvus is an open-source vector database built for scale: distributed indexing, multiple ANN index types, and metadata filtering. It is a common backend when embedding collections outgrow a single process — separating storage, index, and query nodes to serve billion-scale similarity search.

## Details
- Architecture: storage, index, and query nodes are separate and scalable independently; collections, partitions, and shards organize data; consistency and durability are first-class; HNSW, IVF, and disk-based indexes are selectable per collection.
- Capabilities: metadata filtering combined with vector search (hybrid queries); scalar indexes on fields; incremental indexing and compaction; SDKs and a query language beyond raw ANN calls.
- Concrete example: a wiki with millions of embedded articles stores vectors in Milvus with HNSW; queries filter by tag and date while ranking by embedding similarity; a new article embeds and indexes incrementally; the collection scales by adding query nodes.
- Failure modes: index builds lagging ingestion, serving stale vectors; memory pressure from HNSW on large collections; filtering that forces full scans, killing latency; cluster operations underestimated — nodes, shards, and compaction need tuning; consistency settings that trade freshness for latency without clear policy.
- Tradeoffs: Milvus manages lifecycle, replication, and serving at the cost of operating a distributed system; the alternative, an embedded library (FAISS), is simpler and single-node; the mature pattern is Milvus when the corpus and concurrency outgrow in-process search.
- Operational notes: monitor index lag and query latency, size nodes from recall benchmarks, and test failover.
- RSIS3 relevance: a future mykb deployment with many users or massive corpora could host its embedding index in Milvus — the scale-out path for semantic retrieval.

## Practice
- Benchmark recall and latency on the real query mix before committing, since index and node choices lock in performance.
## Related
- [[wiki/data-storage/vector-databases|Vector Databases]] — the category Milvus belongs to
- [[wiki/data-storage/faiss|FAISS]] — the ANN library Milvus builds on
- [[wiki/data-storage/hnsw|HNSW]] — the graph index Milvus offers
- [[wiki/data-storage/embeddings|Embeddings]] — the vectors Milvus indexes
- [[wiki/data-storage/00-index|Data Storage]] — vector database family
