---
type: "concept"
title: "Handshakes"
description: "The protocol negotiations that establish secure, synchronized sessions"
tags: ["handshake", "tls", "tcp", "protocols"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: [
  "https://www.rfc-editor.org/rfc/rfc8446",
  "https://www.rfc-editor.org/rfc/rfc9293",
]
---

# Handshakes

## Summary
Handshakes are the protocol negotiations that establish sessions before data flows. TCP opens connections with a three-way handshake, TLS authenticates and derives keys, and QUIC combines both into one exchange. Handshake behavior drives much of perceived network latency.

## Details
- TCP's three-way handshake (SYN, SYN-ACK, ACK) synchronizes sequence numbers and consumes one round trip before any data.
- TLS 1.3 completes in one round trip after TCP, or zero additional round trips when session resumption with pre-shared keys is used.
- QUIC merges transport and TLS negotiation into a single handshake and supports 0-RTT resumption for returning clients.
- Handshake failures are a common production symptom: packet loss drops SYNs, certificate mismatches abort TLS, and cipher suite mismatch prevents negotiation.
- TCP Fast Open and TLS session resumption are the main ways to reclaim handshake round trips.
- In the mykb graph, handshake mechanics connect the HTTP, TLS, and networking fundamentals nodes and inform latency tuning articles.

## Related
- [[wiki/cloud-infra/dns-over-https|DNS over HTTPS]]
- [[wiki/cloud-infra/anycast-routing|Anycast Routing]]
- [[wiki/cloud-infra/autoscaling|Autoscaling]]
- [[wiki/cloud-infra/availability-zones|Availability Zones]]
