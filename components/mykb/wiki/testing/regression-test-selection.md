---
type: "concept"
title: "Regression Test Selection"
description: "Choosing which tests to run for a given code change"
tags: ["test-selection", "testing", "ci", "incremental"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://www.ibm.com/topics/regression-testing", "https://jestjs.io/docs/cli"]
---

# Regression Test Selection

## Summary
Regression test selection chooses which tests to run for a change by analyzing the dependency graph between code and tests. It runs only affected tests, cutting CI time while preserving coverage of the change.

## Details
- Static selection maps build and test dependencies via import graphs.
- Dynamic selection tracks per-test coverage and selects tests touching changed code.
- Incremental approaches cache results and rerun only what changed plus dependents.
- Tooling: Bazel test targeting, jest --changedSince, pytest last-failed, and CI heuristics.
- Safety: conservative selection must never skip a test that could fail.
- Combine with full runs on merge or release for completeness.
- Biggest wins come on monorepos and very large suites.

## Related
- [[wiki/testing/test-prioritization|Test Prioritization]] — ordering within selected tests
- [[wiki/testing/regression-testing|Regression Testing]] — the goal selection serves
- [[wiki/testing/test-parallelism|Test Parallelism]] — fast selected runs in CI
- [[wiki/testing/ci-quality-gates|CI Quality Gates]] — gates on selected tests
- [[wiki/software-engineering/monorepo-strategies|Monorepo Strategies]] — where selection shines
- [[wiki/software-engineering/git-workflows|Git Workflows]] — change detection sources
