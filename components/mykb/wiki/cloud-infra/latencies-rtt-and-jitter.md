---
type: "concept"
title: "Latency, RTT & Jitter"
description: "Measuring round-trip time, variability, and their effect on protocols"
tags: ["latency", "rtt", "jitter", "networking"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---
# Latency, RTT & Jitter

## Summary

Latency is the time for a packet to traverse a path, RTT is the round trip, and jitter is its variance. They are the three numbers that decide whether a service feels local — and each is dominated by different physics: distance, queueing, and load.

## Details
- Mechanism: propagation delay is fixed by distance (~1ms per 100km fiber), processing and queueing add variable delay; RTT = 2× one-way for request-response; jitter is the standard deviation of RTT, driven by queueing, scheduling, and congestion. TCP and QUIC react to measured RTT; timeouts and retransmissions compound on high-jitter paths.
- Concrete example: a user in Sydney calling a us-east service pays ~200ms RTT before any processing; jitter spikes (bufferbloat, shared links) push p95 to 400ms, breaking interactive UX even when median looks fine; a game or voice app tolerates latency better than jitter, which is why jitter buffers and pacing exist.
- Failure modes: optimizing median RTT while p95/p99 explode (jitter is the UX killer); measuring from the wrong vantage (server-side RTT misses the user's last mile); mistaking retransmission delay for bandwidth limits; and ignoring that TLS handshakes add 1-2 RTTs — a 200ms link becomes 400-600ms to first byte.
- Operational tradeoffs: latency is bought with geography (edge, CDN, region choice), jitter with buffer and congestion control, and both with architecture (fewer round trips, caching, prefetch). Instrument the full path (client → edge → origin) and track p95/p99, not averages.
- RSIS3/mykb relevance: the wiki's global latency dashboard would feed the loop's placement reviews, which weigh region proximity against residency constraints.
- Measurement vantage: instrument both server-side and client-side (RUM); server-side RTT misses the last mile where jitter and loss actually live.
- Budgeting: set latency budgets per user-facing path and trace each hop; the p95 stack-up of five 20ms hops is the number to manage. Include client-side queueing in the budget, since device-level delays dominate on mobile.

## Related
- [[wiki/cloud-infra/http-3-0-rtt|HTTP/3 0-RTT]]
