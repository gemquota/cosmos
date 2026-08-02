---
type: "concept"
title: "HTTP Protocols"
description: "The evolution from HTTP/1.1 to HTTP/2 and HTTP/3"
tags: ["http", "protocols", "web", "networking"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: [
  "https://www.rfc-editor.org/rfc/rfc9112",
  "https://www.rfc-editor.org/rfc/rfc9113",
  "https://www.rfc-editor.org/rfc/rfc9114",
]
---

# HTTP Protocols

## Summary
HTTP is the application protocol of the web, evolving from simple text requests to multiplexed streams. HTTP/1.1, HTTP/2, and HTTP/3 trade complexity for latency and concurrency. Every API and web service in the mykb graph ultimately speaks one of these versions.

## Details
- HTTP/1.1 (RFC 9112) introduced persistent connections, chunked encoding, and host-based virtual hosting, but one request per connection at a time caused head-of-line blocking.
- HTTP/2 (RFC 9113) multiplexes many streams over one TCP connection with binary framing, header compression (HPACK), and server push.
- HTTP/3 (RFC 9114) runs HTTP semantics over QUIC, replacing TCP and TLS to remove TCP-level head-of-line blocking.
- Methods, status codes, and headers remain compatible across versions because they operate at the semantics layer.
- Caching, conditional requests, and content negotiation are specified in the HTTP semantics document (RFC 9110).
- Operationally, upgrading a service from HTTP/1.1 to HTTP/2 changes connection pooling, timeouts, and debugging tooling, which is why protocol version appears in load balancer and CDN configuration.

## Related
- [[wiki/devops-infra/http-caching-directives|HTTP Caching Directives]]
- [[wiki/cloud-infra/http-2-multiplexing|HTTP/2 Multiplexing]]
- [[wiki/os-shell/curl-and-http-clients|curl & HTTP Clients]]
- [[wiki/os-shell/http-basics|HTTP Basics]]
