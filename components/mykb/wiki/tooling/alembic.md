---
type: "concept"
title: "Alembic"
description: "Lightweight database migration tooling for SQLAlchemy with versioned revision scripts"
tags: ["alembic", "migrations", "sqlalchemy", "python", "database"]
timestamp: "2026-07-31T00:00:00Z"
status: "growing"
---

# Alembic

## Summary
Alembic is SQLAlchemy's migration framework: versioned `upgrade()`/`downgrade()` scripts applied in order, with autogenerate support from model metadata.

## How Migrations Work

Alembic stores a linear or branched history of revisions in `alembic/versions/`, each file defining `upgrade()` and `downgrade()` operations. The database tracks the current revision in the `alembic_version` table, and `alembic upgrade head` walks the history applying only pending revisions.

- `alembic revision --autogenerate` diffs models vs database to scaffold migrations.
- Branching, tagging, and `alembic upgrade head` manage complex histories.
- Run migrations in CI before deploy; back up before destructive changes — PITR is the safety net.

## Working Practices

Autogenerate is a starting point, not a review substitute: it cannot reliably detect renames (it sees drop plus create), column type changes need manual confirmation, and server-side defaults or data backfills must be hand-written. A healthy workflow keeps each revision small, reviews the generated diff, and runs migrations against a disposable staging copy of production data before release.

SQLite deserves special care: its `ALTER TABLE` support is limited, so Alembic's batch mode rewrites the table — emit `with op.batch_alter_table(...)` to get drop-column and constraint changes safely.

Operational guidance: lock migrations to a version in CI, run them as a deploy step before the new code lands, never edit an already-applied revision (add a new one instead), and verify `downgrade()` paths for rollback. Destructive operations — dropping tables, truncating, changing column types — should be preceded by a backup, because even with a downgrade script, a failed migration is fastest to recover via a snapshot.

## Alternatives and Fit

Alembic is Python-and-SQLAlchemy-specific; other ecosystems use Django migrations, Flyway, or Prisma migrate. The concepts transfer: versioned, ordered, reversible schema changes with a recorded current version. Choose the tool that matches the ORM in use rather than adding a second migration framework alongside it.

## Related
- [[wiki/tooling/sqlalchemy|SQLAlchemy]] — the toolkit it migrates
- [[wiki/devops-infra/point-in-time-recovery|Point-in-Time Recovery]] — rollback safety net
- [[wiki/devops-infra/backups|Backups]] — pre-migration snapshots
- [[wiki/devops-infra/github-actions|GitHub Actions]] — migration step in CI
- [[wiki/devops-infra/postgresql|PostgreSQL]] — common target
- [[wiki/devops-infra/sqlite|SQLite]] — batch-mode constraints

