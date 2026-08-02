---
type: "concept"
title: "Write-Ahead Logging"
description: "Durable redo/undo records written before data pages"
tags: ["write-ahead-log", "durability", "crash-recovery", "database-internals"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://www.postgresql.org/docs/current/wal-intro.html", "https://dev.mysql.com/doc/refman/8.4/en/innodb-redo-log.html"]
---

# Write-Ahead Logging

## Summary
Write-ahead logging (WAL) is the durability foundation of almost every database: before a dirty page is written to disk, a redo record describing the change is appended to a sequential log. On crash, the log is replayed to reconstruct any change that did not reach the data files.

## Details
- **The WAL rule** — a change is durable only when its log record is flushed to stable storage; data pages may lag behind. This turns random page writes into sequential log appends, the core performance win.
- **Redo vs undo** — redo records allow replaying committed changes; undo (or rollback) segments allow reverting uncommitted changes. Postgres's WAL is primarily redo with hints, while InnoDB keeps separate redo and undo logs.
- **Group commit** — multiple transactions' records are flushed in one fsync, amortizing the cost of durability; Postgres and InnoDB both support it.
- **Checkpoints** — periodic checkpoints flush dirty pages so the log can be truncated; the distance between checkpoints bounds recovery time, and forcing too many checkpoints causes write spikes.
- **WAL as a side channel** — log shipping (Postgres streaming replication, MySQL binlog-based replicas) reuses the log for replication; change data capture tools consume the same stream.
- **Trade-offs** — synchronous commits guarantee durability but pay fsync latency; `synchronous_commit = off` or `innodb_flush_log_at_trx_commit < 1` trade durability for throughput.

## Related
- [[wiki/data-storage/crash-recovery|Crash Recovery]] — replaying WAL after restart
- [[wiki/data-storage/acid-transactions|ACID Transactions]] — durability is the D
- [[wiki/data-storage/buffer-pool-management|Buffer Pool Management]] — pages that lag behind the log
- [[wiki/data-storage/point-in-time-recovery|Point-in-Time Recovery]] — log replay to arbitrary times
- [[wiki/data-storage/replication-strategies|Replication Strategies]] — log-based replication
