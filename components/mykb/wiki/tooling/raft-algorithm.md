---
type: "concept"
title: "Raft Algorithm"
description: "The understandable consensus algorithm for replicated state machines"
tags: ["raft", "consensus", "replication", "algorithm"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://raft.github.io/", "https://raft.github.io/raft.pdf"]
---

# Raft Algorithm

## Summary
Raft is a consensus algorithm designed for understandability: it decomposes consensus into leader election, log replication, and safety, with a strong leader that all reads and writes flow through. etcd, Consul, and CockroachDB use it to replicate state across nodes.

## Details
- Nodes are leaders, followers, or candidates; a leader is elected by majority vote and holds the role until it fails.
- The leader appends entries to its log and replicates them; entries commit when a majority stores them.
- Term numbers and randomized election timeouts keep elections safe and fast.
- Raft's log is the replicated state machine's input; every replica applies the same committed entries.
- Membership changes are first-class in Raft, making cluster resizing safe.
- For the mykb bundle, Raft-backed etcd would provide leader election and leases for multi-node sync.
- Worked example — three wiki sync nodes run Raft: the leader writes an ArticleIndexed entry, a quorum acks, the entry commits, and all replicas apply it in the same order.

Worked example — three wiki sync nodes run Raft: the leader writes an ArticleIndexed entry, a quorum acks, the entry commits, and all replicas apply it in the same order.

## Related
- [[wiki/tooling/consensus-algorithms|Consensus Algorithms]]
- [[wiki/tooling/paxos-algorithm|Paxos Algorithm]]
- [[wiki/tooling/leader-election|Leader Election]]
- [[wiki/compositions/lease-based-locks|Lease-Based Locks]]
- [[wiki/tooling/distributed-consistency|Distributed Consistency]]
- [[wiki/compositions/fencing-tokens|Fencing Tokens]]
- [[wiki/devops-infra/leader-election-and-quorum|Leader Election & Quorum]]
- [[wiki/devops-infra/replication-and-failover-dr|Replication & Failover DR]]
