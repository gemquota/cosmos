---
type: "concept"
title: "DNS-Based Service Discovery"
description: "SRV records and convention-based discovery for services"
tags: ["service-discovery", "dns", "srv", "networking"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---
# DNS-Based Service Discovery

## Summary

DNS-based service discovery maps service names to addresses so clients do not hard-code IPs: SRV records for ports, A/AAAA for endpoints, service registries (Consul, etcd, cloud service discovery) publishing into DNS. It is the simplest discovery mechanism and the one with the worst cache-failure modes.

## Details
- Mechanism: services register names (app.prod.internal) with the registry; the registry updates DNS (or the resolver serves from its store); clients resolve names with short TTLs and retry. Variants: SRV records carry host+port (used by gRPC, Kubernetes headless services), cloud service discovery publishes instance IPs (AWS Cloud Map), and sidecar registrars (Consul) health-check before advertising.
- Concrete example: a microservice calls http://payments.svc.internal:8080 resolved via an internal resolver backed by a registry; a new payments instance registers, unhealthy ones deregister, and clients pick them up within the TTL; a Kubernetes service with no cluster IP exposes pod IPs via DNS for stateful consumers.
- Failure modes: caching defeating failover (long TTLs keep dead IPs alive — use TTL ~5-30s and client-side retry); split-horizon gaps (public resolver serving internal names); registration lag after deployment (clients hit the old IP until propagation); and DNS as a hard dependency — resolver outage takes down all service calls.
- Operational tradeoffs: DNS discovery is simple, ubiquitous, and works everywhere; its cache and propagation semantics are its weakness for fast failover. Pair with client-side retry/load balancing, keep TTLs short for dynamic services, and treat the resolver as critical infrastructure.
- RSIS3/mykb relevance: the wiki's services would resolve through an internal DNS backed by the registry; this note records TTL and retry policy so the loop's failover tests respect discovery lag.
- Health checks: discovery is only as fresh as its health checks; a registry that never deregisters dead instances is a list of traffic black holes.

## Related
- [[wiki/cloud-infra/dns-resolution-process|DNS Resolution Process]]
- [[wiki/devops-infra/service-mesh-sidecars|Service Mesh Sidecars]]
- [[wiki/cloud-infra/dns-over-https|DNS over HTTPS]]
- [[wiki/devops-infra/service-meshes-istio-linkerd|Service Meshes: Istio & Linkerd]]
