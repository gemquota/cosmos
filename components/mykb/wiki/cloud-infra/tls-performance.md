---
type: "concept"
title: "TLS Performance"
description: "Handshake cost, session reuse, and hardware acceleration"
tags: ["tls", "performance", "handshake", "security"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---
# TLS Performance

## Summary

TLS performance is the cost of handshakes, cipher suites, and connection reuse: each new handshake costs 1-3 RTTs, and misconfiguration (old ciphers, renegotiation, no resumption) turns encryption into a latency tax. Modern TLS is fast — when it is not, the cause is almost always operational.

## Details
- Mechanism: TLS 1.3 handshake = 1 RTT (0-RTT with resumption); TLS 1.2 with full handshake = 2 RTTs; session resumption cuts repeat connections; cipher choice matters little on modern CPUs (AES-NI, ChaCha20 for mobile), but negotiation failures force downgrades or renegotiation; connection reuse (HTTP/2 pools, keep-alive) amortizes the handshake across requests.
- Concrete example: a page with 50 assets over HTTP/1.1 pays a handshake per connection unless keep-alive/reuse; moving to HTTP/2 + TLS 1.3 turns that into one handshake, saving hundreds of ms on a high-RTT path; a legacy client forcing TLS 1.2 + RSA key exchange adds RTTs and CPU — measurable in the waterfall.
- Failure modes: ignoring handshake count in performance budgets (every reconnect pays again); cipher/config mismatches causing fallbacks to slower paths; OCSP stapling missing, adding validation round trips; TLS termination at the wrong layer (per-request terminate/re-encrypt thrash); and 0-RTT misuse (replay risk) or non-use (missed latency wins).
- Operational tradeoffs: TLS is not a bottleneck on modern hardware — architecture is: reuse connections, enable 1.3, staple OCSP, and terminate where the session pool lives. Measure TLS handshake time and connection reuse from RUM to find the real cost.
- RSIS3/mykb relevance: the wiki's edge config uses TLS 1.3, OCSP stapling, and long-lived pools; this note is the checklist the loop uses when the handshake metrics regress.
- Certificate path: keep chains short and stapled; an extra CA in the chain is an extra round trip and a larger handshake for every new client.

## Related
- [[wiki/cloud-infra/https-and-tls|HTTPS & TLS]]
- [[wiki/cloud-infra/tls-1-3-session-resumption|TLS 1.3 Session Resumption]]
- [[wiki/cloud-infra/mutual-tls-internal-services|Mutual TLS for Internal Services]]
- [[wiki/os-shell/tls-and-https|TLS & HTTPS]]
- [[wiki/cloud-infra/networking-fundamentals|Networking Fundamentals]]
