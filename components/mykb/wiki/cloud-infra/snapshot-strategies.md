---
type: "concept"
title: "Snapshot Strategies"
description: "Scheduling point-in-time copies of volumes and databases for recovery and rollback"
tags: ["snapshots", "backup", "recovery", "data"]
timestamp: "2026-08-01T00:00:00Z"
status: "stub"
---

# Snapshot Strategies

## Summary
Snapshots capture the state of a volume or database at a moment in time, cheaply and quickly, for restore or rollback.

## Details
- Cloud volume snapshots are incremental and fast; restores create a new volume from the snapshot.
- Cadence is a recovery decision: RPO dictates how often, retention how long.
- Snapshots complement logical backups — they recover the machine, not necessarily the data semantics.
- Open question: how snapshot-based recovery and point-in-time database recovery should be combined.

## Related
- [[wiki/devops-infra/disaster-recovery|Disaster Recovery]] — snapshots are the DR baseline
- [[wiki/devops-infra/point-in-time-recovery|Point-in-Time Recovery]] — finer-grained recovery option
- [[wiki/devops-infra/backups|Backups]] — snapshots as one backup form
- [[wiki/devops-infra/replication|Replication]] — live alternative to snapshots
