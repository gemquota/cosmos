---
type: "concept"
title: "HTTP/3 0-RTT"
description: "Resumed QUIC sessions that send data before the round trip"
tags: ["http3", "quic", "0-rtt", "performance"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---
# HTTP/3 0-RTT

## Summary

HTTP/3 runs HTTP semantics over QUIC, a UDP-based transport with TLS 1.3 built in, 0-RTT connection resumption, and independent streams. Its headline benefits are one fewer round trip on reconnect and no head-of-line blocking across streams.

## Details
- Mechanism: QUIC multiplexes streams over a single UDP connection with per-stream loss recovery, so a lost packet stalls only its stream; TLS 1.3 handshake is integrated, and 0-RTT lets a returning client send data on the first flight (with replay risk for unsafe methods); connection IDs survive IP/network changes, so mobile handoffs do not drop sessions.
- Concrete example: a mobile app reconnecting after a network switch resumes the QUIC connection instantly (connection migration), where TCP+TLS would restart; a video conference keeps audio flowing while a video stream drops packets because streams are isolated; repeat visits with 0-RTT skip a full handshake, saving a RTT on first paint.
- Failure modes: 0-RTT replay — a captured early request can be replayed, so mutating endpoints must be safe under replay or disable 0-RTT for them; UDP blocked on restrictive networks (fall back to HTTP/2); middleboxes that throttle UDP at scale; and proxy/logging stacks that do not parse QUIC, reducing visibility.
- Operational tradeoffs: HTTP/3 is the right default at the edge for lossy and mobile paths; the protocol is more complex to observe and debug, so keep HTTP/2 as fallback and instrument with qlog where available. Measure on real mobile networks — lab throughput rarely shows the loss-related wins.
- RSIS3/mykb relevance: the wiki's edge serving enables HTTP/3 with h2 fallback; this note records the fallback order so the loop's TLS/protocol checks stay aligned.
- Observability: ensure the edge emits protocol-level metrics (h3 vs h2 share); without the split, a silent fallback to h2 hides the regression the network never reports.

## Related
- [[wiki/cloud-infra/http-protocols|HTTP Protocols]]
- [[wiki/cloud-infra/latencies-rtt-and-jitter|Latency, RTT & Jitter]]
- [[wiki/devops-infra/http-caching-directives|HTTP Caching Directives]]
- [[wiki/os-shell/curl-and-http-clients|curl & HTTP Clients]]
- [[wiki/cloud-infra/networking-fundamentals|Networking Fundamentals]]
- [[wiki/syntheses/knowledge-acquisition-workflow|Knowledge Acquisition Workflow]]
- [[wiki/syntheses/mykb-acquisition-curation-and-practices|Acquisition, Curation & Practices]]
