---
type: "concept"
title: "API Filtering"
description: "Query-parameter conventions for narrowing collections by field values"
tags: ["api", "http", "design", "query"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---
# API Filtering

## Summary
Filtering lets clients select server-side which resources match criteria, using query parameters, operators, or a query language. The design choices are syntax, whitelisting, and how nulls, types, and escaping are handled.

## Details
Filtering answers "give me the subset that matches these predicates" — GET /api/orders?status=paid&total_min=100. The spectrum runs from simple equality parameters (status=paid), through operator suffixes (price[gte]=10), to full query languages (OData $filter, GraphQL args, Elasticsearch-style DSLs). The server compiles the filter into a database query; naive implementations string-concatenate and open SQL injection holes.

The mechanism: parameters are parsed, each field name is checked against a whitelist (no arbitrary column names), values are type-coerced (numeric, boolean, date), operators are mapped to a safe query builder or parameterized SQL, and the result set is returned with pagination metadata. Escaping matters: list values (id=1,2,3), ranges (date=2024-01-01..2024-02-01), and quoted strings (name="John Doe") all need unambiguous rules.

Concrete example: an audit log API filters by actor, action, and time window: ?actor=svc-build&action=deploy&since=2026-08-01T00:00:00Z&until=2026-08-02T00:00:00Z. The server whitelists actor/action/timestamp, coerces the ISO timestamps, and runs an indexed range query. A client that needs "all except failed" would use an operator form like status!=failed, which the server must handle without letting != degrade into a full scan on an unindexed column.

Failure modes: allowing arbitrary field names and operators enables enumeration of the schema and expensive queries — a filter on an unindexed column forces a scan; type confusion (filtering a numeric id with string input) can raise 500s or, worse, match unexpectedly; unescaped list and quote syntax breaks valid values; and combining filter plus pagination without a stable order causes rows to shift between pages.

Operational tradeoffs: rich filter syntax (OData, RSQL) is powerful but has a learning curve and a large parser surface; simple equality filters are safe and obvious but force clients to page through everything else. Server-side, filters must be pushed into the database — not applied in memory — for scale, which means the whitelist must map to real indexes. Logs should record the normalized filter, not raw input, to keep PII out of audit trails.

RSIS3/mykb relevance: mykb's TF-IDF search and graph queries are themselves filtering APIs; documenting their filter contract lets RSIS3 loops query memory precisely instead of over-fetching.

## Related
- [[wiki/api-protocols/rest-api-design|REST API Design]] — related coverage in the same cluster
- [[wiki/api-protocols/api-sorting|API Sorting]] — related coverage in the same cluster
- [[wiki/api-protocols/api-expansion|API Expansion]] — related coverage in the same cluster
- [[wiki/api-protocols/sparse-fieldsets|Sparse Fieldsets]] — related coverage in the same cluster
- [[wiki/api-protocols/rest-query-parameters|REST Query Parameters]] — related coverage in the same cluster
- [[wiki/api-protocols/offset-pagination|Offset Pagination]] — related coverage in the same cluster
- [[wiki/api-protocols/cursor-pagination|Cursor Pagination]] — related coverage in the same cluster
