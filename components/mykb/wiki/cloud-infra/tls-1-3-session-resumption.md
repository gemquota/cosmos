---
type: "concept"
title: "TLS 1.3 Session Resumption"
description: "PSK-based resumption and 0-RTT handshakes in TLS 1.3"
tags: ["tls", "resumption", "security", "http"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---
# TLS 1.3 Session Resumption

## Summary

TLS session resumption skips the full handshake on repeat connections: session IDs and session tickets cache the session state, and TLS 1.3 adds 0-RTT early data. Resumption is the difference between 1-RTT and near-0-RTT reconnects — and it has security tradeoffs to manage.

## Details
- Mechanism: TLS 1.2 resumption stores a session (ID server-side or ticket client-side) allowing an abbreviated handshake (~1 RTT); TLS 1.3 tickets (PSKs) allow resumption in one RTT and 0-RTT early data on the first flight; servers issue new tickets per session, tickets are encrypted with a server-side key, and anti-replay protections bound 0-RTT risk — early data must be gated behind authentication whenever the request mutates state.
- Concrete example: a mobile client that connects frequently (every few minutes) with TLS 1.3 resumption saves a full handshake (and its latency on high-RTT links) per reconnect; an HTTP/2 pool that stays warm rarely needs resumption at all; 0-RTT early data lets a client send its first request with the ClientHello — ideal for latency-sensitive APIs, dangerous for non-idempotent ones.
- Failure modes: 0-RTT replay — captured early data can be replayed (must be idempotent or replay-protected); ticket keys unrotated, allowing long-lived session forgery; resumption sessions leaking across clients on shared infrastructure; and ticket size or policy mismatches that silently fall back to full handshakes, hiding the performance regression.
- Operational tradeoffs: resumption trades a little security surface (ticket theft window) for significant latency savings on reconnect-heavy paths; the standard is short ticket lifetimes, rotating ticket keys, and 0-RTT only for safe, idempotent requests. Measure handshake RTT per client population to justify the settings, and size the anti-replay cache to the early-data window.
- RSIS3/mykb relevance: the wiki's API layer enables TLS 1.3 resumption with short-lived tickets; this note records the ticket policy the loop verifies after certificate or proxy changes.

## Related
- [[wiki/cloud-infra/https-and-tls|HTTPS & TLS]]
- [[wiki/cloud-infra/mutual-tls-internal-services|Mutual TLS for Internal Services]]
- [[wiki/cloud-infra/tls-performance|TLS Performance]]
- [[wiki/os-shell/tls-and-https|TLS & HTTPS]]
- [[wiki/cloud-infra/networking-fundamentals|Networking Fundamentals]]
