---
type: "concept"
title: "Backups"
description: "Restorable copies of data enabling recovery from corruption, deletion, and disasters"
tags: ["backups", "database", "recovery", "disaster-recovery", "data"]
timestamp: "2026-07-31T00:00:00Z"
status: "stub"
---

# Backups

## Summary
Backups are restorable copies of data taken on a schedule. They are the last line of defense against corruption, accidental deletion, and ransomware — replication alone does not protect against these.

## Details
- Types: full, incremental, and differential; test restores regularly — an untested backup is a guess.
- Retention policy balances cost vs recovery window; offsite/object-storage copies survive site loss.
- The wiki itself is git-versioned markdown — the ultimate cheap backup for mykb.

## Related
- [[wiki/devops-infra/point-in-time-recovery|Point-in-Time Recovery]] — restore to any moment
- [[wiki/devops-infra/replication|Replication]] — availability, not backup
- [[wiki/devops-infra/postgresql|PostgreSQL]] — pg_dump and WAL archiving
- [[wiki/frontend/aws-s3|AWS S3]] — backup object storage
- [[wiki/ops/gap-report|Gap Analysis Report]] — backup gaps tracked
- [[wiki/devops-infra/github-actions|GitHub Actions]] — scheduled, tested backup jobs in CI
