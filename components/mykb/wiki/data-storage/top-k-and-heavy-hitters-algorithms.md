---
type: "concept"
title: "Top-K and Heavy Hitters Algorithms"
description: "Finding the most frequent items efficiently"
tags: ["top-k", "heavy-hitters", "sketches", "algorithms"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Top-K and Heavy Hitters Algorithms

## Summary

A stub to be expanded into a full article; frames the concept and open questions.

## Details

- Heavy-hitters algorithms (Misra-Gries, SpaceSaving, count-min) find frequent items in one pass.
- They answer 'what are the top sellers/top errors' over massive streams.
- Error bounds depend on frequency thresholds and sketch width.
- Used in logs analytics, network monitoring, and recommendation pipelines.

## Related

- [[wiki/data-storage/olap-vs-oltp|OLAP vs OLTP]] — analytics
- [[wiki/data-storage/top-k-and-heavy-hitters-algorithms|Top-K and Heavy Hitters Algorithms]] — algorithm family
- [[wiki/data-storage/sketch-based-analytics|Sketch Based Analytics]] — sketch analytics
- [[wiki/data-storage/log-collection-and-aggregation|Log Collection & Aggregation]] — log analytics
- [[wiki/data-storage/data-engineering-fundamentals|Data Engineering Fundamentals]] — core data engineering concepts
