---
type: "concept"
title: "Flaky Tests"
description: "Detecting, quarantining, and fixing nondeterministic test failures"
tags: ["flaky-tests", "testing", "ci", "reliability"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://docs.gitlab.com/ee/ci/testing/flaky_tests.html", "https://www.ibm.com/topics/flaky-tests"]
---

# Flaky Tests

## Summary
Flaky tests fail intermittently without code changes, eroding trust in the suite. Teams detect, quarantine, and fix them systematically because flakiness converts CI signal into noise and hides real regressions.

## Details
- Causes: timing and races, network, order dependence, shared state, timezone and locale, random data, missing waits.
- Detection: rerun-until-fail scripts, retry counters, and flaky-test trackers in CI.
- Quarantine: move flaky tests out of the gate into a slow track until fixed.
- Fixes: deterministic clocks, explicit waits over sleeps, isolated state, and seeded randomness.
- Culture: forbid blanket retries that hide flakiness; track flake rate as a metric.
- Bisect flakes with reruns and logs; each test must run independently.
- Investigate flakiness promptly, since it usually signals a real race or leak.

## Related
- [[wiki/testing/test-isolation|Test Isolation]] — shared state is a top flake cause
- [[wiki/testing/test-ordering|Test Ordering]] — order-dependent failures
- [[wiki/testing/test-parallelism|Test Parallelism]] — concurrency amplifies flakiness
- [[wiki/testing/test-timeouts|Test Timeouts]] — bounding hangs from flaky paths
- [[wiki/testing/ci-quality-gates|CI Quality Gates]] — flakiness breaks gate trust
- [[wiki/dev-tools/git-bisect|Git Bisect]] — tracking down flake-inducing changes
