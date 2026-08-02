---
type: "concept"
title: "Database Migration Testing"
description: "Verifying schema migrations run safely forward and backward"
tags: ["database-migrations", "testing", "schema", "rollback"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://docs.flywaydb.org/", "https://www.liquibase.org/"]
---

# Database Migration Testing

## Summary
Database migration testing verifies schema migrations run safely, forward and backward, with data preserved, so releases do not corrupt or lose data. Migrations are among the riskiest deployment steps and deserve explicit test coverage.

## Details
- Tools: Flyway, Liquibase, Alembic for Python, Prisma Migrate, and Django migrations.
- Test clean-database applies, upgrade-from-current-state, rollback, and data preservation.
- Validate idempotency and ordering; test against a copy of production data.
- Backward compatibility: the new schema must work with the old app version during rolling deploys.
- Automate in CI with ephemeral databases; run destructive tests in isolated environments.
- Consider large-table concerns: locking, downtime, and backfill times.
- Version-control migrations and review them like production code.

## Related
- [[wiki/testing/database-testing|Database Testing]] — behavior after migrations
- [[wiki/testing/containerized-test-environments|Containerized Test Environments]] — ephemeral databases for migration runs
- [[wiki/tooling/alembic|Alembic]] — a migration tool under test
- [[wiki/devops-infra/rollback-plans|Rollback Plans]] — downgrade paths migrations verify
- [[wiki/devops-infra/release-trains|Release Trains]] — migrations released with apps
- [[wiki/testing/test-environments|Test Environments]] — staging migration rehearsal
