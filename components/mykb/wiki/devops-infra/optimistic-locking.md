---
type: "concept"
title: "Optimistic Locking"
description: "Detecting concurrent-write conflicts via version fields instead of holding row locks"
tags: ["locking", "concurrency", "database", "conflicts", "orm"]
timestamp: "2026-07-31T00:00:00Z"
status: "stub"
---

# Optimistic Locking

## Summary
Optimistic locking lets concurrent writers proceed without locks and detects conflicts at write time by comparing a version column (`version` or `updated_at`). The losing write is rejected and retried.

## Details
- Implementations: version integer increments or `WHERE version = ?` guards in the UPDATE.
- ORMs (Prisma, TypeORM, SQLAlchemy) expose it as a flag on the model.
- Fits low-contention workloads like wiki note edits; retry the whole transaction on conflict.

## Related
- [[wiki/devops-infra/transactions|Transactions]] — conflict handling within transactions
- [[wiki/devops-infra/isolation-levels|Isolation Levels]] — alternative concurrency control
- [[wiki/js-ts-ecosystem/prisma|Prisma]] — ORM versioning support
- [[wiki/devops-infra/database-indexing|Database Indexing]] — version column lookups
- [[wiki/api-protocols/idempotency|Idempotency]] — retry semantics
