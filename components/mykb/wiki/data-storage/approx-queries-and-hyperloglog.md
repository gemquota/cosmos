---
type: "concept"
title: "Approximate Queries and HyperLogLog"
description: "Fast distinct-count estimation with tiny memory"
tags: ["hyperloglog", "approximate", "distinct-count", "sketches"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Approximate Queries and HyperLogLog

## Summary

A stub to be expanded into a full article; frames the concept and open questions.

## Details

- HLL estimates distinct cardinality in ~1-2KB regardless of dataset size.
- Error is tunable (typically ~0.1-2%) and relative to cardinality.
- Merging HLLs supports distributed, incremental counting.
- Used by ClickHouse, BigQuery, Druid, and most analytics engines.

## Related

- [[wiki/data-storage/olap-vs-oltp|OLAP vs OLTP]] — analytics
- [[wiki/data-storage/distinct-count-and-cardinality-sketches|Distinct Count And Cardinality Sketches]] — sketch family
- [[wiki/data-storage/data-sampling-and-approximate-queries|Data Sampling And Approximate Queries]] — approximation
- [[wiki/data-storage/count-min-sketch-and-bloom-variants|Count Min Sketch And Bloom Variants]] — related sketches
- [[wiki/data-storage/data-engineering-fundamentals|Data Engineering Fundamentals]] — core data engineering concepts
