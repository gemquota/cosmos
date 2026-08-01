---
type: "concept"
title: "Prisma"
description: "Type-safe TypeScript ORM with schema-first modeling, migrations, and query client generation"
tags: ["prisma", "orm", "typescript", "database", "node"]
timestamp: "2026-07-31T00:00:00Z"
status: "stub"
---

# Prisma

## Summary
Prisma is a TypeScript ORM that generates a type-safe client from a declarative `schema.prisma`. It covers migrations, queries, and relations with full typing.

## Details
- Schema-first: models, relations, and enums defined once; `prisma generate` emits the client.
- Prisma Migrate versions schema changes; Studio gives a GUI for data.
- Pairs with Postgres, SQLite, MySQL, and MongoDB; strong fit for Next.js apps.

## Related
- [[wiki/devops-infra/postgresql|PostgreSQL]] — primary database target
- [[wiki/devops-infra/database-indexing|Database Indexing]] — index declarations in schema
- [[wiki/js-ts-ecosystem/typeorm|TypeORM]] — decorator-based alternative
- [[wiki/js-ts-ecosystem/drizzle|Drizzle ORM]] — SQL-first alternative
- [[wiki/js-ts-ecosystem/entities/typescript-patterns|TypeScript Ecosystem]] — type safety patterns
- [[wiki/frontend/static-site-generation|Static Site Generation]] — Prisma powers data-fetching in generated pages
