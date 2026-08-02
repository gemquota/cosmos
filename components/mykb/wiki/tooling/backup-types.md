---
type: "concept"
title: "Backup Types"
description: "Full, incremental, and differential backups and when to use each"
tags: ["backups", "types", "disaster-recovery", "storage"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Backup Types

## Summary
Backup types describe how much data each backup captures: full copies everything, incremental copies changes since the last backup, differential copies changes since the last full. Mixing them trades restore speed against storage cost.

## Details
- Full backups simplify restore; incrementals cut cost but chain restores together.
- Differential backups are a middle ground: bigger than incremental, faster to restore.
- Verify restores from each type — a backup that cannot restore is decoration.
- mykb relevance: the wiki archive does weekly fulls plus daily incrementals.

## Related
- [[wiki/tooling/full-backups|Full Backups]]
- [[wiki/tooling/incremental-backups|Incremental Backups]]
- [[wiki/tooling/backup-verification|Backup Verification]]
- [[wiki/devops-infra/incremental-vs-differential-backups|Incremental vs Differential Backups]]
- [[wiki/compositions/backup-and-restore|Backup and Restore]]
