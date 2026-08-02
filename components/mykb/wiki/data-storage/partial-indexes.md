---
type: "concept"
title: "Partial Indexes"
description: "Indexes over filtered subsets of rows"
tags: ["partial-index", "indexing", "query-tuning", "postgresql"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://www.postgresql.org/docs/current/indexes-partial.html", "https://www.sqlite.org/partialindex.html"]
---

# Partial Indexes

## Summary
A partial index covers only the rows matching a WHERE clause, so it stays small and fast for queries that always filter the same subset. PostgreSQL and SQLite support them natively; MySQL has no direct equivalent, so the pattern is emulated with generated columns.

## Details
- **Definition** — `CREATE INDEX ... ON t (cols) WHERE predicate` indexes only rows satisfying the predicate; the planner uses it when a query's WHERE implies that predicate.
- **Why they win** — a tiny index is cheaper to scan, maintain, and cache; a status column with millions of historical rows and a few hundred active rows becomes a few-page index instead of a large one.
- **Uniqueness tricks** — `CREATE UNIQUE INDEX ... WHERE col IS NOT NULL` enforces uniqueness only on non-null values, implementing partial unique constraints; Postgres uses this pattern for soft-delete tables where `deleted_at` must be unique only once.
- **Matching queries** — for the index to apply, the query predicate must be logically stronger than the index predicate; Postgres checks implication, so `WHERE status = 'active' AND user_id = 5` matches an index on `(user_id) WHERE status = 'active'`.
- **Maintenance** — inserted rows that do not match the predicate skip index writes entirely; deleted matching rows need index cleanup, so the hot-subset pattern keeps writes cheap.

## Related
- [[wiki/data-storage/composite-indexes|Composite Indexes]] — combining partiality with multi-column keys
- [[wiki/data-storage/covering-indexes|Covering Indexes]] — both shrink what the index stores
- [[wiki/data-storage/index-maintenance|Index Maintenance]] — write amplification the partial index avoids
- [[wiki/data-storage/query-tuning|Query Tuning]] — matching predicates to partial indexes
- [[wiki/devops-infra/postgresql|PostgreSQL]] — primary host of partial indexes
