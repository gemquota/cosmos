---
type: "concept"
title: "Test Timeouts"
description: "Bounding test execution to prevent hangs and slow failures"
tags: ["test-timeouts", "testing", "reliability", "ci"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://pytest-timeout.readthedocs.io/", "https://jestjs.io/docs/jest-object"]
---

# Test Timeouts

## Summary
Test timeouts bound how long a test may run before failing, preventing hangs, infinite loops, and deadlocks from stalling whole suites. They are a cheap guard on robustness that also keeps CI deterministic.

## Details
- Configuration: pytest-timeout, Jest testTimeout, JUnit Timeout, and Go context deadlines.
- Set generous per-test limits: too tight causes flakiness on slow CI machines.
- Hangs often reveal leaks: unclosed connections, spawned processes, and event-loop starvation.
- Debugging: dump thread stacks on timeout so failures are diagnosable.
- CI-level global timeouts catch runaway suites and infinite retry loops.
- Distinguish test timeouts from external-call timeouts; both belong in the contract.
- Prefer explicit waits and deadlines inside code over blanket test timeouts.

## Related
- [[wiki/api-protocols/timeouts|Timeouts]] — the runtime counterpart to test timeouts
- [[wiki/testing/flaky-tests|Flaky Tests]] — tight timeouts cause flakiness
- [[wiki/testing/async-testing|Asynchronous Testing]] — async code needs timeout discipline
- [[wiki/testing/ci-quality-gates|CI Quality Gates]] — suite-level time budget
- [[wiki/testing/test-isolation|Test Isolation]] — leaks that hang suites
- [[wiki/api-protocols/retry-backoff|Retry Backoff]] — avoiding retry storms in tests
