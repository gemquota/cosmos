---
type: "entity"
title: "TypeORM"
description: "Decorator-driven TypeScript ORM supporting active-record and data-mapper patterns"
tags: ["typeorm", "orm", "typescript", "database", "node"]
timestamp: "2026-07-31T00:00:00Z"
status: "stub"
---

# TypeORM

## Summary
TypeORM is a TypeScript ORM using class decorators to map entities to tables, supporting both active-record and data-mapper styles plus migrations.

## Details
- Entity decorators (`@Entity`, `@Column`, `@OneToMany`) define the schema in code.
- Supports many databases and syncs schema from entities in dev.
- A project decision record notes TypeORM was chosen for TypeScript support — see the SQLite decision.

## Related
- [[wiki/devops-infra/sqlite|SQLite]] — local database target
- [[wiki/decisions/chose-typeorm-because-it-has-the-best-typescript-support|TypeORM Decision]] — project rationale
- [[wiki/js-ts-ecosystem/prisma|Prisma]] — schema-first alternative
- [[wiki/js-ts-ecosystem/drizzle|Drizzle ORM]] — SQL-first alternative
- [[wiki/js-ts-ecosystem/entities/typescript-patterns|TypeScript Ecosystem]] — typed entities
- [[wiki/api-protocols/rest-apis|REST APIs]] — entity models behind REST backends
