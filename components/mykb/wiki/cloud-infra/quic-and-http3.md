---
type: "concept"
title: "QUIC & HTTP/3"
description: "The UDP-based transport with built-in TLS 1.3 and its HTTP/3 mapping"
tags: ["quic", "http3", "udp", "tls"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---
# QUIC & HTTP/3

## Summary

QUIC is a UDP-based transport with TLS 1.3, stream multiplexing, connection migration, and 0-RTT; HTTP/3 is the HTTP mapping over it. Together they fix TCP's head-of-line blocking and handshake cost — the reasons latency-sensitive web traffic is moving to HTTP/3.

## Details
- Mechanism: QUIC replaces TCP+TLS: handshake combines transport and TLS in one RTT (0-RTT for repeat), streams carry independent loss recovery, connection IDs survive network changes (mobile handoff without renegotiation), and it is encrypted end-to-end by default (including headers). HTTP/3 keeps HTTP semantics with a new frame layer and QPACK header compression.
- Concrete example: a mobile app crossing Wi-Fi→cellular keeps its QUIC connection alive while TCP+TLS would restart (saving hundreds of ms); a page with a lossy video stream and a chat stream — loss on video no longer stalls chat (stream isolation); repeat visitors with 0-RTT see faster first requests.
- Failure modes: 0-RTT replay of mutating requests (idempotency required); UDP blocked/throttled on some networks (fall back to h2); middleboxes mangling QUIC; observability gaps — many log/DPI stacks do not parse QUIC, hiding traffic details; and QPACK/HTTP/3 edge cases in intermediaries.
- Operational tradeoffs: HTTP/3 is the modern default for user-facing edge traffic; enable it with HTTP/2 fallback, monitor both protocols, and reserve deep protocol analysis for TCP when needed. Measure on real mobile networks — the wins concentrate where loss and mobility exist.
- RSIS3/mykb relevance: the wiki's edge config enables h3 with fallbacks; this note records the protocol matrix the loop verifies after edge configuration changes.
- Deployment checklist: verify ALPN negotiates h3, confirm UDP 443 is open on networks you serve, and keep monitoring that splits metrics per protocol so a silent h2 fallback is visible.
- Security note: QUIC's encryption-by-default hides headers from inspection; if compliance requires visibility, use the provider's decrypted-log integration rather than expecting to see plaintext headers.

## Related
- [[wiki/cloud-infra/networking-fundamentals|Networking Fundamentals]]
- [[wiki/cloud-infra/tcp-ip-stack|TCP/IP Stack]]
- [[wiki/syntheses/knowledge-acquisition-workflow|Knowledge Acquisition Workflow]]
- [[wiki/syntheses/mykb-acquisition-curation-and-practices|Acquisition, Curation & Practices]]
