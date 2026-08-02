---
type: "concept"
title: "Flink Stream Processing"
description: "A stateful, fault-tolerant engine for true streaming"
tags: ["flink", "streaming", "state", "exactly-once"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://flink.apache.org/what-is-flink/flink-architecture/", "https://en.wikipedia.org/wiki/Apache_Flink"]
---

# Flink Stream Processing

## Summary

Apache Flink is a distributed stream processing engine with native state and exactly-once guarantees.
It treats streaming as the primary model, with batch as a special case.
Flink dominates heavy stateful stream workloads.
Flink's model treats failure as normal: checkpoints, state, and exactly-once are the baseline, not features.

## Details

- DataStream API and Flink SQL over the same runtime.
- Checkpointing snapshots state for failure recovery.
- State backends (RocksDB, heap) bound state size.
- Event-time processing with watermarks is first-class.
- Runs on Kubernetes, YARN, or standalone clusters.
- Backpressure handling and checkpoint size are the main tuning areas.
- SQL and DataStream APIs share one runtime, easing adoption.
- Flink's checkpoint-based model makes stateful pipelines production-safe in a way batch systems cannot match.

## Related

- [[wiki/data-storage/checkpointing-and-recovery-flink|Checkpointing And Recovery Flink]] — recovery
- [[wiki/data-storage/stateful-stream-processing|Stateful Stream Processing]] — state
- [[wiki/data-storage/flink-sql-and-windows|Flink Sql And Windows]] — SQL
- [[wiki/data-storage/stream-processing-engines|Stream Processing Engines]] — engines
- [[wiki/data-storage/spark-batch-and-streaming|Spark Batch And Streaming]] — Spark comparison
- [[wiki/data-storage/data-warehouse|Data Warehouse]] — warehouse reference

