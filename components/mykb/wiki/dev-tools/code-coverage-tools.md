---
type: "concept"
title: "Code Coverage Tools"
description: "Tools that measure which lines and branches of code execute during a test run"
tags: ["coverage", "testing", "tooling", "quality-gates"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Code Coverage Tools

## Summary
Code coverage tools instrument a program or its bytecode to record which statements, branches, and paths a test suite exercises. Coverage reports guide where tests are missing, though high percentages do not prove correctness.

## Details
- Line, branch, and function coverage are the common metrics; branch coverage catches untested decision outcomes.
- Instrumentation happens at runtime (gcov, JaCoCo) or via tracing (coverage.py, Istanbul), each with a speed tradeoff.
- Thresholds are enforced in CI so coverage regressions fail the build, but they should be paired with mutation testing to expose weak assertions.
- RSIS3 relevance: coverage data on the mykb wiki corpus could show which articles are untested by agent recall drills.

## Related
- [[wiki/dev-tools/code-coverage|Code Coverage]]
- [[wiki/testing/coverage-metrics|Coverage Metrics]]
- [[wiki/testing/mutation-testing|Mutation Testing]]
- [[wiki/software-engineering/static-analysis-tools|Static Analysis Tools]]
- [[wiki/testing/ci-quality-gates|CI Quality Gates]]
- [[wiki/testing/unit-testing|Unit Testing]]
