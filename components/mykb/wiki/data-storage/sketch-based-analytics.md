---
type: "concept"
title: "Sketch-Based Analytics"
description: "Using probabilistic data structures in production analytics"
tags: ["sketches", "analytics", "approximation", "probabilistic"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Sketch-Based Analytics

## Summary

A stub to be expanded into a full article; frames the concept and open questions.

## Details

- Sketches answer cardinality, quantile, and frequency questions at fixed memory.
- Mergeability enables precomputation per partition and time bucket.
- Warehouses expose them as functions (approx_count_distinct, approx_percentile).
- Design: choose error budget, merge strategy, and retention up front.

## Related

- [[wiki/data-storage/olap-vs-oltp|OLAP vs OLTP]] — analytics
- [[wiki/data-storage/probabilistic-data-structures|Probabilistic Data Structures]] — foundations
- [[wiki/data-storage/approx-queries-and-hyperloglog|Approx Queries And Hyperloglog]] — flagship example
- [[wiki/data-storage/distinct-count-and-cardinality-sketches|Distinct Count And Cardinality Sketches]] — cardinality
- [[wiki/data-storage/data-engineering-fundamentals|Data Engineering Fundamentals]] — core data engineering concepts
