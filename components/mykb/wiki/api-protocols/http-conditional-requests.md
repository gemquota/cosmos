---
type: "concept"
title: "HTTP Conditional Requests"
description: "ETag/Last-Modified validators with If-* headers and 304/412 outcomes"
tags: ["http", "conditional-requests", "caching", "concurrency", "etag"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://www.rfc-editor.org/rfc/rfc9110#name-conditional-requests", "https://developer.mozilla.org/en-US/docs/Web/HTTP/Conditional_requests"]
---

# HTTP Conditional Requests

## Summary
Conditional requests attach validators to a request so the server can skip work when a precondition fails. Two validator types — strong and weak ETags, or Last-Modified dates — combine with five If-* headers to power cache revalidation, resumable downloads, and optimistic concurrency.

## Details
- Validators: ETag (strong when byte-identical content, weak with a W/ prefix) and Last-Modified dates; ETags are preferred because dates have one-second granularity and can collide.
- If-Match and If-None-Match compare ETags; If-Modified-Since and If-Unmodified-Since compare dates; If-Range limits a Range request to a matching validator.
- Cache revalidation: a cached response with an ETag is resent with If-None-Match; a matching validator returns 304 Not Modified with no body.
- Write protection: If-Match against the current ETag prevents lost updates — a stale client gets 412 Precondition Failed instead of overwriting newer data.
- Range resumption: If-Range lets a client resume a download only if the representation has not changed; otherwise the server returns the full 200 response.
- Weak validators are safe for caching but must never guard writes, since they tolerate semantically equivalent content differences.

## Related
- [[wiki/api-protocols/http-caching|HTTP Caching]] — revalidation is the caching use of validators
- [[wiki/api-protocols/optimistic-concurrency|Optimistic Concurrency]] — If-Match is the HTTP mechanism for conflict detection
- [[wiki/api-protocols/http-status-codes|HTTP Status Codes]] — 304 and 412 are the conditional outcomes
- [[wiki/api-protocols/http-methods|HTTP Methods]] — conditional logic attaches to any method
- [[wiki/api-protocols/rest-partial-updates|REST Partial Updates]] — PATCH combined with If-Match avoids clobbering
