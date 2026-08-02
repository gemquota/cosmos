---
type: "concept"
title: "Time-Series Queries and Gaps"
description: "Querying timestamped data and handling missing samples"
tags: ["time-series", "gaps", "interpolation", "queries"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Time-Series Queries and Gaps

## Summary

A stub to be expanded into a full article; frames the concept and open questions.

## Details

- Time-series queries filter by time range, aggregate by bucket, and align series.
- Gaps appear when no sample exists; fill strategies: zero, previous, linear interpolation.
- Gap filling must be explicit; default joins can silently drop missing series.
- Time-series DBs optimize range scans and downsampling for this workload.

## Related

- [[wiki/data-storage/time-series-databases|Time-Series Databases]] — TSDB fundamentals
- [[wiki/data-storage/olap-vs-oltp|OLAP vs OLTP]] — workload context
- [[wiki/data-storage/time-bucketing-and-rollups|Time Bucketing and Rollups]] — bucketing
- [[wiki/data-storage/downsampling-and-retention-policies|Downsampling And Retention Policies]] — retention
- [[wiki/data-storage/data-engineering-fundamentals|Data Engineering Fundamentals]] — core data engineering concepts
