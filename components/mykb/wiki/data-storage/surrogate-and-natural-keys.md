---
type: "concept"
title: "Surrogate and Natural Keys"
description: "Artificial stable identifiers versus business-provided identifiers in warehouse modeling"
tags: ["keys", "modeling", "surrogate-keys", "warehouse"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# Surrogate and Natural Keys

## Summary
Surrogate keys are meaningless system-generated identifiers; natural keys come from the source business domain. Surrogates decouple warehouse rows from source changes — reissued or reused natural keys do not corrupt history — while natural keys remain as attributes for joins, deduplication, and SCD versioning.

## Details
- Mechanism: the warehouse assigns a surrogate integer (or hash) as the primary key of a dimension; the natural key (customer id, SKU, email) is stored as a regular attribute with a uniqueness constraint; SCD Type 2 versioning relies on surrogates — each version is a distinct row with the same natural key but a new surrogate.
- Concrete example: a customer dimension uses customer_sk (surrogate) plus customer_id (natural); the source reissues a deleted customer id; the new customer becomes a new row instead of corrupting history; a Type 2 address change inserts a new version under a new surrogate; joins to sources use the natural key.
- Failure modes: using natural keys as primary keys when the source mutates them (history corruption); surrogate collisions from hash-based generation; forgetting the unique constraint on the natural key, allowing duplicates; surrogates without audit columns, losing provenance; natural keys containing PII or secrets stored carelessly.
- Tradeoffs: surrogates buy stability and history-preservation at the cost of an extra layer of indirection; natural keys are human-meaningful and join-friendly but unstable; the mature pattern is surrogate primary keys internally, natural keys as unique business keys, and audit columns tracking lineage.
- Operational notes: enforce natural-key uniqueness, document the mapping, and test reissued-key scenarios.
- RSIS3 relevance: wiki entity rows need the same discipline — a stable internal id with the slug as the natural key keeps renames and history safe.


## Related
- [[wiki/data-storage/surrogate-keys|Surrogate vs Natural Keys]] — existing note on surrogate keys
- [[wiki/data-storage/entity-resolution|Entity Resolution]] — matching records when keys are messy
- [[wiki/data-storage/scd-type-2-slowly-changing-dimensions|Scd Type 2 Slowly Changing Dimensions]] — surrogates enable versioning
- [[wiki/data-storage/dimension-tables-and-grains|Dimension Tables And Grains]] — keys anchor dimension design
- [[wiki/data-storage/data-engineering-fundamentals|Data Engineering Fundamentals]] — core data engineering concepts
