---
type: "concept"
title: "Pandas Performance"
description: "Making pandas workloads fast and memory-efficient"
tags: ["pandas", "performance", "python", "dataframes"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Pandas Performance

## Summary

A stub to be expanded into a full article; frames the concept and open questions.

## Details

- Vectorize with array ops; avoid row-wise loops and apply with Python closures.
- dtype choices (category, float32) and chunked reads cut memory.
- Polars, DuckDB, and cuDF are speedups when pandas patterns hit limits.
- Profile with line_profiler/memory_profiler before optimizing.

## Related

- [[wiki/data-storage/polars-and-dataframes|Polars And Dataframes]] — alternative
- [[wiki/data-storage/numpy-vectorization|Numpy Vectorization]] — numpy layer
- [[wiki/data-storage/dataframes-in-production|Dataframes In Production]] — production patterns
- [[wiki/data-storage/data-engineering-fundamentals|Data Engineering Fundamentals]] — core data engineering concepts
- [[wiki/data-storage/data-warehousing-concepts|Data Warehousing Concepts]] — warehouse fundamentals
