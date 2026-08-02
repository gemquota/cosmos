---
type: "concept"
title: "HTTP/3 and QUIC"
description: "The next-generation web transport: UDP-based QUIC with 0-RTT and independent streams"
tags: ["http3", "quic", "udp", "protocols", "performance"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://www.rfc-editor.org/rfc/rfc9114", "https://quicwg.org/"]
---
# HTTP/3 and QUIC

## Summary
HTTP/3 runs HTTP over QUIC, a UDP-based transport with TLS 1.3 built in. QUIC gives independent streams (no head-of-line blocking), connection migration across networks, and faster handshakes including 0-RTT. It is the default for major browsers and CDNs.

## Details
- **Independent streams** — one lost packet stalls only its own stream, unlike HTTP/2 over TCP.
- **Connection IDs** — clients can migrate between Wi-Fi and cellular without reconnecting, keeping streams alive.
- **Handshake** — TLS 1.3 keys ride the first flight; 0-RTT resumes known connections (with replay risks to manage).
- **Deployment** — UDP must pass firewalls and load balancers; CDNs handle most of the exposure.
- **Worked example** — serving the mykb static bundle over HTTP/3 cuts TTFB for distant readers; the wiki notes QUIC settings in the deployment log.
- **Relevance** — RSIS3's remote fetches benefit from QUIC's resilience on flaky mobile networks.

## Related
- [[wiki/api-protocols/ipv4-vs-ipv6|IPv4 vs IPv6]] — adjacent concept in this wiki
- [[wiki/api-protocols/tcp-vs-udp|TCP vs UDP]] — adjacent concept in this wiki
- [[wiki/web-platforms/preconnect-practice|Preconnect Practice]] — adjacent concept in this wiki
- [[wiki/web-platforms/dns-prefetch|DNS Prefetch]] — adjacent concept in this wiki
- [[wiki/api-protocols/http3|HTTP/3]] — existing coverage
- [[wiki/api-protocols/quic|QUIC]] — existing coverage
- [[wiki/api-protocols/http-keep-alive|HTTP Keep-Alive]] — existing coverage
