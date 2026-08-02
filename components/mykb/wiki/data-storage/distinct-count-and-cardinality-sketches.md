---
type: "concept"
title: "Distinct Count and Cardinality Sketches"
description: "Estimating unique values under memory limits"
tags: ["cardinality", "sketches", "distinct-count", "approximation"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Distinct Count and Cardinality Sketches

## Summary

A stub to be expanded into a full article; frames the concept and open questions.

## Details

- Exact distinct counts need memory proportional to cardinality.
- Sketches (HLL, KMV, HyperLogLog++) trade small memory for small error.
- Merging semantics let sketches compose across shards and time buckets.
- Choose error budget and mergeability over simplicity.

## Related

- [[wiki/data-storage/olap-vs-oltp|OLAP vs OLTP]] — analytics
- [[wiki/data-storage/approx-queries-and-hyperloglog|Approx Queries And Hyperloglog]] — HLL detail
- [[wiki/data-storage/sketch-based-analytics|Sketch Based Analytics]] — sketch analytics
- [[wiki/data-storage/data-sampling-and-approximate-queries|Data Sampling And Approximate Queries]] — approximation
- [[wiki/data-storage/data-engineering-fundamentals|Data Engineering Fundamentals]] — core data engineering concepts
