---
type: "concept"
title: "Dimension Tables and Grains"
description: "The descriptive context tables that give facts their business meaning"
tags: ["dimensions", "grain", "star-schema", "modeling"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# Dimension Tables and Grains

## Summary
Dimension tables hold the descriptive attributes — who, what, where, when — that give fact measures their business meaning. The grain is the level of detail a row represents, and agreeing the grain before modeling prevents double counting; dimensions are often conformed across marts and slowly changing as attributes evolve.

## Details
- Mechanism: a star schema joins fact tables to dimension tables on foreign keys; dimension rows are stable descriptions (customer, product, date, store) with surrogate keys; the grain is declared per fact table — one row per transaction, per line item, per event; dimensions are shared (conformed) so multiple marts slice consistently; slowly changing dimensions track attribute history (Type 1 overwrites, Type 2 adds rows).
- Concrete example: a sales fact at line-item grain joins to product, customer, and date dimensions; aggregating revenue by product slices consistently because every mart uses the same conformed product dimension; a customer changing address is a Type 2 update adding a new row, preserving history.
- Failure modes: grain ambiguity — two teams sum the same fact with different grains, double counting; dimensions that are not conformed, so the same product has different IDs across marts; surrogate keys not stable, breaking history; dimension tables that are actually facts in disguise; role-playing dimensions (date_shipped, date_ordered) modeled as separate tables, multiplying maintenance.
- Tradeoffs: dimensional modeling trades normalization for query speed and comprehension — the star schema is the price of fast analytics; the alternative, normalized modeling, is flexible and hard to query; the mature pattern is conformed dimensions, declared grains, and deliberate handling of slowly changing attributes.
- Operational notes: document the grain per fact, govern dimension changes, and test that joins never multiply fact rows.
- RSIS3 relevance: the wiki's analytics (article counts by status, tag, date) form a natural star schema — dimensions are tags and statuses, and the grain decision prevents double-counted metrics.


## Related
- [[wiki/data-storage/dimensional-modeling|Dimensional Modeling]] — core modeling reference
- [[wiki/data-storage/surrogate-keys|Surrogate vs Natural Keys]] — stable keys for dimension rows
- [[wiki/data-storage/fact-tables-and-measures|Fact Tables And Measures]] — the counterpart table type
- [[wiki/data-storage/conformed-dimensions|Conformed Dimensions]] — shared dimensions across marts
- [[wiki/data-storage/role-playing-dimensions|Role Playing Dimensions]] — dimension reuse with roles
