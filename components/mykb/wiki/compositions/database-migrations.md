---
type: "concept"
title: "Database Migrations"
description: "Versioned, ordered schema changes applied safely to databases"
tags: ["migrations", "databases", "schema", "releases"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://en.wikipedia.org/wiki/Database_migration", "https://en.wikipedia.org/wiki/Backup"]
---

# Database Migrations

## Summary
Database migrations are versioned scripts that evolve a schema in order — upgrade and downgrade — tracked by a migration tool (Alembic, Flyway, Prisma). Practice means additive changes, reviewable diffs, and a safe rollback story for every migration.

## Details
- Each migration is a versioned file with upgrade and downgrade paths; the database records its current version.
- Additive changes (new nullable columns, new tables) are the safe default; renames and drops need multi-step discipline.
- Backfill data before enforcing constraints; enforce in later migrations, not the same one.
- Run migrations as a deploy step before new code lands; test against a production-like copy first.
- Edit never — a deployed migration is history; fix forward with a new migration.
- For the mykb bundle, migrations would version the wiki's metadata store alongside the content tree.
- Worked example — a wiki migration adds a source_status column, backfills it from the sources table, then adds an index; each step is its own reversible revision.

Worked example — a wiki migration adds a source_status column, backfills it from the sources table, then adds an index; each step is its own reversible revision.

## Related
- [[wiki/compositions/additive-migrations|Additive Migrations]]
- [[wiki/compositions/backward-compatible-schema|Backward-Compatible Schema]]
- [[wiki/compositions/data-backfills|Data Backfills]]
- [[wiki/tooling/alembic|Alembic]]
- [[wiki/compositions/backup-and-restore|Backup and Restore]]
- [[wiki/dev-tools/rollback-strategies|Rollback Strategies]]
- [[wiki/testing/database-migration-testing|Database Migration Testing]]
