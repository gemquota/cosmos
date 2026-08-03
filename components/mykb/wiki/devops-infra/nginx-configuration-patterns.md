---
type: "concept"
title: "NGINX Configuration Patterns"
description: "Server blocks, locations, upstreams, and proxy directives done right"
tags: ["nginx", "proxy", "configuration", "web"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# NGINX Configuration Patterns

## Summary
NGINX configuration patterns are the recurring structures for routing, proxying, caching, TLS, and rate limiting in an NGINX server: location blocks, upstreams, proxy_pass, include files, and maps. Well-organized configs treat NGINX as code — split by concern, validated, versioned, and tested.

## Details
- Mechanism: the config is declarative: http/server/location hierarchy; upstream blocks define backend groups with load balancing (round-robin, least_conn, ip_hash); proxy_pass forwards with header rewriting; maps transform variables; include fragments compose configs; `nginx -t` validates before reload.
- Concrete example: an upstream of app servers with health checks and least_conn; a location block proxying /api to the backend with timeouts and retry headers; a static location serving hashed assets with immutable cache headers; a rate-limit zone (limit_req) protecting login; TLS terminated with modern cipher config.
- Failure modes: location matching surprises — prefix vs regex precedence (^~, =, regex) routes traffic to the wrong handler; proxy timeouts misconfigured for slow upstreams, returning 504s; upstreams with no health checks keeping dead backends in rotation; config drift between environments; reload mistakes — a broken config blocks reload and leaves the old one running, hiding the error.
- Tradeoffs: NGINX config is powerful but imperative and easy to abuse; the pattern discipline (small includes, variables, testing) keeps it maintainable; the alternative — a gateway product with a UI or CRDs — trades control for convenience; for most teams, NGINX as code with CI validation is the sweet spot.
- Operational notes: run `nginx -t` in CI, keep config in git with environments as overlays, monitor upstream health and 5xx rates, and test reloads.
- RSIS3 relevance: the dashboard and API endpoints behind NGINX follow these patterns — correct caching, timeouts, and rate limits keep RSIS3's frontend healthy under bursty load.

## Related
- [[wiki/cloud-infra/serverless-computing-patterns|Serverless Computing Patterns]]
- [[wiki/devops-infra/configuration-management-revisited|Configuration Management]]
- [[wiki/devops-infra/haproxy-vs-nginx|HAProxy vs NGINX]]
- [[wiki/devops-infra/api-mesh-patterns|API Mesh Patterns]]
- [[wiki/syntheses/knowledge-acquisition-workflow|Knowledge Acquisition Workflow]] — how stubs grow into full articles in mykb
- [[wiki/syntheses/mykb-acquisition-curation-and-practices|Acquisition, Curation & Practices]] — the curation loop this stub belongs to
