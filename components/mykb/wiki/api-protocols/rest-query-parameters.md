---
type: "concept"
title: "REST Query Parameters"
description: "Filtering, sorting, and searching conventions"
tags: ["rest", "query-parameters", "filtering", "pagination", "api-design"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://learn.microsoft.com/en-us/azure/architecture/best-practices/api-design#filter-and-paginate-data", "https://swagger.io/docs/specification/describing-parameters/"]
---

# REST Query Parameters

## Summary
Query parameters refine a collection resource without multiplying URIs: they filter, sort, search, select fields, and paginate. Consistent conventions turn an ad-hoc URL format into a predictable query language that clients can compose.

## Details
- Filtering: ?status=active, multi-value ?status=active,pending, and range syntax like ?created_at=gte:2026-01-01; operators need a documented grammar so clients can build expressions.
- Sorting: ?sort=name,-created_at (minus for descending); multiple keys give deterministic ordering and stable pagination ties.
- Searching: ?q= is full-text; ?search= with field scoping (field:value) is common; define whether search is case-insensitive and whether it tokenizes.
- Field selection: ?fields=id,name trims payloads for mobile clients; ?include= expands relationships in JSON:API and OData style.
- Pagination: ?page=1&per_page=20 (offset) or ?cursor= (opaque) — cursors stay stable when items are inserted or deleted.
- Validation matters: unknown parameters should not silently 200; 400 or a warning envelope tells clients their request was misread.
- Document the grammar in OpenAPI with parameter objects, examples, and allow-lists so clients and generated SDKs agree.

## Related
- [[wiki/api-protocols/offset-pagination|Offset Pagination]] — limit/offset is the classic paging scheme
- [[wiki/api-protocols/cursor-pagination|Cursor Pagination]] — opaque cursors stay stable under writes
- [[wiki/api-protocols/openapi|OpenAPI]] — query parameters are declared in the spec
- [[wiki/api-protocols/rest-resource-design|REST Resource Design]] — query strings refine collections without new URIs
- [[wiki/api-protocols/http-caching|HTTP Caching]] — parameterized URLs create cache-variant complexity
