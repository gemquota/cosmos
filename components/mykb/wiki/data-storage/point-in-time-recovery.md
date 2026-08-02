---
type: "concept"
title: "Point-in-Time Recovery"
description: "Restoring to arbitrary timestamps via transaction logs"
tags: ["pitr", "recovery", "wal", "backup"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://www.postgresql.org/docs/current/continuous-archiving.html", "https://dev.mysql.com/doc/refman/8.4/en/point-in-time-recovery.html"]
---

# Point-in-Time Recovery

## Summary
Point-in-time recovery (PITR) restores a database to any moment within a retention window by combining a base backup with replayed transaction logs. Instead of being limited to the last backup, an administrator can roll forward to just before an error, a bad migration, or a destructive statement.

## Details
- **The mechanism** — a full or base backup establishes a starting state; then archived log segments are replayed in order up to a chosen point. Postgres uses a base backup plus archived WAL with `recovery_target_time` or `recovery_target_lsn`; MySQL replays binary logs (`mysqlbinlog`) up to a timestamp or log position.
- **What it protects against** — human error is the main use: a dropped table, a bad `UPDATE`, or a broken deployment can be undone by restoring to just before the incident; it also guards against partial corruption and provides an audit-grade recovery path.
- **Requirements** — continuous WAL archiving or binlog retention, plus a base backup; without logs covering the target time, recovery can only reach the last available segment. Managed clouds (RDS, Cloud SQL, Aurora) expose this as "restore to any point in the last N days".
- **Restore procedure** — provision a new instance (PITR normally restores to a new database, never overwriting the primary in place), apply the base backup, replay logs to the target, then verify data and application behavior before promoting.
- **Caveats** — replaying to a precise second requires a transaction boundary near the target, otherwise the recovery stops at the first transaction after it; large log chains make restore slow, which is why periodic base backups bound replay length.
- **Relationship to backups** — PITR upgrades a point-in-time backup chain into a continuous recovery capability; RPO becomes minutes (archiving lag) rather than the backup interval.

## Related
- [[wiki/data-storage/backup-strategies|Backup Strategies]] — the base layer PITR builds on
- [[wiki/data-storage/write-ahead-logging|Write-Ahead Logging]] — the replayed log stream
- [[wiki/data-storage/crash-recovery|Crash Recovery]] — replaying logs after failure
- [[wiki/data-storage/rpo-and-rto|RPO and RTO]] — the objectives PITR improves
- [[wiki/data-storage/disaster-recovery|Disaster Recovery]] — PITR inside larger recovery plans
