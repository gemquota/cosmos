---
type: "concept"
title: "Indexes"
description: "The data structures that make lookups fast"
tags: ["indexes", "performance", "databases", "query-tuning"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://www.postgresql.org/docs/current/indexes.html", "https://en.wikipedia.org/wiki/Database_index"]
---

# Indexes

## Summary

Indexes accelerate reads by organizing data for fast lookup.
They cost write overhead and storage.
Index design follows query patterns.
An index is a bet on future queries; place bets where evidence exists.

## Details

- B-tree, hash, bitmap, and GIN/GiST cover different workloads.
- Composite and covering indexes match multi-column queries.
- Partial indexes target hot subsets; expression indexes index functions.
- Planner statistics decide index usage; vacuum/reindex keep them healthy.
- Over-indexing slows writes; measure before adding.
- Index maintenance is part of the cost, not just creation.
- Use EXPLAIN to verify indexes are actually used.
- Indexes are the highest-leverage performance feature in relational databases.

## Related

- [[wiki/data-storage/indexing-strategies-revisited|Indexing Strategies Revisited]] — strategy
- [[wiki/data-storage/query-planning-and-optimization|Query Planning And Optimization]] — planner
- [[wiki/data-storage/index-maintenance|Index Maintenance]] — maintenance
- [[wiki/data-storage/hash-indexes|Hash Indexes]] — hash
- [[wiki/data-storage/data-quality-dimensions|Data Quality Dimensions]] — quality dimensions
- [[wiki/data-storage/data-observability-and-monitoring|Data Observability and Monitoring]] — observability
- [[wiki/data-storage/data-testing-frameworks|Data Testing Frameworks]] — testing
- [[wiki/data-storage/feature-stores-and-ml-features|Feature Stores and ML Features]] — ML features
- [[wiki/data-storage/data-contracts-and-agreements|Data Contracts and Agreements]] — data contracts
- [[wiki/data-storage/incremental-loading-strategies|Incremental Loading Strategies]] — incremental loading
- [[wiki/data-storage/schema-evolution-in-streams|Schema Evolution In Streams]] — schema evolution
- [[wiki/data-storage/streaming-sinks-and-sources|Streaming Sinks And Sources]] — streams

