---
type: "concept"
title: "Test Ordering"
description: "Controlling and removing dependencies between execution order and results"
tags: ["test-ordering", "testing", "determinism", "ci"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://github.com/pytest-dev/pytest-randomly", "https://www.ibm.com/topics/test-ordering"]
---

# Test Ordering

## Summary
Test ordering controls and removes dependencies between execution order and results. Order-independent tests can run in parallel, be randomized, and pinpoint failures; order-dependent tests are a maintenance trap that hides shared-state bugs.

## Details
- Dependencies arise from shared state, singletons, and external resources not cleaned up.
- Randomize order, via pytest-randomly or Jest sharding, to expose hidden dependencies.
- Explicit ordering needs are rare and should be marked as such.
- CI should vary the random seed per run to surface order bugs early.
- Fix the root cause, isolation, rather than hardcoding order.
- Sequential order is a performance compromise for stateful integration tests.
- Log the execution order used so failing runs reproduce.

## Related
- [[wiki/testing/test-isolation|Test Isolation]] — the root fix for order dependence
- [[wiki/testing/test-parallelism|Test Parallelism]] — randomization enables concurrency
- [[wiki/testing/flaky-tests|Flaky Tests]] — order bugs manifest as flakes
- [[wiki/testing/test-prioritization|Test Prioritization]] — deliberate ordering by risk
- [[wiki/testing/regression-test-selection|Regression Test Selection]] — choosing subsets without order traps
- [[wiki/testing/test-data-management|Test Data Management]] — avoiding order-dependent datasets
