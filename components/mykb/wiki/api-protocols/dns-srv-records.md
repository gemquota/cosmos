---
type: "concept"
title: "DNS SRV Records"
description: "Service discovery via SRV records"
tags: ["dns", "srv-records", "service-discovery", "networking", "infrastructure"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://www.rfc-editor.org/rfc/rfc2782", "https://en.wikipedia.org/wiki/SRV_record"]
---

# DNS SRV Records

## Summary
SRV records (RFC 2782) let DNS advertise a service's hostname, port, priority, and weight: _service._proto.name -> priority weight port target. They move service discovery into DNS, letting clients find any service instance set without hard-coding ports — the mechanism behind LDAP, SIP, XMPP, Kubernetes headless services, and Consul.

## Details
- Format: _service._proto.example.com IN SRV priority weight port target; underscore-prefixed names avoid collisions with host records.
- Priority and weight: lower priority wins; equal priorities split load by weight — the protocol's built-in load distribution.
- Lookup usage: clients resolve the SRV set, pick per priority/weight (with retries on failed targets), then resolve the target A/AAAA record.
- Discovery stacks: Kubernetes headless services publish per-pod SRV records; Consul and etcd-backed DNS (CoreDNS) expose service endpoints the same way.
- Health integration: records only exist for healthy instances when the publisher removes failed endpoints (k8s readiness, Consul health checks).
- Limitations: no native TTL tuning for fast failover (k8s solves with short TTLs), and no per-instance metadata beyond the record fields.
- gRPC relevance: gRPC's DNS resolver can use SRV records for round-robin targets in some configurations, though xDS is preferred for rich policies.

## Related
- [[wiki/api-protocols/dns-load-balancing|DNS Load Balancing]] — priority/weight distribution across records
- [[wiki/api-protocols/grpc-load-balancing|gRPC Load Balancing]] — how gRPC resolves and balances targets
- [[wiki/infrastructure/service-discovery-patterns|Service Discovery Patterns]] — the broader discovery landscape
- [[wiki/api-protocols/health-checks|Health Checks]] — readiness determines which SRV targets exist
- [[wiki/devops-infra/kubernetes|Kubernetes]] — headless services publish SRV records
