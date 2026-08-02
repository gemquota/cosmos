---
type: "concept"
title: "TimescaleDB and Postgres Extensions"
description: "Time-series power inside Postgres"
tags: ["timescaledb", "postgres", "time-series", "extensions"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://docs.timescale.com/", "https://en.wikipedia.org/wiki/TimescaleDB"]
---

# TimescaleDB and Postgres Extensions

## Summary

TimescaleDB turns Postgres into a time-series database via hypertables.
It keeps SQL compatibility while adding partitioning and compression.
Postgres extensions in general extend the engine without forks.
Postgres extensions are a platform strategy: Timescale adds time-series superpowers without leaving SQL.

## Details

- Hypertables auto-partition by time; chunks are regular Postgres tables.
- Continuous aggregates incrementally refresh rollups.
- Native compression cuts storage for old chunks.
- Full SQL and joins with relational data.
- The extension model makes Postgres a platform.
- Compression and continuous aggregates reduce storage and query cost.
- Hypertable chunking keeps inserts and scans fast.
- TimescaleDB proves that Postgres can be a time-series platform without giving up SQL.

## Related

- [[wiki/data-storage/time-bucketing-and-rollups|Time Bucketing And Rollups]] — rollups
- [[wiki/data-storage/continuous-aggregates-and-materialized-views|Continuous Aggregates And Materialized Views]] — aggregates
- [[wiki/data-storage/time-series-queries-and-gaps|Time Series Queries And Gaps]] — queries
- [[wiki/data-storage/time-series-databases|Time-Series Databases]] — TSDB
- [[wiki/data-storage/downsampling-and-retention-policies|Downsampling And Retention Policies]] — retention
- [[wiki/data-storage/data-warehouse|Data Warehouse]] — warehouse reference

