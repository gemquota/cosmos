---
type: "concept"
title: "Parquet and ORC"
description: "The open columnar file formats of the data lake"
tags: ["parquet", "orc", "columnar", "formats"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://parquet.apache.org/docs/file-format/", "https://orc.apache.org/docs/", "https://en.wikipedia.org/wiki/Apache_Parquet"]
---

# Parquet and ORC

## Summary

Parquet and ORC are open, columnar file formats optimized for analytical workloads.
Both store column statistics per row group to enable skipping.
They are the interchange standard for lakehouse data.
Both formats are open and widely supported, so ecosystem fit matters more than raw benchmarks.

## Details

- Parquet: Apache project, wide engine support, nested data via record shredding.
- ORC: optimized for Hive ecosystems with built-in indexes.
- Both support multiple compression codecs (snappy, zstd, gzip).
- Predicate pushdown uses row-group min/max stats.
- Choose by ecosystem: both are excellent; interoperability is now common.
- Nested data support differs subtly; test with your schema.
- Row-group sizing affects parallelism and pruning granularity.
- Standardize on one primary format for your lake to keep tooling and skills focused, and document exceptions.

## Related

- [[wiki/data-storage/columnar-storage-formats|Columnar Storage Formats]] — columnar concepts
- [[wiki/data-storage/predicate-pushdown-and-projection|Predicate Pushdown And Projection]] — pushdown
- [[wiki/data-storage/file-format-selection-metrics|File Format Selection Metrics]] — choosing formats
- [[wiki/data-storage/columnar-storage|Columnar Storage]] — columnar
- [[wiki/data-storage/compression-codecs|Compression Codecs]] — codecs

