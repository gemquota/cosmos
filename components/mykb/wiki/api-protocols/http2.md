---
type: "concept"
title: "HTTP/2"
description: "Multiplexing, streams, and prioritization"
tags: ["http2", "http", "multiplexing", "protocols", "performance"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://www.rfc-editor.org/rfc/rfc9113", "https://developer.mozilla.org/en-US/docs/Glossary/HTTP_2"]
---

# HTTP/2

## Summary
HTTP/2 (RFC 9113) replaces HTTP/1.1's one-request-per-connection model with multiplexed streams over a single TCP connection: many concurrent requests share one socket, headers compress via HPACK, and the server can push or prioritize. It fixed head-of-line blocking at the request level while keeping the HTTP semantics unchanged.

## Details
- Multiplexing: requests and responses travel as interleaved frames on independent streams; one connection carries hundreds of concurrent requests.
- Frames and streams: DATA, HEADERS, SETTINGS, and WINDOW_UPDATE frames; streams are identified by IDs and closed with RST_STREAM or END_STREAM.
- HPACK: header compression using static/dynamic tables and Huffman coding — repeated field names cost almost nothing.
- Prioritization: clients declare stream priorities (dependencies and weights); servers interleave frames to respect them, improving perceived latency.
- Flow control: per-stream and per-connection windows (WINDOW_UPDATE) let receivers bound buffering — no more TCP-only backpressure.
- Server push: servers could send speculative resources (mostly deprecated in practice; many servers disable it).
- Transport reality: HTTP/2 still sits on TCP, so packet loss causes connection-level head-of-line blocking — the motivation for HTTP/3 over QUIC.

## Related
- [[wiki/api-protocols/hpack|HPACK]] — the header compression of HTTP/2
- [[wiki/api-protocols/http2-flow-control|HTTP/2 Flow Control]] — window-based backpressure
- [[wiki/api-protocols/http3|HTTP/3]] — the QUIC-based successor
- [[wiki/api-protocols/http-keep-alive|HTTP Keep-Alive]] — persistent connections become stream reuse
- [[wiki/api-protocols/grpc|gRPC]] — gRPC is HTTP/2-native
