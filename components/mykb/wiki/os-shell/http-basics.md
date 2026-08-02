---
type: "concept"
title: "HTTP Basics"
description: "Methods, status codes, headers, and request flow"
tags: ["http", "rest", "web", "protocol"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://www.rfc-editor.org/rfc/rfc9110", "https://www.rfc-editor.org/rfc/rfc9112"]
---

# HTTP Basics

## Summary
HTTP is the request/response protocol of the web: a client sends a method, path, and headers to a server, which replies with a status code, headers, and a body. RFC 9110 defines semantics, and 9112 defines the HTTP/1.1 wire format.

## Details
- Methods: GET (read), POST (create/action), PUT (replace), PATCH (partial update), DELETE, HEAD (headers only), OPTIONS (capabilities).
- Status classes: 1xx informational, 2xx success (200 OK, 201 Created, 204 No Content), 3xx redirects (301, 302, 304 Not Modified), 4xx client errors (400, 401, 403, 404, 429), 5xx server errors (500, 502, 503).
- Headers: Host (virtual hosting), Content-Type (media type), Content-Length, Cache-Control, Authorization, User-Agent, and cookies via Set-Cookie/Cookie.
- HTTP/1.1 keep-alive reuses one connection; HTTP/2 multiplexes streams over one connection; HTTP/3 runs over QUIC/UDP.
- Request flow: DNS lookup, TCP/TLS handshake, send request, read response, close or reuse — visible with curl -v.
- Idempotency: GET/PUT/DELETE are safe to retry; POST is not — the reason webhooks need idempotency keys.
- Caching: responses declare freshness with Cache-Control; conditional requests (If-None-Match) return 304 to save bandwidth.

## Related
- [[wiki/os-shell/tls-and-https|TLS & HTTPS]] — HTTP encrypted in transit
- [[wiki/os-shell/curl-and-http-clients|curl & HTTP Clients]] — driving HTTP from the shell
- [[wiki/os-shell/tcp-ports-and-services|TCP Ports & Services]] — HTTP on 80, HTTPS on 443
- [[wiki/api-protocols/rest-apis|REST APIs]] — HTTP semantics applied to APIs
- [[wiki/api-protocols/http-caching|HTTP Caching]] — freshness and validation in depth
