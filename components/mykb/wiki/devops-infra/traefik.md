---
type: "concept"
title: "Traefik"
description: "Cloud-native reverse proxy and ingress controller that auto-discovers containers and services"
tags: ["traefik", "reverse-proxy", "kubernetes", "containers", "networking"]
timestamp: "2026-07-31T00:00:00Z"
status: "stub"
---

# Traefik

## Summary
Traefik is a cloud-native reverse proxy that discovers services dynamically from container labels, Kubernetes ingresses, or DNS. It integrates Let's Encrypt for automatic TLS.

## Details
- Providers (Docker, K8s, Consul) generate routing config automatically — no manual reloads.
- Middlewares add auth, rate limiting, retries, and compression per route.
- Popular as the ingress gateway for self-hosted apps and local stacks.

## Related
- [[wiki/devops-infra/kubernetes|Kubernetes]] — ingress provider
- [[wiki/security/lets-encrypt|Let's Encrypt]] — automatic certificates
- [[wiki/api-protocols/rate-limiting|Rate Limiting]] — middleware enforcement
- [[wiki/devops-infra/docker-compose|Docker Compose]] — label-based discovery
- [[wiki/devops-infra/caddy|Caddy]] — simpler static alternative
