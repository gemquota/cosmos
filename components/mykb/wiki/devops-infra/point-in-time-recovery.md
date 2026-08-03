---
type: "concept"
title: "Point-in-Time Recovery"
description: "Restoring a database to an arbitrary moment using full backups plus archived transaction logs"
tags: ["pitr", "backups", "recovery", "database", "postgresql"]
timestamp: "2026-07-31T00:00:00Z"
status: "growing"
---

# Point-in-Time Recovery

## Summary
Point-in-Time Recovery (PITR) restores a database to any moment by replaying archived WAL (write-ahead log) segments over a full backup. It recovers from mistakes — a bad migration, an accidental delete, a bad update — not just from crashes: any event with a timestamp can be undone.

## Details
- Mechanics: take a base backup (pg_basebackup or a full snapshot), enable continuous WAL archiving to durable storage, and keep an archive log. At recovery, restore the base backup, configure recovery_target_time (or recovery_target_lsn/xid), and replay WAL up to that point; Postgres stops exactly at the target, producing a consistent database as of that instant.
- Concrete example: a migration drops a table at 14:03; recovery targets 14:02:59, replays the archived WAL, and the table is back; a mistakenly deleted customer record is recovered the same way; the same archive supports a standby or a second instance for forensics.
- Failure modes: WAL archiving gaps — a segment never archived (checkpoint stalls, archive_command failures) makes recovery silently miss transactions; retention that is too short for the lookback you need (object storage with lifecycle rules is the answer for long windows); recovery_target_time without a matching stop point in the WAL, restoring to the nearest segment boundary; running PITR on the primary instead of a restored copy; archive storage corrupted or encrypted-with-lost-keys.
- Tradeoffs: PITR gives precise, mistake-reversing recovery at the cost of archive storage, archiving overhead, and restore time proportional to WAL volume; it complements, not replaces, replication — replication answers failover, PITR answers restore-to-before; the operational bill is regular restore drills that actually exercise the target-time path.
- Operational notes: automate archive verification, run quarterly PITR drills in CI, and document the recovery_target workflow in the runbook.
- RSIS3 relevance: if the MyKB store ever lands in Postgres, PITR is the mechanism for undoing a bad wiki-wide edit or migration — the memory layer deserves the same mistake-recovery guarantees as any production database.

## Related
- [[wiki/devops-infra/backups|Backups]] — PITR builds on base backups
- [[wiki/devops-infra/replication|Replication]] — the availability complement
- [[wiki/devops-infra/postgresql|PostgreSQL]] — WAL archiving setup
- [[wiki/frontend/aws-s3|AWS S3]] — WAL archive target
- [[wiki/tooling/alembic|Alembic]] — migrations that make PITR necessary
- [[wiki/devops-infra/github-actions|GitHub Actions]] — restore drills run in CI
