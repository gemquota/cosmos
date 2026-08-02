---
type: "concept"
title: "Property-Based Testing"
description: "Generating diverse inputs to verify invariants across a wide input space"
tags: ["property-based-testing", "testing", "generators", "invariants"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://hypothesis.readthedocs.io/en/latest/", "https://junit.org/junit5/docs/current/user-guide/"]
---

# Property-Based Testing

## Summary
Property-based testing replaces hand-written examples with generated inputs that must satisfy invariants, properties that hold for every valid input. It finds edge cases humans never think to write and shrinks failures to minimal counterexamples.

## Details
- Libraries: Hypothesis for Python, QuickCheck for Haskell, fast-check for JavaScript, jqwik for Java, proptest for Rust.
- Define properties: round-trips, commutativity, invariants, oracle comparisons, and no-crash guarantees.
- Generators produce ints, strings, lists, dicts, and custom data; strategies explore boundaries automatically.
- Shrinking: on failure the framework reduces the input to the smallest repro, aiding debugging.
- Ideal for parsers, serializers, search, sorting, validation logic, and stateful systems.
- Pair with unit tests: examples document intent, properties prove invariants.
- Pitfalls: generators yielding trivial inputs, and asserting exact output without an oracle.

## Related
- [[wiki/dev-tools/property-based-testing|Property-Based Testing]] — developer-tooling view of the same practice
- [[wiki/testing/test-oracles|Test Oracles]] — invariants are the oracle properties check
- [[wiki/testing/fuzzing|Fuzz Testing]] — random inputs without invariants
- [[wiki/testing/parametrized-tests|Parametrized Tests]] — explicit tables versus generated cases
- [[wiki/testing/metamorphic-testing|Metamorphic Testing]] — relations between outputs as properties
- [[wiki/testing/differential-testing|Differential Testing]] — comparing implementations on generated inputs
