---
type: "concept"
title: "Transactional Facts"
description: "One row per event at the finest grain"
tags: ["transactional-facts", "modeling", "facts", "grain"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Transactional Facts

## Summary

A stub to be expanded into a full article; frames the concept and open questions.

## Details

- Transactional facts record each event (sale line, click, log entry) as a row.
- They are additive, queryable at the finest grain, and support drill-through.
- Volume grows fastest; partition and aggregate for speed.
- Most additive measures live here.

## Related

- [[wiki/data-storage/dimensional-modeling|Dimensional Modeling]] — modeling
- [[wiki/data-storage/fact-tables-and-measures|Fact Tables And Measures]] — facts
- [[wiki/data-storage/grain-and-additivity|Grain And Additivity]] — grain
- [[wiki/data-storage/aggregation-levels|Aggregation Levels]] — aggregation
- [[wiki/data-storage/data-engineering-fundamentals|Data Engineering Fundamentals]] — core data engineering concepts
