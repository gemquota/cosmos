---
type: "concept"
title: "StarRocks and Doris"
description: "Open-source MPP engines for real-time and high-concurrency analytics"
tags: ["starrocks", "doris", "mpp", "olap"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# StarRocks and Doris

## Summary

A stub to be expanded into a full article; frames the concept and open questions.

## Details

- Doris is an Apache-licensed MPP database for real-time analytics; StarRocks forked from it with added optimizations.
- Both use columnar storage, materialized views, and MySQL-protocol compatibility.
- They target sub-second queries over large tables with high concurrency and low admin overhead.
- Common in China and increasingly global for interactive analytics replacing legacy OLAP stacks.

## Related

- [[wiki/data-storage/massively-parallel-processing|Massively Parallel Processing]] — MPP query model
- [[wiki/data-storage/columnar-storage|Columnar Storage]] — columnar storage basis
- [[wiki/data-storage/real-time-dashboards-and-alerts|Real Time Dashboards And Alerts]] — serving workloads
- [[wiki/data-storage/materialized-views-and-incremental-refresh|Materialized Views And Incremental Refresh]] — built-in MV acceleration
- [[wiki/data-storage/data-engineering-fundamentals|Data Engineering Fundamentals]] — core data engineering concepts
