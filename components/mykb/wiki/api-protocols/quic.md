---
type: "concept"
title: "QUIC"
description: "QUIC transport: handshake, 0-RTT, and migration"
tags: ["quic", "transport", "udp", "tls", "protocols"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://www.rfc-editor.org/rfc/rfc9000", "https://blog.cloudflare.com/the-quic-handshake/"]
---

# QUIC

## Summary
QUIC (RFC 9000) is a modern transport protocol over UDP combining TCP-like reliability, TLS 1.3 encryption, and HTTP/2-style multiplexing into one handshake. It delivers connection IDs for migration, 0-RTT resumption, and independent streams — the foundation of HTTP/3.

## Details
- Design: QUIC replaces the TCP+TLS+HTTP layering with a single handshake that negotiates transport AND TLS together, halving round trips.
- Handshake: 1-RTT for new connections (one round trip total to start sending), 0-RTT for resumed ones (data on the first flight).
- Streams: independent bidirectional and unidirectional streams with their own flow control; loss in one stream does not stall others.
- Connection IDs: clients and servers address connections by ID rather than (IP, port), enabling seamless network migration.
- Encryption: TLS 1.3 is integral; even transport headers like packet numbers are partially encrypted, hiding metadata from middleboxes.
- Loss recovery: packet-number-based recovery with ACK ranges; QUIC pioneered more precise RTT estimation and faster recovery than TCP.
- Adoption: HTTP/3 (RFC 9114), and increasingly as a generic transport (e.g., for gRPC and custom protocols); UDP support is the main deployment blocker.

## Related
- [[wiki/api-protocols/http3|HTTP/3]] — HTTP over QUIC
- [[wiki/api-protocols/tls-handshake|TLS Handshake]] — TLS 1.3 is embedded in QUIC
- [[wiki/api-protocols/http2|HTTP/2]] — the stream model QUIC generalizes
- [[wiki/api-protocols/grpc|gRPC]] — gRPC is exploring QUIC transport
- [[wiki/api-protocols/backpressure|Backpressure]] — per-stream flow control in QUIC
