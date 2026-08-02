---
type: "concept"
title: "Disaster Recovery"
description: "Failover, geo-redundancy, and recovery drills"
tags: ["disaster-recovery", "failover", "geo-redundancy", "business-continuity"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://learn.microsoft.com/en-us/azure/architecture/resiliency/disaster-recovery", "https://docs.aws.amazon.com/whitepapers/latest/disaster-recovery-workloads-on-aws/disaster-recovery-workloads-on-aws.html"]
---

# Disaster Recovery

## Summary
Disaster recovery (DR) is the practice of restoring systems and data after a catastrophic failure — loss of a data center, region, or primary infrastructure. Where backups protect against data loss, DR protects against loss of service, using failover, geo-redundancy, and rehearsed recovery procedures to meet RPO and RTO targets.

## Details
- **Scope of a disaster** — DR addresses large-scale events: site loss, prolonged power or network outage, ransomware, or operator error that takes out the primary environment. It is distinct from routine recovery of a single crashed server.
- **Recovery tiers** — AWS's four-tier model ranges from backup-and-restore (highest RTO/RPO, lowest cost) through pilot light (replicated data, minimal running footprint), warm standby (scaled-down live copy), to multi-site active/active (near-zero RTO/RPO, highest cost).
- **Failover mechanics** — databases fail over via promoted replicas or managed services (Postgres standby promotion, MySQL replication, Aurora/cloud-managed failover); application traffic shifts via DNS, load balancers, or traffic managers; state must move with it.
- **Geo-redundancy** — copies live in a second region or availability zone; asynchronous replication keeps RPO small, while synchronous replication in the same region protects against node loss but not region loss.
- **RPO and RTO as contracts** — every DR plan states measurable objectives; the chosen architecture must be sized so the recovery procedure actually meets them under load, not just in a demo.
- **Testing** — unexercised DR plans fail in practice: run game days, chaos exercises, and restore drills on real data; document runbooks, contacts, and decision criteria for failback.

## Related
- [[wiki/data-storage/backup-strategies|Backup Strategies]] — the data-loss side of recovery
- [[wiki/data-storage/rpo-and-rto|RPO and RTO]] — the objectives DR architectures serve
- [[wiki/data-storage/replication-strategies|Replication Strategies]] — failover mechanisms
- [[wiki/data-storage/point-in-time-recovery|Point-in-Time Recovery]] — restoring to clean states
- [[wiki/data-storage/storage-tiering|Storage Tiering]] — warm standby footprint sizing
