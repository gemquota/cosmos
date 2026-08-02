---
type: "concept"
title: "Keyset and Seek Pagination"
description: "Paging by comparing against the last row's key"
tags: ["keyset-pagination", "seek", "pagination", "sql"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Keyset and Seek Pagination

## Summary

A stub to be expanded into a full article; frames the concept and open questions.

## Details

- Keyset pagination uses WHERE (key) > last_seen ORDER BY key LIMIT n.
- It stays O(log n) and stable even as rows are inserted.
- Composite keysets (created_at, id) need matching composite indexes.
- Tradeoff: no random page access without extra work.

## Related

- [[wiki/data-storage/composite-indexes|Composite Indexes]] — composite key indexes
- [[wiki/api-services/pagination-and-cursor-patterns|Pagination And Cursor Patterns]] — pagination
- [[wiki/api-services/offset-vs-cursor-pagination|Offset Vs Cursor Pagination]] — model comparison
- [[wiki/data-storage/sql-optimization-techniques|Sql Optimization Techniques]] — query tuning
- [[wiki/data-storage/data-engineering-fundamentals|Data Engineering Fundamentals]] — core data engineering concepts
