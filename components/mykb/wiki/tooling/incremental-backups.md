---
type: "concept"
title: "Incremental Backups"
description: "Backups that store only data changed since the previous backup"
tags: ["backups", "incremental", "disaster-recovery", "storage"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Incremental Backups

## Summary
Incremental backups capture only the changes since the last backup — much smaller and faster than fulls, but restores must replay the whole chain. They are the standard cost-control for large datasets.

## Details
- The restore chain (full + all increments) is only as good as its weakest link; test it.
- Deduplicating backups (restic, Borg) collapse many increments into efficient storage.
- Corruption in one increment breaks every restore that needs it — verify and guard.
- mykb relevance: the wiki archive uses incremental sync with periodic full anchors.

## Related
- [[wiki/tooling/backup-types|Backup Types]]
- [[wiki/tooling/full-backups|Full Backups]]
- [[wiki/tooling/backup-verification|Backup Verification]]
- [[wiki/devops-infra/backup-tools-restic-borg|Backup Tools: Restic/Borg]]
- [[wiki/tooling/rpo-rto|RPO/RTO]]
