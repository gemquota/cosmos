---
type: "concept"
title: "Cursor Pagination"
description: "Opaque cursor-based paging for stable iteration"
tags: ["pagination", "cursor", "api-design", "streaming", "reliability"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://www.citusdata.com/blog/2016/03/30/friends-dont-let-friends-db-fetch/", "https://graphql.org/learn/pagination/"]
---

# Cursor Pagination

## Summary
Cursor pagination returns an opaque cursor that encodes the position of the last item; the client passes it back to fetch the next page. Because the cursor pins a position rather than an offset, new rows cannot shift the window, making it the standard for feeds, logs, and realtime collections.

## Details
- Shape: GET /items?limit=20 returns data plus next_cursor; the client sends ?cursor=<opaque> for the next page; cursors are often base64-encoded (id, timestamp) pairs.
- Stability: the cursor is a position, so rows inserted ahead of it do not change what comes next — no duplicates, no skips, unlike offset paging.
- Implementation: encode the sort key (created_at, id) and decode server-side, then seek with WHERE (created_at, id) > (?, ?) ORDER BY ... LIMIT n, using a composite index.
- Trade-offs: cursors cannot jump to an arbitrary page, and total counts are unavailable without a separate query — acceptable for infinite feeds.
- Bidirectional paging adds a before_cursor for previous pages; Relay-style connections formalize this with edges and pageInfo.
- Security: treat cursors as opaque and validate them; a tampered cursor should return 400, never a database error or a full dump.

## Related
- [[wiki/api-protocols/keyset-pagination|Keyset Pagination]] — the SQL technique cursors encode
- [[wiki/api-protocols/offset-pagination|Offset Pagination]] — the scheme cursors replace
- [[wiki/api-protocols/graphql-connections|GraphQL Connections]] — Relay connections are cursor paging formalized
- [[wiki/api-protocols/rest-query-parameters|REST Query Parameters]] — cursor and limit parameters in the query string
- [[wiki/devops-infra/database-indexing|Database Indexing]] — composite indexes make seeks fast
