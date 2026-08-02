---
type: "concept"
title: "Compare-and-Swap"
description: "The atomic primitive that updates a value only if it matches an expected value"
tags: ["compare-and-swap", "atomics", "concurrency", "primitives"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Compare-and-Swap

## Summary
Compare-and-swap (CAS) atomically writes a new value only when the current value equals an expected one, retrying on failure. It is the primitive behind lock-free algorithms, optimistic concurrency, and many distributed leases.

## Details
- CAS loops build increment, push, and update operations without locks.
- ABA problem: a value can change and return to the same value between attempts — version tags fix it.
- Hardware CAS is per-address; software CAS (etcd, Redis WATCH) extends it to remote state.
- mykb relevance: CAS on the wiki index entry prevents lost updates from concurrent writers.

## Related
- [[wiki/compositions/lock-free-structures|Lock-Free Structures]]
- [[wiki/api-protocols/optimistic-concurrency|Optimistic Concurrency]]
- [[wiki/compositions/lost-update-problem|Lost Update Problem]]
- [[wiki/software-engineering/concurrency-models|Concurrency Models]]
- [[wiki/compositions/distributed-locks|Distributed Locks]]
