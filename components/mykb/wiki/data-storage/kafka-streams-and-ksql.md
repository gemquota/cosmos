---
type: "concept"
title: "Kafka Streams and ksqlDB"
description: "Stream processing inside the Kafka ecosystem via library and SQL"
tags: ["kafka-streams", "ksqldb", "stream-processing", "kafka"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Kafka Streams and ksqlDB

## Summary

A stub to be expanded into a full article; frames the concept and open questions.

## Details

- Kafka Streams is a Java library: topology, state stores (RocksDB), and exactly-once processing.
- ksqlDB is a SQL engine on Kafka Streams for stream/table transformations without writing Java.
- Stream-table duality is native: streams and tables are duals, enabling joins and materializations.
- Both inherit Kafka's retention, ordering, and partitioning semantics.

## Related

- [[wiki/data-storage/exactly-once-semantics|Exactly-Once Semantics]] — transactional guarantees
- [[wiki/data-storage/stream-table-duality|Stream Table Duality]] — core duality concept
- [[wiki/data-storage/flink-sql-and-windows|Flink SQL and Windows]] — SQL streaming alternative
- [[wiki/data-storage/data-engineering-fundamentals|Data Engineering Fundamentals]] — core data engineering concepts
- [[wiki/data-storage/data-warehousing-concepts|Data Warehousing Concepts]] — warehouse fundamentals
