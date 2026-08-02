---
type: "concept"
title: "NumPy Vectorization"
description: "Array operations that avoid Python-level loops"
tags: ["numpy", "vectorization", "python", "performance"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# NumPy Vectorization

## Summary

A stub to be expanded into a full article; frames the concept and open questions.

## Details

- NumPy applies operations element-wise on contiguous arrays in C.
- Broadcasting and universal functions (ufuncs) express loops as array ops.
- Memory layout (C vs F order) and dtype affect cache behavior.
- Vectorized code is faster, shorter, and easier to parallelize.

## Related

- [[wiki/data-storage/pandas-performance|Pandas Performance]] — pandas uses numpy
- [[wiki/data-storage/polars-and-dataframes|Polars And Dataframes]] — vectorized frames
- [[wiki/data-storage/vectorized-query-execution|Vectorized Query Execution]] — engine analog
- [[wiki/data-storage/data-engineering-fundamentals|Data Engineering Fundamentals]] — core data engineering concepts
- [[wiki/data-storage/data-warehousing-concepts|Data Warehousing Concepts]] — warehouse fundamentals
