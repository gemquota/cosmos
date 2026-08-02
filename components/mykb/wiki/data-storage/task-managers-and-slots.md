---
type: "concept"
title: "Task Managers and Slots"
description: "Flink's unit of compute and how parallelism maps to resources"
tags: ["flink", "task-managers", "slots", "parallelism"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Task Managers and Slots

## Summary

A stub to be expanded into a full article; frames the concept and open questions.

## Details

- TaskManagers are worker processes; slots bound how many operator tasks run per worker.
- Each slot gets a share of memory; slot count sets local parallelism.
- Chaining packs operators into tasks to reduce overhead.
- Sizing slots vs memory is the main Flink capacity planning lever.

## Related

- [[wiki/data-storage/stream-processing-engines|Stream Processing Engines]] — engine architecture
- [[wiki/data-storage/flink-stream-processing|Flink Stream Processing]] — Flink overview
- [[wiki/data-storage/resource-scheduling-in-spark|Resource Scheduling In Spark]] — Spark's parallel resource model
- [[wiki/data-storage/stateful-stream-processing|Stateful Stream Processing]] — state per task
- [[wiki/data-storage/data-engineering-fundamentals|Data Engineering Fundamentals]] — core data engineering concepts
