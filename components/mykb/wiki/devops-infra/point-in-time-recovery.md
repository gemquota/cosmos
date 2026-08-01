---
type: "concept"
title: "Point-in-Time Recovery"
description: "Restoring a database to an arbitrary moment using full backups plus archived transaction logs"
tags: ["pitr", "backups", "recovery", "database", "postgresql"]
timestamp: "2026-07-31T00:00:00Z"
status: "stub"
---

# Point-in-Time Recovery

## Summary
Point-in-Time Recovery (PITR) restores a database to any moment by replaying archived WAL (write-ahead log) segments over a full backup. It recovers from mistakes, not just crashes.

## Details
- Mechanics: base backup + continuous WAL archiving + `pg_rewind`/`pg_restore` style replay to a target time.
- Recovery windows depend on WAL retention — archive to object storage for long lookbacks.
- Distinguish from replication: PITR answers "restore to before the bad migration", not failover.

## Related
- [[wiki/devops-infra/backups|Backups]] — PITR builds on base backups
- [[wiki/devops-infra/replication|Replication]] — the availability complement
- [[wiki/devops-infra/postgresql|PostgreSQL]] — WAL archiving setup
- [[wiki/frontend/aws-s3|AWS S3]] — WAL archive target
- [[wiki/tooling/alembic|Alembic]] — migrations that make PITR necessary
- [[wiki/devops-infra/github-actions|GitHub Actions]] — restore drills run in CI
