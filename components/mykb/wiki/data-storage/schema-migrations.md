---
type: "concept"
title: "Schema Migrations"
description: "Versioned DDL change management and rollout"
tags: ["schema-migrations", "ddl", "versioning", "database-change-management"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://www.postgresql.org/docs/current/ddl.html", "https://docs.getdbt.com/docs/collaborate/migrate"]
---

# Schema Migrations

## Summary
Schema migrations are versioned, ordered DDL changes applied to a database over time. Teams store migration files in the repository, apply them in sequence with a tool (Flyway, Liquibase, Alembic, Prisma Migrate), and record the applied version so every environment converges on the same schema.

## Details
- **Versioned files** — each migration has a unique version and name, e.g., `20260801_add_wiki_tags.sql`; the tool tracks applied versions in a bookkeeping table, guaranteeing each runs exactly once.
- **Up/down pairs** — most frameworks define forward and rollback scripts; down migrations are best-effort and often tested only in staging, so forward-only with compensating migrations is a common alternative.
- **DDL transactionality** — PostgreSQL wraps DDL in transactions, so a failed migration rolls back fully; MySQL implicitly commits DDL, forcing manual verification and careful ordering.
- **Locking and downtime** — `ALTER TABLE ADD COLUMN` with a default can rewrite a whole table and lock writes; Postgres 11+ makes `ADD COLUMN ... DEFAULT` metadata-only, while MySQL 8's `INSTANT` algorithm covers more cases.
- **Review practice** — migrations are code: peer-reviewed, run in CI against a scratch database, and applied with expand-contract or blue-green patterns when zero downtime matters.

## Related
- [[wiki/data-storage/schema-evolution|Schema Evolution]] — the ongoing process migrations enable
- [[wiki/data-storage/expand-contract-migrations|Expand-Contract Migrations]] — zero-downtime rollout pattern
- [[wiki/data-storage/backfilling|Backfilling]] — data work that follows DDL
- [[wiki/data-storage/data-contracts|Data Contracts]] — agreeing schema changes with consumers
- [[wiki/devops-infra/changelog-practices|Changelog Practices]] — versioning conventions
