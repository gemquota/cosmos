---
type: "concept"
title: "Code Coverage"
description: "The percentage of code exercised by tests, used as a signal for test sufficiency"
tags: ["testing", "metrics", "quality", "coverage"]
timestamp: "2026-08-01T00:00:00Z"
status: "stub"
---

# Code Coverage

## Summary
Code coverage measures which lines, branches, or paths tests execute. It is a useful signal for finding untested code, but it measures exercise, not correctness — 100% coverage can still miss bugs.

## Details
- Line vs branch coverage: branch coverage catches untested decision paths.
- Use as a floor and a diff gate (new code must be covered), not a target to game.
- RSIS3 relevance: wiki link validation covers the graph; missing links are uncovered edges.

## Related
- [[wiki/testing/entities/test-patterns|Testing Patterns]] — coverage guides where tests are missing
- [[wiki/dev-tools/mutation-testing|Mutation Testing]] — a stronger check that coverage games cannot fool
- [[wiki/testing/eval-sets|Eval Sets]] — for LLM systems, evals are the coverage story
- [[wiki/software-engineering/refactoring|Refactoring]] — the refactoring safety net coverage describes
