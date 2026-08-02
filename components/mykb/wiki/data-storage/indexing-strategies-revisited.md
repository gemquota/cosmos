---
type: "concept"
title: "Indexing Strategies Revisited"
description: "Choosing index types and designs for your query patterns"
tags: ["indexing", "performance", "databases", "query-tuning"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://www.postgresql.org/docs/current/indexes.html", "https://en.wikipedia.org/wiki/Database_index"]
---

# Indexing Strategies Revisited

## Summary

Indexes trade write cost and storage for faster reads.
The right index depends on selectivity, query shape, and cardinality.
Indexing is iterative: measure, index, and re-measure.
Indexes are only useful if the planner chooses them; keep statistics fresh and analyze hot queries.

## Details

- Types: B-tree, hash, bitmap, GIN/GiST, and covering indexes.
- Composite indexes match multi-column predicates and ORDER BY.
- Partial and expression indexes target narrow hot paths.
- Index bloat and maintenance need regular attention.
- Query planners use statistics to choose indexes; stale stats mislead.
- Measure index hit ratios and drop indexes nobody uses.
- Index bloat from updates needs periodic reindexing.
- Index design is iterative; review query logs quarterly and adjust indexes to the workload that actually exists.

## Related

- [[wiki/data-storage/b-tree-and-lsm-trees|B-Trees and LSM Trees]] — underlying structures
- [[wiki/data-storage/query-planning-and-optimization|Query Planning And Optimization]] — planner use
- [[wiki/data-storage/composite-indexes|Composite Indexes]] — composite
- [[wiki/data-storage/covering-indexes|Covering Indexes]] — covering
- [[wiki/data-storage/index-maintenance|Index Maintenance]] — maintenance
- [[wiki/data-storage/data-quality-dimensions|Data Quality Dimensions]] — quality dimensions
- [[wiki/data-storage/data-observability-and-monitoring|Data Observability and Monitoring]] — observability
- [[wiki/data-storage/data-testing-frameworks|Data Testing Frameworks]] — testing
- [[wiki/data-storage/feature-stores-and-ml-features|Feature Stores and ML Features]] — ML features
- [[wiki/data-storage/data-contracts-and-agreements|Data Contracts and Agreements]] — data contracts
- [[wiki/data-storage/incremental-loading-strategies|Incremental Loading Strategies]] — incremental loading
- [[wiki/data-storage/schema-evolution-in-streams|Schema Evolution In Streams]] — schema evolution
- [[wiki/data-storage/streaming-sinks-and-sources|Streaming Sinks And Sources]] — streams

