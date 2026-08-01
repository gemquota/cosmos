---
type: "concept"
title: "Property-Based Testing"
description: "Testing by generating many inputs and checking invariants that must hold for all of them"
tags: ["testing", "properties", "generative", "random"]
timestamp: "2026-08-01T00:00:00Z"
status: "stub"
---

# Property-Based Testing

## Summary
Property-based testing states invariants — 'reversing a list twice yields the original' — and lets a generator try hundreds or thousands of inputs. Tools like Hypothesis, QuickCheck, and fast-check find edge cases hand-written tests miss.

## Details
- Shrinking reduces failing inputs to a minimal reproducer automatically.
- Best for pure functions and parsers; needs deterministic, fast properties.
- RSIS3 relevance: wiki link-validation rules are properties every article must satisfy.

## Related
- [[wiki/testing/entities/test-patterns|Testing Patterns]] — property tests complement example tests
- [[wiki/dev-tools/benchmark-testing|Benchmark Testing]] — generative inputs stress performance too
- [[wiki/dev-tools/repl-driven-development|Repl-Driven Development]] — interactive exploration feeds property discovery
- [[wiki/software-engineering/functional-programming|Functional Programming]] — pure functions make the best property targets
- [[wiki/software-engineering/refactoring|Refactoring]] — properties protect behavior-preserving change
- [[wiki/testing/eval-sets|Eval Sets]] — generated inputs sharpen eval suites
