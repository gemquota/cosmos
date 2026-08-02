---
type: "concept"
title: "Log Collection & Aggregation"
description: "Flume-style agents shipping logs to central stores"
tags: ["log-collection", "log-aggregation", "observability", "flume"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://flume.apache.org/FlumeUserGuide.html", "https://grafana.com/docs/loki/latest/"]
---

# Log Collection & Aggregation

## Summary
Log collection and aggregation moves logs from thousands of servers and containers into a central store where they can be searched, correlated, and retained. Agents tail local files or capture stdout, ship events over the network, and a central pipeline buffers, parses, and indexes them for query.

## Details
- **Agents** — lightweight daemons run on each host: Filebeat, Fluent Bit, Vector, Promtail, and Flume agents tail files, read journald, or scrape container stdout and forward with backpressure-aware buffering.
- **The classic Flume model** — Flume has three components: sources (avro, spooldir, tail) ingest events, channels (memory, file, Kafka) buffer them durably, and sinks (HDFS, Kafka, Solr) deliver them; this source-channel-sink decomposition appears in most collection pipelines.
- **Central pipeline** — a broker (Kafka) or aggregator (Logstash, Fluentd) buffers bursts and fans out to stores; batching and compression keep network and index cost down.
- **Stores and query** — the destination shapes the trade-off: Elasticsearch/Lucene indexes for interactive search; Loki for log-oriented, label-indexed storage with low ingest cost; object storage plus a query engine for cheap long-term retention.
- **Pipeline resilience** — file-position checkpoints make collection at-least-once; disk-backed buffers survive agent restarts; dead-letter handling parks malformed records; sampling and structured logging reduce volume.
- **Key metrics** — per-source ingestion rate, dropped events, lag between generation and indexing, and parse failure rates are the operational signals; correlation IDs tie logs to traces and metrics.

## Related
- [[wiki/data-storage/event-streaming-platforms|Event Streaming Platforms]] — the buffering backbone
- [[wiki/data-storage/data-observability|Data Observability]] — monitoring pipeline health
- [[wiki/data-storage/object-storage|Object Storage]] — cheap archival tiers for logs
- [[wiki/data-storage/data-lifecycle-management|Data Lifecycle Management]] — retention for log stores
- [[wiki/data-storage/backpressure|Backpressure]] — agent buffering when sinks lag
- [[wiki/devops-infra/observability|Observability]] — the consuming dashboards
