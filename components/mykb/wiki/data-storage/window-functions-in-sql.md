---
type: "concept"
title: "Window Functions in SQL"
description: "Computing values across related rows without collapsing them"
tags: ["window-functions", "sql", "analytics", "ranking"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://www.postgresql.org/docs/current/functions-window.html", "https://en.wikipedia.org/wiki/Window_function_(SQL)"]
---

# Window Functions in SQL

## Summary

Window functions compute aggregates and rankings over a sliding frame of rows.
They keep row-level detail while adding context like running totals and ranks.
Window functions are indispensable for analytical SQL.
Window functions replace self-joins and application-side loops for many analytical problems.

## Details

- PARTITION BY defines groups; ORDER BY defines order within them.
- Frames (ROWS/RANGE BETWEEN) scope the window precisely.
- Common uses: running totals, moving averages, lag/lead, and rankings.
- They cannot be used in WHERE; wrap in a subquery or CTE.
- Performance depends on partitioning and sort support.
- Frame specification (ROWS vs RANGE) changes results subtly; verify.
- Materialize window results when reused across many queries.
- Window functions are the difference between SQL that reports and SQL that analyzes.

## Related

- [[wiki/data-storage/ranking-and-tiling-window-functions|Ranking And Tiling Window Functions]] — ranking family
- [[wiki/data-storage/lag-and-lead-analytics|Lag And Lead Analytics]] — positional
- [[wiki/data-storage/cte-and-query-rewrites|CTEs and Query Rewrites]] — composition
- [[wiki/data-storage/olap-vs-oltp|OLAP vs OLTP]] — analytics
- [[wiki/data-storage/sql-optimization-techniques|SQL Optimization Techniques]] — tuning
- [[wiki/data-storage/data-warehouse|Data Warehouse]] — warehouse reference

