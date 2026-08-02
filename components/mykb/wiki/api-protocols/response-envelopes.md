---
type: "concept"
title: "Response Envelopes"
description: "data/meta/error wrapper conventions"
tags: ["response-envelopes", "api-design", "json", "conventions", "errors"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://jsonapi.org/format/#document-structure", "https://www.moesif.com/blog/technical/api-design/REST-API-Design-Best-Practices-for-Parameters-and-Query-String-Usage/"]
---

# Response Envelopes

## Summary
A response envelope wraps payloads in a consistent object: { data: ..., meta: ..., error: ... }. It gives every response a uniform shape for metadata, pagination, and errors — at the cost of nesting, verbosity, and breaking the 'plain resource' intuition that HTTP caching and simple clients expect.

## Details
- Common shapes: { data, meta } for success and { error: { code, message, details } } for failure; JSON:API's document structure is the canonical example.
- What the envelope carries: data (the resource), meta (pagination counts, server time, request id), errors (structured failures), and links.
- Benefits: uniform client parsing, extensible metadata without polluting resources, and a single place for pagination info.
- Costs: every response is nested (breaking naive clients), payloads grow, and HTTP caching keys on the URL regardless of envelope content.
- Errors in the envelope vs status codes: use BOTH — the status code class drives retry logic; the envelope body carries machine-readable details.
- When to skip envelopes: bulk/download endpoints and streams (NDJSON, files) where framing matters more than shape.
- Consistency rule: whatever you choose, apply it to every endpoint including errors — mixed shapes are the real bug.

## Related
- [[wiki/api-protocols/error-contract-design|Error Contract Design]] — the error half of the envelope
- [[wiki/api-protocols/json-api-spec|JSON:API]] — a standardized envelope
- [[wiki/api-protocols/problem-details|Problem Details]] — the RFC-standard error body
- [[wiki/api-protocols/rest-query-parameters|REST Query Parameters]] — meta carries pagination info
- [[wiki/api-protocols/http-status-codes|HTTP Status Codes]] — status classes and envelopes work together
