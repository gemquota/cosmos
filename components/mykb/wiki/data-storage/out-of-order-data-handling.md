---
type: "concept"
title: "Out-of-Order Data Handling"
description: "Dealing with events that arrive after their event time"
tags: ["out-of-order", "streaming", "event-time", "watermarks"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Out-of-Order Data Handling

## Summary

A stub to be expanded into a full article; frames the concept and open questions.

## Details

- Distributed systems produce out-of-order events; event-time processing must accommodate them.
- Watermarks bound expected lateness; grace periods hold state for stragglers.
- Late events can be dropped, side-output for repair, or trigger recomputation.
- Choosing the lateness bound is a completeness-vs-latency tradeoff.

## Related

- [[wiki/data-storage/stream-windowing|Stream Windowing]] — window closing logic
- [[wiki/data-storage/watermarks-and-idle-sources|Watermarks And Idle Sources]] — progress signaling
- [[wiki/data-storage/late-data-and-triggers|Late Data and Triggers]] — trigger policies
- [[wiki/data-storage/event-time-vs-processing-time|Event Time Vs Processing Time]] — which clock to trust
- [[wiki/data-storage/data-engineering-fundamentals|Data Engineering Fundamentals]] — core data engineering concepts
