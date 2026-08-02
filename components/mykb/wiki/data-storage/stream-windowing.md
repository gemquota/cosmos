---
type: "concept"
title: "Stream Windowing"
description: "Tumbling, sliding, and session windows for aggregation"
tags: ["stream-windowing", "event-time", "aggregation", "flink"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://nightlies.apache.org/flink/flink-docs-stable/docs/dev/datastream/operators/windows/", "https://kafka.apache.org/37/documentation/streams/developer-guide/dsl-api.html"]
---

# Stream Windowing

## Summary
Windowing groups an unbounded stream into finite chunks so aggregations — counts, sums, averages, top-N — can be computed over defined time spans. The window type and time semantics decide what each group contains and when results are emitted.

## Details
- **Window types** — tumbling windows are fixed-size, non-overlapping (every 5 minutes); sliding windows overlap (a 10-minute window advancing every minute) for smooth metrics; session windows close after a gap of inactivity, fitting user-session analysis; global windows cover the whole stream.
- **Processing time vs event time** — processing-time windows use the machine clock (simple, but results depend on arrival order and latency); event-time windows use timestamps in the data, so results are correct even for out-of-order and delayed events — the standard choice for analytics.
- **Watermarks** — event-time windows emit when a watermark proves all events up to the window end have arrived; watermark lag trades completeness for latency: too aggressive, windows miss stragglers; too conservative, results are late.
- **Late data** — events arriving after their window can be dropped, side-output for repair, or trigger an update; Flink's allowed-lateness and Kafka Streams' grace periods define the policy per window.
- **Where windows live** — window state is stored per key in the engine's state store, so the number of concurrent keys/windows and their TTL bound resource use; long sessions or huge key counts need state size planning.
- **Output and refinement** — engines can emit one result per window close (fire-on-close) or update results incrementally (accumulating/emitting mode), trading latency for repeated output volume.

## Related
- [[wiki/data-storage/stream-processing-engines|Stream Processing Engines]] — where windows execute
- [[wiki/data-storage/event-streaming-platforms|Event Streaming Platforms]] — the event source and timestamps
- [[wiki/data-storage/batch-vs-stream-processing|Batch vs Stream Processing]] — bounded vs unbounded grouping
- [[wiki/data-storage/exactly-once-semantics|Exactly-Once Semantics]] — correct aggregation across replays
- [[wiki/data-storage/time-series-databases|Time-Series Databases]] — the downstream store for window results
