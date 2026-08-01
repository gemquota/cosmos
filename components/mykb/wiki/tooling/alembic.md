---
type: "concept"
title: "Alembic"
description: "Lightweight database migration tooling for SQLAlchemy with versioned revision scripts"
tags: ["alembic", "migrations", "sqlalchemy", "python", "database"]
timestamp: "2026-07-31T00:00:00Z"
status: "stub"
---

# Alembic

## Summary
Alembic is SQLAlchemy's migration framework: versioned `upgrade()`/`downgrade()` scripts applied in order, with autogenerate support from model metadata.

## Details
- `alembic revision --autogenerate` diffs models vs database to scaffold migrations.
- Branching, tagging, and `alembic upgrade head` manage complex histories.
- Run migrations in CI before deploy; back up before destructive changes — PITR is the safety net.

## Related
- [[wiki/tooling/sqlalchemy|SQLAlchemy]] — the toolkit it migrates
- [[wiki/devops-infra/point-in-time-recovery|Point-in-Time Recovery]] — rollback safety net
- [[wiki/devops-infra/backups|Backups]] — pre-migration snapshots
- [[wiki/devops-infra/github-actions|GitHub Actions]] — migration step in CI
- [[wiki/devops-infra/postgresql|PostgreSQL]] — common target
