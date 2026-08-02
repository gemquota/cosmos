---
type: "concept"
title: "Join Strategies in Streams"
description: "Combining multiple streams and tables in stream processing"
tags: ["stream-join", "streaming", "kafka-streams", "flink"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Join Strategies in Streams

## Summary

A stub to be expanded into a full article; frames the concept and open questions.

## Details

- Stream-stream joins correlate events on keys within windowed time bounds.
- Stream-table joins enrich events with current table state (lookup style).
- Table-table joins merge changelogs into a joined materialized view.
- State stores back all joins, so state size and TTL matter.

## Related

- [[wiki/data-storage/stream-processing-engines|Stream Processing Engines]] — engines with joins
- [[wiki/data-storage/join-algorithms|Join Algorithms]] — join algorithms
- [[wiki/data-storage/windowed-joins-and-temporal-joins|Windowed Joins And Temporal Joins]] — time-bounded joins
- [[wiki/data-storage/stream-table-duality|Stream Table Duality]] — stream/table roles
- [[wiki/data-storage/data-engineering-fundamentals|Data Engineering Fundamentals]] — core data engineering concepts
