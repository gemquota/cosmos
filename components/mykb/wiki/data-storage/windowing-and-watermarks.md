---
type: "concept"
title: "Windowing and Watermarks"
description: "Grouping stream events by time with bounded lateness"
tags: ["windowing", "watermarks", "streaming", "event-time"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://en.wikipedia.org/wiki/Stream_processing", "https://nightlies.apache.org/flink/flink-docs-stable/"]
---

# Windowing and Watermarks

## Summary

Windows group events into finite buckets for aggregation.
Watermarks declare event-time progress so windows close predictably.
Windowing is where streaming meets real semantics.
Watermark strategy is a product decision: how much lateness you tolerate shapes result accuracy.

## Details

- Tumbling, sliding, and session windows suit different analyses.
- Event-time windows need watermarks to handle out-of-order data.
- Allowed lateness and triggers decide late-data handling.
- Processing-time windows are simple but order-dependent.
- Windowing state grows with window count and key cardinality.
- State cleanup and idle handling prevent unbounded memory.
- Test windows with out-of-order and late event fixtures.
- Document window semantics in the metric catalog so consumers know what each number means.

## Related

- [[wiki/data-storage/event-time-vs-processing-time|Event Time Vs Processing Time]] — clocks
- [[wiki/data-storage/watermarks-and-idle-sources|Watermarks And Idle Sources]] — watermark detail
- [[wiki/data-storage/sessionization-and-activity-windows|Sessionization And Activity Windows]] — session windows
- [[wiki/data-storage/stream-windowing|Stream Windowing]] — existing note
- [[wiki/data-storage/late-data-and-triggers|Late Data And Triggers]] — late records
- [[wiki/data-storage/data-warehouse|Data Warehouse]] — warehouse reference

