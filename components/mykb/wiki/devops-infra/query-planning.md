---
type: "concept"
title: "Query Planning"
description: "How databases turn SQL into execution plans, choosing join orders and index access paths"
tags: ["query-planning", "database", "performance", "sql", "optimizer"]
timestamp: "2026-07-31T00:00:00Z"
status: "stub"
---

# Query Planning

## Summary
Query planning is the optimizer's job of translating SQL into an execution plan: table order, join methods, and index usage. Understanding plans is the core of database performance work.

## Details
- `EXPLAIN ANALYZE` reveals actual vs estimated costs; look for seq scans, sorts, and nested loops.
- Statistics (row estimates) drive choices; stale stats cause bad plans — run `ANALYZE`.
- Parameters, missing indexes, and join order are the usual culprits in slow queries.

## Related
- [[wiki/devops-infra/database-indexing|Database Indexing]] — plans choose index paths
- [[wiki/devops-infra/postgresql|PostgreSQL]] — EXPLAIN tooling
- [[wiki/devops-infra/connection-pooling|Connection Pooling]] — concurrency effects
- [[wiki/devops-infra/observability|Observability]] — slow-query monitoring
