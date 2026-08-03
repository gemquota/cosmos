---
type: "concept"
title: "Caddy & Traefik"
description: "Modern reverse proxies with automatic TLS and dynamic configuration"
tags: ["caddy", "traefik", "proxy", "tls"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# Caddy & Traefik

## Summary
Caddy and Traefik are modern reverse proxies that remove the two most error-prone manual tasks of the NGINX generation: TLS certificate management and dynamic configuration from service discovery. Caddy automates ACME/Let's Encrypt issuance and renewal; Traefik discovers backends from container labels, Kubernetes ingresses, or provider APIs and reloads routes automatically.

## Details
- Caddy: automatic HTTPS from a small `Caddyfile` (`reverse_proxy localhost:8080`), HTTP/3, on-demand and internal CAs, plugins for S3/Consul config; ideal for single-host and small-mesh setups where the file is the config.
- Traefik: entry points, routers, and services composed from providers (Docker labels, Kubernetes CRDs, Consul); a middleware chain (auth, rate limit, retries, headers) attaches per route; the dashboard exposes live routing state.
- Concrete example: a compose file labels `traefik.http.routers.app.rule=Host(`app.example.com`)` plus a certresolver, and Traefik obtains and renews the certificate; Caddy does the same with two lines in the Caddyfile, including OCSP stapling and automatic renewal.
- Failure modes: ACME rate limits when many hostnames are issued at once (use the staging CA for tests and reuse resolvers); discovery churn — a restarting container can briefly remove and re-add routes, dropping in-flight requests; middleware misordering changes semantics; automatic reloads can mask config errors that only surface in logs, so validate config in CI (`caddy validate`, `traefik --validate`).
- Tradeoffs: label- and file-driven configuration is more magical and less auditable than NGINX config, so config-as-code diff discipline matters; both are single-process, so HA requires running several instances behind a load balancer; Caddy is simpler and more portable, Traefik scales better into multi-provider clusters.
- RSIS3 relevance: the dashboard and MyKB daemon are exactly the local services where automatic TLS and label-based discovery remove manual proxy upkeep from RSIS3's operational loops.

## Related
- [[wiki/devops-infra/caddy|Caddy]] — related coverage in the same cluster
- [[wiki/devops-infra/traefik|Traefik]] — related coverage in the same cluster
- [[wiki/devops-infra/kubernetes-control-plane|Kubernetes Control Plane]] — related coverage in the same cluster
- [[wiki/devops-infra/observability-pillars|Observability Pillars]] — related coverage in the same cluster
- [[wiki/syntheses/knowledge-acquisition-workflow|Knowledge Acquisition Workflow]] — how stubs grow into full articles in mykb
- [[wiki/syntheses/mykb-acquisition-curation-and-practices|Acquisition, Curation & Practices]] — the curation loop this stub belongs to
