---
type: "concept"
title: "CSV vs Parquet Tradeoffs"
description: "When row-oriented text beats columnar binary and vice versa"
tags: ["csv", "parquet", "formats", "tradeoffs"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# CSV vs Parquet Tradeoffs

## Summary

A stub to be expanded into a full article; frames the concept and open questions.

## Details

- CSV: human-readable, universal, but slow to scan and weakly typed.
- Parquet: compressed, columnar, typed, ideal for analytics at scale.
- CSV wins for small exchanges and ad-hoc tooling; Parquet wins for warehouse/lake loads.
- Schema-on-read vs schema-on-write changes the tradeoff surface.

## Related

- [[wiki/data-storage/columnar-storage|Columnar Storage]] — columnar
- [[wiki/data-storage/compression-codecs|Compression Codecs]] — compression
- [[wiki/data-storage/open-data-formats|Open Data Formats]] — open formats
- [[wiki/data-storage/file-format-selection-metrics|File Format Selection Metrics]] — selection metrics
- [[wiki/data-storage/data-engineering-fundamentals|Data Engineering Fundamentals]] — core data engineering concepts
