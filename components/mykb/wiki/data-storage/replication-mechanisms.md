---
type: "concept"
title: "Replication Mechanisms"
description: "Copying data across servers for durability, scale, and availability"
tags: ["replication", "high-availability", "distributed-systems", "databases"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://en.wikipedia.org/wiki/Replication_(computing)", "https://www.postgresql.org/docs/current/logical-replication.html"]
---

# Replication Mechanisms

## Summary

Replication keeps copies of data on multiple nodes so the system survives failures and scales reads.
Mechanisms differ by topology, sync semantics, and consistency guarantees.
Choosing the right mechanism is a core database design decision.
Replication design is a consistency-and-availability contract; document the tradeoffs explicitly.

## Details

- Leader-based replication: one primary accepts writes, replicas follow.
- Multi-leader and leaderless topologies trade consistency for availability.
- Synchronous replication trades latency for durability; async risks data loss.
- Physical replication copies storage-level changes; logical replicates logical operations.
- Replication interacts with consistency models, quorums, and conflict resolution.
- Failover is only as good as its testing; run regular promotion drills.
- Lag monitoring should alert before stale reads reach users.
- Write down the replication topology in your architecture docs; future engineers will thank you when they debug a failover.

## Related

- [[wiki/data-storage/logical-replication|Logical Replication]] — logical mechanism
- [[wiki/data-storage/physical-replication|Physical Replication]] — physical mechanism
- [[wiki/data-storage/read-replicas-and-scaling|Read Replicas and Scaling]] — read scaling
- [[wiki/data-storage/replication-strategies|Replication Strategies]] — existing note
- [[wiki/data-storage/multi-leader-replication|Multi-Leader Replication]] — multi-leader
- [[wiki/data-storage/data-quality-dimensions|Data Quality Dimensions]] — quality dimensions
- [[wiki/data-storage/data-observability-and-monitoring|Data Observability and Monitoring]] — observability
- [[wiki/data-storage/data-testing-frameworks|Data Testing Frameworks]] — testing
- [[wiki/data-storage/feature-stores-and-ml-features|Feature Stores and ML Features]] — ML features
- [[wiki/data-storage/data-contracts-and-agreements|Data Contracts and Agreements]] — data contracts
- [[wiki/data-storage/incremental-loading-strategies|Incremental Loading Strategies]] — incremental loading
- [[wiki/data-storage/schema-evolution-in-streams|Schema Evolution In Streams]] — schema evolution
- [[wiki/data-storage/streaming-sinks-and-sources|Streaming Sinks And Sources]] — streams

