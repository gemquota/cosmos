---
type: "concept"
title: "API Sorting"
description: "Stable sort-parameter conventions and multi-field ordering in APIs"
tags: ["api", "http", "design", "query"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---
# API Sorting

## Summary
Sorting lets clients choose the order of a result set via parameters like sort=-created_at. The contract must define field names, direction syntax, nulls, and a stable tiebreaker or pagination breaks.

## Details
Sorting answers "in what order?" — GET /api/events?sort=-created_at,id returns newest events first, ties broken by id. The common syntax is comma-separated fields with an optional minus prefix for descending, or ?order=asc|desc as a separate parameter. The server maps the sort fields to SQL ORDER BY columns, again through a whitelist, and adds a unique tiebreaker (usually id) so pagination boundaries are deterministic.

The mechanism: without a total order, pagination is undefined — two pages can disagree about which row is next. The standard fix is ORDER BY client-fields, id, because id is unique and stable. Multi-field sorts (sort=-priority,created_at) let clients express "urgent first, then oldest" and must be honored in the same order the server documents, with nulls placed consistently (NULLS FIRST versus NULLS LAST) since databases differ by default.

Concrete example: a dashboard lists jobs sorted by sort=-status,-created_at — the server whitelists status and created_at, treats the leading minus as descending, and appends id. A client asking sort=author.name (a joined relation) may be rejected because the whitelist covers only top-level columns; that is a deliberate scope decision the docs must state, or clients will build fragile client-side sorts.

Failure modes: sorting on an unindexed column forces a sort of the whole result set and can make a previously fast query pathological; client-supplied column names passed through unsanitized enable injection or schema probing; case-insensitive versus case-sensitive collations differ across databases, so the same API returns different orders in different environments; and sorting on a mutable column (updated_at) without a tiebreaker causes rows to jump pages.

Operational tradeoffs: server-side sorting keeps clients thin and orders stable but limits expressiveness (only whitelisted fields); client-side sorting is flexible but only works on already-fetched pages, which is wrong once the collection exceeds one page. The right default is server-side sorting with a documented field list, a stable tiebreaker, and collation pinned in the API contract. Sort performance belongs in query plans, and logs should record the normalized ORDER BY.

RSIS3/mykb relevance: the dashboard's pulse and graph views sort telemetry; documenting the sort contract keeps dashboard queries and RSIS3 analysis scripts consistent about tie-breaking.

## Related
- [[wiki/api-protocols/rest-api-design|REST API Design]] — related coverage in the same cluster
- [[wiki/api-protocols/api-expansion|API Expansion]] — related coverage in the same cluster
- [[wiki/api-protocols/sparse-fieldsets|Sparse Fieldsets]] — related coverage in the same cluster
- [[wiki/api-protocols/api-pagination|API Pagination]] — related coverage in the same cluster
- [[wiki/api-protocols/rest-query-parameters|REST Query Parameters]] — related coverage in the same cluster
- [[wiki/api-protocols/offset-pagination|Offset Pagination]] — related coverage in the same cluster
- [[wiki/api-protocols/cursor-pagination|Cursor Pagination]] — related coverage in the same cluster
