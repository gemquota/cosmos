---
type: "concept"
title: "ksqlDB and SQL Streaming"
description: "SQL stream processing in the Kafka ecosystem"
tags: ["ksqldb", "sql", "streaming", "kafka"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# ksqlDB and SQL Streaming

## Summary

A stub to be expanded into a full article; frames the concept and open questions.

## Details

- ksqlDB turns Kafka topics into streams/tables queried with SQL.
- It supports windows, joins, and materialized views backed by Kafka Streams.
- Server mode runs headless queries; pull queries read current materialized state.
- Choose when the team knows SQL but not JVM stream programming.

## Related

- [[wiki/data-storage/event-streaming-platforms|Event Streaming Platforms]] — Kafka
- [[wiki/data-storage/kafka-streams-and-ksql|Kafka Streams And Ksql]] — Kafka Streams
- [[wiki/data-storage/stream-table-duality|Stream Table Duality]] — duality
- [[wiki/data-storage/flink-sql-and-windows|Flink Sql And Windows]] — alternative SQL
- [[wiki/data-storage/data-engineering-fundamentals|Data Engineering Fundamentals]] — core data engineering concepts
