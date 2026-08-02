---
type: "concept"
title: "Leaderless Replication"
description: "Quorum reads and writes without a single primary"
tags: ["leaderless-replication", "quorum", "dynamodb", "cassandra"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://cassandra.apache.org/doc/latest/cassandra/architecture/dynamo.html", "https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/HowItWorks.ReadConsistency.html"]
---

# Leaderless Replication

## Summary
Leaderless replication lets any replica accept reads and writes, with no single primary coordinating them. Clients send operations to multiple replicas and rely on quorums to ensure correctness; this design, popularized by Amazon Dynamo and adopted by Cassandra and Riak, favors availability and low write latency.

## Details
- **The model** — every node is writable; a write goes to `W` replicas and a read to `R` replicas out of `N` total. When `W + R > N`, at least one node that saw the write is read, so the quorum condition keeps data consistent enough for converged writes.
- **Quorum arithmetic** — `W + R > N` prevents reading stale data for quorum-completed operations; tuning `W` and `R` trades consistency for latency and availability (e.g., `W=1` for fast writes, `R=1` for fast reads, full quorum for strong consistency).
- **Reconciliation** — because nodes accept writes concurrently, versions diverge; read repair fixes stale replicas during reads, hinted handoff queues writes for temporarily down nodes, and anti-entropy processes reconcile asynchronously. Vector clocks or timestamps order versions.
- **Failure behavior** — with `N=3, W=2, R=2`, one node can fail and the system still serves; sloppy quorums even accept writes for nodes outside the replica set when the preferred ones are down (Dynamo's approach), providing high availability at the cost of stronger consistency guarantees.
- **When it fits** — latency-sensitive, availability-critical workloads that tolerate eventual consistency; Cassandra's tunable consistency levels and DynamoDB's consistency options expose the dial.
- **Trade-offs** — no single writer simplifies failover, but conflict resolution, tombstone handling, and monitoring divergence are ongoing operational costs.

## Related
- [[wiki/data-storage/quorum-protocols|Quorum Protocols]] — the read/write arithmetic in depth
- [[wiki/data-storage/consistency-models|Consistency Models]] — what leaderless systems guarantee
- [[wiki/data-storage/consistent-hashing|Consistent Hashing]] — replica placement in the ring
- [[wiki/data-storage/cap-theorem|CAP Theorem]] — why the design exists
- [[wiki/data-storage/replication-strategies|Replication Strategies]] — leaderless vs primary-replica
- [[wiki/data-storage/wide-column-stores|Wide-Column Stores]] — Cassandra's data model
