---
type: "concept"
title: "Batch vs Stream Processing"
description: "Bounded versus unbounded processing trade-offs"
tags: ["batch-processing", "stream-processing", "spark", "flink"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://spark.apache.org/docs/latest/structured-streaming-programming-guide.html", "https://nightlies.apache.org/flink/flink-docs-stable/docs/concepts/overview/"]
---

# Batch vs Stream Processing

## Summary
Batch processing runs bounded jobs over finite datasets on a schedule; stream processing runs continuously over unbounded data as it arrives. The two share engines — Spark Structured Streaming, Flink — but differ in latency, cost model, and failure semantics, with microbatch and event-time windows blurring the line.

## Details
- **Batch characteristics** — data is bounded and known in advance; jobs run on schedules or triggers, optimize for throughput, and retry by re-running. Simple to reason about, excellent for reprocessing and backfills.
- **Stream characteristics** — data is unbounded; computations run continuously with state, windows, and watermarks; latency drops to seconds but state management, ordering, and late data complicate correctness.
- **Microbatch** — Spark Structured Streaming processes small batches (seconds of data) for near-stream latency with batch semantics; Kafka consumers and delta tables make the boundaries explicit.
- **Event time vs processing time** — streams must decide whether to aggregate by when events happened or when they arrived; watermarks handle late events, and results may update as late data arrives.
- **Cost and ops** — batch consumes compute in bursts and is cheap to pause; streams hold running jobs, checkpoints, and state that must be monitored, scaled, and recovered.
- **Choice framing** — latency SLA decides: hourly reports batch, real-time dashboards stream, and many teams run both with the same pipeline code via engines that unify the model.

## Related
- [[wiki/data-storage/stream-processing-engines|Stream Processing Engines]] — Flink/Spark-style runtimes
- [[wiki/data-storage/stream-windowing|Stream Windowing]] — the time semantics of streams
- [[wiki/data-storage/lambda-architecture|Lambda Architecture]] — running both paths
- [[wiki/data-storage/event-streaming-platforms|Event Streaming Platforms]] — the stream transport
- [[wiki/data-storage/backfilling|Backfilling]] — batch-style reprocessing
