---
type: "concept"
title: "Schema Normalization"
description: "Structuring tables to eliminate redundancy and update anomalies"
tags: ["normalization", "schema", "databases", "design"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Schema Normalization

## Summary
Schema normalization organizes columns into tables so each fact is stored once, removing redundancy and the anomalies that come with it — update, insert, and delete problems. It is the relational design discipline behind good schemas.

## Details
- Normal forms (1NF-3NF) define increasingly strict rules about dependencies.
- Normalization trades joins and query complexity for write safety.
- Reality is a balance: normalized core with deliberate denormalization for reads.
- mykb relevance: wiki metadata tables normalize tags, sources, and links into relations.

## Related
- [[wiki/compositions/normalization-forms|Normalization Forms]]
- [[wiki/compositions/denormalization-tradeoffs|Denormalization Tradeoffs]]
- [[wiki/compositions/normalization-forms|Schema Normalization]]
- [[wiki/compositions/backward-compatible-schema|Backward-Compatible Schema]]
- [[wiki/compositions/database-migrations|Database Migrations]]
