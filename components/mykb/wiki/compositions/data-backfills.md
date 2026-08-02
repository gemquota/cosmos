---
type: "concept"
title: "Data Backfills"
description: "Filling in derived or migrated data for existing records"
tags: ["backfills", "data", "migrations", "databases"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Data Backfills

## Summary
A data backfill computes and writes values for records that predate a new field or rule — new column defaults, derived metrics, re-indexed content. Backfills are the data half of schema evolution and need idempotency and resumability.

## Details
- Run backfills in batches with checkpoints so they survive restarts.
- Make backfill logic idempotent: re-running must not corrupt or double-apply.
- Backfill before enforcing constraints, then validate counts and samples.
- mykb relevance: the wiki backfilled slug fields and tag indexes in one migration pass.

## Related
- [[wiki/compositions/backward-compatible-schema|Backward-Compatible Schema]]
- [[wiki/compositions/additive-migrations|Additive Migrations]]
- [[wiki/compositions/database-migrations|Database Migrations]]
- [[wiki/compositions/idempotent-writes|Idempotent Writes]]
- [[wiki/compositions/dual-writes|Dual Writes]]
