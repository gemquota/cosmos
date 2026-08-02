---
type: "concept"
title: "Small File Problem and Compaction"
description: "Too many tiny files degrading lakehouse query performance"
tags: ["compaction", "small-files", "lakehouse", "performance"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Small File Problem and Compaction

## Summary

A stub to be expanded into a full article; frames the concept and open questions.

## Details

- Tiny files bloat metadata, slow planning, and waste object-store requests.
- Compaction rewrites many small files into fewer large ones in the background.
- Delta/Hudi auto-compaction and Iceberg rewrite actions manage this.
- Streaming ingestion and unbounded partitions are the usual causes.

## Related

- [[wiki/data-storage/vacuuming-and-compaction|Vacuuming & Compaction]] — compaction concept
- [[wiki/data-storage/data-lake|Data Lake]] — lake storage
- [[wiki/data-storage/data-lake-file-layouts|Data Lake File Layouts]] — layout targets
- [[wiki/data-storage/streaming-sinks-and-sources|Streaming Sinks And Sources]] — streaming writes
- [[wiki/data-storage/data-engineering-fundamentals|Data Engineering Fundamentals]] — core data engineering concepts
