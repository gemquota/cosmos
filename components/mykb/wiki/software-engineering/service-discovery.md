---
type: "concept"
title: "Service Discovery"
description: "Mechanisms that let services locate each other's addresses at runtime"
tags: ["distributed-systems", "networking", "microservices", "dns"]
timestamp: "2026-08-01T00:00:00Z"
status: "stub"
---

# Service Discovery

## Summary
Service discovery answers the question: what address do I use to reach service X? In dynamic environments where instances come and go, static config is not enough; discovery registries or DNS-based resolution are required.

## Details
- Client-side discovery queries a registry (Consul, etcd, Eureka); server-side discovery sits behind a load balancer.
- Health checks prune dead instances from the registry so clients do not call the departed.
- RSIS3 relevance: any future multi-process agent or daemon mesh will need the same registry discipline.

## Related
- [[wiki/software-engineering/microservices-architecture|Microservices Architecture]] — services need discovery as soon as they scale horizontally
- [[wiki/api-protocols/health-checks|Health Checks]] — the liveness signal discovery relies on
- [[wiki/devops-infra/kubernetes|Kubernetes]] — built-in service discovery via DNS and endpoints
- [[wiki/devops-infra/envoy|Envoy]] — a proxy that performs discovery on behalf of clients
