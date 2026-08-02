---
type: "concept"
title: "Consistency Models"
description: "Strong, causal, and eventual consistency guarantees"
tags: ["consistency", "replication", "distributed-systems", "eventual-consistency"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/HowItWorks.ReadConsistency.html", "https://learn.microsoft.com/en-us/azure/cosmos-db/consistency-levels"]
---

# Consistency Models

## Summary
A consistency model is the contract between a replicated data store and its clients about which reads see which writes. Models range from strong (linearizable) to eventual, and each trades freshness for latency and availability.

## Details
- **Strong consistency** — every read returns the result of the most recent acknowledged write; implemented with quorums or consensus (Raft, Paxos). Simple to reason about but costs latency and availability during partitions.
- **Linearizability** — the strongest practical form: operations appear to take effect atomically at a single point in time that respects real-time ordering; databases and coordination services (etcd, ZooKeeper) provide it.
- **Causal consistency** — reads respect cause-and-effect order (a write and a later write that read it) but not arbitrary concurrent order; cheaper than strong consistency and sufficient for many collaborative and social workloads.
- **Eventual consistency** — replicas converge over time once writes stop; reads may see stale values. DynamoDB's default reads, Cassandra with weak consistency levels, and DNS propagation are classic examples.
- **Session and read-your-writes guarantees** — weaker than global strong consistency but stronger than plain eventual: a client always sees its own writes. Most practical systems advertise these as a compromise.
- **Choosing a model** — the application's correctness requirements drive the choice: financial ledgers want strong; product catalogs, feeds, and counters tolerate bounded staleness; Cosmos DB exposes five named levels (strong, bounded staleness, session, consistent prefix, eventual) as a spectrum.

## Related
- [[wiki/data-storage/cap-theorem|CAP Theorem]] — why the choice exists at all
- [[wiki/data-storage/quorum-protocols|Quorum Protocols]] — mechanisms behind consistency levels
- [[wiki/data-storage/leaderless-replication|Leaderless Replication]] — eventual consistency in practice
- [[wiki/data-storage/crdts|CRDTs]] — convergent structures for eventual consistency
- [[wiki/data-storage/raft-consensus|Raft Consensus]] — building strong consistency
- [[wiki/data-storage/replication-strategies|Replication Strategies]] — synchronous vs asynchronous propagation
