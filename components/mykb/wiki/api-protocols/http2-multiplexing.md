---
type: "concept"
title: "HTTP/2 Multiplexing"
description: "Binary framing, stream multiplexing, and header compression that remove head-of-line blocking"
tags: ["http2", "protocols", "performance", "networking", "multiplexing"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://www.rfc-editor.org/rfc/rfc9113", "https://developer.mozilla.org/en-US/docs/Glossary/HTTP_2"]
---
# HTTP/2 Multiplexing

## Summary
HTTP/2 keeps HTTP semantics but replaces text framing with binary frames multiplexed over one TCP connection. Many requests share the connection without head-of-line blocking, and HPACK compresses headers. Servers push and stream independently, and most modern traffic runs HTTP/2.

## Details
- **Streams and frames** — each request/response is a stream of frames; interleaving lets slow responses not block fast ones.
- **HPACK** — header compression encodes static and dynamic tables, cutting repeated header overhead dramatically.
- **Prioritization** — streams carry weights and dependencies; browsers and servers cooperate on ordering.
- **Connection reuse** — one connection per origin reduces handshakes; TLS 1.3 makes setup cheap.
- **Caveats** — TCP-level head-of-line blocking persists, motivating HTTP/3 over QUIC; connection coalescing changes cache-key assumptions.
- **Worked example** — the mykb API serves many small JSON endpoints over one HTTP/2 connection, reducing latency for the dashboard.
- **Relevance** — RSIS3's parallel source fetches map to HTTP/2 streams, but browsers cap per-origin connections.

## Related
- [[wiki/web-platforms/preconnect-practice|Preconnect Practice]] — adjacent concept in this wiki
- [[wiki/web-platforms/dns-prefetch|DNS Prefetch]] — adjacent concept in this wiki
- [[wiki/web-platforms/link-rel-attributes|Link rel Attributes]] — adjacent concept in this wiki
- [[wiki/api-protocols/http-parameter-pollution|HTTP Parameter Pollution]] — adjacent concept in this wiki
- [[wiki/api-protocols/http2|HTTP/2]] — existing coverage
- [[wiki/api-protocols/hpack|HPACK]] — existing coverage
- [[wiki/api-protocols/http2-flow-control|HTTP/2 Flow Control]] — existing coverage
