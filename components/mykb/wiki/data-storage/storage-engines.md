---
type: "concept"
title: "Storage Engines"
description: "Pluggable heap, LSM, and columnar engines behind one SQL layer"
tags: ["storage-engine", "database-internals", "lsm", "heap"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://dev.mysql.com/doc/refman/8.4/en/innodb-storage-engine.html", "https://www.postgresql.org/docs/current/storage.html"]
---

# Storage Engines

## Summary
A storage engine manages how rows are physically organized, indexed, and made durable beneath the SQL layer. MySQL's pluggable architecture and PostgreSQL's fixed heap design show two ways to separate storage from query processing.

## Details
- **Engine interface** — MySQL exposes a table-handler API so `InnoDB`, `MyISAM`, and `RocksDB` coexist behind one SQL layer; each engine supplies its own indexing, locking, and transaction support.
- **Heap plus indexes (Postgres)** — data rows live in an unordered heap; every index stores pointers to heap tuples via CTIDs, so index maintenance is independent of physical order.
- **Clustered index engines (InnoDB)** — the primary key orders the data pages themselves; secondary indexes point at the primary key, so changing the PK forces a full table rebuild.
- **LSM engines (RocksDB)** — append-only writes feed memtables and SSTables, trading read complexity for write throughput; popular for write-heavy workloads and embedded use.
- **Columnar engines** — analytic engines store per-column data and skip indexes in favor of scans and compression; see ClickHouse's MergeTree and DuckDB's column blocks.
- **mykb relevance** — Postgres (heap) and DuckDB (columnar) cover transactional and analytical reads here; matching the engine to the query pattern matters more than SQL dialect.

## Related
- [[wiki/data-storage/lsm-trees|LSM Trees]] — the write-optimized engine family
- [[wiki/data-storage/b-tree-indexing|B-Tree Indexing]] — the index structure most engines build on
- [[wiki/data-storage/columnar-storage|Columnar Storage]] — the analytical engine layout
- [[wiki/data-storage/clustered-tables|Clustered Tables]] — physical ordering choices inside engines
- [[wiki/data-storage/buffer-pool-management|Buffer Pool Management]] — caching inside the engine
- [[wiki/data-storage/write-ahead-logging|Write-Ahead Logging]] — durability mechanics shared by engines
