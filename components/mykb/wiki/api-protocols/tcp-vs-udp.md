---
type: "concept"
title: "TCP vs UDP"
description: "Reliable connection-oriented versus fast datagram transport protocols"
tags: ["network", "tcp", "udp", "protocols"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---
# TCP vs UDP

## Summary
TCP and UDP are the two transport protocols of the IP suite, and they make opposite bets: TCP guarantees ordered, reliable, connection-oriented delivery at the cost of latency and overhead, while UDP delivers datagrams as fast as possible with no ordering, retransmission, or connection state. Almost every web API runs on TCP; almost every real-time, loss-tolerant, or connectionless protocol runs on UDP.

## Details
- Mechanism: TCP establishes a connection with a three-way handshake, sequences bytes, retransmits lost segments, and paces transmission with congestion control (slow start, AIMD, algorithms like CUBIC). UDP simply wraps a payload with source and destination ports and a checksum and hands it to the network; the application sees whatever arrives, in whatever order, with no guarantee of delivery. The tradeoff is visible in the numbers: TCP's handshake adds a round trip before data flows, and loss recovery adds head-of-line blocking, while UDP can send immediately and never stalls a stream on one lost packet.
- Concrete examples: DNS queries, NTP time sync, VoIP, live video, and multiplayer game traffic use UDP because a stale retransmission is worse than none and latency matters more than completeness; HTTP/1.1, HTTP/2, SSH, and nearly all request/response APIs use TCP because correctness and order are non-negotiable. QUIC and HTTP/3 are the interesting middle: they run over UDP but re-implement reliability, ordering, and encryption in the application layer, which kills head-of-line blocking at the transport level and speeds up connection establishment.
- Failure modes: the classic TCP failure is retransmission storms under packet loss, where throughput collapses to a fraction of capacity (the "bufferbloat" and tail-latency problems); the classic UDP failure is silently dropping the newest state and not knowing it, since there is no acknowledgment. Middleboxes and firewalls are another axis: NAT traversal for UDP needs tricks like STUN/TURN, and some networks throttle UDP entirely, which is why QUIC deployments must plan fallbacks.
- Operational tradeoffs: choose TCP when every byte must arrive in order (transactions, APIs, file transfer); choose UDP when freshness beats completeness (telemetry, voice, gaming) or when the connectionless model simplifies multicast and discovery. The web-platform answer is to not choose at all for most APIs: use TCP-based HTTP today and adopt HTTP/3 when intermediaries support it, while reserving raw UDP for specialized protocols.
- RSIS3/mykb relevance: RSIS3 telemetry and pulse streams are freshness-sensitive, so they fit UDP or QUIC-style loss-tolerant delivery, while registry and knowledge-graph writes must be TCP-reliable — a useful mnemonic that state you can recompute may travel fast, but state that is authoritative must travel reliably.

## Related
- [[wiki/api-protocols/dns-fundamentals|DNS Fundamentals]] — related coverage in the same cluster
- [[wiki/api-protocols/ipv4-vs-ipv6|IPv4 vs IPv6]] — related coverage in the same cluster
- [[wiki/api-protocols/tcp-vs-udp|TCP vs UDP]] — related coverage in the same cluster
- [[wiki/api-protocols/ipv4-vs-ipv6|IPv4 vs IPv6]] — related coverage in the same cluster
- [[wiki/api-protocols/http-keep-alive|HTTP Keep-Alive]] — related coverage in the same cluster
- [[wiki/api-protocols/dns-load-balancing|DNS Load Balancing]] — related coverage in the same cluster
- [[wiki/api-protocols/load-balancing|Load Balancing]] — related coverage in the same cluster
