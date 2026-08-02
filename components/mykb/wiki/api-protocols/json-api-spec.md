---
type: "concept"
title: "JSON:API"
description: "Resource and relationship conventions with compound documents"
tags: ["json-api", "media-type", "rest", "serialization", "api-design"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://jsonapi.org/format/", "https://jsonapi.org/examples/"]
---

# JSON:API

## Summary
JSON:API is a specification for building JSON APIs that standardizes resource envelopes, relationship links, sparse fieldsets, filtering, pagination, and compound documents. It defines the application/vnd.api+json media type so clients and servers share one predictable wire format.

## Details
- Top-level object: data (resource, resource collection, or null), meta, errors, links, and jsonapi; exactly one of data or errors appears.
- Resource objects have type and id, plus attributes (non-relational fields) and relationships (references to other resources).
- Compound documents: include=author,tags appends related resources in an included array, collapsing N+1 round trips into one response.
- Relationship objects carry links (self, related) and data (resource identifiers) — the client can link or unlink via PATCH on the relationship endpoint.
- Sparse fieldsets (?fields[articles]=title,body), filtering (?filter[status]=published), sorting (?sort=-created_at), and pagination (?page[offset]/[limit] or ?page[cursor]) are standardized.
- Errors are arrays of objects with id, status, code, title, and detail plus source pointers, aligning with RFC 9457 Problem Details semantics.
- The spec is a strong baseline for public CRUD APIs, though its strict envelope costs flexibility for bespoke response shapes.

## Related
- [[wiki/api-protocols/problem-details|Problem Details]] — JSON:API error objects mirror the format
- [[wiki/api-protocols/rest-resource-design|REST Resource Design]] — resources and relationships are first-class
- [[wiki/api-protocols/graphql-fragments|GraphQL Fragments]] — field selection maps to JSON:API sparse fieldsets
- [[wiki/api-protocols/content-negotiation|Content Negotiation]] — application/vnd.api+json is a negotiated media type
- [[wiki/api-protocols/hateoas|HATEOAS]] — links objects drive navigation
