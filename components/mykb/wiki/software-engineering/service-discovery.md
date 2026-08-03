---
type: "concept"
title: "Service Discovery"
description: "Mechanisms that let services locate each other's addresses at runtime"
tags: ["distributed-systems", "networking", "microservices", "dns"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
---
# Service Discovery

## Summary

Service discovery answers "where is this service right now?" — DNS-based, registry-based (Consul, etcd, Zookeeper), or platform-native (Kubernetes, cloud service discovery). It replaces hard-coded addresses and makes elastic, self-healing architectures possible.

## Details
- Mechanism: services register instances (address, port, health) with a registry; consumers resolve via the registry or DNS; health checks deregister dead instances; client-side discovery (resolved list in the consumer) vs server-side (load balancer queries the registry) are the two consumption models. Kubernetes abstracts this with DNS + endpoints; Consul/etcd serve non-K8s stacks.
- Concrete example: a payments service scales to 5 instances; new ones register with Consul, old ones deregister on health-check failure; an API gateway (server-side) queries the registry for the current list and load-balances; a client library (client-side) gets the list and balances itself, cutting one hop.
- Failure modes: stale registrations after crashes (TTLs and health checks must be reliable); registry as single point of failure (run quorum, plan for its loss); DNS caching defeating failover (short TTLs); and discovery adding a dependency to every startup — bootstrap without the registry must still work (cached last-known endpoints).
- Operational tradeoffs: discovery buys elasticity and self-healing at the cost of infrastructure and eventual consistency (registration lag); the pattern is platform-native discovery where available (K8s), registry for VMs, and DNS as the universal fallback.
- RSIS3/mykb relevance: the wiki's services would resolve through the platform registry with DNS fallback; this note records the registration and health-check conventions the loop relies on during scaling.
- Startup order: consumers must tolerate registry unavailability at boot by retrying or using cached endpoints; a registry outage should degrade discovery, not disable the fleet.
- Registration hygiene: implement graceful deregistration on shutdown and let health checks purge crash leftovers; stale entries are the main source of "route to dead instance" errors.

## Related
- [[wiki/software-engineering/microservices-architecture|Microservices Architecture]] — services need discovery as soon as they scale horizontally
- [[wiki/api-protocols/health-checks|Health Checks]] — the liveness signal discovery relies on
- [[wiki/devops-infra/kubernetes|Kubernetes]] — built-in service discovery via DNS and endpoints
- [[wiki/devops-infra/envoy|Envoy]] — a proxy that performs discovery on behalf of clients
