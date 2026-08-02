---
type: "concept"
title: "Database Replication Revisited"
description: "Replication topologies, guarantees, and operational realities"
tags: ["replication", "high-availability", "consistency", "databases"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://en.wikipedia.org/wiki/Replication_(computing)", "https://www.postgresql.org/docs/current/hot-standby.html"]
---

# Database Replication Revisited

## Summary

Replication copies data across nodes for availability, durability, and read scale.
Topology and sync mode determine consistency and failover behavior.
Operationally, replication is about lag, failover, and conflict management.
Replication is a distributed-systems decision made at design time and paid for forever; choose topology and sync depth deliberately.

## Details

- Single-leader, multi-leader, and leaderless topologies trade simplicity for availability.
- Synchronous replication minimizes data loss; asynchronous minimizes latency.
- Replication lag causes stale reads and read-after-write anomalies.
- Failover promotion needs monitoring, fencing, and tested procedures.
- Conflict resolution (LWW, CRDTs, application logic) must be explicit in multi-writer setups.
- Monitor lag per replica and alert on divergence from policy.
- Document failover runbooks and test them under load.
- Replication maturity is measured by failover drills and lag visibility, not by the number of replicas.

## Related

- [[wiki/data-storage/replication-mechanisms|Replication Mechanisms]] — mechanisms
- [[wiki/data-storage/read-replicas-and-scaling|Read Replicas And Scaling]] — read scaling
- [[wiki/data-storage/eventual-consistency-and-conflict-resolution|Eventual Consistency And Conflict Resolution]] — conflicts
- [[wiki/data-storage/replication-strategies|Replication Strategies]] — strategies
- [[wiki/data-storage/multi-leader-replication|Multi-Leader Replication]] — multi-leader
- [[wiki/data-storage/data-quality-dimensions|Data Quality Dimensions]] — quality dimensions
- [[wiki/data-storage/data-observability-and-monitoring|Data Observability and Monitoring]] — observability
- [[wiki/data-storage/data-testing-frameworks|Data Testing Frameworks]] — testing
- [[wiki/data-storage/feature-stores-and-ml-features|Feature Stores And Ml Features]] — ML features
- [[wiki/data-storage/data-contracts-and-agreements|Data Contracts and Agreements]] — data contracts
- [[wiki/data-storage/incremental-loading-strategies|Incremental Loading Strategies]] — incremental loading
- [[wiki/data-storage/schema-evolution-in-streams|Schema Evolution In Streams]] — schema evolution

