---
type: "concept"
title: "Replication"
description: "Copying data from primary to replica nodes for availability, read scaling, and disaster recovery"
tags: ["replication", "database", "high-availability", "postgresql", "data"]
timestamp: "2026-07-31T00:00:00Z"
status: "stub"
---

# Replication

## Summary
Replication continuously copies writes from a primary database to replicas. It provides failover targets and offloads read traffic, at the cost of replication lag.

## Details
- Streaming replication (WAL-based) keeps replicas near-current; synchronous modes trade latency for durability.
- Read replicas serve analytics and search; promote a replica for failover.
- Consider lag when reading replicas for consistency-sensitive logic.

## Related
- [[wiki/devops-infra/postgresql|PostgreSQL]] — WAL streaming model
- [[wiki/devops-infra/backups|Backups]] — replication is not backup
- [[wiki/devops-infra/point-in-time-recovery|Point-in-Time Recovery]] — complements WAL
- [[wiki/devops-infra/sharding|Sharding]] — scaling beyond replicas
- [[wiki/devops-infra/connection-pooling|Connection Pooling]] — replica routing
- [[wiki/devops-infra/observability|Observability]] — replication-lag monitoring
