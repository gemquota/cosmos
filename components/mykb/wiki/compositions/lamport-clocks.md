---
type: "concept"
title: "Lamport Clocks"
description: "Logical counters that impose a total order on events"
tags: ["lamport-clocks", "logical-time", "causality", "distributed-systems"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---
# Lamport Clocks

## Summary

Lamport clocks assign each event a counter that ticks on send, giving a total order consistent with causality — if event A causes B, A's clock is smaller. They order events cheaply but cannot detect concurrency between incomparable events.

## Details
- Mechanism: each process keeps a counter; on a local event it increments; on send it attaches its counter; on receive it sets its counter to max(local, received) + 1; the resulting order is consistent with causality (causally related events order correctly) but incomparable events get an arbitrary, consistent total order — concurrency is invisible.
- Concrete example: wiki sync events use Lamport timestamps to linearize merge order across replicas — every replica agrees on a total order even without a shared clock; mutual exclusion algorithms (Ricart-Agrawala-style) use Lamport order to break ties fairly; the failure pattern is relying on Lamport order to detect concurrent edits (it cannot — that needs vector clocks).
- Failure modes: treating Lamport order as causal truth (arbitrary order of concurrent events can mislead); using wall-clock time as the counter (clocks drift and reorder events); and monotonicity violations when counters reset or merge incorrectly.
- Operational tradeoffs: Lamport clocks are cheap (one integer per process) and sufficient for total ordering; the trade is that concurrency detection and causality queries need vector clocks or version vectors; the discipline is choosing the clock to the question — total order here, concurrency there.
- RSIS3/mykb relevance: the wiki's sync layer would linearize event order with Lamport timestamps, giving every replica the same merge sequence at minimal overhead.
- Counter persistence: counters must survive restarts without resetting below the last issued value, or ordering guarantees break across crashes.
- Choice guidance: use Lamport when only a total order is needed; upgrade to vector clocks the moment concurrent-write detection or causality queries enter the requirements.

## Related
- [[wiki/compositions/vector-clocks|Vector Clocks]]
- [[wiki/compositions/version-vectors|Version Vectors]]
- [[wiki/tooling/consensus-algorithms|Consensus Algorithms]]
- [[wiki/compositions/causal-consistency|Causal Consistency]]
- [[wiki/tooling/distributed-consistency|Distributed Consistency]]
