---
type: "concept"
title: "Property Testing Libraries"
description: "Libraries that generate many random inputs to check invariants instead of hand-written examples"
tags: ["property-testing", "testing", "libraries", "randomized"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# Property Testing Libraries

## Summary
Property testing libraries (QuickCheck, Hypothesis, fast-check) generate hundreds of random inputs and check that a property holds for all of them. They find edge cases that example tests never imagine, turning invariants into executable checks.

## Details
- Mechanism: the library provides generators (integers, strings, structures, custom types), combinators to build complex inputs, and a runner that executes the property over many cases; shrinking finds the minimal counterexample; strategies and seeds control the search; integration with the test framework makes properties run like ordinary tests.
- Concrete example: Hypothesis `@given(st.text())` on a function that must never raise for any string; fast-check asserting a round-trip law for a serializer; QuickCheck checking an ordering invariant for a sort; a failing case is shrunk to the shortest string that breaks the property, pinpointing the bug.
- Failure modes: generators that produce only happy inputs, missing hostile cases; properties that are tautological or over-constrained; stateful libraries used for side-effecting code, creating flaky failures; shrinking bugs that produce non-failing reproducers; suites so large they slow CI to a crawl (size and max_examples need tuning).
- Tradeoffs: libraries give broad, automated coverage at the cost of learning the generator API and runtime; the alternative, example tests, is simpler and blind; the payoff is that edge cases surface as minimal, debuggable counterexamples.
- Operational notes: fix seeds for reproducible CI, tune max_examples per suite, and convert every finding into a permanent regression example.
- RSIS3 relevance: link-resolution and frontmatter rules are properties that could be tested across the wiki corpus — the same generative checking for the wiki's invariants.

## Practice
- Author properties alongside examples: examples document intent, properties prove invariants at scale.
- Use custom generators for domain types so the library explores realistic structures, not just primitives.
- Combine libraries with model-based testing: generate a sequence of operations and check that the system state always matches the model, catching the stateful bugs that single-input properties miss.
## Related
- [[wiki/dev-tools/property-based-testing|Property-Based Testing]]
- [[wiki/testing/property-based-testing|Property-Based Testing]]
- [[wiki/testing/fuzzing|Fuzzing]]
- [[wiki/software-engineering/unit-testing-practice|Unit Testing Practice]]
- [[wiki/testing/ci-quality-gates|CI Quality Gates]]
