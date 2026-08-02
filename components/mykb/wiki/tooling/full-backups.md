---
type: "concept"
title: "Full Backups"
description: "Complete copies of all data taken at a point in time"
tags: ["backups", "full", "disaster-recovery", "storage"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Full Backups

## Summary
A full backup copies everything — every file, every table — so a restore starts from a complete, consistent snapshot. It is the anchor of any backup chain: simplest to restore, most expensive to store.

## Details
- Schedule fulls on a cadence matched to RPO and data-change rates.
- Snapshot-based fulls (filesystem or VM snapshots) are fast but need consistent state capture.
- Keep a small number of fulls plus the increments that extend them.
- mykb relevance: monthly full archives anchor the wiki's recovery chain.

## Related
- [[wiki/tooling/backup-types|Backup Types]]
- [[wiki/tooling/incremental-backups|Incremental Backups]]
- [[wiki/tooling/snapshot-hierarchy|Snapshot Hierarchy]]
- [[wiki/compositions/backup-and-restore|Backup and Restore]]
- [[wiki/tooling/backup-verification|Backup Verification]]
