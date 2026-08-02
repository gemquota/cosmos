---
type: "concept"
title: "Data Modeling: Star Schema"
description: "The fact-and-dimension design at the heart of dimensional warehousing"
tags: ["star-schema", "facts", "dimensions", "modeling"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://en.wikipedia.org/wiki/Star_schema", "https://en.wikipedia.org/wiki/Dimensional_modeling"]
---

# Data Modeling: Star Schema

## Summary

A star schema centers on one or more fact tables joined to surrounding dimension tables.
Facts hold measures and dimension keys at a declared grain; dimensions provide descriptive context.
It is the workhorse design for BI because it is simple to understand, query, and optimize.
Star schemas reward up-front grain decisions; changing grain later means rewriting facts and re-validating reports.

## Details

- Grain first: decide exactly what one fact row represents before modeling.
- Additive measures sum across dimensions; semi- and non-additive measures need rules.
- Conformed dimensions let multiple marts share a consistent business vocabulary.
- Star schemas trade normalization for query speed; snowflakes re-normalize some dimensions.
- Modern warehouses still map OLTP sources to star-shaped marts for analytics.
- Surrogate keys plus natural-key audit columns keep joins stable across source changes.
- Design for the questions asked today, but keep additive measures flexible enough for tomorrow.
- Validate star designs with real query patterns before building; the schema should follow the questions, not the source system.

## Related

- [[wiki/data-storage/fact-tables-and-measures|Fact Tables And Measures]] — fact design
- [[wiki/data-storage/dimension-tables-and-grains|Dimension Tables And Grains]] — dimension design
- [[wiki/data-storage/conformed-dimensions|Conformed Dimensions]] — shared dimensions
- [[wiki/data-storage/dimensional-modeling|Dimensional Modeling]] — existing modeling note
- [[wiki/data-storage/data-modeling|Data Modeling]] — modeling concepts

