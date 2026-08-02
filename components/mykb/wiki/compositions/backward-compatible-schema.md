---
type: "concept"
title: "Backward-Compatible Schema"
description: "Schema changes that old code and old data can still use"
tags: ["schema", "compatibility", "migrations", "databases"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Backward-Compatible Schema

## Summary
A backward-compatible schema change lets old versions of the application keep working against the new schema — additive columns, nullable additions, and deferred enforcement. It decouples deploy from data migration.

## Details
- Additive changes (new nullable column, new table) are backward compatible; renames and drops are not.
- Follow expand-migrate-contract: add, backfill, then tighten in later releases.
- Compatibility is versioned policy: define how many old app versions you must support.
- mykb relevance: wiki frontmatter additions are additive so older readers ignore them.

## Related
- [[wiki/compositions/additive-migrations|Additive Migrations]]
- [[wiki/compositions/database-migrations|Database Migrations]]
- [[wiki/api-protocols/api-backward-compatibility|API Backward Compatibility]]
- [[wiki/compositions/data-backfills|Data Backfills]]
- [[wiki/dev-tools/continuous-delivery|Continuous Delivery]]
