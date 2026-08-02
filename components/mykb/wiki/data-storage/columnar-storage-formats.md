---
type: "concept"
title: "Columnar Storage Formats"
description: "Storing data by column for fast analytical scans"
tags: ["columnar", "parquet", "orc", "olap"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://en.wikipedia.org/wiki/Column-oriented_DBMS", "https://clickhouse.com/docs/"]
---

# Columnar Storage Formats

## Summary

Columnar formats store each column's values contiguously, so scans touch only needed columns.
They compress well because values within a column share type and patterns.
Columnar storage is the foundation of modern analytics engines.
Columnar formats changed analytics economics: scans that once took minutes now take seconds.

## Details

- Columnar layout maximizes scan throughput and compression ratio.
- Per-column encodings (dictionary, delta, RLE) adapt to data.
- Row-group organization enables skipping and parallelism.
- Parquet and ORC dominate lakes; in-memory formats like Arrow follow the same idea.
- Write cost and update difficulty are the tradeoffs versus row stores.
- They pair with vectorized execution and code generation for peak speed.
- Row-based access on columnar files is slow; choose per workload.
- Columnar formats made analytical queries cheap enough to run interactively, changing how warehouses are built.

## Related

- [[wiki/data-storage/parquet-and-orc|Parquet And Orc]] — file formats
- [[wiki/data-storage/apache-arrow-and-in-memory|Apache Arrow and In-Memory Analytics]] — in-memory columnar
- [[wiki/data-storage/column-pruning-and-vectorized-reads|Column Pruning And Vectorized Reads]] — read path
- [[wiki/data-storage/columnar-storage|Columnar Storage]] — existing note
- [[wiki/data-storage/vectorized-query-execution|Vectorized Query Execution]] — execution
- [[wiki/data-storage/data-quality-dimensions|Data Quality Dimensions]] — quality dimensions
- [[wiki/data-storage/data-observability-and-monitoring|Data Observability And Monitoring]] — observability
- [[wiki/data-storage/data-testing-frameworks|Data Testing Frameworks]] — testing
- [[wiki/data-storage/feature-stores-and-ml-features|Feature Stores And Ml Features]] — ML features
- [[wiki/data-storage/data-contracts-and-agreements|Data Contracts And Agreements]] — data contracts
- [[wiki/data-storage/incremental-loading-strategies|Incremental Loading Strategies]] — incremental loading
- [[wiki/data-storage/schema-evolution-in-streams|Schema Evolution In Streams]] — schema evolution

