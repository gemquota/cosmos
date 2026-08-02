---
type: "concept"
title: "Database Normalization"
description: "Normal forms and removing redundancy from schemas"
tags: ["normalization", "normal-forms", "schema-design", "relational-design"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://en.wikipedia.org/wiki/Database_normalization", "https://www.postgresql.org/docs/current/ddl.html"]
---

# Database Normalization

## Summary
Normalization is the systematic removal of redundancy from relational schemas using normal forms. Each form eliminates a class of anomalies — update, insert, and delete — by decomposing tables until every non-key attribute depends on the whole key.

## Details
- **First normal form (1NF)** — every cell holds a single value; no repeating groups or arrays. It is mostly table-stakes in modern engines.
- **Second normal form (2NF)** — no partial dependencies: non-key columns must depend on the entire composite key, not a subset; removes redundancy in join tables with extra attributes.
- **Third normal form (3NF)** — no transitive dependencies: non-key columns must not depend on other non-key columns; e.g., storing `city` when `zip` already determines it violates 3NF.
- **BCNF and beyond** — Boyce-Codd normal form tightens 3NF for overlapping candidate keys; 4NF handles multivalued dependencies, and 5NF handles join dependencies — rarely needed in practice.
- **Decomposition** — normalization splits tables and adds foreign keys; queries that used to be single-table now need joins, so the schema gains write safety at the cost of read complexity.
- **Practical stance** — normalize to 3NF as the default, then denormalize deliberately where measured queries justify it; premature denormalization bakes in the anomalies normalization prevents.

## Related
- [[wiki/data-storage/denormalization|Denormalization]] — the deliberate reversal
- [[wiki/data-storage/database-constraints|Database Constraints]] — enforcing the decomposed model
- [[wiki/data-storage/data-modeling|Data Modeling]] — the design process normalization guides
- [[wiki/data-storage/surrogate-keys|Surrogate vs Natural Keys]] — keys that survive decomposition
- [[wiki/data-storage/join-algorithms|Join Algorithms]] — the cost of recombining decomposed tables
