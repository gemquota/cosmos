---
type: "concept"
title: "Load Balancing"
description: "Distributing client traffic across backend instances to improve availability, latency, and capacity utilization"
tags: ["load-balancing", "traffic", "l4", "l7", "resilience"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://www.nginx.com/resources/glossary/load-balancing/"]
---

# Load Balancing

## Summary
Load balancing distributes incoming traffic across a pool of backend instances so no single server is overwhelmed and failures are absorbed gracefully. It operates at L4 (connections) or L7 (HTTP) and is a core availability primitive for web services. Health checks decide which backends are eligible to receive traffic.

## Details
- L4 balancers forward TCP/UDP connections based on IP and port; L7 balancers inspect HTTP and can route by path, host, header, or cookie — with TLS termination and rewriting.
- Algorithms: round-robin, least-connections, weighted distribution, and consistent hashing for session affinity without sticky sessions.
- Health-based behavior: unhealthy backends are drained and removed; this is why health-check design directly determines deploy safety.
- Topology: a single load balancer is a single point of failure, so production setups use VIPs with keepalived, DNS-based failover (GSLB), or a cloud LB per availability zone.
- TLS termination at the edge shifts certificate management to the balancer and enables inspection, but requires end-to-end TLS discipline back to backends.
- Worked example: nginx upstreams with active health checks + least_conn; Envoy clusters with outlier detection; cloud LBs with instance-group targets for autoscaling.
- In this wiki the pattern is instantiated by nginx, Envoy, Traefik, Caddy, and Cloudflare, and by Kubernetes Service types (ClusterIP, NodePort, LoadBalancer).

## Related
- [[wiki/infrastructure/health-check-patterns|Health Check Patterns]] — decides which backends receive traffic
- [[wiki/cloud-infra/latency-optimization|Latency Optimization]] — what good balancing improves
- [[wiki/infrastructure/zero-downtime-deploys|Zero-Downtime Deploys]] — rolling changes behind the balancer
- [[wiki/devops-infra/nginx|Nginx]] — L7 load balancing and reverse proxy
- [[wiki/devops-infra/envoy|Envoy]] — advanced L7 balancing with outlier detection
- [[wiki/devops-infra/cloudflare|Cloudflare]] — global edge load balancing and DNS
