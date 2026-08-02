---
type: "concept"
title: "Lambda Architecture"
description: "Dual batch and speed layers for analytics"
tags: ["lambda-architecture", "batch-processing", "stream-processing", "data-architecture"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://spark.apache.org/docs/latest/", "https://kafka.apache.org/documentation/"]
---

# Lambda Architecture

## Summary
Lambda architecture computes analytics results from two parallel paths: a batch layer that reprocesses all historical data for accuracy, and a speed layer that produces low-latency approximations of recent data. A serving layer merges both results so queries see near-real-time answers that converge on the correct ones as the batch catches up.

## Details
- **The three layers** — the batch layer stores the immutable master dataset and computes batch views; the speed layer consumes the live stream and computes approximate views for the window the batch has not yet covered; the serving layer answers queries by merging batch and speed views.
- **Why it exists** — pre-streaming-era engines could not recompute everything quickly, so the speed layer covered the freshness gap between batch runs; the design trades operational complexity for both accuracy and low latency.
- **Costs** — two codebases computing the same logic differently are a maintenance hazard: logic drift between layers produces inconsistent answers, and replaying the speed layer against the batch layer is notoriously difficult.
- **Variants and mitigations** — Lambda-lite recomputes a bounded recent window in batch rather than streaming; some teams make the batch layer the source of truth and treat speed results as provisional, or use lambda only for specific metrics.
- **Modern position** — with fast engines (Spark, Trino), streaming SQL, and replayable event logs, the Kappa alternative — one streaming path with replay — removes the dual-codebase problem; Lambda survives where legacy batch infrastructure or very large historical scans are unavoidable.
- **Choosing** — pick Lambda when a single streaming engine cannot handle historical replay scale; otherwise prefer a single path to avoid operating two systems that must agree.

## Related
- [[wiki/data-storage/kappa-architecture|Kappa Architecture]] — the single-path alternative
- [[wiki/data-storage/batch-vs-stream-processing|Batch vs Stream Processing]] — the two execution styles
- [[wiki/data-storage/event-streaming-platforms|Event Streaming Platforms]] — the speed layer's input
- [[wiki/data-storage/materialized-views|Materialized Views]] — batch views as precomputed results
- [[wiki/data-storage/data-lake|Data Lake]] — the immutable master dataset
