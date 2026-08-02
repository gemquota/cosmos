---
type: "concept"
title: "Normalization Forms"
description: "The 1NF-3NF/BCNF rules that structure dependency-free tables"
tags: ["normalization", "normal-forms", "databases", "design"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Normalization Forms

## Summary
Normal forms are progressive rules for table structure: 1NF requires atomic columns, 2NF removes partial dependencies, 3NF removes transitive dependencies, BCNF tightens 3NF. They exist to kill redundancy and update anomalies.

## Details
- Most practical schemas stop at 3NF/BCNF; higher forms (4NF, 5NF) are academic in most shops.
- Each form fixes a specific anomaly: partial dependencies, transitive dependencies, multi-valued facts.
- Denormalization is a deliberate, documented exception — not ignorance of the forms.
- mykb relevance: wiki tag tables pass 3NF by separating tags into their own relation.

## Related
- [[wiki/compositions/schema-normalization|Schema Normalization]]
- [[wiki/compositions/denormalization-tradeoffs|Denormalization Tradeoffs]]
- [[wiki/software-engineering/entities-vs-value-objects|Entities vs Value Objects]]
- [[wiki/compositions/database-migrations|Database Migrations]]
- [[wiki/software-engineering/domain-driven-design|Domain-Driven Design]]
