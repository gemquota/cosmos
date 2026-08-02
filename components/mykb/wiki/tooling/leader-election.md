---
type: "concept"
title: "Leader Election"
description: "Choosing one node to coordinate work that must not run in parallel"
tags: ["leader-election", "distributed-systems", "coordination", "reliability"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Leader Election

## Summary
Leader election picks a single node to own exclusive work — scheduling, writes, migrations — while others stand by. Implementations use leases on a shared store (etcd, ZooKeeper, DB locks) so the role transfers cleanly on failure.

## Details
- Leases bound the leader's mandate; lost lease means step down and hand over.
- Fencing tokens protect against split-brain writes from a stale leader.
- Elections must be safe under partitions — quorum-based stores give that safety.
- mykb relevance: one wiki worker runs the sync scheduler; the rest stand by via lease.

## Related
- [[wiki/compositions/lease-based-locks|Lease-Based Locks]]
- [[wiki/compositions/fencing-tokens|Fencing Tokens]]
- [[wiki/devops-infra/leader-election-and-quorum|Leader Election and Quorum]]
- [[wiki/tooling/consensus-algorithms|Consensus Algorithms]]
- [[wiki/compositions/distributed-locks|Distributed Locks]]
