---
type: "concept"
title: "Offset vs Cursor Pagination"
description: "Two pagination models and their tradeoffs"
tags: ["pagination", "cursors", "offset", "api-design"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Offset vs Cursor Pagination

## Summary

A stub to be expanded into a full article; frames the concept and open questions.

## Details

- Offset pagination (page=2&size=50) is easy but slow on large offsets and drifts under concurrent writes.
- Cursor pagination returns an opaque token that pins the position.
- Cursors keep queries stable and O(log n) via keyset indexes.
- Choose cursors for production APIs, offsets for tiny admin lists.

## Related

- [[wiki/api-services/pagination-and-cursor-patterns|Pagination And Cursor Patterns]] — pagination overview
- [[wiki/api-services/keyset-and-seek-pagination|Keyset And Seek Pagination]] — keyset mechanics
- [[wiki/api-services/limit-offset-performance-problems|Limit Offset Performance Problems]] — offset costs
- [[wiki/api-services/api-design-for-data|Api Design For Data]] — API design
- [[wiki/data-storage/data-engineering-fundamentals|Data Engineering Fundamentals]] — core data engineering concepts
