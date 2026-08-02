---
type: "concept"
title: "Data Modeling"
description: "Choosing entities, attributes, relationships, and keys"
tags: ["data-modeling", "schema-design", "entities", "relationships"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://www.postgresql.org/docs/current/ddl.html", "https://docs.getdbt.com/docs/build/data-modeling"]
---

# Data Modeling

## Summary
Data modeling translates business requirements into entities, attributes, relationships, and keys. The conceptual model captures meaning, the logical model fixes structure and constraints, and the physical model makes engine-specific choices about storage, indexes, and partitioning.

## Details
- **Entity-relationship modeling** — identify entity types (customer, order), their attributes, and relationship cardinalities (one-to-many, many-to-many); ER diagrams make the model reviewable by non-engineers.
- **Keys** — choose primary keys, natural or surrogate, and define unique and foreign keys that encode business rules; key choice drives clustering, sharding, and join performance later.
- **Normalization** — decompose to remove redundancy (3NF is the common target), then denormalize deliberately for read-heavy paths; the model should be normalized at the logical layer even if the physical layer deviates.
- **Relationships in practice** — foreign keys enforce referential integrity; many-to-many relationships need join tables; polymorphic associations (a generic `parent_id`) are a modeling smell that weakens constraints.
- **Engine fit** — relational models map to normalized tables; document stores absorb nested aggregates; warehouses use star schemas; time-series data wants explicit time dimensions. The same concepts adapt, not copy.
- **Evolution** — models change; migrations, additive columns, and versioned schemas keep the model alive without rewrites.

## Related
- [[wiki/data-storage/database-normalization|Database Normalization]] — removing redundancy in the model
- [[wiki/data-storage/surrogate-keys|Surrogate vs Natural Keys]] — key selection trade-offs
- [[wiki/data-storage/database-constraints|Database Constraints]] — encoding the model as rules
- [[wiki/data-storage/schema-migrations|Schema Migrations]] — changing the model safely
- [[wiki/data-storage/dimensional-modeling|Dimensional Modeling]] — warehouse-specific modeling
