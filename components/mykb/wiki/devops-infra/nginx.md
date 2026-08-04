---
type: "entity"
title: "Nginx"
description: "High-performance web server and reverse proxy handling static content, TLS, caching, and load balancing"
tags: ["nginx", "webserver", "reverse-proxy", "tls", "devops"]
timestamp: "2026-07-31T00:00:00Z"
status: "stub"
---

# Nginx

## Summary
Nginx is a high-performance web server and reverse proxy known for serving static files, terminating TLS, caching responses, and load-balancing upstreams. It powers a large share of the public web.

## Details
- Event-driven architecture handles many concurrent connections with low memory.
- Common roles: static hosting, API gateway in front of FastAPI/Flask, TLS termination.
- Config is declarative (`nginx.conf`); `nginx -t` validates before reload.

## Related
- [[wiki/api-protocols/http-caching|HTTP Caching]] — proxy cache configuration
- [[wiki/security/https|HTTPS]] — TLS termination patterns
- [[wiki/api-protocols/health-checks|Health Checks]] — upstream health monitoring
- [[wiki/frontend/static-site-generation|Static Site Generation]] — static file serving
- [[wiki/devops-infra/caddy|Caddy]] — simpler auto-TLS alternative
