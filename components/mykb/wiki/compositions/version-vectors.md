---
type: "concept"
title: "Version Vectors"
description: "Per-replica counters that track causal history and detect concurrent updates"
tags: ["version-vectors", "causality", "replication", "conflicts"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Version Vectors

## Summary
A version vector maps each replica to its update count, capturing causal history: if one vector dominates another, the states are ordered; if they diverge, writes are concurrent and need resolution. It is the core bookkeeping of optimistic replication.

## Details
- Compare vectors: A <= B means B includes A's updates; incomparable means concurrent.
- Vector clocks are the client/counter variant; both detect the same causality.
- Vectors grow with replica count — prune and garbage-collect carefully.
- mykb relevance: wiki replicas keep version vectors to detect divergent article edits.

## Related
- [[wiki/compositions/vector-clocks|Vector Clocks]]
- [[wiki/compositions/lamport-clocks|Lamport Clocks]]
- [[wiki/compositions/conflict-resolution-strategies|Conflict Resolution Strategies]]
- [[wiki/compositions/sync-engines|Sync Engines]]
- [[wiki/compositions/causal-consistency|Causal Consistency]]
