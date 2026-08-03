---
type: "concept"
title: "HTTP/2 Multiplexing"
description: "Concurrent streams over one connection with head-of-line tradeoffs"
tags: ["http2", "multiplexing", "streams", "performance"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---
# HTTP/2 Multiplexing

## Summary

HTTP/2 multiplexing sends many requests over one TCP connection using binary frames with per-stream priorities, ending HTTP/1.1's head-of-line request blocking and connection-per-asset waste. Its limitation — TCP-level head-of-line blocking — is exactly what HTTP/3 removes.

## Details
- Mechanism: a single connection carries interleaved streams; each request/response is a stream identified by an ID, frames carry headers/data, and stream priorities/weights hint scheduling; header compression (HPACK) and server push round out the protocol. Browsers reuse one connection per origin instead of 6; TLS 1.2+ is required (ALPN h2).
- Concrete example: a page with 80 assets loads over one HTTP/2 connection instead of 6 HTTP/1.1 connections — fewer handshakes, no serialization per connection; a chat API streams responses while a large upload runs on another stream; priority hints let the browser ask for the hero image before below-fold content.
- Failure modes: TCP head-of-line blocking — one lost packet stalls all streams on that connection (worst on lossy mobile links); servers/apps that treat one connection as one client for rate limiting or pooling break; HPACK vulnerabilities historically (CRIME-class); and proxies/middleboxes that mishandle HTTP/2 settings or trailers.
- Operational tradeoffs: HTTP/2 is a default win for web delivery; the remaining lever is HTTP/3/QUIC for lossy paths, and connection pooling discipline on the service side. Verify h2 is negotiated (curl -I or DevTools protocol column) and monitor connection reuse per origin.
- RSIS3/mykb relevance: the wiki's static hosting serves over HTTP/2 with h3 enabled at the edge; this note records the protocol verification the loop's release checks include.
- Server tuning: check that the origin advertises h2 (ALPN) and that proxies do not downgrade; a silent h1 fallback forfeits multiplexing and connection reuse.
- TLS interplay: h2 requires ALPN; confirm the TLS layer advertises it, since a certificate-only config change can silently drop the protocol.

## Related
- [[wiki/cloud-infra/http-protocols|HTTP Protocols]]
- [[wiki/cloud-infra/connection-multiplexing|Connection Multiplexing]]
- [[wiki/devops-infra/http-caching-directives|HTTP Caching Directives]]
- [[wiki/os-shell/curl-and-http-clients|curl & HTTP Clients]]
- [[wiki/cloud-infra/networking-fundamentals|Networking Fundamentals]]
- [[wiki/syntheses/knowledge-acquisition-workflow|Knowledge Acquisition Workflow]]
- [[wiki/syntheses/mykb-acquisition-curation-and-practices|Acquisition, Curation & Practices]]
