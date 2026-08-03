---
type: "concept"
title: "Code Coverage Tools"
description: "Tools that measure which lines and branches of code execute during a test run"
tags: ["coverage", "testing", "tooling", "quality-gates"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# Code Coverage Tools

## Summary
Code coverage tools instrument a program or its bytecode to record which statements, branches, and paths a test suite exercises. Coverage reports guide where tests are missing — though high percentages do not prove correctness, since untested assertions can still let broken behavior pass.

## Details
- Mechanism: instrumentation is either static (inserting counters at compile time, as gcov and JaCoCo do) or runtime tracing (coverage.py, Istanbul); execution counters are aggregated into reports per file and function; line, branch, and function coverage are the common metrics, with branch coverage catching untested decision outcomes that line coverage misses.
- Concrete example: CI runs the test suite with coverage enabled, uploads the report, and enforces a threshold — a regression below 80% line or 70% branch fails the build; a branch report shows an error path never exercised; a diff-coverage check requires new code to be covered, keeping the bar from slipping.
- Failure modes: coverage theater — teams chase percentages with tests that execute code without asserting behavior (mutation testing exposes this); coverage of glue code inflating the number while critical paths stay untested; thresholds too low to matter or too high, blocking legitimate changes; flaky coverage tools (branch misclassification, parallel-run merging bugs); ignoring the uncovered-diff signal, letting new code arrive untested.
- Tradeoffs: coverage gives an objective map of what ran, at the cost of instrumentation overhead and a metric that is easy to game; the alternative — no coverage — leaves blind spots invisible until production; the mature pattern is thresholds on new code, branch awareness, and pairing with mutation testing to test the tests.
- Operational notes: upload reports per commit, track coverage trends, and review uncovered diffs in code review.
- RSIS3 relevance: coverage data on the mykb wiki corpus could show which articles are untested by agent recall drills — the same map-of-what-ran idea applied to knowledge.

## Related
- [[wiki/dev-tools/code-coverage|Code Coverage]]
- [[wiki/testing/coverage-metrics|Coverage Metrics]]
- [[wiki/testing/mutation-testing|Mutation Testing]]
- [[wiki/software-engineering/static-analysis-tools|Static Analysis Tools]]
- [[wiki/testing/ci-quality-gates|CI Quality Gates]]
- [[wiki/testing/unit-testing|Unit Testing]]
