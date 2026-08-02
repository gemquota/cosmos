---
type: "concept"
title: "Time-Series Databases"
description: "Append-heavy stores optimized for timestamped data"
tags: ["time-series", "influxdb", "prometheus", "tsdb"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://docs.influxdata.com/influxdb/v2/reference/key-concepts/", "https://prometheus.io/docs/prometheus/latest/storage/"]
---

# Time-Series Databases

## Summary
Time-series databases (TSDBs) are purpose-built for timestamped measurements — metrics, sensor readings, logs, market data — where the workload is overwhelmingly append-heavy writes and range queries over time. InfluxDB, Prometheus, TimescaleDB, and ClickHouse optimize storage layout and query paths for this shape.

## Details
- **Data model** — each sample is a timestamp plus a value, tagged with label or field dimensions (host, region, metric name); queries filter by tags and aggregate over time ranges, so the model is a series per (metric, tag-set) rather than arbitrary relational tables.
- **Storage design** — series are compressed aggressively: delta-encoding timestamps, XOR or Gorilla-style float compression, and dictionary-encoding labels shrink sample bytes dramatically; Prometheus's TSDB uses chunked blocks with compression, InfluxDB's storage engine applies similar per-series encodings.
- **Write path** — ingestion is optimized for high-cardinality, high-rate appends: batching, out-of-order tolerance (with limits), and partitioning by time; InfluxDB shards by time (`influx_storage` shards), Prometheus appends into a WAL-backed head block, and TimescaleDB uses hypertables partitioned by time.
- **Query path** — downsampling, continuous aggregates (TimescaleDB), and PromQL/Flux/InfluxQL aggregations over windows (last hour, mean per 5 minutes) are first-class; retention and downsample policies (InfluxDB retention policies, Prometheus retention) bound storage.
- **Trade-offs** — specialized TSDBs beat general-purpose databases on ingest throughput and compression, but offer weaker SQL and multi-table joins; TimescaleDB and ClickHouse trade some specialization for SQL compatibility.
- **Use cases** — infrastructure and application monitoring, IoT telemetry, financial tick data, and the downstream sink for stream-windowing results.

## Related
- [[wiki/data-storage/columnar-storage|Columnar Storage]] — the compression philosophy
- [[wiki/data-storage/stream-windowing|Stream Windowing]] — producing the aggregates stored here
- [[wiki/data-storage/data-lifecycle-management|Data Lifecycle Management]] — retention and downsampling
- [[wiki/data-storage/table-partitioning|Table Partitioning]] — time-based hypertable structure
- [[wiki/data-storage/vacuuming-and-compaction|Vacuuming & Compaction]] — segment merging in TSDBs
- [[wiki/data-storage/storage-tiering|Storage Tiering]] — hot vs cold series data
