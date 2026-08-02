---
type: "concept"
title: "Streaming Sinks and Sources"
description: "The endpoints that feed and consume event streams"
tags: ["streaming", "sinks", "sources", "integration"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Streaming Sinks and Sources

## Summary

A stub to be expanded into a full article; frames the concept and open questions.

## Details

- Sources read from databases (CDC), queues, files, or device protocols into the stream.
- Sinks write to warehouses, lakes, search indexes, caches, and downstream APIs.
- Key properties: exactly-once support, schema handling, and backpressure propagation.
- At-least-once sinks need idempotent targets; batch sinks buffer to control file sizes.

## Related

- [[wiki/data-storage/event-streaming-platforms|Event Streaming Platforms]] — broker landscape
- [[wiki/data-storage/bulk-vs-streaming-ingestion|Bulk Vs Streaming Ingestion]] — ingestion style
- [[wiki/data-storage/connectors|Connectors]] — connector layer
- [[wiki/data-storage/dead-letter-queues-and-retries|Dead Letter Queues And Retries]] — failed records routing
- [[wiki/data-storage/data-engineering-fundamentals|Data Engineering Fundamentals]] — core data engineering concepts
