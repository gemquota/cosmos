---
type: "concept"
title: "DNS Load Balancing"
description: "Round-robin and weighted DNS distribution"
tags: ["dns", "load-balancing", "round-robin", "networking", "high-availability"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://www.cloudflare.com/learning/dns/glossary/round-robin-dns/", "https://www.rfc-editor.org/rfc/rfc1034"]
---

# DNS Load Balancing

## Summary
DNS load balancing distributes traffic by returning different IPs (or records) for the same name: classic round-robin shuffles A records per query, while weighted policies and geo-aware answers skew distribution. It is the first hop of almost every distributed system — the cheapest form of load balancing, with real trade-offs.

## Details
- Round-robin: a zone file with multiple A records; resolvers return them in rotation, spreading clients across servers.
- Weighted: geo or weighted policies (via DNS providers or load balancers) return some IPs more often, matching capacity per region or pool.
- Latency-based: managed DNS (Route 53, Cloudflare) returns the nearest or fastest endpoint using health and latency telemetry.
- Health integration: records for unhealthy instances are removed (health checks) or clients retry the next IP in the set.
- Caching is the catch: resolver and browser TTL caching freezes distributions and delays failover; short TTLs improve agility but raise query volume.
- Split-horizon: internal vs external names resolve differently, letting internal clients avoid NAT and external clients hit the edge.
- Limits: DNS cannot see connection health or load per connection — pair it with L4/L7 load balancers for real-time decisions.

## Related
- [[wiki/api-protocols/dns-srv-records|DNS SRV Records]] — service discovery with ports and weights
- [[wiki/api-protocols/load-balancing|Load Balancing]] — DNS is the distribution first hop
- [[wiki/api-protocols/health-checks|Health Checks]] — health-aware record removal
- [[wiki/api-protocols/grpc-load-balancing|gRPC Load Balancing]] — gRPC resolves DNS then balances client-side
- [[wiki/cloud-infra/dns-management|DNS Management]] — operating DNS at scale
