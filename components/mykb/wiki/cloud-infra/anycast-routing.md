---
type: "concept"
title: "Anycast Routing"
description: "Advertising the same IP from multiple locations so clients reach the nearest one"
tags: ["anycast", "routing", "bgp", "edge"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---
# Anycast Routing

## Summary

Anycast advertises the same IP from multiple locations and lets routers send each user to the nearest one. It is what makes CDNs, DNS, and global load balancers fast and resilient — at the cost of per-session consistency requirements.

## Details
- Mechanism: the same prefix is announced via BGP from many sites; routers pick the best path per destination, so different users (and sometimes different packets of one user) land at different sites. Protocols must tolerate this: DNS and HTTP reconnects are fine; long-lived TCP sessions and stateful apps are not, unless engineered with session affinity or shared state.
- Concrete example: 1.1.1.1 and 8.8.8.8 are anycast — a DNS query from Tokyo resolves at a Tokyo PoP; CDN edge IPs are anycast so video flows from the nearest edge; a health-checked anycast VIP fails over by withdrawing the route from a broken site.
- Failure modes: TCP flows pinning to one site while routing flaps (anycast + BGP convergence = session drops); stateful services (websockets, gaming) breaking unless sticky; overlapping anycast announcements leaking or conflicting; and hijacking — anycast prefixes are targets for BGP hijacks, needing RPKI/ROA protection.
- Operational tradeoffs: anycast buys latency reduction, DDoS absorption, and fast failover; it costs control over session locality and demands stateless or shared-state design. Use it for stateless protocols (DNS, HTTP edge) and reserve unicast + DNS steering for sticky workloads.
- RSIS3/mykb relevance: the hub and cosmos deployments rely on anycast DNS/CDN; this note records the architecture so the loop does not build stateful assumptions over anycast endpoints.
- Session design: keep anycast-facing protocols stateless or share state across sites; a websocket pinned to one PoP breaks when the route changes mid-session.
- Hijack defense: protect anycast prefixes with RPKI/ROA so a mistaken announcement cannot redirect your traffic to an attacker's network.

## Related
- [[wiki/cloud-infra/bgp-routing|BGP Routing]]
- [[wiki/infrastructure/eventbridge-and-routing|Eventbridge And Routing]]
- [[wiki/os-shell/routing-and-forwarding|Routing & Forwarding]]
- [[wiki/cloud-infra/networking-fundamentals|Networking Fundamentals]]
