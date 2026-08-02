---
type: "concept"
title: "Serverless Data Platforms"
description: "Compute that scales to zero with no capacity planning"
tags: ["serverless", "bigquery", "warehouse", "scaling"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Serverless Data Platforms

## Summary

A stub to be expanded into a full article; frames the concept and open questions.

## Details

- Serverless engines allocate compute per query (BigQuery, Athena, Snowflake on-demand).
- No cluster management; concurrency handled by the platform.
- Cost shifts to per-query or per-slot models; idle costs near zero.
- Watch for long-running jobs and unbounded scans on metered pricing.

## Related

- [[wiki/data-storage/data-warehouse|Data Warehouse]] — warehouse context
- [[wiki/infrastructure/bigquery-architecture|Bigquery Architecture]] — serverless example
- [[wiki/infrastructure/on-demand-vs-reserved-compute|On Demand Vs Reserved Compute]] — pricing tradeoffs
- [[wiki/infrastructure/data-freshness-and-sla-tracking|Data Freshness And Sla Tracking]] — SLA management
- [[wiki/data-storage/data-engineering-fundamentals|Data Engineering Fundamentals]] — core data engineering concepts
