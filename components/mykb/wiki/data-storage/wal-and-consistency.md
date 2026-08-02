---
type: "concept"
title: "WAL and Consistency"
description: "Write-ahead logging as the durability backbone of databases"
tags: ["wal", "durability", "crash-recovery", "databases"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://www.postgresql.org/docs/current/wal-intro.html", "https://en.wikipedia.org/wiki/Write-ahead_logging"]
---

# WAL and Consistency

## Summary

Write-ahead logging (WAL) records every change before the data pages are modified.
On crash, the database replays the log to restore consistency.
WAL is why databases can offer durable commits at high speed.
WAL design directly determines durability, recovery speed, and replication options.

## Details

- A commit is durable once its WAL record is flushed to stable storage.
- Group commit batches fsyncs to improve throughput.
- Postgres, MySQL, and most engines expose WAL for replication and PITR.
- WAL archives enable continuous backup and point-in-time recovery.
- WAL and MVCC together give crash safety plus concurrent readers.
- Checkpoint tuning balances crash recovery time against write throughput.
- WAL archiving is the foundation of point-in-time recovery.
- WAL tuning is a durability-and-performance knob; measure both before and after changing checkpoint or sync settings.

## Related

- [[wiki/data-storage/mvcc-and-isolation-levels|MVCC and Isolation Levels]] — concurrency companion
- [[wiki/data-storage/backup-restore-and-pitr-revisited|Backup, Restore, and PITR Revisited]] — WAL-based recovery
- [[wiki/data-storage/physical-replication|Physical Replication]] — WAL shipping
- [[wiki/data-storage/write-ahead-logging|Write-Ahead Logging]] — existing note
- [[wiki/data-storage/crash-recovery|Crash Recovery]] — recovery
- [[wiki/data-storage/data-quality-dimensions|Data Quality Dimensions]] — quality dimensions
- [[wiki/data-storage/data-observability-and-monitoring|Data Observability and Monitoring]] — observability
- [[wiki/data-storage/data-testing-frameworks|Data Testing Frameworks]] — testing
- [[wiki/data-storage/feature-stores-and-ml-features|Feature Stores and ML Features]] — ML features
- [[wiki/data-storage/data-contracts-and-agreements|Data Contracts and Agreements]] — data contracts
- [[wiki/data-storage/incremental-loading-strategies|Incremental Loading Strategies]] — incremental loading
- [[wiki/data-storage/schema-evolution-in-streams|Schema Evolution In Streams]] — schema evolution
- [[wiki/data-storage/streaming-sinks-and-sources|Streaming Sinks And Sources]] — streams

