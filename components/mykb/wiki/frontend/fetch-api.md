---
type: "concept"
title: "Fetch API"
description: "HTTP requests, streaming, and abort control"
tags: [fetch", "http", "javascript", "web-apis", "networking"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API", "https://fetch.spec.whatwg.org/"]
---

# Fetch API

## Summary
The Fetch API is the modern way to make HTTP requests from JavaScript, replacing XMLHttpRequest. fetch() returns a promise for a Response, supports streaming bodies, request cancellation via AbortController, and fine-grained control over headers, credentials, and caching. It is the foundation of nearly every client-side data layer.

## Details
- Basics: fetch(url, {method, headers, body}) returns a promise; response.json() and response.text() parse the body.
- Streaming: response.body is a ReadableStream, enabling progress display and chunked processing.
- Cancellation: AbortController aborts in-flight requests, preventing stale responses and wasted bandwidth.
- Credentials: credentials: "include" sends cookies cross-origin; default is same-origin for fetch.
- Caching: cache modes (default, no-store, reload) control how the browser cache participates.
- Errors: fetch rejects only on network failure — HTTP 404 and 500 still resolve, so status checks are on the caller.

## Related
- [[wiki/frontend/cors|CORS]] — the cross-origin rules fetch enforces
- [[wiki/api-protocols/rest-apis|REST APIs]] — the typical fetch target
- [[wiki/frontend/service-workers|Service Workers]] — intercepting fetch events
- [[wiki/frontend/web-workers|Web Workers]] — fetching from background threads
- [[wiki/api-protocols/timeouts|Timeouts]] — combining abort with timeout logic
- [[wiki/api-protocols/websockets|WebSockets]] — the streaming alternative for push
