---
type: "concept"
title: "Database Transactions"
description: "Atomic units of work that group operations to commit or roll back together"
tags: ["transactions", "database", "acid", "concurrency", "sql"]
timestamp: "2026-07-31T00:00:00Z"
status: "stub"
---

# Database Transactions

## Summary
A transaction groups multiple operations into one atomic unit: either all commit or all roll back. Transactions preserve consistency under concurrency and crashes.

## Details
- BEGIN/COMMIT/ROLLBACK framing; savepoints allow partial rollback.
- Isolation levels trade consistency for concurrency; choose per workload.
- Keep transactions short — long ones hold locks and bloat connection pools.

## Related
- [[wiki/devops-infra/acid|ACID]] — the guarantees behind transactions
- [[wiki/devops-infra/isolation-levels|Isolation Levels]] — concurrency semantics
- [[wiki/devops-infra/optimistic-locking|Optimistic Locking]] — conflict handling without locks
- [[wiki/api-protocols/idempotency|Idempotency]] — application-level dedup around transactions
- [[wiki/devops-infra/sqlite|SQLite]] — transactional by default
