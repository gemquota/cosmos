---
type: "concept"
title: "Data Compression Techniques"
description: "Reducing storage and IO with encodings and codecs"
tags: ["compression", "codecs", "storage", "performance"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://en.wikipedia.org/wiki/Data_compression", "https://clickhouse.com/docs/"]
---

# Data Compression Techniques

## Summary

Compression shrinks data to cut storage cost and IO time.
Columnar formats compress best because values are similar.
Codec choice balances ratio against CPU cost.
Compression choices are measurable tradeoffs; benchmark with representative data.

## Details

- General codecs: gzip, zstd, snappy, LZ4.
- Columnar encodings: dictionary, delta, run-length.
- Compression trades CPU for IO; zstd is the modern default.
- Compress before transfer and at rest; measure both.
- High-cardinality columns compress poorly; dates compress well.
- Columnar formats make compression nearly free.
- Compress early in pipelines to save network and storage.
- Compression is the cheapest performance improvement available: less IO is always faster.

## Related

- [[wiki/data-storage/encoding-and-dictionary-encoding|Encoding And Dictionary Encoding]] — encodings
- [[wiki/data-storage/parquet-and-orc|Parquet And Orc]] — format codecs
- [[wiki/data-storage/hot-and-cold-data-tiering|Hot And Cold Data Tiering]] — cost
- [[wiki/data-storage/compression-codecs|Compression Codecs]] — existing note
- [[wiki/data-storage/columnar-storage-formats|Columnar Storage Formats]] — columnar
- [[wiki/data-storage/data-quality-dimensions|Data Quality Dimensions]] — quality dimensions
- [[wiki/data-storage/data-observability-and-monitoring|Data Observability And Monitoring]] — observability
- [[wiki/data-storage/data-testing-frameworks|Data Testing Frameworks]] — testing
- [[wiki/data-storage/feature-stores-and-ml-features|Feature Stores And Ml Features]] — ML features
- [[wiki/data-storage/data-contracts-and-agreements|Data Contracts And Agreements]] — data contracts
- [[wiki/data-storage/incremental-loading-strategies|Incremental Loading Strategies]] — incremental loading
- [[wiki/data-storage/schema-evolution-in-streams|Schema Evolution In Streams]] — schema evolution
- [[wiki/data-storage/streaming-sinks-and-sources|Streaming Sinks And Sources]] — streams
- [[wiki/data-storage/data-warehouse|Data Warehouse]] — warehouse reference

