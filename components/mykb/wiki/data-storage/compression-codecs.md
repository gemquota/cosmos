---
type: "concept"
title: "Compression Codecs"
description: "Dictionary, run-length, delta, and general-purpose encodings"
tags: ["compression", "codecs", "columnar-storage", "storage-engines"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://parquet.apache.org/docs/file-format/", "https://docs.oracle.com/en/database/oracle/oracle-database/23/cncpt/data-compression.html"]
---

# Compression Codecs

## Summary
Compression shrinks data at rest and in memory by exploiting repetition and ordering. Columnar formats pair specialized encodings — dictionary, run-length, delta — with general-purpose codecs like Snappy or Zstandard, letting analytical engines read far fewer bytes per query.

## Details
- **Dictionary encoding** — replaces repeated values with integer codes stored in a dictionary; ideal for low-cardinality columns like country codes or status enums.
- **Run-length encoding (RLE)** — stores a value plus a count for consecutive runs; extremely effective on sorted or bitmap-like columns where the same value repeats.
- **Delta encoding** — stores differences between consecutive values; works well for timestamps and monotonic keys, and pairs with variable-length integer coding (varint).
- **General-purpose codecs** — Snappy and LZ4 prioritize speed, Zstandard balances ratio and throughput, Gzip maximizes ratio; columnar engines pick per-column codecs so hot columns use fast paths.
- **Where it lives** — Parquet and ORC apply encodings per column chunk; Postgres has built-in TOAST compression for large values and optional LZ4 since v14; Oracle and SQL Server support page- and column-level compression.
- **Trade-offs** — compression costs CPU on writes and decompression latency on reads, so sortedness and cardinality statistics decide the winning codec.

## Related
- [[wiki/data-storage/columnar-storage|Columnar Storage]] — the layout compression exploits
- [[wiki/data-storage/bitmap-indexes|Bitmap Indexes]] — RLE-heavy structures
- [[wiki/data-storage/olap-vs-oltp|OLAP vs OLTP]] — why warehouses compress aggressively
- [[wiki/data-storage/storage-tiering|Storage Tiering]] — compression interacts with media choice
- [[wiki/data-storage/vectorized-query-execution|Vectorized Query Execution]] — decompressing batches at a time
