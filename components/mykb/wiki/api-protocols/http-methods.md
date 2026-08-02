---
type: "concept"
title: "HTTP Methods"
description: "Semantics of GET, POST, PUT, PATCH, DELETE: safety and idempotency"
tags: ["http", "methods", "idempotency", "rest", "web-platforms"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://www.rfc-editor.org/rfc/rfc9110#name-methods", "https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods"]
---

# HTTP Methods

## Summary
HTTP method semantics define what a request asks the server to do, and each method carries guarantees about safety and idempotency that clients, proxies, and caches rely on. RFC 9110 registers the standard methods — GET, HEAD, POST, PUT, DELETE, CONNECT, OPTIONS, TRACE, and PATCH — and defines the two properties that shape retry behavior.

## Details
- Safe methods (GET, HEAD, OPTIONS, TRACE) must not change server state, so crawlers, prefetchers, and caches may issue them freely.
- Idempotent methods (GET, HEAD, PUT, DELETE, OPTIONS, TRACE) produce the same effect when repeated; POST is neither safe nor idempotent.
- PUT replaces the target resource with the request representation, and DELETE removes it — both stay idempotent even when a repeat returns 404.
- PATCH applies a partial modification described by the body; it is only idempotent when the representation semantics guarantee it, such as with application/merge-patch.
- POST triggers creation and other state-changing actions, so retries can duplicate effects; payment and order APIs add Idempotency-Key headers on top.
- HEAD is GET without a response body, used for existence and metadata checks; CONNECT establishes tunnels; OPTIONS advertises server capabilities.
- Extensions can register new methods (for example WebDAV's PROPFIND or MKCOL), but custom methods must follow the token grammar and document their semantics.

## Related
- [[wiki/api-protocols/rest-apis|REST APIs]] — method semantics are the core of REST contracts
- [[wiki/api-protocols/http-status-codes|HTTP Status Codes]] — each method's possible outcomes map to status classes
- [[wiki/api-protocols/idempotency|Idempotency]] — method guarantees are the baseline for retry safety
- [[wiki/api-protocols/rest-resource-design|REST Resource Design]] — resources define which methods apply to which URIs
- [[wiki/api-protocols/rest-partial-updates|REST Partial Updates]] — PATCH semantics for non-idempotent edits
- [[wiki/api-protocols/http-caching|HTTP Caching]] — safe methods are the only ones caches may replay
