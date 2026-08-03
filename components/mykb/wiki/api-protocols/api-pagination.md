---
type: "concept"
title: "API Pagination"
description: "Offset, cursor, and keyset strategies for slicing large result sets"
tags: ["api", "pagination", "http", "design"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---
# API Pagination

## Summary
Pagination bounds response size and cost by returning one page of a collection with a way to fetch the next. Offset and cursor are the two dominant designs, with tradeoffs in stability, cost, and ordering.

## Details
Pagination is how large collections are sliced: the client asks for a page (limit plus offset or cursor) and the server returns a slice plus the means to get the next one. Offset pagination (?limit=50&offset=100) skips N rows; cursor pagination (?limit=50&cursor=eyJpZCI6MTIzfQ==) returns rows after a position token. The cursor encodes the last item's sort key, usually base64url-encoded, and is opaque to clients.

The mechanism: offset pagination maps directly to LIMIT/OFFSET SQL, which is simple but forces the database to scan and discard offset rows every page — O(n) per page — and breaks when rows are inserted or deleted between pages (items shift, duplicates or gaps appear). Cursor pagination uses a keyset predicate (WHERE (created_at, id) > (:ts, :id) ORDER BY created_at, id LIMIT n), which is index-friendly and stable under concurrent writes because the predicate is positional, not numerical.

Concrete example: a webhook event feed pages newest-first by event id. With offset pagination, a burst of new events between page fetches causes the client to skip or re-read events; with cursor pagination each cursor is a stable position, so every event is seen exactly once even as new events stream in. That is why cursor pagination is the standard for feeds, logs, and change-data-capture style APIs.

Failure modes: deep offsets are expensive — page 10,000 scans 500,000 rows; cursor tokens tied to a mutable sort key (updated_at) can skip rows when the key changes mid-pagination; unbounded limit lets clients request absurd pages; and cursor-plus-filter combinations that do not keep the cursor in the filter set produce wrong results. Encrypting or signing cursors prevents clients from guessing positions or tampering.

Operational tradeoffs: offset pagination is easy to implement, debug, and jump to arbitrary pages, which suits admin tables; cursor pagination is more robust and cheaper at scale but cannot jump to a random page and requires a stable, unique sort key (id or created_at+id). Response conventions vary (items array plus next/prev links versus next_page_token), but the important contract is: a next URL, not a recipe, and a stable order.

RSIS3/mykb relevance: the wiki graph and search APIs paginate node lists; cursor-style contracts prevent RSIS3 loops from double-counting nodes during consolidation sweeps.

## Related
- [[wiki/api-protocols/rest-api-design|REST API Design]] — related coverage in the same cluster
- [[wiki/api-protocols/api-filtering|API Filtering]] — related coverage in the same cluster
- [[wiki/api-protocols/api-sorting|API Sorting]] — related coverage in the same cluster
- [[wiki/api-protocols/api-expansion|API Expansion]] — related coverage in the same cluster
- [[wiki/api-protocols/rest-query-parameters|REST Query Parameters]] — related coverage in the same cluster
- [[wiki/api-protocols/offset-pagination|Offset Pagination]] — related coverage in the same cluster
- [[wiki/api-protocols/cursor-pagination|Cursor Pagination]] — related coverage in the same cluster
