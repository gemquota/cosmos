---
type: "entity"
title: "JSONL"
description: "JSON Lines: newline-delimited JSON records for streaming and logging"
tags: ["entity", "acronym", "jsonl", "data-formats", "streaming"]
timestamp: "2026-07-19T22:41:41Z"
resource: ""
---

# JSONL

## Summary

JSONL, or JSON Lines, is a text format where each line is one complete JSON value, so records can be appended, streamed, and processed incrementally. It matters because it combines human-readable JSON with log-friendly, resumable streaming. Tools that read JSONL can tail files, parallelize processing, and resume after interruption.

## Details

- **Definition** — A JSONL file holds one JSON object or array per line, separated by newline characters, with no trailing comma or wrapper document.
- **Streaming** — Line-oriented records append and stream naturally: a consumer can read, parse, and emit each line without loading the whole file.
- **Worked example** — An agent logs each tool call as one JSONL line with timestamp, action, and result; analysis tools filter and aggregate lines without full-file parsing.
- **Comparison with JSON** — A single JSON document must be fully parsed and is awkward to append; JSONL trades a container for incremental access.
- **Comparison with CSV** — JSONL preserves nesting and types that CSV flattens, at the cost of larger files and schema-less rows.
- **Common failure modes** — Embedded newlines inside string values break naive line readers, and trailing whitespace or BOMs trip strict parsers.
- **Practical relevance** — Log pipelines, dataset distribution, and event streams commonly use JSONL because it is append-only and resumable.
- **Variants** — NDJSON is the same format under a different name; gzip-compressed JSONL balances size with streaming.
- **Telemetry note** — The stub correctly tags JSONL to JSON; this note records the format as observed in API and data sessions.
- **Schema drift** — Lines can carry different shapes over time; recording a schema version per line eases migration and backfill.
- **Tooling** — jq, grep, and awk process JSONL directly, and most log shippers parse it natively, so it slots into existing pipelines.
- **Worked example** — A batch job reads a JSONL corpus, filters lines by field, and writes a reduced JSONL file, resuming from a byte offset after interruption.

## Related

- [[wiki/api-protocols/ndjson-streaming|NDJSON Streaming]] — the same format in APIs
- [[wiki/dev-tools/structured-logs|Structured Logs]] — JSONL as log format
- [[wiki/data-storage/open-knowledge-format|Open Knowledge Format]] — structured knowledge records
- [[wiki/os-shell/jq-json-processing|JQ JSON Processing]] — filtering JSONL streams
- [[wiki/data-storage/columnar-storage-formats|Columnar Storage Formats]] — analytics alternative
- [[wiki/concepts/event-segmentation|Event Segmentation]] — line as event unit
