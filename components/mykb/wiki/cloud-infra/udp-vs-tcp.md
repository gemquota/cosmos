---
type: "concept"
title: "UDP vs TCP"
description: "Reliable streams versus datagrams and when each transport fits"
tags: ["udp", "tcp", "transport", "protocols"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: [
  "https://www.rfc-editor.org/rfc/rfc9293",
  "https://www.rfc-editor.org/rfc/rfc768",
]
---

# UDP vs TCP

## Summary
TCP and UDP are the two transport protocols of the Internet with opposite design goals: reliability and order versus speed and simplicity. Choosing correctly between them shapes latency, throughput, and application architecture. Modern protocols increasingly layer reliability on top of UDP instead of using TCP directly.

## Details
- TCP provides streams: ordered bytes, flow control, congestion control, and retransmission, at the cost of connection state and head-of-line blocking.
- UDP provides datagrams: no connection, no ordering, no retransmission, but minimal overhead and full control for the application.
- RFC 9293 documents modern TCP; RFC 768 is still the UDP specification after decades of use.
- Real-time media, gaming, and DNS prefer UDP because a stale packet is worse than a lost one, while file transfer and web traffic prefer TCP.
- QUIC rebuilds TCP-like reliability over UDP and adds TLS 1.3, which is why HTTP/3 chooses it.
- In practice both appear on every host: the same kernel sockets API serves them, differing only in the transport protocol field and connection handling.

## Related
- [[wiki/cloud-infra/tcp-retransmission|TCP Retransmission]]
- [[wiki/infrastructure/nvme-over-fabrics-tcp|NVMe over Fabrics (TCP)]]
- [[wiki/os-shell/osi-model-and-tcp-ip|OSI Model & TCP/IP]]
- [[wiki/os-shell/tcp-connection-lifecycle|TCP Connections]]
