---
type: "concept"
title: "JSON Lines and NDJSON"
description: "Stream-friendly newline-delimited JSON"
tags: ["json-lines", "ndjson", "formats", "streaming"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# JSON Lines and NDJSON

## Summary

A stub to be expanded into a full article; frames the concept and open questions.

## Details

- Each line is one JSON object, so files are appendable and stream-parseable.
- No array-wrapping means partial files stay readable.
- Great for logs, ingestion, and incremental exports.
- Tradeoffs: no schema, larger than columnar, and parsing cost per line.

## Related

- [[wiki/data-storage/json-ld|JSON-LD]] — JSON variants
- [[wiki/data-storage/json-and-semi-structured-data|Json And Semi Structured Data]] — JSON handling
- [[wiki/data-storage/open-data-formats|Open Data Formats]] — formats
- [[wiki/data-storage/data-import-export-patterns|Data Import Export Patterns]] — interchange
- [[wiki/data-storage/data-engineering-fundamentals|Data Engineering Fundamentals]] — core data engineering concepts
