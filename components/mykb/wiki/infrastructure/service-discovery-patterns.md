---
type: "concept"
title: "Service Discovery Patterns"
description: "How services find each other's addresses: DNS, registries, and proxies"
tags: ["service-discovery", "dns", "registries", "patterns"]
timestamp: "2026-08-01T00:00:00Z"
status: "stub"
---

# Service Discovery Patterns

## Summary
Service discovery answers "where is the other service?" — via DNS names, client-side registries, or server-side proxies. In dynamic environments like Kubernetes, addresses change constantly, so discovery must be automated.

## Details
- DNS-based discovery (kube-dns, Consul DNS) is simplest: names resolve to current endpoints.
- Registry-based discovery (Consul, etcd) gives richer health and metadata but needs client integration.
- Server-side discovery via load balancers or meshes keeps clients dumb.
- Open question: how discovery and configuration should merge in a mesh world.

## Related
- [[wiki/devops-infra/load-balancing|Load Balancing]] — server-side discovery
- [[wiki/infrastructure/service-mesh|Service Mesh]] — mesh-native service identity
- [[wiki/cloud-infra/dns-management|DNS Management]] — DNS as a discovery mechanism
- [[wiki/devops-infra/envoy|Envoy]] — proxy-side discovery
