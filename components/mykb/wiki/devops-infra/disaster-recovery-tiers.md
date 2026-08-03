---
type: "concept"
title: "Disaster Recovery Tiers"
description: "The RTO/RPO spectrum from tape to synchronous mirroring"
tags: ["dr", "tiers", "rto", "rpo"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# Disaster Recovery Tiers

## Summary
Disaster recovery tiers classify systems by how much downtime and data loss they can tolerate, and therefore how much DR machinery they get. RTO (time to restore service) and RPO (maximum acceptable data loss) define the tiers; a tier map allocates replication, backups, failover, and testing effort proportionally to business criticality.

## Details
- Mechanism: each service declares RTO and RPO targets; tiers bundle the matching tooling — Tier 1 (minutes RTO/RPO) gets synchronous replication, automated failover, and continuous testing; Tier 2 (hours) gets asynchronous replication and runbook-driven recovery; Tier 3 (days) gets periodic backups and manual restore. The tier is the contract that justifies cost.
- Concrete example: an online payment service in Tier 1 with multi-region synchronous replicas and automated failover; an internal reporting database in Tier 2 with hourly backups and a documented recovery runbook; archived logs in Tier 3 with monthly snapshots restored on demand.
- Failure modes: mislabeling — a service treated as Tier 3 that actually needs hours of recovery (the tier map must be reviewed as systems change); RTO met while RPO is silently violated (restores lose the last window of writes); untested tier assumptions where the "automated" failover has never run; over-provisioning every system at Tier 1, which makes DR unaffordable and untestable.
- Tradeoffs: tighter tiers cost more in replication, storage, and testing time; looser tiers save money but lengthen outages; the tiering conversation forces explicit product decisions about which data and downtime actually matter.
- Operational notes: rehearse each tier's recovery path in game days, monitor that recovery tooling (replication lag, backup freshness) stays within tier bounds, and revisit tiers when systems change.
- RSIS3 relevance: RSIS3's memory store and checkpoints deserve an explicit tier — cheap RPO for the wiki (git pushes) and a defined recovery path for state files.

## Related
- [[wiki/cloud-infra/azure-blob-access-tiers|Azure Blob Access Tiers]]
- [[wiki/devops-infra/disaster-recovery|Disaster Recovery]]
- [[wiki/devops-infra/point-in-time-recovery|Point-in-Time Recovery]]
- [[wiki/infrastructure/pulsar-architecture-and-tiers|Pulsar Architecture And Tiers]]
- [[wiki/devops-infra/kubernetes-control-plane|Kubernetes Control Plane]]
- [[wiki/devops-infra/observability-pillars|Observability Pillars]]
- [[wiki/syntheses/knowledge-acquisition-workflow|Knowledge Acquisition Workflow]] — how stubs grow into full articles in mykb
- [[wiki/syntheses/mykb-acquisition-curation-and-practices|Acquisition, Curation & Practices]] — the curation loop this stub belongs to
