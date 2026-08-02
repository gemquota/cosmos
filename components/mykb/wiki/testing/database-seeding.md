---
type: "concept"
title: "Database Seeding"
description: "Populating test databases with known initial state"
tags: ["database-seeding", "testing", "fixtures", "test-data"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://www.prisma.io/docs/orm/prisma-migrate/workflows/seeding", "https://laravel.com/docs/seeders"]
---

# Database Seeding

## Summary
Database seeding populates test databases with known initial state, reference data, users, and scenario fixtures, so tests run against predictable data. Good seeding makes tests readable, fast to write, and stable to assert.

## Details
- Levels: reference and master data once, per-suite fixtures, and per-test scenario data.
- Tools: Prisma seed, Rails db:seed, custom SQL and JSON fixtures, plus factories.
- Seed via SQL or ORM; keep seeds versioned and reproducible.
- Deterministic IDs and timestamps make assertions stable.
- Per-test setup through fixtures and transaction rollback beats heavyweight reseeding.
- Production-shaped data, cardinality and skew, matters for performance tests.
- Never share seeds implicitly across tests; name and isolate what each test needs.

## Related
- [[wiki/testing/factories-and-fixtures|Factories and Fixtures]] — building objects to seed
- [[wiki/testing/test-data-management|Test Data Management]] — the broader provisioning discipline
- [[wiki/testing/in-memory-databases|In-Memory Databases]] — fast seeding targets
- [[wiki/testing/database-testing|Database Testing]] — queries against seeded state
- [[wiki/testing/test-isolation|Test Isolation]] — per-test seeded state
- [[wiki/testing/fake-data-generators|Fake Data Generators]] — realistic seed values
