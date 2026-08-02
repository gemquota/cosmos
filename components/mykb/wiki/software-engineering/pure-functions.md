---
type: "concept"
title: "Pure Functions"
description: "Functions whose output depends only on inputs and that have no side effects"
tags: ["functional-programming", "purity", "design", "testing"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Pure Functions

## Summary
A pure function returns the same output for the same input and changes nothing observable: no I/O, no mutation, no global state. Purity makes functions trivial to test, cache, parallelize, and reason about.

## Details
- Determinism and no-side-effects are the two rules; both are checkable in principle.
- Move effects to the boundary: read inputs, call pure logic, write outputs.
- Memoization and parallel execution are free wins for pure functions.
- mykb relevance: pure functions for slug-to-path mapping make wiki build logic trivially testable.

## Related
- [[wiki/software-engineering/immutability-practice|Immutability Practice]]
- [[wiki/software-engineering/referential-transparency|Referential Transparency]]
- [[wiki/software-engineering/side-effect-isolation|Side Effect Isolation]]
- [[wiki/software-engineering/functional-programming|Functional Programming]]
- [[wiki/testing/unit-testing|Unit Testing]]
