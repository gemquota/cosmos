---
type: "concept"
title: "Reverse Proxies"
description: "Fronting origin servers for TLS, routing, and protection"
tags: ["reverse-proxy", "nginx", "routing", "web"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: [
  "https://docs.nginx.com/nginx/admin-guide/web-server/reverse-proxy/",
  "https://httpd.apache.org/docs/2.4/mod/mod_proxy.html",
]
---

# Reverse Proxies

## Summary
A reverse proxy sits in front of origin servers, terminating client connections and forwarding requests. It is the enforcement point for TLS, routing, caching, and basic security. Almost every production web architecture has one.

## Details
- Reverse proxies hide origin topology, letting servers change IPs and ports without client impact.
- TLS termination moves certificate management to one place; the proxy then re-encrypts or forwards in plaintext inside the network.
- Routing rules split traffic by host or path to different backends, enabling microservice front-ends.
- Caching and compression at the proxy reduce origin load and response times for repeatable content.
- NGINX and Apache document the pattern thoroughly, with directives for proxy_pass and mod_proxy respectively.
- In the mykb graph, reverse proxies connect to ingress controllers, API gateways, and web application firewall articles.
- Operationally, alerting thresholds and runbook steps for this concept belong in the SLO, incident, and runbook articles of this cluster.
- Pipelines and GitOps practices in the delivery articles show how this concept is deployed and promoted safely.

## Related
- [[wiki/devops-infra/zero-trust-access-proxies|Zero Trust Access Proxies]]
- [[wiki/devops-infra/identity-aware-proxies|Identity-Aware Proxies]]
- [[wiki/devops-infra/acid|ACID]]
- [[wiki/devops-infra/alert-fatigue|Alert Fatigue]]
