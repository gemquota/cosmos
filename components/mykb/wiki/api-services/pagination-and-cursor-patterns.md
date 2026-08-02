---
type: "concept"
title: "Pagination and Cursor Patterns"
description: "Fetching large result sets safely across API pages"
tags: ["pagination", "cursors", "api-design", "performance"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Pagination and Cursor Patterns

## Summary

A stub to be expanded into a full article; frames the concept and open questions.

## Details

- Pagination limits response size and bounds query cost per request.
- Offset pagination is simple but degrades; cursor/keyset pagination is stable under writes.
- Cursors encode position and filter state, enabling consistent page walks.
- Return next/prev cursors in responses so clients never build URLs by hand.

## Related

- [[wiki/api-services/api-design-for-data|Api Design For Data]] — API design
- [[wiki/api-services/offset-vs-cursor-pagination|Offset Vs Cursor Pagination]] — comparison
- [[wiki/api-services/keyset-and-seek-pagination|Keyset And Seek Pagination]] — keyset detail
- [[wiki/api-services/limit-offset-performance-problems|Limit Offset Performance Problems]] — offset pitfalls
- [[wiki/data-storage/data-engineering-fundamentals|Data Engineering Fundamentals]] — core data engineering concepts
