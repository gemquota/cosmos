---
type: "concept"
title: "Vacuuming & Compaction"
description: "Reclaiming dead rows and merging storage segments"
tags: ["vacuum", "compaction", "postgresql", "storage-maintenance"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://www.postgresql.org/docs/current/routine-vacuuming.html", "https://cassandra.apache.org/doc/latest/cassandra/operating/compaction/index.html"]
---

# Vacuuming & Compaction

## Summary
Vacuuming and compaction are background maintenance processes that reclaim space from dead data and keep storage layouts efficient. MVCC databases leave old row versions behind after updates and deletes; log-structured stores accumulate overlapping sorted segments. Both must be reclaimed or storage and read performance degrade.

## Details
- **Postgres vacuum** — MVCC means `UPDATE`/`DELETE` mark old tuples dead; `VACUUM` removes dead tuples and makes space reusable, and `VACUUM ANALYZE` also refreshes statistics. Autovacuum runs automatically, driven by dead-tuple thresholds, with `n_dead_tup` visible in `pg_stat_user_tables`.
- **Bloat** — when vacuum lags, tables and indexes bloat: queries scan dead rows, and storage grows; `pgstattuple` and `pg_bloat_check` style queries estimate bloat, and `VACUUM FULL` rewrites the table to compact it, taking locks in exchange.
- **Freezing and wraparound** — transaction IDs are finite; Postgres freezes old tuples (`autovacuum_freeze_max_age`) to prevent transaction-ID wraparound, a hard failure mode that makes vacuum not just hygiene but correctness.
- **LSM compaction** — Cassandra, RocksDB, and LevelDB merge overlapping SSTables in the background; size-tiered compaction merges similar-size tables (simpler, higher space overhead), leveled compaction bounds overlapping runs (lower read amplification, more writes). Compaction is also where tombstones are finally discarded.
- **Compaction in wide-column stores** — Cassandra's `nodetool compact` and its table- and keyspace-level strategies determine when SSTables merge; operator tuning balances write amplification, read amplification, and space.
- **Monitoring** — vacuum counts/duration, bloat percentage, compaction backlog, and `pending_compactions` are the signals; scheduled maintenance windows suit large rewrites.

## Related
- [[wiki/data-storage/lsm-trees|LSM Trees]] — the compaction home turf
- [[wiki/data-storage/multiversion-concurrency-control|Multiversion Concurrency Control]] — why dead rows exist
- [[wiki/data-storage/index-maintenance|Index Maintenance]] — the index side of bloat
- [[wiki/data-storage/wide-column-stores|Wide-Column Stores]] — compaction strategies in practice
- [[wiki/data-storage/database-performance-monitoring|Database Performance Monitoring]] — watching bloat and backlogs
- [[wiki/data-storage/crdts|CRDTs]] — tombstone reclamation parallels
