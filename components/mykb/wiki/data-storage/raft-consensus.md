---
type: "entity"
title: "Raft Consensus"
description: "Log-based leader election and replication protocol"
tags: ["raft", "consensus", "distributed-systems", "replication"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://etcd.io/docs/v3.5/learning/why-etcd/", "https://developer.hashicorp.com/consul/docs/architecture/consensus"]
---

# Raft Consensus

## Summary
Raft is a consensus algorithm that lets a cluster of nodes agree on an ordered log of state changes even when some nodes fail or messages are delayed. It elects a single leader that replicates entries to a majority, and it is the engine behind etcd, Consul, CockroachDB, and many coordination services.

## Details
- **Leader election** — nodes are leaders, followers, or candidates; followers that hear no heartbeat start an election, candidates request votes, and the first to win a majority becomes leader for a term; randomized election timeouts prevent split votes.
- **Log replication** — the leader appends entries, sends them with the previous log index and term, and commits once a majority of nodes have stored them; followers apply committed entries to their state machines, so the replicated log is the single source of truth.
- **Safety and ordering** — the log is append-only and ordered; the leader never overwrites committed entries, and a candidate cannot win without the most up-to-date log (the election restriction), which preserves the property that committed entries are never lost.
- **Failures** — a leader that loses the majority stalls writes until a new election; network partitions leave the minority side unable to commit, providing the classic CP behavior: availability is sacrificed to keep consistency.
- **Comparison to Paxos** — Raft was designed as a more understandable Paxos: it decomposes consensus into leader election, log replication, and safety, and adds explicit term-based leadership; Paxos is more flexible in some edge cases but harder to implement correctly.
- **Production role** — Raft powers etcd (Kubernetes control-plane state), Consul sessions and key-value, and replicated state machines in CockroachDB and TiKV; it suits metadata, coordination, and strongly consistent small-state workloads, not bulk data storage.

## Related
- [[wiki/data-storage/quorum-protocols|Quorum Protocols]] — the majority foundation Raft uses
- [[wiki/data-storage/consistency-models|Consistency Models]] — linearizability via consensus
- [[wiki/data-storage/replication-strategies|Replication Strategies]] — consensus vs asynchronous replication
- [[wiki/data-storage/cap-theorem|CAP Theorem]] — the CP side of the trade-off
- [[wiki/data-storage/distributed-transactions|Distributed Transactions]] — consensus as the coordinator
