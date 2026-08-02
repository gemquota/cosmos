---
type: "concept"
title: "Property Testing Libraries"
description: "Libraries that generate many random inputs to check invariants instead of hand-written examples"
tags: ["property-testing", "testing", "libraries", "randomized"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Property Testing Libraries

## Summary
Property testing libraries (QuickCheck, Hypothesis, fast-check) generate hundreds of random inputs and check that a property holds for all of them. They find edge cases that example tests never imagine.

## Details
- Properties are invariants: round-trip laws, ordering laws, or model comparisons against a reference implementation.
- Shrinking reduces a failing input to a minimal counterexample, which is the killer feature for debugging.
- Integration with CI keeps generative tests running on every push; seed-based replay fixes flaky findings.
- mykb relevance: link-resolution and frontmatter rules are properties that could be tested across the wiki corpus.

## Related
- [[wiki/dev-tools/property-based-testing|Property-Based Testing]]
- [[wiki/testing/property-based-testing|Property-Based Testing]]
- [[wiki/testing/fuzzing|Fuzzing]]
- [[wiki/software-engineering/unit-testing-practice|Unit Testing Practice]]
- [[wiki/testing/ci-quality-gates|CI Quality Gates]]
