---
type: "concept"
title: "OLAP Cubes and Rollups"
description: "Pre-aggregated multidimensional analytics"
tags: ["olap", "cubes", "rollups", "aggregation"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://en.wikipedia.org/wiki/OLAP_cube", "https://en.wikipedia.org/wiki/Online_analytical_processing"]
---

# OLAP Cubes and Rollups

## Summary

OLAP cubes pre-aggregate measures across dimensions for fast slicing.
Rollups store coarser summaries to serve common queries instantly.
Modern engines provide the same speed with better flexibility.
Pre-aggregation is a latency-for-storage tradeoff that still powers interactive analytics.

## Details

- Cube structure: measures + dimensions + hierarchies.
- Pre-computation trades storage for query latency.
- Slicing, dicing, and drill-down navigate cube space.
- Star-tree and aggregate tables are the modern equivalents.
- Incremental refresh keeps rollups fresh without full rebuilds.
- Modern engines expose the same power without rigid cube schemas.
- Refresh scheduling must match data arrival cadence.
- Rollups remain the fastest path to sub-second answers over billions of rows.

## Related

- [[wiki/data-storage/aggregation-levels|Aggregation Levels]] — levels
- [[wiki/data-storage/rollups-and-drilldowns|Rollups And Drilldowns]] — navigation
- [[wiki/data-storage/materialized-views-and-incremental-refresh|Materialized Views and Incremental Refresh]] — refresh
- [[wiki/data-storage/olap-vs-oltp|OLAP vs OLTP]] — workloads
- [[wiki/data-storage/drill-through-and-slicing|Drill Through And Slicing]] — drill
- [[wiki/data-storage/data-warehouse|Data Warehouse]] — warehouse reference
- [[wiki/data-storage/data-quality-dimensions|Data Quality Dimensions]] — quality dimensions

