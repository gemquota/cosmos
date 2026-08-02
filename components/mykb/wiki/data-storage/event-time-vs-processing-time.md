---
type: "concept"
title: "Event Time vs Processing Time"
description: "Two clocks in stream processing and why the distinction matters"
tags: ["event-time", "processing-time", "streaming", "time"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Event Time vs Processing Time

## Summary

A stub to be expanded into a full article; frames the concept and open questions.

## Details

- Event time is when the event happened; processing time is when the engine sees it.
- Event-time processing is deterministic and correct under delays; processing time is low-latency but order-dependent.
- Watermarks reconcile the two, mapping event-time progress onto processing time.
- Choose per use case: monitoring wants processing time; billing wants event time.

## Related

- [[wiki/data-storage/stream-windowing|Stream Windowing]] — time-based windows
- [[wiki/data-storage/windowing-and-watermarks|Windowing And Watermarks]] — watermark mapping
- [[wiki/data-storage/out-of-order-data-handling|Out Of Order Data Handling]] — why event time is hard
- [[wiki/data-storage/ordering-and-timestamp-assignment|Ordering And Timestamp Assignment]] — assigning timestamps
- [[wiki/data-storage/data-engineering-fundamentals|Data Engineering Fundamentals]] — core data engineering concepts
