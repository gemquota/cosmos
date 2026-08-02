---
type: "concept"
title: "Crash Recovery"
description: "Checkpoints, log replay, and restart procedures after failure"
tags: ["crash-recovery", "write-ahead-log", "checkpoints", "database-internals"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://www.postgresql.org/docs/current/wal-intro.html", "https://dev.mysql.com/doc/refman/8.4/en/innodb-recovery.html"]
---

# Crash Recovery

## Summary
Crash recovery restores a database to a consistent state after power loss or process failure. Using the write-ahead log plus a known checkpoint, the engine replays committed changes and rolls back uncommitted ones, typically completing in seconds to minutes regardless of how long the database ran.

## Details
- **Restart sequence** — on startup, the engine locates the last checkpoint, reads the log from there, and replays redo records to reconstruct pages that were not flushed. Postgres calls this REDO; InnoDB performs log apply followed by undo rollback.
- **Checkpoints** — a checkpoint marks a log position before which all changes are already on disk. Recovery need only replay records after it; frequent checkpoints shorten recovery but cost write throughput.
- **Crash consistency** — pages may be torn or partially written; InnoDB's doublewrite buffer or filesystem atomic page writes prevent applying a half-written page, while Postgres checks page headers and skips corrupted pages with `ignore_checksum_failure`.
- **Undo and aborted transactions** — records from transactions that never committed are rolled back (InnoDB) or simply ignored because their effects were never visible (Postgres MVCC).
- **Replica recovery** — replicas re-apply the same log stream; if a replica falls behind or loses state, it re-syncs from a base backup plus archived WAL.
- **Operational guidance** — recovery time grows with checkpoint distance and write volume, so teams tune checkpoint intervals, monitor recovery duration, and rehearse failovers.

## Related
- [[wiki/data-storage/write-ahead-logging|Write-Ahead Logging]] — the log recovery replays
- [[wiki/data-storage/backup-strategies|Backup Strategies]] — base backups paired with logs
- [[wiki/data-storage/point-in-time-recovery|Point-in-Time Recovery]] — recovery to an arbitrary moment
- [[wiki/data-storage/rpo-and-rto|RPO and RTO]] — the objectives recovery serves
- [[wiki/devops-infra/point-in-time-recovery|Point-in-Time Recovery]] — operational restore practice
