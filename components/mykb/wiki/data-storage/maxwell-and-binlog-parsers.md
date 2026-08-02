---
type: "concept"
title: "Maxwell and Binlog Parsers"
description: "Lightweight MySQL binlog-to-event tools"
tags: ["maxwell", "binlog", "mysql", "cdc"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Maxwell and Binlog Parsers

## Summary

A stub to be expanded into a full article; frames the concept and open questions.

## Details

- Maxwell reads MySQL binlogs and writes JSON change events to Kafka or other sinks.
- It maintains a bootstrapping mode to backfill tables before live capture.
- Binlog parsers are cheaper than full CDC platforms for MySQL-only needs.
- Caveats: binlog retention, DDL handling, and row vs statement format choices.

## Related

- [[wiki/data-storage/cdc-change-data-capture|Change Data Capture]] — CDC fundamentals
- [[wiki/data-storage/debezium-and-cdc-tools|Debezium And Cdc Tools]] — fuller-featured alternative
- [[wiki/data-storage/change-data-capture|Change Data Capture]] — mechanisms
- [[wiki/data-storage/event-streaming-platforms|Event Streaming Platforms]] — where events land
- [[wiki/data-storage/data-engineering-fundamentals|Data Engineering Fundamentals]] — core data engineering concepts
