---
type: "concept"
title: "API Expansion"
description: "Embedding or expanding related resources in a single response"
tags: ["api", "http", "design", "graphql"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---
# API Expansion

## Summary
Embedding or expanding related resources in a single response. A stub in the mykb wiki that frames the concept and the questions to expand into a full article.

## Details
- Embedding related resources saves round trips but grows payloads
- Expansion depth needs caps to prevent nested bombs
- Open question — when does expansion beat GraphQL-style composition?

## Related
- [[wiki/api-protocols/rest-api-design|REST API Design]] — related coverage in the same cluster
- [[wiki/api-protocols/sparse-fieldsets|Sparse Fieldsets]] — related coverage in the same cluster
- [[wiki/api-protocols/api-pagination|API Pagination]] — related coverage in the same cluster
- [[wiki/api-protocols/api-filtering|API Filtering]] — related coverage in the same cluster
- [[wiki/api-protocols/rest-query-parameters|REST Query Parameters]] — related coverage in the same cluster
- [[wiki/api-protocols/offset-pagination|Offset Pagination]] — related coverage in the same cluster
- [[wiki/api-protocols/cursor-pagination|Cursor Pagination]] — related coverage in the same cluster
