---
type: "concept"
title: "Code Review for Tests"
description: "Reviewing tests for assertion quality, coverage, and maintainability"
tags: ["code-review", "testing", "review", "quality"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://google.github.io/eng-practices/review/review-look-for/", "https://www.ibm.com/topics/code-review"]
---

# Code Review for Tests

## Summary
Reviewing tests themselves, assertions, coverage, readability, and intent, is as important as reviewing production code. Weak tests pass review quietly and let regressions through while giving false confidence.

## Details
- Review whether each test fails for the right reason and assertions are meaningful.
- Check isolation, no order dependence, no sleeps, determinism, and good naming.
- Look for copied tests, over-mocking, implementation-detail assertions, and empty assertions.
- Verify tests exercise behavior users care about, not just coverage.
- Use coverage and mutation hints to spot untested branches.
- Treat test review as a first-class review type.
- Automate some checks: linters, coverage gates, and mutation score on critical modules.

## Related
- [[wiki/software-engineering/code-review|Code Review]] — the general practice this applies
- [[wiki/testing/mutation-testing|Mutation Testing]] — surviving mutants flag weak tests
- [[wiki/testing/coverage-metrics|Coverage Metrics]] — what review can inspect
- [[wiki/testing/flaky-tests|Flaky Tests]] — reviewing tests that flake
- [[wiki/testing/measuring-test-roi|Measuring Test ROI]] — justifying test maintenance
- [[wiki/testing/test-frameworks|Test Frameworks]] — idioms review checks
