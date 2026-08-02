---
type: "concept"
title: "RPO and RTO"
description: "Recovery point and time objectives for planning"
tags: ["rpo", "rto", "disaster-recovery", "backup"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://docs.aws.amazon.com/whitepapers/latest/disaster-recovery-workloads-on-aws/disaster-recovery-workloads-on-aws.html", "https://learn.microsoft.com/en-us/azure/site-recovery/site-recovery-overview"]
---

# RPO and RTO

## Summary
RPO (recovery point objective) and RTO (recovery time objective) are the two numbers that define acceptable recovery: RPO is how much data loss is tolerable, measured in time, and RTO is how long the service may stay down. Every backup and disaster-recovery architecture is a cost trade-off against these targets.

## Details
- **RPO — how much data you can lose** — the maximum age of data that may be lost on failure: an RPO of 15 minutes means at most the last 15 minutes of writes disappear. RPO is bounded by the replication or backup interval — nightly backups imply up to 24 hours of loss.
- **RTO — how long recovery takes** — the maximum downtime between failure and restored service: an RTO of 1 hour means the restore procedure must complete within an hour. RTO is bounded by restore speed, runbooks, staffing, and whether standby capacity exists.
- **They are separate** — a fast restore with old data meets RTO but not RPO, and vice versa; planning must state both. "We backed up" is not a plan — the plan names numbers and proves the architecture can hit them.
- **Cost relationship** — tighter objectives cost more: synchronous replication and warm standby clusters beat backup-and-restore on both numbers but cost multiples in hardware and complexity; the classic guidance is to size DR to the business value of the data.
- **Measurement** — RPO is usually verifiable by monitoring replication lag and backup freshness; RTO is verifiable only by timed restore drills, which is why disaster-recovery testing is a standing practice rather than a one-time exercise.
- **Setting them** — work backwards from business impact (lost revenue, compliance fines, trust) rather than picking round numbers; then choose architecture (backup and restore, pilot light, warm standby, active/active) that meets both.

## Related
- [[wiki/data-storage/backup-strategies|Backup Strategies]] — the mechanisms behind RPO
- [[wiki/data-storage/disaster-recovery|Disaster Recovery]] — the plan RPO/RTO drive
- [[wiki/data-storage/point-in-time-recovery|Point-in-Time Recovery]] — shrinking RPO with logs
- [[wiki/data-storage/replication-strategies|Replication Strategies]] — synchronous options for low RPO
- [[wiki/data-storage/storage-tiering|Storage Tiering]] — cost-efficient standby footprints
