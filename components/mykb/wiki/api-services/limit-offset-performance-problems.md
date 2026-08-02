---
type: "concept"
title: "LIMIT/OFFSET Performance Problems"
description: "Why large offsets are slow and how to avoid them"
tags: ["limit-offset", "pagination", "performance", "sql"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# LIMIT/OFFSET Performance Problems

## Summary

A stub to be expanded into a full article; frames the concept and open questions.

## Details

- OFFSET n forces the engine to scan and discard n rows before returning results.
- Cost grows linearly; deep pages time out or blow memory.
- Alternatives: keyset pagination, covering indexes, or precomputed pages.
- Watch for unstable ordering: without a total order key, pages drift.

## Related

- [[wiki/data-storage/query-tuning|Query Tuning]] — query performance
- [[wiki/api-services/keyset-and-seek-pagination|Keyset and Seek Pagination]] — the fix
- [[wiki/api-services/offset-vs-cursor-pagination|Offset Vs Cursor Pagination]] — models
- [[wiki/data-storage/indexing-strategies-revisited|Indexing Strategies Revisited]] — index support
- [[wiki/data-storage/data-engineering-fundamentals|Data Engineering Fundamentals]] — core data engineering concepts
