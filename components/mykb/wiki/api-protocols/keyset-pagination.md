---
type: "concept"
title: "Keyset Pagination"
description: "Seek-based paging on indexed keys"
tags: ["pagination", "keyset", "databases", "sql", "performance"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://use-the-index-luke.com/sql/partial-results/fetch-next-page", "https://www.citusdata.com/blog/2016/03/30/friends-dont-let-friends-db-fetch/"]
---

# Keyset Pagination

## Summary
Keyset (seek) pagination pages by remembering the last seen row and asking the database for rows after it: WHERE (sort_key) > last_seen ORDER BY sort_key LIMIT n. With an index on the sort key, every page costs the same regardless of depth — the pattern behind cursor pagination.

## Details
- Core query: WHERE created_at < ? and (created_at, id) < (?, ?) for composite keys; the tuple comparison keeps ties deterministic.
- Index requirement: the ORDER BY columns must be indexed, ideally with the filter columns, or the engine falls back to a full sort or scan.
- Stable vs. offset: deep pages stay O(log n) per page instead of O(offset), and concurrent inserts do not disturb the window.
- Tie-breakers: a sort key alone is ambiguous (equal timestamps), so append a unique column such as id to the tuple comparison.
- Downsides: no jump-to-page, no total count, and complex multi-column conditions that are hard to express in some query-builder APIs.
- Encoding: the last-key is exposed as an opaque cursor (often base64) so clients never construct raw tuples; this is exactly how cursor APIs are built internally.

## Related
- [[wiki/api-protocols/cursor-pagination|Cursor Pagination]] — the API shape built on keyset seeks
- [[wiki/api-protocols/offset-pagination|Offset Pagination]] — the O(n) scheme keyset replaces
- [[wiki/devops-infra/database-indexing|Database Indexing]] — composite indexes power the seek
- [[wiki/api-protocols/rest-query-parameters|REST Query Parameters]] — exposing keyset keys in query params
- [[wiki/api-protocols/graphql-connections|GraphQL Connections]] — connections wrap keyset logic in edges
