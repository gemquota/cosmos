---
type: "concept"
title: "Isolation Levels"
description: "Policies governing how concurrent transactions see each other's uncommitted and committed changes"
tags: ["isolation", "transactions", "database", "concurrency", "sql"]
timestamp: "2026-07-31T00:00:00Z"
status: "stub"
---

# Isolation Levels

## Summary
Isolation levels define what concurrent transactions may observe: read uncommitted, read committed, repeatable read, and serializable. Each trades consistency for concurrency.

## Details
- Phenomena controlled: dirty reads, non-repeatable reads, phantoms.
- Defaults vary — Postgres defaults to read committed; some engines default higher.
- Serializable is safest but costs throughput; use it where correctness dominates.

## Related
- [[wiki/devops-infra/transactions|Transactions]] — isolation within the ACID frame
- [[wiki/devops-infra/acid|ACID]] — the I of ACID
- [[wiki/devops-infra/optimistic-locking|Optimistic Locking]] — application-level isolation
- [[wiki/devops-infra/postgresql|PostgreSQL]] — isolation in practice
- [[wiki/devops-infra/observability|Observability]] — lock-wait and contention monitoring
