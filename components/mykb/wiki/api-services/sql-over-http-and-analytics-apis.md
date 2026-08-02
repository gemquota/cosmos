---
type: "concept"
title: "SQL over HTTP and Analytics APIs"
description: "Running SQL through REST endpoints"
tags: ["sql-over-http", "analytics-api", "rest", "query"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# SQL over HTTP and Analytics APIs

## Summary

A stub to be expanded into a full article; frames the concept and open questions.

## Details

- Services like Trino, ClickHouse, BigQuery, and DuckDB expose SQL over HTTP.
- Design: read-only by default, query timeouts, result limits, and cost caps.
- Return results as JSON, Arrow, or CSV depending on client needs.
- Parameterized queries and prepared statements prevent injection and enable caching.

## Related

- [[wiki/api-services/api-design-for-data|Api Design For Data]] — API design
- [[wiki/data-storage/duckdb-and-embedded-analytics|Duckdb And Embedded Analytics]] — embedded SQL
- [[wiki/data-storage/presto-and-trino|Presto And Trino]] — HTTP SQL engine
- [[wiki/api-services/rate-limiting-data-apis|Rate Limiting Data Apis]] — protection
- [[wiki/data-storage/data-engineering-fundamentals|Data Engineering Fundamentals]] — core data engineering concepts
