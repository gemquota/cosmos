---
type: "concept"
title: "Test Parallelism"
description: "Running tests concurrently across processes and workers to cut wall time"
tags: ["test-parallelism", "testing", "ci", "performance"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://github.com/pytest-dev/pytest-xdist", "https://jestjs.io/docs/cli"]
---

# Test Parallelism

## Summary
Test parallelism runs suites concurrently across processes, workers, and machines to cut wall-clock time. Speed lets teams run larger suites in CI and keeps feedback loops tight enough to stay meaningful.

## Details
- Tooling: pytest-xdist, Jest and Vitest workers, Playwright shards, Go test parallel, and JUnit parallel execution.
- Parallelize at three levels: tests within a process, processes on a machine, machines in CI.
- Constraint: tests must be isolated; shared databases and ports need partitioning.
- Sharding splits a suite into equal buckets for distributed runners.
- Parallelism amplifies resource contention and flakiness; watch CPU and database load.
- Seeds and file ordering must not depend on scheduling.
- Pair with test selection and caching to skip unchanged work entirely.

## Related
- [[wiki/testing/test-isolation|Test Isolation]] — the precondition for parallel runs
- [[wiki/testing/test-ordering|Test Ordering]] — order independence enables concurrency
- [[wiki/testing/flaky-tests|Flaky Tests]] — parallelism can surface flakes
- [[wiki/testing/ci-quality-gates|CI Quality Gates]] — parallel suites keep gates fast
- [[wiki/testing/test-prioritization|Test Prioritization]] — scheduling within parallel workers
- [[wiki/testing/containerized-test-environments|Containerized Test Environments]] — isolated infrastructure per worker
