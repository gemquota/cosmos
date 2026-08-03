---
type: "concept"
title: "Replication & Failover DR"
description: "Copying data across sites and switching over when a site fails"
tags: ["replication", "failover", "dr", "availability"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# Replication & Failover DR

## Summary
Replication copies data to multiple locations for availability; failover switches traffic to a replica when the primary fails; disaster recovery (DR) is the end-to-end plan to restore service at scale after a major loss. Replication is the mechanism, failover is the reaction, and DR is the guarantee that ties them to business targets.

## Details
- Replication mechanics: synchronous replication commits on both primary and replica (zero data loss, higher latency, availability coupling); asynchronous replication accepts a lag window (better latency, potential loss on failover); variants include statement-based, logical, and physical replication depending on the database.
- Failover mechanics: detection (health checks, quorum), promotion of the best replica (most advanced position), repointing clients (DNS, VIP, connection pools), and rejoin of the old primary as a replica.
- DR mechanics: the plan spans RPO/RTO targets, runbooks, site selection (same-region multi-AZ versus cross-region), backup fallback when replication is not enough, and regular drills that actually fail over.
- Concrete example: a Postgres pair with synchronous replication in one region plus an async replica in another; regional loss promotes the async replica with up to seconds of data loss; a DR drill fails over to the second region quarterly and restores the application from the promoted database.
- Failure modes: split-brain after failover when the old primary accepts writes; async lag larger than expected, losing recent transactions; failover to a replica with different schema or config; DR plans that have never been run, failing at the worst moment; replication config silently broken, so the replica was never current.
- Tradeoffs: synchronous replication minimizes data loss but couples primary availability to the replica; async maximizes availability but accepts loss; the choice is a business decision about which risk is worse, and DR is only as good as the drills that prove it.
- Operational notes: monitor replication lag continuously, test failover in game days, and keep the DR runbook current.
- RSIS3 relevance: the MyKB store's availability story is the same — decide the RPO/RTO, pick replication mode, and drill the failover before the first real loss.

## Related
- [[wiki/infrastructure/redundancy-and-failover-dc|Datacenter Redundancy & Failover]]
- [[wiki/devops-infra/database-failover-automation|Database Failover Automation]]
- [[wiki/devops-infra/replication|Replication]]
- [[wiki/devops-infra/kubernetes-control-plane|Kubernetes Control Plane]]
- [[wiki/devops-infra/observability-pillars|Observability Pillars]]
