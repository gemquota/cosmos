---
type: "concept"
title: "HTTP Fundamentals"
description: "The request-response protocol underpinning the web: methods, headers, status codes, and caching"
tags: ["http", "web-platforms", "protocols", "rest", "api"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://developer.mozilla.org/en-US/docs/Web/HTTP/Overview", "https://www.rfc-editor.org/rfc/rfc9110"]
---
# HTTP Fundamentals

## Summary
HTTP is the application-layer protocol that carries most of the web: browsers talk HTTP to servers, mobile apps talk HTTP to APIs, and agents talk HTTP to tools. HTTP/1.1 remains the baseline, HTTP/2 multiplexes streams, and HTTP/3 runs over QUIC. Any API work, frontend or backend, is really HTTP work.

## Details
- **Request model** — a client sends a method (GET, POST, PUT, PATCH, DELETE), a target URI, headers, and optionally a body; the server replies with a status code, headers, and a body. RFC 9110 defines semantics like caching, authentication, and conditional requests.
- **Statelessness** — each request is independent; state lives in cookies, tokens, or server stores, which is why scaling HTTP services horizontally is straightforward.
- **Caching** — Cache-Control, ETag, and Last-Modified let clients and intermediaries reuse responses. This is the cheapest performance lever on the web.
- **Content negotiation** — Accept and Content-Type headers let one URL serve JSON, HTML, or other representations.
- **Worked example** — mykb's daemon calls its FastAPI backend over HTTP with JSON bodies; the wiki graphs HTTP endpoints, status codes, and caching rules so API design decisions stay traceable.
- **Relevance** — RSIS3's acquisition workers treat each curl-verified source fetch as an HTTP transaction; retry and timeout behavior is governed by HTTP semantics.

## Related
- [[wiki/api-protocols/url-structure|URL Structure]] — adjacent concept in this wiki
- [[wiki/api-protocols/uri-vs-url|URI vs URL]] — adjacent concept in this wiki
- [[wiki/api-protocols/percent-encoding|Percent-Encoding]] — adjacent concept in this wiki
- [[wiki/api-protocols/punycode-domains|Punycode Domains]] — adjacent concept in this wiki
- [[wiki/api-protocols/http-methods|HTTP Methods]] — existing coverage
- [[wiki/api-protocols/http-headers|HTTP Headers]] — existing coverage
- [[wiki/security-auth/same-origin-policy|Same-Origin Policy]] — existing coverage
