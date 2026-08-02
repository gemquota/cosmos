---
type: "concept"
title: "Additive Migrations"
description: "Schema changes that only add structures, never removing or breaking"
tags: ["additive-migrations", "schema", "migrations", "databases"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Additive Migrations

## Summary
Additive migrations expand the schema — new columns, tables, indexes — without altering or removing existing ones, so old code and data keep working through the transition. They are the safe default for rolling deployments.

## Details
- Add columns as nullable or with safe defaults; backfill separately; enforce later.
- Index additions are additive and non-breaking; drops and renames are not.
- Sequence matters: each migration must leave the system runnable by both old and new code.
- mykb relevance: wiki schema grows additively; legacy fields are deprecated, not dropped.

## Related
- [[wiki/compositions/backward-compatible-schema|Backward-Compatible Schema]]
- [[wiki/compositions/database-migrations|Database Migrations]]
- [[wiki/compositions/data-backfills|Data Backfills]]
- [[wiki/dev-tools/rollback-strategies|Rollback Strategies]]
- [[wiki/dev-tools/continuous-delivery|Continuous Delivery]]
