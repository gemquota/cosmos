---
type: "concept"
title: "Offset Pagination"
description: "Limit/offset paging, costs, and instability"
tags: ["pagination", "offset", "api-design", "databases", "rest"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://learn.microsoft.com/en-us/azure/architecture/best-practices/api-design#pagination", "https://www.moesif.com/blog/technical/api-design/REST-API-Design-Filtering-Sorting-and-Pagination/"]
---

# Offset Pagination

## Summary
Offset pagination pages through a collection with page and per_page (or limit and offset) parameters: the server skips offset rows and returns limit rows. It is the easiest scheme to implement and reason about, but it degrades on large offsets and drifts when rows change between pages.

## Details
- Mechanics: GET /items?limit=20&offset=40 returns rows 41-60; the response typically includes total count so clients can render page numbers.
- Cost: the database must count and skip offset rows on every page — OFFSET 100000 forces the engine to scan and discard 100k rows, so deep pages get progressively slower.
- Instability: inserts or deletes between requests shift the window, so rows can be duplicated or skipped; sorting must be total (with a tie-breaker key) or drift is worse.
- Total counts are expensive on large tables; many APIs drop count or make it approximate to keep paging cheap.
- Good fits: admin tables, small datasets, and interfaces that need jump-to-page; bad fits: feeds and logs that grow unboundedly.
- Improvements: cap per_page (default 20, max 100), validate negative offsets, and combine with a stable sort key to minimize drift.

## Related
- [[wiki/api-protocols/cursor-pagination|Cursor Pagination]] — opaque cursors fix offset instability
- [[wiki/api-protocols/keyset-pagination|Keyset Pagination]] — indexed seek paging scales to deep pages
- [[wiki/api-protocols/rest-query-parameters|REST Query Parameters]] — pagination parameters live in the query string
- [[wiki/devops-infra/database-indexing|Database Indexing]] — indexes make seek-based paging fast
- [[wiki/api-protocols/api-analytics|API Analytics]] — paging behavior shows up in usage metrics
