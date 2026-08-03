---
type: "concept"
title: "Property-Based Testing"
description: "Testing by generating many inputs and checking invariants that must hold for all of them"
tags: ["testing", "properties", "generative", "random"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
---

# Property-Based Testing

## Summary
Property-based testing states invariants — reversing a list twice yields the original — and lets a generator try hundreds or thousands of inputs. Tools like Hypothesis, QuickCheck, and fast-check find edge cases hand-written tests miss, because the machine explores inputs the author never imagined.

## Details
- Mechanism: define a property (a function of input that must hold) and generators for the input domain; the library generates many inputs, runs the property, and reports failures; shrinking reduces a failing input to a minimal reproducer automatically; replaying with a fixed seed makes findings reproducible.
- Concrete example: a URL normalizer property — normalizing twice equals normalizing once; a parser property — parsing then serializing round-trips; a sorting property — the output is sorted and is a permutation of the input; Hypothesis finds a Unicode edge case in the normalizer that hand-written examples missed.
- Failure modes: properties that are too weak (trivially true) or wrong (asserting buggy behavior as law); generators that do not cover the domain (only valid inputs, missing hostile ones); properties with side effects or nondeterminism, causing flaky failures; slow properties making thousands of runs impractical; shrinking producing a reproducer that no longer fails.
- Tradeoffs: property tests are the strongest complement to example tests — they trade authoring skill and runtime for broad input coverage; the alternative, hand-picked examples, is easy and blind; the mature pattern is a core of example tests plus properties for invariants, round-trips, and parsers.
- Operational notes: run in CI, keep seeds for replay, and triage every property failure into a regression example.
- RSIS3 relevance: wiki link-validation rules are properties every article must satisfy — generative testing proves the rules hold across the corpus.

## Related
- [[wiki/testing/entities/test-patterns|Testing Patterns]] — property tests complement example tests
- [[wiki/dev-tools/benchmark-testing|Benchmark Testing]] — generative inputs stress performance too
- [[wiki/dev-tools/repl-driven-development|Repl-Driven Development]] — interactive exploration feeds property discovery
- [[wiki/software-engineering/functional-programming|Functional Programming]] — pure functions make the best property targets
- [[wiki/software-engineering/refactoring|Refactoring]] — properties protect behavior-preserving change
- [[wiki/testing/eval-sets|Eval Sets]] — generated inputs sharpen eval suites
