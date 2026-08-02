---
type: "concept"
title: "HTTP/3"
description: "HTTP over QUIC: features and benefits"
tags: ["http3", "quic", "http", "protocols", "performance"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://www.rfc-editor.org/rfc/rfc9114", "https://blog.cloudflare.com/http3-the-past-present-and-future/"]
---

# HTTP/3

## Summary
HTTP/3 (RFC 9114) is HTTP semantics over QUIC instead of TCP+TLS: each request runs on its own QUIC stream, so packet loss on one stream never blocks others. It brings faster handshakes (0-RTT), connection migration across networks, and built-in encryption — the protocol stack behind modern CDN traffic.

## Details
- What changes: HTTP/1.1 and HTTP/2 run over TCP; HTTP/3 runs over QUIC (UDP-based), with QUIC providing reliability, ordering, and TLS 1.3.
- No head-of-line blocking: a lost packet affects only the streams holding that data; other streams keep flowing (fixing HTTP/2-over-TCP's weakness).
- 0-RTT: clients with a cached session can send data on the first flight, cutting connection setup latency for repeat visits.
- Connection migration: QUIC connections carry a connection ID, so switching Wi-Fi to cellular keeps the connection alive — mobile-friendly.
- QPACK: header compression adapted for out-of-order delivery (QCRAM) replaces HPACK's ordering assumptions.
- Deployment: HTTP/3 uses UDP 443; middleboxes historically throttled UDP, but CDNs (Cloudflare, Fastly, Google) and browsers now support it broadly.
- Server push is dropped in HTTP/3; multiplexing plus early hints covers the use cases.

## Related
- [[wiki/api-protocols/quic|QUIC]] — the transport HTTP/3 runs on
- [[wiki/api-protocols/http2|HTTP/2]] — the predecessor HTTP/3 improves on
- [[wiki/api-protocols/tls-handshake|TLS Handshake]] — TLS 1.3 is built into QUIC
- [[wiki/api-protocols/hpack|HPACK]] — QPACK replaces it over QUIC
- [[wiki/api-protocols/http-keep-alive|HTTP Keep-Alive]] — connection economics change again
