---
type: "concept"
title: "Vector Clocks"
description: "Per-process counters that detect causality and concurrency between events"
tags: ["vector-clocks", "causality", "concurrency", "distributed-systems"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Vector Clocks

## Summary
Vector clocks keep one counter per process, updated on send and receive, so event comparison reveals causality: equal-or-greater in every component means causal; incomparable means concurrent. They are the standard way to detect conflicting updates.

## Details
- Causality: A happened-before B iff A's vector is component-wise <= B's.
- Incomparable vectors mean the events raced — the trigger for conflict resolution.
- Cost grows with the number of processes; the real world caps it per replica set.
- mykb relevance: wiki replicas compare vector clocks to find divergent article versions.

## Related
- [[wiki/compositions/lamport-clocks|Lamport Clocks]]
- [[wiki/compositions/version-vectors|Version Vectors]]
- [[wiki/compositions/causal-consistency|Causal Consistency]]
- [[wiki/compositions/conflict-resolution-strategies|Conflict Resolution Strategies]]
- [[wiki/compositions/sync-engines|Sync Engines]]
