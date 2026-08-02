---
type: "concept"
title: "Streaming Data Pipelines"
description: "Processing data continuously as it arrives"
tags: ["streaming", "pipelines", "kafka", "flink"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://en.wikipedia.org/wiki/Stream_processing", "https://en.wikipedia.org/wiki/Data_pipeline"]
---

# Streaming Data Pipelines

## Summary

Streaming pipelines process records continuously with low latency instead of in scheduled batches.
They power real-time dashboards, event-driven applications, and fraud detection.
Streaming adds ordering, windowing, and state-management complexity.
Streaming is a semantic commitment: ordering, windows, and state must be designed, not assumed.

## Details

- Event streams (Kafka, Pulsar) decouple producers from consumers.
- Engines (Flink, Spark Structured Streaming) provide windows, joins, and state.
- Delivery guarantees: at-least-once, exactly-once, and idempotent sinks.
- Backpressure and dead-letter handling keep pipelines stable.
- Stream-table duality lets streaming and batch share one model.
- Start with the simplest pipeline that meets latency needs; add state later.
- Test streaming pipelines against replays to verify correctness.
- Streaming pipelines should be designed with replay in mind, because reprocessing after a logic fix is inevitable.

## Related

- [[wiki/data-storage/kafka-and-event-streams|Kafka and Event Streams]] — event backbone
- [[wiki/data-storage/flink-stream-processing|Flink Stream Processing]] — processing engine
- [[wiki/data-storage/windowing-and-watermarks|Windowing And Watermarks]] — time handling
- [[wiki/data-storage/batch-vs-stream-processing|Batch vs Stream Processing]] — batch vs stream
- [[wiki/data-storage/stream-processing-engines|Stream Processing Engines]] — engines
- [[wiki/data-storage/data-quality-dimensions|Data Quality Dimensions]] — quality dimensions
- [[wiki/data-storage/data-observability-and-monitoring|Data Observability and Monitoring]] — observability
- [[wiki/data-storage/data-testing-frameworks|Data Testing Frameworks]] — testing
- [[wiki/data-storage/feature-stores-and-ml-features|Feature Stores and ML Features]] — ML features
- [[wiki/data-storage/data-contracts-and-agreements|Data Contracts and Agreements]] — data contracts
- [[wiki/data-storage/incremental-loading-strategies|Incremental Loading Strategies]] — incremental loading
- [[wiki/data-storage/schema-evolution-in-streams|Schema Evolution In Streams]] — schema evolution
- [[wiki/data-storage/streaming-sinks-and-sources|Streaming Sinks And Sources]] — streams

