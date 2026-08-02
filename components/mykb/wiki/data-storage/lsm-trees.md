---
type: "concept"
title: "LSM Trees"
description: "Memtables, SSTables, and leveled compaction in log-structured stores"
tags: ["lsm-tree", "sstable", "compaction", "write-optimized"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://cassandra.apache.org/doc/latest/cassandra/architecture/storage-engine.html", "https://github.com/google/leveldb/blob/main/doc/impl.md"]
---

# LSM Trees

## Summary
A log-structured merge (LSM) tree turns random writes into sequential appends. Writes land in an in-memory memtable, flush to immutable sorted string tables (SSTables), and background compaction merges overlapping levels — a design that makes write-heavy and time-series workloads fast at the cost of read amplification.

## Details
- **Write path** — inserts and updates append to a write-ahead log for durability, then mutate an in-memory memtable; when the memtable fills, it is flushed as a sorted SSTable.
- **Read path** — a lookup probes the memtable, then each SSTable level from newest to oldest; per-level bloom filters skip tables that cannot contain the key.
- **Compaction** — merges overlapping SSTables into larger sorted runs, discarding stale versions of keys. Leveled compaction bounds the number of overlapping tables per level; size-tiered compaction instead merges similarly sized tables.
- **Amplification** — LSM designs trade space and read amplification for low write amplification; point reads, especially for rarely read keys, may touch many files unless bloom filters are used.
- **Representative systems** — LevelDB and RocksDB are embedded LSM stores; Cassandra, HBase, InfluxDB, and many key-value engines use LSM variants; PostgreSQL 16's `zheap`-era work and MySQL's InnoDB remain B-tree based, so LSM is a design axis rather than a default.

## Related
- [[wiki/data-storage/vacuuming-and-compaction|Vacuuming & Compaction]] — reclaiming dead data in both LSM and heap engines
- [[wiki/data-storage/write-ahead-logging|Write-Ahead Logging]] — durability layer under the memtable
- [[wiki/data-storage/storage-engines|Storage Engines]] — where LSM sits relative to the SQL layer
- [[wiki/data-storage/buffer-pool-management|Buffer Pool Management]] — the B-tree-world analogue
- [[wiki/data-storage/time-series-databases|Time-Series Databases]] — append-heavy workloads LSM suits
- [[wiki/data-storage/wide-column-stores|Wide-Column Stores]] — Cassandra-style LSM consumers
