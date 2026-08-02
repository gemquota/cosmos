---
type: "concept"
title: "Backup Strategies"
description: "Full, incremental, and differential backup planning"
tags: ["backup", "recovery", "rpo", "data-protection"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://www.postgresql.org/docs/current/backup.html", "https://dev.mysql.com/doc/refman/8.4/en/backup-and-recovery.html"]
---

# Backup Strategies

## Summary
A backup strategy defines how copies of data are created, rotated, and restored so that failures can be recovered within target RPO and RTO budgets. The core choices are backup type (full, incremental, differential), storage location and retention, and how backups are verified.

## Details
- **Full backups** — a complete copy of the dataset at a point in time; simple to restore but slow and expensive to produce frequently.
- **Incremental backups** — only changes since the last backup of any kind; cheap and fast, but restore requires replaying the full chain, which raises RTO and risks one bad link invalidating everything.
- **Differential backups** — all changes since the last full backup; larger than incrementals but restore needs only the full plus the latest differential, a middle ground many products use.
- **Physical vs logical** — physical backups copy raw files or page-level changes (e.g., `pg_basebackup`, file snapshots) and restore fast; logical backups dump data as SQL or delimited files (`pg_dump`, `mysqldump`), which are portable but slower to restore.
- **Location and retention** — off-site or object-storage copies survive server loss; retention tiers keep more frequent recent backups and sparser older ones to bound cost.
- **Verification** — a backup is only real when restored successfully; scheduled restore drills, checksums, and `pg_verifybackup`-style checks catch silent corruption before it matters.
- **Integration** — WAL archiving and point-in-time recovery turn full-plus-incremental chains into continuous backup for databases.

## Related
- [[wiki/data-storage/point-in-time-recovery|Point-in-Time Recovery]] — replaying transaction logs on top of backups
- [[wiki/data-storage/rpo-and-rto|RPO and RTO]] — targets a strategy must meet
- [[wiki/data-storage/disaster-recovery|Disaster Recovery]] — the larger failover context
- [[wiki/data-storage/write-ahead-logging|Write-Ahead Logging]] — the log stream that enables PITR
- [[wiki/data-storage/object-storage|Object Storage]] — cheap durable backup targets
- [[wiki/devops-infra/backups|Backups]] — operational runbooks for backup automation
