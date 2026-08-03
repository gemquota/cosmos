---
type: "concept"
title: "HAProxy vs NGINX"
description: "Choosing between a dedicated L4/L7 load balancer and a web server proxy"
tags: ["haproxy", "nginx", "load-balancing", "proxy"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# HAProxy vs NGINX

## Summary
HAProxy and NGINX are the two workhorse reverse proxies: HAProxy is a purpose-built TCP/HTTP load balancer famous for reliability, precise health checks, and connection management; NGINX is a web server plus proxy with rich module ecosystem, caching, and TLS features. Choosing between them depends on whether the workload is pure load balancing or full request serving.

## Details
- HAProxy strengths: superb load balancing (round-robin, leastconn, hash-based stickiness), robust health checks with rise/fall thresholds, active/backup failover, connection queues and rate limiting, and a battle-tested core; config is text-based and reloadable without dropping connections (exclusive mode).
- NGINX strengths: static file serving and caching (proxy_cache, FastCGI), URL rewriting and routing flexibility, TLS offload with session resumption, gzip/Brotli, and an extensive module ecosystem (Lua, auth, WAF); it doubles as the origin for static content.
- Concrete example: HAProxy in front of a database or service fleet with TCP health checks and leastconn balancing; NGINX serving the static dashboard, caching API responses, and terminating TLS; many stacks run both — NGINX as web tier, HAProxy as the L4/L7 front door.
- Failure modes: misconfigured health checks that mark healthy backends down (or vice versa), causing mass traffic shifts; reload mistakes dropping sessions (HAProxy handles reloads well; NGINX needs careful worker management); connection limits hit under load (both need tuning of file descriptors and timeouts); TLS configuration drift between proxy tiers.
- Tradeoffs: HAProxy trades web-server features for load-balancing purity and predictability; NGINX trades some balancing sophistication for breadth; the tiebreaker is operational familiarity, ecosystem, and whether caching/serving features matter.
- Operational notes: test reload paths, monitor backend health-state flaps, and keep proxy config in version control with validation in CI.
- RSIS3 relevance: whichever proxy fronts the dashboard or API, its health checks and timeouts define how RSIS3's observability sees availability — a bad check hides real failures, so checks must exercise the actual request path.

## Related
- [[wiki/devops-infra/nginx-configuration-patterns|NGINX Configuration Patterns]]
- [[wiki/devops-infra/nginx|Nginx]]
