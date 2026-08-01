---
type: "concept"
title: "Disaster Recovery"
description: "Planning and mechanisms to restore service after region-scale failures, defined by RPO and RTO"
tags: ["disaster-recovery", "rto", "rpo", "backups", "resilience"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://docs.aws.amazon.com/whitepapers/latest/disaster-recovery-workloads-on-aws/disaster-recovery-workloads-on-aws.html"]
---

# Disaster Recovery

## Summary
Disaster recovery is the plan and technology stack for surviving catastrophic failures — lost regions, data centers, or entire providers. It is quantified by RPO (how much data may be lost) and RTO (how long recovery may take). Strategies range from backup-and-restore to active-active replication, chosen against the cost of downtime.

## Details
- Objectives: RPO is the maximum acceptable data loss in time (e.g., 15 minutes of writes), RTO is the maximum acceptable downtime after failure; both are business decisions.
- Strategy ladder, from cheapest to fastest: backup-and-restore (hours), pilot light (minimal core running, scale up on failover), warm standby (reduced fleet running), and multi-site active-active (both regions serve traffic).
- Data protection: backups, snapshots, and replication are the raw material — but a backup only counts if restores are tested; see snapshot strategies.
- Failover mechanics: DNS and load-balancer switches, database promotion, and automated runbooks; failback is often harder than failover and needs rehearsal.
- Testing is mandatory: untested DR plans fail in real disasters; regular game days verify RTO/RPO claims.
- Cost trade-off: active-active costs the most to run but recovers fastest; the right tier depends on the service's value.
- For mykb, DR means the wiki's content and agent state surviving a host loss: versioned exports in object storage, replicated database, and a tested restore script.

## Related
- [[wiki/cloud-infra/snapshot-strategies|Snapshot Strategies]] — point-in-time copies as the DR baseline
- [[wiki/cloud-infra/availability-zones|Availability Zones]] — failure domains for failover placement
- [[wiki/cloud-infra/multi-cloud-strategy|Multi-Cloud Strategy]] — provider-level DR ambitions
- [[wiki/devops-infra/backups|Backups]] — the restore-and-recover tier
- [[wiki/devops-infra/point-in-time-recovery|Point-in-Time Recovery]] — fine-grained restore semantics
- [[wiki/devops-infra/replication|Replication]] — keeping a standby current
