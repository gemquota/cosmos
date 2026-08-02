---
type: "concept"
title: "Late Data and Triggers"
description: "When windows fire and how late records are incorporated"
tags: ["triggers", "late-data", "windowing", "streaming"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Late Data and Triggers

## Summary

A stub to be expanded into a full article; frames the concept and open questions.

## Details

- Triggers decide when a window's results are emitted: on close, early, or on update.
- Late records can update already-emitted results (with retraction) if allowed.
- Allowed lateness + triggers give approximate-then-correct results.
- Beam and Flink expose explicit trigger APIs; Kafka Streams uses suppression.

## Related

- [[wiki/data-storage/stream-windowing|Stream Windowing]] — window fundamentals
- [[wiki/data-storage/windowing-and-watermarks|Windowing And Watermarks]] — watermark interplay
- [[wiki/data-storage/out-of-order-data-handling|Out Of Order Data Handling]] — lateness model
- [[wiki/data-storage/flink-sql-and-windows|Flink Sql And Windows]] — Flink SQL windows
- [[wiki/data-storage/data-engineering-fundamentals|Data Engineering Fundamentals]] — core data engineering concepts
