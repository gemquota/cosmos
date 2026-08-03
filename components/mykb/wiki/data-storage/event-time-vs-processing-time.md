---
type: "concept"
title: "Event Time vs Processing Time"
description: "Two clocks in stream processing and why the distinction matters"
tags: ["event-time", "processing-time", "streaming", "time"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# Event Time vs Processing Time

## Summary
Event time is when an event happened; processing time is when the streaming engine sees it. Event-time processing is deterministic and correct under delays, while processing time is low-latency but order-dependent — the choice between the two determines whether results survive late data, retries, and reprocessing.

## Details
- Mechanism: event time comes from timestamps in the data; processing time comes from the engine's clock; watermarks map event-time progress onto processing time, bounding how long the engine waits for late events; windows can be assigned by either clock.
- Concrete example: a billing pipeline uses event time so a delayed click is billed in the hour it actually happened, not the hour the batch ran; a monitoring dashboard uses processing time because it wants the freshest view even if event timestamps lag; a replay of a failed job produces identical event-time results but different processing-time results.
- Failure modes: using processing time for correctness-critical aggregation, so replays and late data change the numbers; watermarks set too tight, dropping legitimate late events; event timestamps absent or corrupt, forcing processing-time fallbacks that silently change semantics; clocks skewed across producers, distorting event-time windows.
- Tradeoffs: event time is correct and reproducible at the cost of latency and watermark complexity; processing time is simple and fresh at the cost of non-determinism; the mature pattern is event time for anything auditable or billable and processing time for monitoring, with watermarks tuned to real late-data rates.
- Operational notes: monitor watermark lag and late-data drop rates, validate timestamps at ingestion, and replay jobs to verify determinism.
- RSIS3 relevance: RSIS3's pulse and sync history have event timestamps — event-time aggregation keeps loop statistics correct across replays.


## Related
- [[wiki/data-storage/stream-windowing|Stream Windowing]] — time-based windows
- [[wiki/data-storage/windowing-and-watermarks|Windowing And Watermarks]] — watermark mapping
- [[wiki/data-storage/out-of-order-data-handling|Out Of Order Data Handling]] — why event time is hard
- [[wiki/data-storage/ordering-and-timestamp-assignment|Ordering And Timestamp Assignment]] — assigning timestamps
- [[wiki/data-storage/data-engineering-fundamentals|Data Engineering Fundamentals]] — core data engineering concepts
