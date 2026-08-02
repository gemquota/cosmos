---
type: "concept"
title: "Backup and Restore"
description: "Protecting data with copies that have been proven recoverable"
tags: ["backup", "restore", "disaster-recovery", "data"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://en.wikipedia.org/wiki/Backup", "https://en.wikipedia.org/wiki/Business_continuity_planning"]
---

# Backup and Restore

## Summary
Backup and restore is the discipline of copying data so it can be recovered after loss — and proving the copies work. The definition of a good backup is not that it exists, but that it restores; verification and drills are the heart of the practice.

## Details
- Design with RPO and RTO: how much loss is acceptable and how fast must recovery be?
- Layer backup types: full anchors with incremental chains, plus replication for the shortest RPO.
- The 3-2-1 rule is a baseline: three copies, two media, one offsite — immutability protects against ransomware.
- Restore is the test: automated verification and scheduled restore drills catch silent corruption.
- Secrets and access: backups must be encrypted and restore paths need tested credentials.
- For the mykb bundle, the wiki archives article history with fulls plus incremental sync to object storage.
- Worked example — the wiki archive keeps weekly fulls and daily increments in geo-redundant object storage with object lock; a monthly drill restores to a scratch tree and diffs against the live bundle.

Worked example — the wiki archive keeps weekly fulls and daily increments in geo-redundant object storage with object lock; a monthly drill restores to a scratch tree and diffs against the live bundle.

## Related
- [[wiki/tooling/backup-types|Backup Types]]
- [[wiki/tooling/rpo-rto|RPO/RTO]]
- [[wiki/tooling/backup-verification|Backup Verification]]
- [[wiki/tooling/immutability-backups|Immutability Backups]]
- [[wiki/tooling/business-continuity|Business Continuity]]
- [[wiki/tooling/restore-drills|Restore Drills]]
- [[wiki/tooling/full-backups|Full Backups]]
- [[wiki/tooling/incremental-backups|Incremental Backups]]
- [[wiki/devops-infra/backups|Backups]]
- [[wiki/devops-infra/point-in-time-recovery|Point-in-Time Recovery]]
