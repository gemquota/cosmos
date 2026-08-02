---
type: "concept"
title: "CRDT Practice"
description: "Conflict-free replicated data types that converge without coordination"
tags: ["crdt", "replication", "conflicts", "design"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# CRDT Practice

## Summary
CRDTs are data structures — counters, sets, registers, maps — whose operations converge to the same state on every replica regardless of delivery order. They power offline collaboration (Figma-ish multiplayer, collaborative docs) without a central conflict resolver.

## Details
- State-based CRDTs merge whole states; op-based CRDTs propagate operations; both converge.
- Sizes and garbage collection can grow unboundedly — design tombstones and compaction.
- CRDTs give convergence, not semantic correctness: business rules still need your logic.
- mykb relevance: wiki tag sets and view counters are natural CRDTs across sync replicas.

## Related
- [[wiki/compositions/operational-transform|Operational Transform]]
- [[wiki/compositions/conflict-resolution-strategies|Conflict Resolution Strategies]]
- [[wiki/compositions/version-vectors|Version Vectors]]
- [[wiki/compositions/eventual-consistency-practice|Eventual Consistency Practice]]
- [[wiki/compositions/sync-engines|Sync Engines]]
