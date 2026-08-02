---
type: "concept"
title: "API Pagination"
description: "Offset, cursor, and keyset strategies for slicing large result sets"
tags: ["api", "pagination", "http", "design"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---
# API Pagination

## Summary
Offset, cursor, and keyset strategies for slicing large result sets. A stub in the mykb wiki that frames the concept and the questions to expand into a full article.

## Details
- Offset pagination is simple but drifts; cursor and keyset paginate consistently
- Pagination style shapes cacheability and index design
- Open question — which pagination fits streaming sinks best?

## Related
- [[wiki/api-protocols/rest-api-design|REST API Design]] — related coverage in the same cluster
- [[wiki/api-protocols/api-filtering|API Filtering]] — related coverage in the same cluster
- [[wiki/api-protocols/api-sorting|API Sorting]] — related coverage in the same cluster
- [[wiki/api-protocols/api-expansion|API Expansion]] — related coverage in the same cluster
- [[wiki/api-protocols/rest-query-parameters|REST Query Parameters]] — related coverage in the same cluster
- [[wiki/api-protocols/offset-pagination|Offset Pagination]] — related coverage in the same cluster
- [[wiki/api-protocols/cursor-pagination|Cursor Pagination]] — related coverage in the same cluster
