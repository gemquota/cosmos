---
type: "concept"
title: "SQLAlchemy"
description: "Python SQL toolkit and ORM providing the industry-standard database access layer"
tags: ["sqlalchemy", "python", "orm", "sql", "database"]
timestamp: "2026-07-31T00:00:00Z"
status: "stub"
---

# SQLAlchemy

## Summary
SQLAlchemy is Python's de facto SQL toolkit and ORM: a Core expression language plus an ORM layer, with Alembic as its migration partner. It powers FastAPI/Flask stacks.

## Details
- Core vs ORM lets you go from raw SQL-ish expressions to mapped classes.
- Dialect support spans Postgres, SQLite, MySQL, and more; connection pooling built in.
- Pairs with FastAPI (used by RSIS3 dashboards) for typed models and sessions.

## Related
- [[wiki/tooling/alembic|Alembic]] — SQLAlchemy migrations
- [[wiki/devops-infra/postgresql|PostgreSQL]] — primary dialect
- [[wiki/devops-infra/connection-pooling|Connection Pooling]] — engine pool settings
- [[wiki/api-protocols/rest-apis|REST APIs]] — FastAPI + SQLAlchemy stacks
- [[wiki/concepts/mykb-implementation-report|Mykb Implementation Report]] — Python stack notes
