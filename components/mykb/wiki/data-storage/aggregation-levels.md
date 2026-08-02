---
type: "concept"
title: "Aggregation Levels"
description: "Precomputing summaries at multiple grains"
tags: ["aggregation", "rollups", "modeling", "performance"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Aggregation Levels

## Summary

A stub to be expanded into a full article; frames the concept and open questions.

## Details

- Pre-aggregated tables (rollups, summary tables) answer common questions fast.
- Levels: daily, weekly, by region, by product category.
- Queries drill down when pre-aggregations lack detail.
- Maintain via incremental refresh; stale aggregates mislead.

## Related

- [[wiki/data-storage/materialized-views|Materialized Views]] — materialization
- [[wiki/data-storage/rollups-and-drilldowns|Rollups And Drilldowns]] — rollup design
- [[wiki/data-storage/materialized-views-and-incremental-refresh|Materialized Views And Incremental Refresh]] — refresh
- [[wiki/data-storage/olap-cubes-and-rollups|Olap Cubes And Rollups]] — cube context
- [[wiki/data-storage/data-engineering-fundamentals|Data Engineering Fundamentals]] — core data engineering concepts
