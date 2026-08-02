---
type: "concept"
title: "Content Negotiation"
description: "Accept header negotiation for representations"
tags: ["http", "content-negotiation", "media-types", "rest", "web-platforms"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://www.rfc-editor.org/rfc/rfc9110#name-content-negotiation", "https://developer.mozilla.org/en-US/docs/Web/HTTP/Content_negotiation"]
---

# Content Negotiation

## Summary
Content negotiation lets one URI serve multiple representations of the same resource. Clients state preferences with Accept, Accept-Language, and Accept-Encoding; servers pick the best fit and record the choice in Vary so caches keep variants separate. It separates what a resource is from how it is rendered.

## Details
- The Accept header lists media types with q-values (quality weights): Accept: application/json;q=0.9, text/html;q=0.5 signals relative preference.
- Server-driven negotiation happens on every request and is where Vary matters: a cache keyed only on URL would mix JSON and HTML variants unless Vary: Accept separates them.
- Agent-driven negotiation inverts the flow: the server returns 300 Multiple Choices or links and lets the client select; it is rare in practice.
- Pragmatic APIs fix the representation via path or extension (for example /api/v1 or /api/v1.json) instead of negotiating, because Vary-heavy caching is complex and error-prone.
- Language negotiation (Accept-Language) shares the same mechanics and drives localized content and error messages.
- For APIs, JSON:API, vendor media types like application/vnd.api+json, and versioned media types are all negotiated representations of the same resource.

## Related
- [[wiki/api-protocols/http-compression|HTTP Compression]] — Accept-Encoding negotiates the wire format
- [[wiki/api-protocols/media-type-versioning|Media Type Versioning]] — vendor media types extend negotiation to versions
- [[wiki/api-protocols/http-caching|HTTP Caching]] — Vary headers keep negotiated variants cacheable
- [[wiki/api-protocols/rest-resource-design|REST Resource Design]] — resources stay URI-stable across representations
- [[wiki/api-protocols/json-api-spec|JSON:API]] — a concrete negotiated media type for APIs
