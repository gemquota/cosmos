---
type: "decision"
title: "chose TypeORM because it has the best TypeScript support"
description: "Decision: chose TypeORM because it has the best TypeScript support"
tags: ["decision", "typescript", "orm", "database", "typeorm"]
timestamp: "2026-07-19T10:08:17.112Z"
---

# Chose TypeORM Because It Has the Best TypeScript Support

## Summary

This decision record documents the choice of TypeORM as the data-access layer because of its TypeScript support. ORM selection shapes the entire data layer — entity modeling, migrations, querying, and type safety — so the decision is worth preserving with its rationale and trade-offs. Future teams can revisit this record when evaluating the choice against new alternatives.

## Details

- **Decision context** — A TypeScript project needed an object-relational mapper that integrates type safety, schema management, and querying with the language's type system.
- **Criteria** — First-class TypeScript types, decorator-based entity definitions, migration tooling, and broad database support weighed heavily in the comparison.
- **Alternatives considered** — Other ORMs and query builders offer different trade-offs: some favor runtime flexibility or lighter footprints, and raw SQL maximizes control at the cost of boilerplate.
- **Why chosen** — TypeORM's decorator-driven entities and repository API keep types flowing from the schema into queries, which the decision records as the decisive advantage.
- **Trade-offs** — TypeORM adds abstraction, learning overhead, and some runtime behavior that differs from hand-written SQL; migration discipline and query review mitigate the risks.
- **Worked example** — An entity defined as a decorated class yields typed repositories, so a rename refactors the schema mapping and all type-checked queries together.
- **Common failure modes** — Letting entities drift from migrations, writing raw queries that bypass type safety, and upgrading major versions without auditing behavior changes.
- **Revisit conditions** — The decision should be revisited if type safety demands change, if the ORM's maintenance or performance becomes a bottleneck, or if a clearly superior alternative emerges.
- **Status** — Recorded as a standing decision; it captures rationale for future readers who would otherwise rediscover the trade-offs.

## Related

- [[wiki/decisions/decided-to-use-sqlite-for-the-local-database-because-it-re|SQLite Decision]] — a related data-layer choice
- [[wiki/decisions/model-selection-practice|Model Selection in Practice]] — choosing tools by evidence
- [[wiki/data-storage/sql-engines|SQL Engines]] — the database layer
- [[wiki/data-storage/database-normalization|Database Normalization]] — modeling entities
- [[wiki/decisions/self-hosting|Self-Hosting]] — deployment autonomy
- [[wiki/api-services/categories/api-rest/subcategories/rest-http/mariadb|MariaDB]] — a target database
