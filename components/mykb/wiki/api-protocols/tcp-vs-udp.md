---
type: "concept"
title: "TCP vs UDP"
description: "Reliable connection-oriented versus fast datagram transport protocols"
tags: ["network", "tcp", "udp", "protocols"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---
# TCP vs UDP

## Summary
Reliable connection-oriented versus fast datagram transport protocols. A stub in the mykb wiki that frames the concept and the questions to expand into a full article.

## Details
- TCP guarantees order and reliability; UDP trades both for low latency
- QUIC and HTTP/3 run over UDP with reliability added at the application layer
- Open question — where is raw UDP still the right call for web APIs?

## Related
- [[wiki/api-protocols/dns-fundamentals|DNS Fundamentals]] — related coverage in the same cluster
- [[wiki/api-protocols/ipv4-vs-ipv6|IPv4 vs IPv6]] — related coverage in the same cluster
- [[wiki/api-protocols/tcp-vs-udp|TCP vs UDP]] — related coverage in the same cluster
- [[wiki/api-protocols/ipv4-vs-ipv6|IPv4 vs IPv6]] — related coverage in the same cluster
- [[wiki/api-protocols/http-keep-alive|HTTP Keep-Alive]] — related coverage in the same cluster
- [[wiki/api-protocols/dns-load-balancing|DNS Load Balancing]] — related coverage in the same cluster
- [[wiki/api-protocols/load-balancing|Load Balancing]] — related coverage in the same cluster
