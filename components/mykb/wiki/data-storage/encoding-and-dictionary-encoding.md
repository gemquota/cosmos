---
type: "concept"
title: "Encoding and Dictionary Encoding"
description: "Column-level encodings that make columnar storage fast"
tags: ["dictionary-encoding", "encodings", "columnar", "compression"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://en.wikipedia.org/wiki/Dictionary_coder", "https://parquet.apache.org/docs/file-format/"]
---

# Encoding and Dictionary Encoding

## Summary

Dictionary encoding maps repeated values to small integer codes.
Delta and run-length encodings exploit ordering and repetition.
Encodings are the reason columnar formats compress so well.
Encodings turn repetitive columns into tiny, fast-to-scan data.

## Details

- Dictionary encoding: value -> code table, codes stored.
- Delta encoding: store differences between consecutive values.
- Run-length encoding: collapse repeated runs.
- Encodings enable fast filtering without decompression.
- Parquet/ORC choose encodings per column automatically.
- Encoding choice can be left to format defaults for most columns.
- Dictionary-encoded filters avoid decompression entirely.
- Encodings are why columnar files are small and fast at the same time.

## Related

- [[wiki/data-storage/data-compression-techniques|Data Compression Techniques]] — compression
- [[wiki/data-storage/columnar-storage-formats|Columnar Storage Formats]] — columnar
- [[wiki/data-storage/parquet-and-orc|Parquet And Orc]] — formats
- [[wiki/data-storage/compression-codecs|Compression Codecs]] — codecs
- [[wiki/data-storage/bloom-filters-and-skipping|Bloom Filters and Skipping]] — skipping
- [[wiki/data-storage/data-quality-dimensions|Data Quality Dimensions]] — quality dimensions
- [[wiki/data-storage/data-observability-and-monitoring|Data Observability and Monitoring]] — observability
- [[wiki/data-storage/data-testing-frameworks|Data Testing Frameworks]] — testing
- [[wiki/data-storage/feature-stores-and-ml-features|Feature Stores And Ml Features]] — ML features
- [[wiki/data-storage/data-contracts-and-agreements|Data Contracts and Agreements]] — data contracts
- [[wiki/data-storage/incremental-loading-strategies|Incremental Loading Strategies]] — incremental loading
- [[wiki/data-storage/schema-evolution-in-streams|Schema Evolution In Streams]] — schema evolution
- [[wiki/data-storage/streaming-sinks-and-sources|Streaming Sinks And Sources]] — streams
- [[wiki/data-storage/data-warehouse|Data Warehouse]] — warehouse reference

