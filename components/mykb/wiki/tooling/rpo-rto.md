---
type: "concept"
title: "RPO/RTO"
description: "The recovery point and recovery time objectives that define disaster recovery targets"
tags: ["rpo", "rto", "disaster-recovery", "planning"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# RPO/RTO

## Summary
RPO (recovery point objective) is how much data loss is acceptable; RTO (recovery time objective) is how long recovery may take. Together they define the backup frequency, replication strategy, and failover design of a system.

## Details
- RPO drives backup cadence: an hour of acceptable loss means at most hourly backups.
- RTO drives warmth: a five-minute RTO requires hot standbys, not tape restores.
- Set them per system — a wiki's RPO/RTO differ from a payment ledger's.
- mykb relevance: the wiki targets near-zero RPO via continuous sync and minutes of RTO.

## Related
- [[wiki/tooling/backup-types|Backup Types]]
- [[wiki/tooling/failover-practice|Failover Practice]]
- [[wiki/tooling/business-continuity|Business Continuity]]
- [[wiki/tooling/restore-drills|Restore Drills]]
- [[wiki/compositions/backup-and-restore|Backup and Restore]]
