---
type: "concept"
title: "Point of Presence"
description: "Physical network facilities where providers interconnect with last-mile networks"
tags: ["pop", "networking", "edge", "cdn"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---
# Point of Presence

## Summary

A point of presence (PoP) is a provider's local facility where traffic enters their network — the physical anchor of CDN, DNS, and edge compute. PoP density determines how close users get to cached content and how well DDoS is absorbed.

## Details
- Mechanism: providers lease space in colocation facilities worldwide, each with routers, caches, and (increasingly) compute; anycast or DNS routing sends users to the nearest PoP; caches store popular content, origin shields fetch the rest; edge functions run at the PoP, so "the edge" is literally where the user meets the network.
- Concrete example: a CDN with 300+ PoPs serves a Tokyo user from Tokyo, not the US origin — 150ms becomes 5ms for cached assets; a DNS anycast network answers queries at the closest PoP, making resolution fast everywhere; DDoS traffic is dropped at the PoP boundary, far from origin.
- Failure modes: PoP congestion degrading one region (routing may not shift traffic promptly); cache misses at cold PoPs causing origin load spikes; geo-IP routing sending users to a farther PoP when the nearest is degraded; and edge compute at PoPs having different limits than the origin platform, breaking deployment assumptions.
- Operational tradeoffs: more PoPs mean better latency and absorption but more surface to operate (or pay for); managed CDNs bundle this at per-GB cost. Decide what must be at the PoP (cache, DNS, small compute) vs origin (stateful, heavy compute) and verify with real user telemetry per region.
- RSIS3/mykb relevance: the wiki's edge deployment would track per-PoP cache-hit and latency metrics, feeding the loop's decisions about what moves to the edge.
- Latency verification: use RUM per PoP to confirm users actually land where routing intends; geo-IP and anycast can disagree with the nearest PoP.
- Failover rehearsal: simulate a PoP outage and confirm traffic shifts; the routing convergence time is the number that matters for availability.

## Related
- [[wiki/devops-infra/point-in-time-recovery|Point-in-Time Recovery]]
