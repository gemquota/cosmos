---
type: "concept"
title: "Watermarks and Idle Sources"
description: "Signals of event-time progress in stream processing"
tags: ["watermarks", "event-time", "streaming", "flink"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Watermarks and Idle Sources

## Summary

A stub to be expanded into a full article; frames the concept and open questions.

## Details

- Watermarks declare that events before a timestamp are (mostly) complete.
- Idle sources with no events can stall watermarks; engines offer idle-source detection.
- Watermark strategy (bounded out-of-orderness, periodic, punctuated) shapes latency.
- Late data after the watermark goes to side outputs or is dropped by policy.

## Related

- [[wiki/data-storage/stream-windowing|Stream Windowing]] — windows depend on watermarks
- [[wiki/data-storage/windowing-and-watermarks|Windowing And Watermarks]] — windowing mechanics
- [[wiki/data-storage/event-time-vs-processing-time|Event Time Vs Processing Time]] — time domains
- [[wiki/data-storage/late-data-and-triggers|Late Data And Triggers]] — handling late records
- [[wiki/data-storage/data-engineering-fundamentals|Data Engineering Fundamentals]] — core data engineering concepts
