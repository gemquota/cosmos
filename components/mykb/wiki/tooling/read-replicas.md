---
type: "concept"
title: "Read Replicas"
description: "Copies of a database that serve reads while the primary takes writes"
tags: ["read-replicas", "databases", "scaling", "replication"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Read Replicas

## Summary
Read replicas are followers that answer read queries, offloading the primary and scaling read capacity. Writes still hit the primary; replicas trail by replication lag.

## Details
- Route read-heavy workloads (reports, search) to replicas; keep writes on the primary.
- Stale reads are possible — choose per-query: fresh primary read or cheap replica read.
- Replicas double as failover targets and backup sources.
- mykb relevance: the wiki search index reads from a replica so writes stay fast.

## Related
- [[wiki/tooling/replication-lag|Replication Lag]]
- [[wiki/tooling/quorum-reads|Quorum Reads]]
- [[wiki/tooling/failover-practice|Failover Practice]]
- [[wiki/devops-infra/database-failover-automation|Database Failover Automation]]
- [[wiki/tooling/distributed-consistency|Distributed Consistency]]
