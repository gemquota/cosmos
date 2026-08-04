---
type: "entity"
title: "Caddy"
description: "Web server and reverse proxy with automatic HTTPS via Let's Encrypt by default"
tags: ["caddy", "webserver", "reverse-proxy", "tls", "go"]
timestamp: "2026-07-31T00:00:00Z"
status: "stub"
---

# Caddy

## Summary
Caddy is a Go-based web server and reverse proxy that enables HTTPS automatically: it obtains and renews Let's Encrypt certificates with zero config. Its simple `Caddyfile` syntax lowers ops overhead.

## Details
- Automatic TLS, HTTP/2/3, and sane defaults make secure hosting nearly frictionless.
- Useful as a TLS-terminating reverse proxy in front of local services (dashboards, daemons).
- Compare to Nginx: Caddy trades some configurability for automation.

## Related
- [[wiki/security/lets-encrypt|Let's Encrypt]] — automatic certificate source
- [[wiki/security/https|HTTPS]] — TLS by default
- [[wiki/devops-infra/nginx|Nginx]] — classic alternative
- [[wiki/devops-infra/traefik|Traefik]] — container-native proxy alternative
- [[wiki/api-protocols/http-caching|HTTP Caching]] — proxy caching
