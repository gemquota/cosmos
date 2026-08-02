---
type: "concept"
title: "Test Isolation"
description: "Ensuring each test starts from clean, independent state"
tags: ["test-isolation", "testing", "state", "determinism"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://docs.pytest.org/en/stable/how-to/fixtures.html", "https://www.ibm.com/topics/test-isolation"]
---

# Test Isolation

## Summary
Test isolation guarantees each test starts from clean, independent state and leaves no trace behind. Isolated tests run in any order, in parallel, and fail with clear causes instead of cascading interference.

## Details
- Scope: in-memory state, database rows, files, environment variables, caches, and global singletons.
- Mechanisms: fresh fixtures per test, rolled-back transactions, per-test databases, and reset hooks.
- pytest fixtures and JUnit setup methods rebuild state; Testcontainers recreate containers.
- Shared static state is the classic leak: mocks and singletons must reset between tests.
- Isolation enables parallelism, randomized order, and rerun-on-failure workflows.
- Isolation has a cost in setup overhead; balance with session-scoped read-only data.
- A test that fails alone but passes in the suite is an isolation bug.

## Related
- [[wiki/testing/test-ordering|Test Ordering]] — isolation removes order dependence
- [[wiki/testing/test-parallelism|Test Parallelism]] — isolation is the precondition
- [[wiki/testing/flaky-tests|Flaky Tests]] — state leaks are a flake source
- [[wiki/testing/database-seeding|Database Seeding]] — known state per test
- [[wiki/testing/in-memory-databases|In-Memory Databases]] — fast isolated persistence
- [[wiki/testing/test-data-management|Test Data Management]] — provisioning isolated datasets
