---
type: "concept"
title: "Drizzle ORM"
description: "SQL-first, lightweight TypeScript ORM that keeps queries close to SQL with full type inference"
tags: ["drizzle", "orm", "typescript", "sql", "database"]
timestamp: "2026-07-31T00:00:00Z"
status: "stub"
---

# Drizzle ORM

## Summary
Drizzle ORM is a "no magic" TypeScript ORM: SQL-like query builders and schema definitions with zero overhead and full type inference, increasingly popular in Next.js projects.

## Details
- Drizzle Kit handles migrations; drizzle-orm keeps bundle small (no runtime reflection).
- Queries read like SQL — `eq`, `and`, `desc` — while staying typed.
- Compare: Prisma abstracts more, Drizzle stays closer to the database.

## Related
- [[wiki/js-ts-ecosystem/prisma|Prisma]] — higher-abstraction alternative
- [[wiki/js-ts-ecosystem/typeorm|TypeORM]] — decorator-based alternative
- [[wiki/devops-infra/postgresql|PostgreSQL]] — typical target
- [[wiki/devops-infra/query-planning|Query Planning]] — SQL control matters
- [[wiki/js-ts-ecosystem/entities/typescript-patterns|TypeScript Ecosystem]] — inference-first typing
- [[wiki/frontend/static-site-generation|Static Site Generation]] — SQL-first data layer for static exports
