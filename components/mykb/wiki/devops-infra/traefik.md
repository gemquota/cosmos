---
type: "entity"
title: "Traefik"
description: "Cloud-native reverse proxy and ingress controller that auto-discovers containers and services"
tags: ["traefik", "reverse-proxy", "kubernetes", "containers", "networking"]
timestamp: "2026-07-31T00:00:00Z"
status: "growing"
---

# Traefik

## Summary
Traefik is a cloud-native reverse proxy that discovers services dynamically from container labels, Kubernetes ingresses, or DNS. It integrates Let's Encrypt for automatic TLS.

## Details
- Providers (Docker, K8s, Consul) generate routing config automatically — no manual reloads.
- Middlewares add auth, rate limiting, retries, and compression per route.
- Popular as the ingress gateway for self-hosted apps and local stacks.

## Architecture

Traefik runs a control loop: providers watch infrastructure, translate changes into a dynamic configuration model, and the proxy applies new routing rules without a restart. That is the key difference from static proxies like [[wiki/devops-infra/nginx|Nginx]], where config is edited by hand and reloaded. Router rules match by host, path, and headers, then forward to a target service; middleware chains wrap each route, so authentication, rate limiting, retries, and compression apply per route. The dashboard exposes routing, health, and middleware state in one view.

## Providers

Providers are the adapters that feed dynamic configuration. The Docker provider reads container labels such as `traefik.http.routers.app.rule=Host(\`app.example.com\`)`, so a new container becomes routable the moment it starts. The Kubernetes provider watches Ingress and IngressRoute resources, which is why Traefik is a common in-cluster ingress controller alongside [[wiki/devops-infra/kubernetes|Kubernetes]]. Consul, etcd, file, and DNS providers cover bare-metal and cloud environments. [[wiki/devops-infra/helm|Helm]] charts package Traefik for Kubernetes, and [[wiki/devops-infra/docker-compose|Docker Compose]] relies on label-based discovery for local stacks.

## Middlewares and TLS

Middlewares are the composable unit of traffic policy: BasicAuth, rate limiting, circuit breakers, retries, and header rewriting chain per router. TLS is automated through ACME — Traefik obtains and renews certificates from [[wiki/security/lets-encrypt|Let's Encrypt]] for routed hosts, or serves certs from files and secrets. [[wiki/devops-infra/envoy|Envoy]] offers similar dynamic control with a different model, and [[wiki/devops-infra/caddy|Caddy]] is a simpler alternative that automates TLS with less integration.

## Deployment Notes

Operators run Traefik as an edge container or a Kubernetes DaemonSet, publishing ports 80 and 443. Sizing tracks connection count rather than service count, and health checks and logs feed the [[wiki/devops-infra/load-balancing|load balancing]] and [[wiki/devops-infra/api-gateway-patterns|API gateway patterns]] it implements. Because routing is data-driven, discipline shifts to naming conventions and label hygiene: consistent labels keep configuration self-documenting, while ad-hoc labels turn the proxy into a tangle of routes.

## Related
- [[wiki/devops-infra/kubernetes|Kubernetes]] — ingress provider
- [[wiki/security/lets-encrypt|Let's Encrypt]] — automatic certificates
- [[wiki/api-protocols/rate-limiting|Rate Limiting]] — middleware enforcement
- [[wiki/devops-infra/docker-compose|Docker Compose]] — label-based discovery
- [[wiki/devops-infra/caddy|Caddy]] — simpler static alternative
