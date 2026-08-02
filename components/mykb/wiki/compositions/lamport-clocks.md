---
type: "concept"
title: "Lamport Clocks"
description: "Logical counters that impose a total order on events"
tags: ["lamport-clocks", "logical-time", "causality", "distributed-systems"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Lamport Clocks

## Summary
Lamport clocks assign each event a counter that ticks on send, giving a total order consistent with causality — if event A causes B, A's clock is smaller. They order events cheaply but cannot detect concurrency between incomparable events.

## Details
- Rule: increment on local events and on receive, take max plus one.
- Lamport order is consistent with causality but not equal to it — incomparable events get arbitrary order.
- The classic use is total ordering for replicated logs and mutual exclusion.
- mykb relevance: wiki sync events use Lamport timestamps to linearize merge order.

## Related
- [[wiki/compositions/vector-clocks|Vector Clocks]]
- [[wiki/compositions/version-vectors|Version Vectors]]
- [[wiki/tooling/consensus-algorithms|Consensus Algorithms]]
- [[wiki/compositions/causal-consistency|Causal Consistency]]
- [[wiki/tooling/distributed-consistency|Distributed Consistency]]
