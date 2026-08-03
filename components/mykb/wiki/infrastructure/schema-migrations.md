---
type: "concept"
title: "Schema Migrations"
description: "Versioned, reversible changes to database schemas that ship safely alongside application deploys"
tags: ["schema", "migrations", "databases", "deployments"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
---

# Schema Migrations

## Summary
Schema migrations change database structure in versioned, ordered steps that apply once and roll back deliberately. They are where deployments and data meet — and where most release risk lives. Done well, they let application and database changes ship in the same rhythm; done poorly, they lock tables, strand half-applied DDL, or silently drop data.

## Details
- Expand-and-contract: add columns and backfill first, deploy the new code, then drop the old columns — this keeps old and new code compatible through the transition. Adding a NOT NULL column, for example, needs a three-phase dance: add it nullable, backfill every row, then alter the constraint.
- Migrations must be idempotent and strictly ordered; locks and long-running DDL need planning. MySQL's ALTER TABLE commonly rewrites the whole table, while Postgres can add columns without a full rewrite but still takes locks when validating CHECK constraints.
- Blue-green and canary deploys force migrations to work with two code versions at once: every query the old version issues must still succeed against the new schema, and vice versa.
- Failure modes: migrations applied out of order, partial failure in databases without transactional DDL, long locks during peak traffic, and version skew between a rolling fleet and the database. Downgrades are often the hardest part because data written by the new version may not fit the old shape.
- Tradeoffs: explicit, versioned SQL files (Flyway, Liquibase) give reviewability and control but need discipline; ORM auto-migrations are fast to generate but can silently make destructive changes.
- Operational practice: test against production-sized data, run migrations as a separate deploy step, use advisory locks to serialize, keep a dry run in CI, and gate deploys on migration health rather than baking them into the app startup path.
- RSIS3/mykb relevance: migrations are a recurring failure pattern in any loop that touches persistent state; this node supplies the canonical ordering rules and reminds retrievals to separate schema change from data migration.

## Related
- [[wiki/infrastructure/blue-green-deployments|Blue-Green Deployments]] — two versions share one schema
- [[wiki/devops-infra/release-versioning|Release Versioning]] — paired with release versions
- [[wiki/devops-infra/postgresql|PostgreSQL]] — common migration target
- [[wiki/devops-infra/mysql|MySQL]] — common migration target
