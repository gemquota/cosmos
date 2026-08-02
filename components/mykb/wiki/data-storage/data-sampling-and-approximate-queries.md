---
type: "concept"
title: "Data Sampling and Approximate Queries"
description: "Trading exactness for speed on huge datasets"
tags: ["sampling", "approximate", "analytics", "performance"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Data Sampling and Approximate Queries

## Summary

A stub to be expanded into a full article; frames the concept and open questions.

## Details

- Sampling answers exploratory questions fast with bounded error.
- Row-level sampling, stratified sampling, and sketch-based approx differ in accuracy.
- Approximate aggregations (HLL, t-digest, TopK) give near-exact answers cheaply.
- Decide tolerance per use case: dashboards tolerate error, billing does not.

## Related

- [[wiki/data-storage/olap-vs-oltp|OLAP vs OLTP]] — analytics context
- [[wiki/data-storage/approx-queries-and-hyperloglog|Approx Queries And Hyperloglog]] — HLL
- [[wiki/data-storage/probabilistic-data-structures|Probabilistic Data Structures]] — sketch family
- [[wiki/data-storage/data-quality-dimensions|Data Quality Dimensions]] — accuracy expectations
- [[wiki/data-storage/data-engineering-fundamentals|Data Engineering Fundamentals]] — core data engineering concepts
