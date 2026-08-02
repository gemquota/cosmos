---
type: "concept"
title: "Causal Consistency"
description: "The consistency model where causally related operations are seen in order"
tags: ["causal-consistency", "consistency", "distributed-systems", "models"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Causal Consistency

## Summary
Causal consistency guarantees every replica observes causally related operations in the same order, while concurrent operations may appear in any order. It is the strongest model that remains implementable without coordination — the sweet spot of many systems.

## Details
- Causally related: a reply must not appear before its question; an edit before its base.
- COPS, causal memory, and many replicated stores implement causal consistency.
- Stronger than eventual, weaker than linearizable — a documented, practical tradeoff.
- mykb relevance: wiki comments and replies need causal order; standalone articles do not.

## Related
- [[wiki/compositions/eventual-consistency-practice|Eventual Consistency Practice]]
- [[wiki/compositions/strong-consistency|Strong Consistency]]
- [[wiki/compositions/vector-clocks|Vector Clocks]]
- [[wiki/tooling/distributed-consistency|Distributed Consistency]]
- [[wiki/compositions/read-your-writes|Read-Your-Writes]]
