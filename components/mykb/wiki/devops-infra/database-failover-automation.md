---
type: "concept"
title: "Database Failover Automation"
description: "Automated promotion of replicas when the primary fails"
tags: ["failover", "database", "replication", "automation"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# Database Failover Automation

## Summary
Database failover automation moves primary database role to a replica automatically when the primary fails — detecting outage, promoting the best replica, and repointing clients. It converts minutes-to-hours of manual recovery into seconds-to-minutes, at the cost of careful design to avoid split-brain and data loss.

## Details
- Mechanism: a failure detector (health checks, quorum, consensus) decides the primary is down; the promotion elects a replica with the most complete transaction log; DNS, connection pools, or proxies repoint clients; the old primary, when it returns, must rejoin as a replica and reconcile its divergence.
- Concrete example: Patroni with etcd for Postgres — etcd provides the quorum, Patroni demotes a failing primary, promotes a replica with `pg_ctl promote`, and virtual IP or DNS moves; managed databases (RDS Multi-AZ failover) automate the same with a shorter window; Kubernetes operators (CloudNativePG, Zalando) do it in-cluster.
- Failure modes: split-brain — the old primary comes back and accepts writes while the new primary is active; asynchronous replication data loss — a replica promoted without the last transactions; failover storms — a flapping detector promoting repeatedly during a network partition; client retry storms against the new primary before it is ready; schema or version drift between primary and replica making promotion unsafe.
- Tradeoffs: automatic failover reduces downtime but every automation tradeoff shows up here — false failovers interrupt an otherwise healthy service, and automated promotion may promote a lagged replica; pair automation with sync replication or RPO checks where data loss is unacceptable, and always test failover in game days.
- Operational notes: define a clear failover runbook, set thresholds to avoid flapping, monitor replication lag continuously, and rehearse failover until it is boring.
- RSIS3 relevance: the MyKB store, if database-backed, needs the same failover design — retrieval continuity for the loops depends on it.

## Related
- [[wiki/cloud-infra/storage-tiering-automation|Storage Tiering Automation]]
- [[wiki/infrastructure/redundancy-and-failover-dc|Datacenter Redundancy & Failover]]
- [[wiki/devops-infra/replication-and-failover-dr|Replication & Failover DR]]
- [[wiki/devops-infra/database-indexing|Database Indexing]]
- [[wiki/devops-infra/kubernetes-control-plane|Kubernetes Control Plane]]
- [[wiki/syntheses/knowledge-acquisition-workflow|Knowledge Acquisition Workflow]] — how stubs grow into full articles in mykb
- [[wiki/syntheses/mykb-acquisition-curation-and-practices|Acquisition, Curation & Practices]] — the curation loop this stub belongs to
