---
type: "concept"
title: "Predicate Pushdown and Projection"
description: "Pushing filters and column selection into storage engines"
tags: ["predicate-pushdown", "projection", "query-optimization", "columnar"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Predicate Pushdown and Projection

## Summary

A stub to be expanded into a full article; frames the concept and open questions.

## Details

- Predicate pushdown evaluates filters in storage, returning only matching rows.
- Projection pushdown reads only needed columns from columnar files.
- Parquet row groups, ORC stripes, and zone maps make pushdown effective.
- Engines advertise pushdown capabilities; not all connectors support all pushdowns.

## Related

- [[wiki/data-storage/vectorized-query-execution|Vectorized Query Execution]] — columnar execution
- [[wiki/data-storage/columnar-storage|Columnar Storage]] — columnar formats
- [[wiki/data-storage/partition-pruning-and-zone-maps|Partition Pruning and Zone Maps]] — pruning companion
- [[wiki/data-storage/column-pruning-and-vectorized-reads|Column Pruning And Vectorized Reads]] — read path
- [[wiki/data-storage/data-engineering-fundamentals|Data Engineering Fundamentals]] — core data engineering concepts
