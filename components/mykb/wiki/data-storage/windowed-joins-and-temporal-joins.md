---
type: "concept"
title: "Windowed Joins and Temporal Joins"
description: "Joining events within time windows or at a point in time"
tags: ["windowed-join", "temporal-join", "streaming", "time"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Windowed Joins and Temporal Joins

## Summary

A stub to be expanded into a full article; frames the concept and open questions.

## Details

- Windowed joins pair events whose timestamps fall within a window, matching by key.
- Temporal joins (Flink) join an event with the version of a table valid at its time.
- Both need state retention to cover late and out-of-order arrivals.
- Choosing bounds (grace, watermark) determines completeness vs latency.

## Related

- [[wiki/data-storage/stream-windowing|Stream Windowing]] — window semantics
- [[wiki/data-storage/join-strategies-in-streams|Join Strategies In Streams]] — join taxonomy
- [[wiki/data-storage/windowing-and-watermarks|Windowing And Watermarks]] — time progress
- [[wiki/data-storage/out-of-order-data-handling|Out Of Order Data Handling]] — late arrival effects
- [[wiki/data-storage/data-engineering-fundamentals|Data Engineering Fundamentals]] — core data engineering concepts
