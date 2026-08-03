---
type: "concept"
title: "TCP Nagle & Delayed ACK"
description: "Small-packet coalescing and the latency interaction between them"
tags: ["tcp", "nagle", "delayed-ack", "networking"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# TCP Nagle & Delayed ACK

## Summary
Nagle's algorithm and delayed ACK are two TCP optimizations that coalesce small packets to reduce network load — and their interaction is one of the classic sources of latency in request/response protocols. Nagle holds a small write until the previous unacknowledged data is acknowledged; delayed ACK holds an acknowledgment for up to ~40-200ms hoping to piggyback it on outgoing data; together, on a request/response loop, they can add up to a full round-trip's worth of delay per transaction.

## Details
- Mechanism: Nagle's algorithm (RFC 896) allows a sender to have at most one small unacknowledged segment in flight: if a small write arrives while an earlier segment is unacknowledged, the kernel buffers it until the ACK arrives (or until enough data accumulates to fill a full segment). This reduces the number of tiny packets on connections that send dribbles of data. Delayed ACK (RFC 1122) makes the receiver wait up to ~40ms (Linux: `tcp_delack_min`/`tcp_delack_max`, typically 40-200ms, batched to one ACK per two segments) before acknowledging, so the ACK can piggyback on application data instead of traveling alone. Each is sensible in isolation; together they stall: the sender waits for an ACK before sending the next small request byte (Nagle), and the receiver waits to send that ACK (delayed ACK), producing up to ~40ms+ extra latency per exchange.
- Concrete examples: an SSH session typing one character at a time — with Nagle alone, each keystroke waits for the previous ACK (the "interactive latency" problem, mitigated by `TCP_NODELAY` and urgent data in modern ssh); a chat or RPC client with a request/response pattern seeing ~40ms added per call; the classic fix is `setsockopt(TCP_NODELAY)` on the sender — disabling Nagle so small writes go immediately, which eliminates the stall *provided* the application also does its own batching for genuinely tiny writes.
- Failure modes: the classic failure is setting `TCP_NODELAY` while forgetting the ACK side: Linux's `TCP_QUICKACK` (and, on the sender side, the delayed-ACK timer still applies to the peer's ACKs) — disabling Nagle alone helps, but the full fix for latency-critical loops is Nagle off plus quick ACK on the receiving end. Over-aggressive disabling without application batching floods the network with tiny packets (packet rate, not byte rate, is the constraint on many links and middleboxes), causing CPU and NAT-table pressure. The interaction is also why some protocols (HTTP/2, gRPC) moved away from tiny independent messages entirely.
- Operational tradeoffs: both algorithms are pure wins for bulk transfers (large downloads, streaming) where coalescing saves packets without adding perceptible latency, and pure costs for latency-sensitive small-message exchanges. The practice rules: leave defaults for bulk traffic; set `TCP_NODELAY` on request/response and interactive sockets; pair it with application-level message batching so you do not emit one packet per byte; and measure with `tcpdump`/Wireshark (look for the ACK-wait stalls) before blaming the network. RSIS3/mykb relevance: the daemon's API and agent-callback traffic is request/response — the classic Nagle/delayed-ACK victim; disabling Nagle on those sockets and batching telemetry writes is the transport-level counterpart to loop batching discipline.

## Related
- [[wiki/cloud-infra/tcp-ip-stack|TCP/IP Stack]]
- [[wiki/cloud-infra/udp-vs-tcp|UDP vs TCP]]
- [[wiki/cloud-infra/tcp-retransmission|TCP Retransmission]]
- [[wiki/infrastructure/nvme-over-fabrics-tcp|NVMe over Fabrics (TCP)]]
- [[wiki/syntheses/knowledge-acquisition-workflow|Knowledge Acquisition Workflow]] — how stubs grow into full articles in mykb
- [[wiki/syntheses/mykb-acquisition-curation-and-practices|Acquisition, Curation & Practices]] — the curation loop this stub belongs to
