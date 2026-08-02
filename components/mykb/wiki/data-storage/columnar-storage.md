---
type: "concept"
title: "Columnar Storage"
description: "Per-column physical layout, scan efficiency, and compression"
tags: ["columnar", "storage-layout", "compression", "olap"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://clickhouse.com/docs/en/introduction", "https://parquet.apache.org/docs/"]
---

# Columnar Storage

## Summary
Columnar storage places all values of one column contiguously instead of keeping whole rows together. This layout lets analytical engines read only the columns a query touches and compress them far better than row stores can.

## Details
- **Layout** — a table's column values live in separate regions (column chunks/segments); reconstructing a row means gathering values from each column at the same offset.
- **Scan efficiency** — aggregations over one or two columns read only those byte ranges; row stores must pull full rows, wasting I/O on untouched fields.
- **Compression wins** — adjacent values in a column share types and often distributions, so delta, dictionary, and run-length encodings achieve ratios row stores cannot; some engines scan compressed data directly.
- **Write path** — random point updates are expensive because a logical row is scattered across columns; columnar engines favor append/merge patterns, which is why they suit OLAP ingestion.
- **Formats and systems** — Parquet and ORC are the open file formats; ClickHouse, DuckDB, Redshift, and BigQuery use columnar storage internally.
- **mykb relevance** — the wiki corpus is a natural columnar workload: TF-IDF and embedding metadata scans touch few columns of many rows, exactly what columnar layout accelerates.

## Related
- [[wiki/data-storage/vectorized-query-execution|Vectorized Query Execution]] — the processing model columnar enables
- [[wiki/data-storage/compression-codecs|Compression Codecs]] — encodings that exploit column locality
- [[wiki/data-storage/olap-vs-oltp|OLAP vs OLTP]] — the workload split driving layout choice
- [[wiki/data-storage/storage-engines|Storage Engines]] — how engines adopt the layout
- [[wiki/data-storage/open-table-formats|Open Table Formats]] — columnar files plus table metadata
- [[wiki/data-storage/materialized-views|Materialized Views]] — precomputed analytical results on columnar stores
