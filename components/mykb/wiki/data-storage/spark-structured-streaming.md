---
type: "concept"
title: "Spark Structured Streaming"
description: "Micro-batch and continuous processing on the Spark engine"
tags: ["spark", "streaming", "micro-batch", "structured-streaming"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Spark Structured Streaming

## Summary

A stub to be expanded into a full article; frames the concept and open questions.

## Details

- Structured Streaming treats streams as unbounded tables with the DataFrame API.
- Micro-batch mode processes in small intervals; continuous mode (experimental) lowers latency.
- Checkpointing and WALs provide fault tolerance; output modes (append, update, complete) define results.
- Event-time windows and watermarks handle late data with drop or threshold policies.

## Related

- [[wiki/data-storage/stream-processing-engines|Stream Processing Engines]] — engine landscape
- [[wiki/data-storage/exactly-once-semantics|Exactly-Once Semantics]] — guarantees
- [[wiki/data-storage/spark-batch-and-streaming|Spark Batch And Streaming]] — unified Spark model
- [[wiki/data-storage/windowing-and-watermarks|Windowing And Watermarks]] — time handling
- [[wiki/data-storage/checkpointing-and-recovery-flink|Checkpointing And Recovery Flink]] — Flink's analogous mechanism
