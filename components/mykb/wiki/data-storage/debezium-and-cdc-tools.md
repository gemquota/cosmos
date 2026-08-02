---
type: "concept"
title: "Debezium and CDC Tools"
description: "Change data capture connectors that stream database changes"
tags: ["cdc", "debezium", "kafka-connect", "replication"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Debezium and CDC Tools

## Summary

A stub to be expanded into a full article; frames the concept and open questions.

## Details

- Debezium captures row-level changes from Postgres, MySQL, SQL Server, and others via logs.
- It emits change events to Kafka topics with before/after images and metadata.
- CDC enables streaming ETL, event-driven architecture, and cache invalidation.
- Alternatives: Maxwell (binlog), Fivetran/Airbyte connectors, and native replication.

## Related

- [[wiki/data-storage/cdc-change-data-capture|Change Data Capture]] — CDC concept
- [[wiki/data-storage/event-streaming-platforms|Event Streaming Platforms]] — event destination
- [[wiki/data-storage/change-data-capture|Change Data Capture]] — deep dive
- [[wiki/data-storage/maxwell-and-binlog-parsers|Maxwell And Binlog Parsers]] — MySQL binlog alternative
- [[wiki/data-storage/transactional-outbox-and-cdc-relay|Transactional Outbox And Cdc Relay]] — outbox + CDC pattern
