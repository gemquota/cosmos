---
type: "concept"
title: "CAP Theorem"
description: "Consistency, availability, and partition-tolerance trade-offs"
tags: ["cap-theorem", "distributed-systems", "consistency", "availability"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://cassandra.apache.org/doc/latest/cassandra/architecture/guarantees.html", "https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/HowItWorks.ReadConsistency.html"]
---

# CAP Theorem

## Summary
The CAP theorem states that a distributed data system cannot simultaneously guarantee strong consistency, availability, and partition tolerance. During a network partition, a system must choose between serving reads/writes that may be stale (availability) and refusing responses until nodes agree (consistency).

## Details
- **The three properties** — consistency means every read returns the latest write; availability means every request receives a non-error response; partition tolerance means the system continues operating when messages between nodes are lost or delayed.
- **The real trade-off** — since partitions are unavoidable in real networks, the practical choice is CP vs AP during a partition: CP systems (ZooKeeper, etcd, HBase) pause writes and reject some requests; AP systems (Cassandra, DynamoDB, Riak) keep serving from reachable replicas, possibly with stale data.
- **A common misreading** — CAP does not mean choosing between consistency and availability in normal operation; systems can be fully consistent and available when the network is healthy, and CAP only forces the choice when a partition exists.
- **PACELC extension** — if a partition occurs choose Availability or Consistency (PAC); else choose Latency or Consistency (ELC), which captures the everyday design decision of synchronous vs asynchronous replication.
- **Consistency dials** — DynamoDB offers eventual, strongly consistent, and transactional reads; Cassandra offers per-query consistency levels; the higher the level, the more replicas must agree, trading latency and availability for freshness.

## Related
- [[wiki/data-storage/consistency-models|Consistency Models]] — what consistency means in practice
- [[wiki/data-storage/quorum-protocols|Quorum Protocols]] — how AP systems trade consistency for availability
- [[wiki/data-storage/leaderless-replication|Leaderless Replication]] — Dynamo-style designs CAP describes
- [[wiki/data-storage/raft-consensus|Raft Consensus]] — CP systems' approach to agreement
- [[wiki/data-storage/replication-strategies|Replication Strategies]] — where partitions bite
- [[wiki/data-storage/distributed-transactions|Distributed Transactions]] — consistency demands across nodes
