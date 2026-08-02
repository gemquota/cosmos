---
type: "concept"
title: "Load Balancing"
description: "Distribution algorithms and health-aware routing"
tags: ["load-balancing", "traffic", "reliability", "infrastructure", "http"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://www.nginx.com/resources/glossary/load-balancing/", "https://www.envoyproxy.io/docs/envoy/latest/intro/arch_overview/upstream/load_balancing/overview"]
---

# Load Balancing

## Summary
Load balancing distributes traffic across a pool of servers to spread load, survive failures, and enable rolling deployments. Algorithms range from simple round-robin to least-request and consistent hashing, and every balancer combines distribution with health checks that keep failed backends out of rotation.

## Details
- L4 vs L7: L4 balancers forward TCP/UDP flows (IP + port); L7 balancers inspect HTTP (host, path, headers) for smarter routing and rewriting.
- Algorithms: round-robin, weighted round-robin, least-connections/least-request, random, and consistent hashing (sticky by key without session tables).
- Health-aware: active checks (periodic probes) and passive checks (error-rate tracking) mark backends unhealthy; traffic stops until they recover.
- Sticky sessions: needed for stateful backends (WebSockets, in-memory sessions); cookies, client IP, or hash-based affinity trade evenness for stability.
- Graceful degradation: balancers drain connections during rollouts (connection draining) so in-flight work completes before shutdown.
- Client-side vs server-side: gRPC uses client-side balancing; HTTP/2 and QUIC change how much the balancer can observe per connection.
- DNS interplay: DNS round-robin distributes at the resolver level; load balancers and DNS records are often layered (multi-region failover).

## Related
- [[wiki/api-protocols/grpc-load-balancing|gRPC Load Balancing]] — client-side balancing for multiplexed RPCs
- [[wiki/api-protocols/dns-load-balancing|DNS Load Balancing]] — resolver-level distribution
- [[wiki/api-protocols/health-checks|Health Checks]] — readiness feeds balancer decisions
- [[wiki/api-protocols/api-gateway|API Gateway]] — gateways are L7 balancers plus policy
- [[wiki/devops-infra/load-balancing|Load Balancing (DevOps)]] — the operations-focused companion
