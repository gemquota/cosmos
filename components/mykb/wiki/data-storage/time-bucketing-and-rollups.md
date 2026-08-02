---
type: "concept"
title: "Time Bucketing and Rollups"
description: "Aggregating timestamps into aligned intervals"
tags: ["time-bucketing", "rollups", "aggregation", "time-series"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Time Bucketing and Rollups

## Summary

A stub to be expanded into a full article; frames the concept and open questions.

## Details

- Buckets (5m, 1h, 1d) align timestamps for GROUP BY aggregation.
- Rollups precompute coarser buckets to make long-range queries fast.
- Continuous aggregates keep rollups fresh as data arrives.
- Choose bucket size to match query frequency and retention.

## Related

- [[wiki/data-storage/time-series-databases|Time-Series Databases]] — TSDB
- [[wiki/data-storage/materialized-views|Materialized Views]] — materialization
- [[wiki/data-storage/continuous-aggregates-and-materialized-views|Continuous Aggregates And Materialized Views]] — continuous aggregates
- [[wiki/data-storage/time-series-queries-and-gaps|Time Series Queries And Gaps]] — query side
- [[wiki/data-storage/data-engineering-fundamentals|Data Engineering Fundamentals]] — core data engineering concepts
