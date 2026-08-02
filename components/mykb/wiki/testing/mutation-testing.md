---
type: "concept"
title: "Mutation Testing"
description: "Injecting faults to measure how well tests detect real defects"
tags: ["mutation-testing", "testing", "effectiveness", "mutants"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://stryker-mutator.io/", "https://pitest.org/"]
---

# Mutation Testing

## Summary
Mutation testing injects small faults, called mutants, into source code and checks whether the test suite fails on each one. It measures test effectiveness, the kill ratio, rather than mere coverage, revealing behavior that tests do not actually verify.

## Details
- Common mutations: flip operators, delete statements, change constants, and remove conditions.
- Tools: Stryker for JavaScript, TypeScript, .NET, and JVM; PIT for Java; Mutmut for Python; Infection for PHP.
- A surviving mutant means either untested code or assertions too weak to catch the fault.
- The kill ratio is a stronger quality signal than line coverage.
- Cost: every mutant needs a test run, so use incremental, scoped runs in CI.
- Focus on surviving mutants in critical logic; not every mutant is worth killing.
- Equivalent mutants, behavior-preserving changes, need manual classification.

## Related
- [[wiki/dev-tools/mutation-testing|Mutation Testing]] — developer-tooling view of the technique
- [[wiki/testing/coverage-metrics|Coverage Metrics]] — reach versus effectiveness
- [[wiki/testing/branch-coverage|Branch Coverage]] — a weaker cousin of mutation score
- [[wiki/testing/code-review-for-tests|Code Review for Tests]] — reviewing why mutants survive
- [[wiki/testing/ci-quality-gates|CI Quality Gates]] — enforcing mutation thresholds
- [[wiki/testing/test-frameworks|Test Frameworks]] — the suite being mutated
