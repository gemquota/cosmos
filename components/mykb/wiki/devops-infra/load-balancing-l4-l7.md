---
type: "concept"
title: "Load Balancing L4-L7"
description: "Distributing traffic at transport or application layers"
tags: ["load-balancing", "l4", "l7", "traffic"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: [
  "https://docs.nginx.com/nginx/admin-guide/load-balancer/http-load-balancer/",
  "https://www.haproxy.org/",
]
---

# Load Balancing L4-L7

## Summary
Load balancers distribute traffic across backend instances to scale capacity and tolerate failure. L4 balancers forward at the transport layer; L7 balancers inspect application content. The choice determines what routing, health checking, and protocol features are available.

## Details
- L4 load balancing operates on TCP/UDP connections and forwards packets with minimal inspection, preserving protocol opacity and performing very well on raw throughput and connection counts.
- L7 load balancing terminates the connection, reads HTTP requests, and can route by host, path, headers, or cookies.
- Health checks drive backend membership: failed backends are removed from rotation automatically.
- Algorithms range from round-robin to least-connections to consistent hashing for session affinity.
- Load balancers also terminate TLS, add security headers, and absorb slowloris-style attacks.
- In Kubernetes, Services and Ingress controllers play the same roles, so L4/L7 concepts map directly to cluster networking.
- Operationally, alerting thresholds and runbook steps for this concept belong in the SLO, incident, and runbook articles of this cluster.

## Related
- [[wiki/devops-infra/envoy-data-plane|Envoy Data Plane]]
- [[wiki/devops-infra/nginx-configuration-patterns|NGINX Configuration Patterns]]
- [[wiki/devops-infra/load-balancing|Load Balancing]]
- [[wiki/devops-infra/acid|ACID]]
