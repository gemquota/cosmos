---
type: "concept"
title: "Geo-Redundancy"
description: "Storing data copies in separate geographic locations to survive site loss"
tags: ["geo-redundancy", "storage", "replication", "disaster-recovery"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Geo-Redundancy

## Summary
Geo-redundancy replicates data across distant locations so a regional event — flood, power loss, provider outage — cannot destroy the only copy. It is the storage half of multi-region strategy.

## Details
- Cloud providers offer geo-replicated storage (S3 CRR, GCS dual-region) with lag measured in minutes.
- Geo copies serve reads and disaster recovery, but not zero-loss writes by default.
- Verify replication actually works: test recovery from the geo copy regularly.
- mykb relevance: the wiki archive geo-mirrors so the knowledge base survives region loss.

## Related
- [[wiki/tooling/multi-region|Multi-Region]]
- [[wiki/compositions/backup-and-restore|Backup and Restore]]
- [[wiki/cloud-infra/data-residency-and-locality|Data Residency and Locality]]
- [[wiki/tooling/multi-region|Geo-Redundancy]]
- [[wiki/tooling/business-continuity|Business Continuity]]
