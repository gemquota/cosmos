---
type: "concept"
title: "In-Memory Databases"
description: "Using embedded in-memory databases to speed up integration tests"
tags: ["in-memory-databases", "testing", "sqlite", "isolation"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://www.sqlite.org/inmemorydb.html", "https://www.h2database.com/html/main.html"]
---

# In-Memory Databases

## Summary
In-memory databases embed a real database engine inside the test process, SQLite in-memory mode, H2, or DuckDB, giving fast, isolated persistence for tests. They trade dialect fidelity for speed and simplicity.

## Details
- SQLite in-memory mode, H2 for Java, DuckDB, and in-process Postgres flavors are common.
- Speed: no network or disk; each test gets a fresh, isolated database.
- Limitations: dialect differences in functions, constraints, and locking can mask real behavior.
- Transaction behavior and concurrency differ from the production engine.
- Strategy: use in-memory for fast logic tests and containerized real-engine tests for fidelity.
- Combine with schema migration tests to check dialect compatibility.
- Watch for SQL that passes in-memory but fails on Postgres or MySQL.

## Related
- [[wiki/testing/database-testing|Database Testing]] — the layer in-memory engines speed up
- [[wiki/testing/containerized-test-environments|Containerized Test Environments]] — real engines when fidelity matters
- [[wiki/testing/database-migration-testing|Database Migration Testing]] — dialect compatibility checks
- [[wiki/testing/test-isolation|Test Isolation]] — fresh databases per test
- [[wiki/testing/fakes|Fakes]] — in-memory persistence as a fake
- [[wiki/devops-infra/sqlite|SQLite]] — the embedded engine commonly used
