---
type: "concept"
title: "REST Resource Design"
description: "Nouns, sub-resources, and URI modeling conventions"
tags: ["rest", "resource-design", "uri", "api-design", "http"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://restfulapi.net/resource-naming/", "https://learn.microsoft.com/en-us/azure/architecture/best-practices/api-design"]
---

# REST Resource Design

## Summary
REST resource design models an API as nouns: collections, items, and sub-resources addressed by stable URIs, with HTTP methods as the verbs. Good design makes URIs predictable and readable while keeping the underlying data model from leaking into the surface.

## Details
- Use plural nouns for collections (/users), singular items (/users/42), and sub-resources for owned relationships (/users/42/orders); avoid verbs in paths because methods carry the action.
- Identifiers should be opaque and stable — integers, UUIDs, or slugs — never mutable attributes like email addresses that can change ownership.
- Nesting beyond two levels signals a missing resource: /orgs/1/repos/1/issues/1 may better be /issues/1 with query filters.
- URI conventions: kebab-case or snake_case chosen once, no trailing slashes, no file extensions, and percent-encoding for anything outside the unreserved set.
- Design for the client's needs rather than mirroring the database: aggregation endpoints and projection resources are legitimate.
- Versioning belongs in the path or media type, not in query parameters, and each resource's method set should be the full set clients need.

## Related
- [[wiki/api-protocols/rest-apis|REST APIs]] — resources are the core abstraction of REST
- [[wiki/api-protocols/rest-query-parameters|REST Query Parameters]] — query strings refine collections without new URIs
- [[wiki/api-protocols/rest-non-crud-actions|REST Non-CRUD Actions]] — actions that do not fit noun-plus-method modeling
- [[wiki/api-protocols/http-methods|HTTP Methods]] — verbs are fixed; nouns carry the modeling
- [[wiki/api-protocols/rest-maturity-model|REST Maturity Model]] — resource modeling is the level-2 step
