---
type: "concept"
title: "Consensus Algorithms"
description: "The algorithms that let distributed processes agree on a value despite failures"
tags: ["consensus", "distributed-systems", "algorithms", "replication"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://en.wikipedia.org/wiki/Consensus_(computer_science)", "https://raft.github.io/"]
---

# Consensus Algorithms

## Summary
Consensus algorithms let a set of processes agree on a single value — a log entry, a leader, a commit — even when some processes fail or messages are delayed. Paxos and Raft are the canonical practical algorithms; they underpin replicated databases and coordination services.

## Details
- Consensus guarantees agreement, validity, and termination under a defined failure model (crash, not Byzantine, in the common case).
- The FLP result shows deterministic consensus is impossible under unbounded asynchrony; practical algorithms work with timeouts and majority quorums.
- Paxos is the foundational algorithm, famously elegant and hard to implement correctly; Raft is its understandable cousin, used by etcd and Consul.
- Consensus enables replicated state machines: every replica applies the same log, so state stays identical.
- Costs: a quorum round trip per decision, a leader to coordinate, and liveness under partition.
- For the mykb bundle, consensus would back leader election and lock leases if sync runs on multiple nodes.
- Worked example — the wiki sync cluster runs Raft via etcd: one node leads, the others follow, and writes commit only when a majority acknowledges.

Worked example — the wiki sync cluster runs Raft via etcd: one node leads, the others follow, and writes commit only when a majority acknowledges.

## Related
- [[wiki/tooling/raft-algorithm|Raft Algorithm]]
- [[wiki/tooling/paxos-algorithm|Paxos Algorithm]]
- [[wiki/tooling/leader-election|Leader Election]]
- [[wiki/tooling/distributed-consistency|Distributed Consistency]]
- [[wiki/compositions/lease-based-locks|Lease-Based Locks]]
- [[wiki/compositions/strong-consistency|Strong Consistency]]
- [[wiki/tooling/quorum-reads|Quorum Reads]]
- [[wiki/compositions/fencing-tokens|Fencing Tokens]]
- [[wiki/devops-infra/leader-election-and-quorum|Leader Election & Quorum]]
- [[wiki/api-protocols/optimistic-concurrency|Optimistic Concurrency]]
