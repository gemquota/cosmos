---
type: "concept"
title: "File Format Selection Metrics"
description: "Choosing between CSV, JSON, Parquet, ORC, and Arrow for a workload"
tags: ["file-format", "parquet", "orc", "tradeoffs"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# File Format Selection Metrics

## Summary

A stub to be expanded into a full article; frames the concept and open questions.

## Details

- Metrics: compression ratio, scan throughput, write cost, schema flexibility, and ecosystem support.
- Parquet leads for analytics on lakes; ORC for Hive-centric stacks; JSONL for ingestion.
- Measure with representative data: compression and read benchmarks vary by cardinality.
- Consider splitting (fast writes) vs compacting (fast reads) tradeoffs.

## Related

- [[wiki/data-storage/columnar-storage|Columnar Storage]] — columnar basis
- [[wiki/data-storage/compression-codecs|Compression Codecs]] — codec impact
- [[wiki/data-storage/parquet-and-orc|Parquet And Orc]] — format deep dive
- [[wiki/data-storage/csv-parquet-tradeoffs|Csv Parquet Tradeoffs]] — CSV comparison
- [[wiki/data-storage/data-engineering-fundamentals|Data Engineering Fundamentals]] — core data engineering concepts
