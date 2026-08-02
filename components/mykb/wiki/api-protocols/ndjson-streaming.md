---
type: "concept"
title: "NDJSON Streaming"
description: "Newline-delimited JSON event streams"
tags: ["ndjson", "streaming", "json", "events", "data-formats"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://github.com/ndjson/ndjson-spec", "https://jsonlines.org/"]
---

# NDJSON Streaming

## Summary
NDJSON (newline-delimited JSON) is a stream format where each line is a complete JSON value. It is trivially parseable line-by-line, incremental, and language-agnostic — the de facto format for bulk export, log ingestion, and simple event feeds that do not need a richer envelope.

## Details
- Format rules: each line is one JSON document terminated by \n; the last line may omit the newline; values are typically objects.
- Parsing simplicity: readers split on newlines and JSON.parse each line — no framing protocol, no length prefixes, resumable from any line.
- Incremental delivery: producers write and flush per line, so consumers see events as they happen (progress logs, job results, test reports).
- Streaming over HTTP: served with Content-Type: application/x-ndjson, often over chunked encoding or SSE-like flows; tools like curl can tail it.
- Comparison: JSON Lines is the canonical name; JSONL and NDJSON are used interchangeably; both are stricter than pretty-printed JSON arrays.
- Use cases: log shipment (Fluentd, ELK), bulk data exchange, dataset training files, and event cursors where each line carries an id.
- Validation: because each line is independent, a corrupt line can be skipped or retried without losing the whole stream.

## Related
- [[wiki/api-protocols/streaming-apis|Streaming APIs]] — NDJSON is a lightweight stream payload
- [[wiki/api-protocols/server-sent-events|Server-Sent Events]] — SSE adds metadata fields over NDJSON
- [[wiki/data-storage/open-knowledge-format|Open Knowledge Format]] — line-oriented formats complement structured wiki data
- [[wiki/api-protocols/at-least-once-delivery|At-Least-Once Delivery]] — line ids enable dedup and resume
- [[wiki/api-protocols/json-api-spec|JSON:API]] — structured JSON vs minimal NDJSON envelopes
