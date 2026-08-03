---
type: "concept"
title: "Backups"
description: "Restorable copies of data enabling recovery from corruption, deletion, and disasters"
tags: ["backups", "database", "recovery", "disaster-recovery", "data"]
timestamp: "2026-07-31T00:00:00Z"
status: "growing"
---

# Backups

## Summary
Backups are restorable copies of data taken on a schedule. They are the last line of defense against corruption, accidental deletion, and ransomware — replication alone does not protect against these. A backup that is not regularly restored and verified is only a hope.

## Details
- Mechanism: a backup pipeline has four parts — capture (full, incremental, or differential; file copy, logical dump like pg_dump, or storage snapshot), transport (local disk, object storage, tape), retention (how long copies live, governed by RPO/RTO and compliance), and restore (the only step that proves the copy works).
- Concrete examples: nightly pg_dump plus continuous WAL archiving gives point-in-time recovery; a git repository's remote pushes make every commit a restorable point; object-storage versioning gives accidental-delete protection for static assets.
- Failure modes: untested restores (silent corruption or missing files discovered only in a disaster), backup jobs that fail quietly for weeks (alert on staleness, not just job success), retention too short for compliance or forensics, and ransomware reaching mounted backup volumes — mitigated by immutability, offline copies, and least-privilege credentials.
- Tradeoffs: every tier costs storage, bandwidth, and operational time; match the tier to data value and required RTO — hot databases need frequent, fast restores; archives need cheap, infrequent ones. Full backups restore fastest but cost most; incrementals are cheap but depend on the whole chain remaining intact.
- Operational notes: run restore drills, monitor backup age and size, document a runbook per restore type, and separate backup credentials from production credentials.
- RSIS3/mykb relevance: the wiki is git-versioned markdown, so the git remote plus an encrypted export is the cheapest reliable backup; RSIS3's registry and state files deserve the same treatment so loop history and checkpoints survive machine loss.

## Related
- [[wiki/devops-infra/point-in-time-recovery|Point-in-Time Recovery]] — restore to any moment
- [[wiki/devops-infra/replication|Replication]] — availability, not backup
- [[wiki/devops-infra/postgresql|PostgreSQL]] — pg_dump and WAL archiving
- [[wiki/frontend/aws-s3|AWS S3]] — backup object storage
- [[wiki/ops/gap-report|Gap Analysis Report]] — backup gaps tracked
- [[wiki/devops-infra/github-actions|GitHub Actions]] — scheduled, tested backup jobs in CI
