---
type: "concept"
title: "Distributed Locks"
description: "Mutual exclusion across processes and machines"
tags: ["distributed-locks", "coordination", "concurrency", "reliability"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Distributed Locks

## Summary
Distributed locks give mutually exclusive access to a resource across processes on different machines, typically via a shared store (Redis, etcd, ZooKeeper, DB rows). They work only if the lock store is reliable, and they need leases to survive holder crashes.

## Details
- Implementations: SETNX-with-expiry, etcd leases, ZooKeeper ephemeral nodes.
- Leases bound lock hold time; a crashed holder must not hold forever.
- Split-brain risk: a lock is only as safe as its store and your fencing discipline.
- mykb relevance: wiki sync uses distributed locks so two workers never publish at once.

## Related
- [[wiki/compositions/lease-based-locks|Lease-Based Locks]]
- [[wiki/compositions/fencing-tokens|Fencing Tokens]]
- [[wiki/tooling/leader-election|Leader Election]]
- [[wiki/tooling/consensus-algorithms|Consensus Algorithms]]
- [[wiki/compositions/pessimistic-locking|Pessimistic Locking]]
