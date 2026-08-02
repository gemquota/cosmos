---
type: "concept"
title: "Kappa Architecture"
description: "Single streaming path replacing the batch layer"
tags: ["kappa-architecture", "stream-processing", "lambda-architecture", "event-sourcing"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://kafka.apache.org/documentation/streams/", "https://nightlies.apache.org/flink/flink-docs-stable/docs/concepts/overview/"]
---

# Kappa Architecture

## Summary
Kappa architecture processes all data through a single streaming path instead of maintaining separate batch and speed layers. The streaming log retains the full history, and stored views are recomputed by replaying the log — so the "batch" job is just a stream job run from the beginning.

## Details
- **One codebase, one path** — the same streaming topology handles both real-time and historical computation: run it live for current data, or start it at an earlier offset to rebuild state; results converge because the code and data are identical.
- **The log as the system of record** — an immutable, replayable event log (Kafka) is the source of truth; derived stores (search indexes, caches, analytics tables) are materialized views that can be rebuilt by replay, which also fixes corrupt views by recomputation.
- **Replay as the batch equivalent** — reprocessing on a schema change or logic fix means launching a second job from a point in the log, letting it catch up, then switching readers — no separate nightly batch needed.
- **Comparing to Lambda** — Lambda keeps a batch layer (correct, slow) and a speed layer (fast, approximate) with a serving layer merging both; Kappa removes the batch layer, trading the merge complexity for the requirement that the stream engine handle large-scale replays efficiently.
- **When it fits** — event-sourced systems, analytics on event streams, and shops already running Kafka-style platforms; batch-only or complex ETL-heavy workloads with legacy dependencies may not benefit.
- **Practical notes** — log retention must cover the replay horizon or the system is not truly replayable; stateful jobs need checkpointing, and rebuilding very large state can be slow, which is why some teams add a hybrid "Lambda-lite" batch job for cold rebuilds.

## Related
- [[wiki/data-storage/lambda-architecture|Lambda Architecture]] — the dual-layer design Kappa replaces
- [[wiki/data-storage/event-streaming-platforms|Event Streaming Platforms]] — the replayable log
- [[wiki/data-storage/stream-processing-engines|Stream Processing Engines]] — the single processing path
- [[wiki/data-storage/materialized-views|Materialized Views]] — derived stores rebuilt by replay
- [[wiki/data-storage/backfilling|Backfilling]] — replay-driven recomputation
