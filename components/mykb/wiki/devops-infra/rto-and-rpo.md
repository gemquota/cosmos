---
type: "concept"
title: "RTO & RPO"
description: "Recovery time and recovery point objectives that size DR plans"
tags: ["rto", "rpo", "dr", "recovery"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# RTO & RPO

## Summary
RTO (Recovery Time Objective) and RPO (Recovery Point Objective) define what recovery must achieve: RTO is the maximum acceptable downtime before service must be restored; RPO is the maximum acceptable data loss measured in time. Every backup, replication, and failover decision is a tradeoff against these two numbers.

## Details
- RTO: the clock starts at failure and ends when service is usable; it drives how much recovery automation you need — minutes of RTO demands automated failover, hours allow runbooks, days allow manual rebuild.
- RPO: the window of acceptable loss; zero RPO demands synchronous replication or continuous archiving, minutes allow async replication, hours allow periodic backups.
- Concrete example: a payment system with RTO 15 minutes and RPO 0 uses synchronous replication and automated failover; an analytics warehouse with RTO 24h and RPO 1h uses hourly backups and a documented restore path; an archive with RTO 1 week and RPO 1 week uses monthly snapshots.
- Failure modes: targets stated but never measured — no drill proves the RTO is actually met; RPO assumed from backup frequency without accounting for restore lag; targets that are aspirational rather than designed (RTO 5 minutes for a system with manual recovery); a single recovery path that cannot meet either target during a real regional failure.
- Tradeoffs: tighter targets cost more — replication, storage, automation, testing; looser targets are cheap but painful when used; the numbers should be negotiated with the business, then the architecture should be designed to them, and drills should verify them.
- Operational notes: document RTO/RPO per system, measure them in drills, and renegotiate when systems change.
- Measurement: RTO is met only when restored service passes a health check — time the drill to that point, not to the moment traffic is accepted.
- RSIS3 relevance: the wiki and MyKB store need explicit RTO/RPO — decide how long recovery may take and how much history can be lost before choosing the backup and replication machinery.

## Related
- [[wiki/devops-infra/kubernetes-control-plane|Kubernetes Control Plane]]
- [[wiki/devops-infra/observability-pillars|Observability Pillars]]
