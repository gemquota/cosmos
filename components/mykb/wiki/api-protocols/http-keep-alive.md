---
type: "concept"
title: "HTTP Keep-Alive"
description: "Persistent connections, reuse, and connection pooling"
tags: ["http", "keep-alive", "connections", "performance", "networking"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://www.rfc-editor.org/rfc/rfc9112#name-persistent-connections", "https://developer.mozilla.org/en-US/docs/Web/HTTP/Connection_management_in_HTTP_1.x"]
---

# HTTP Keep-Alive

## Summary
Persistent connections let one TCP connection carry many HTTP requests, avoiding the cost of a fresh TCP handshake and, historically, a TLS handshake per request. HTTP/1.1 enables keep-alive by default; HTTP/2 multiplexes many streams over one connection, and HTTP/3 does the same over QUIC.

## Details
- HTTP/1.0 required the Connection: keep-alive header; HTTP/1.1 keeps connections open unless Connection: close is sent, making the header a downgrade signal.
- Reuse requires the server to know when a request ends — Content-Length or chunked transfer encoding — otherwise the client cannot delimit responses.
- Proxies and intermediaries must treat Connection as a hop-by-hop field and remove it before forwarding.
- Connection pooling: clients cap concurrent connections per origin (browsers historically around six), queue requests, and return idle connections to the pool instead of closing them.
- Idle timeouts and half-open connections need detection: a request that hangs past its deadline must be retried on a fresh connection, which is why clients send requests with read timeouts.
- HTTP/2 and HTTP/3 collapse the per-origin connection budget to a single connection, so keep-alive economics shift from connection reuse to stream reuse.

## Related
- [[wiki/api-protocols/http2|HTTP/2]] — multiplexing replaces head-of-line blocking on persistent connections
- [[wiki/api-protocols/http3|HTTP/3]] — QUIC connections survive network migration
- [[wiki/api-protocols/timeouts|Timeouts]] — idle and request timeouts govern connection hygiene
- [[wiki/devops-infra/connection-pooling|Connection Pooling]] — pool sizing controls reuse and tail latency
- [[wiki/api-protocols/chunked-transfer-encoding|Chunked Transfer Encoding]] — chunking enables keep-alive for streamed bodies
