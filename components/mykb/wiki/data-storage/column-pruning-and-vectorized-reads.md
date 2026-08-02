---
type: "concept"
title: "Column Pruning and Vectorized Reads"
description: "Reading only the columns you need, in bulk batches"
tags: ["column-pruning", "vectorized", "columnar", "performance"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Column Pruning and Vectorized Reads

## Summary

A stub to be expanded into a full article; frames the concept and open questions.

## Details

- Column pruning avoids reading unneeded columns from columnar storage.
- Vectorized reads process batches of rows with tight loops and SIMD-friendly layouts.
- Parquet/ORC pages, Arrow columnar buffers, and engine code generation combine.
- Together they turn wide-table scans into narrow, fast reads.

## Related

- [[wiki/data-storage/columnar-storage|Columnar Storage]] — columnar formats
- [[wiki/data-storage/vectorized-query-execution|Vectorized Query Execution]] — execution model
- [[wiki/data-storage/apache-arrow-and-in-memory|Apache Arrow And In Memory]] — Arrow buffers
- [[wiki/data-storage/predicate-pushdown-and-projection|Predicate Pushdown And Projection]] — pushdown context
- [[wiki/data-storage/data-engineering-fundamentals|Data Engineering Fundamentals]] — core data engineering concepts
