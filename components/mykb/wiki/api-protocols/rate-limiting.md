---
type: "concept"
title: "Rate Limiting"
description: "Controlling how many requests a client may make in a window to protect APIs from abuse and overload"
tags: ["rate-limiting", "api", "security", "scaling", "http"]
timestamp: "2026-07-31T00:00:00Z"
status: "growing"
source: ["https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/429"]
---

# Rate Limiting

## Summary
Rate limiting caps how many requests a client can issue within a time window, protecting APIs from abuse, credential-stuffing, and accidental overload. Servers enforce limits per API key, IP, or account tier and signal exhaustion with HTTP 429 Too Many Requests plus retry headers. It is a prerequisite for public APIs, LLM providers, and any shared infrastructure.

## Details
- Fixed window, sliding window, token bucket, and leaky bucket are the main algorithms; token bucket (burst-tolerant) is the most common.
- Headers: `RateLimit-Limit`, `RateLimit-Remaining`, `RateLimit-Reset`, and `Retry-After` tell clients when they may retry.
- Client behavior: honor `Retry-After`, back off exponentially, and add jitter to avoid synchronized retry storms.
- Distributed enforcement uses Redis counters or gateway middleware (Envoy, Nginx, Cloudflare) so limits hold across instances.
- Worked example: the mykb daemon should rate-limit its own outbound embedding calls to the LLM API, treating 429s as schedule hints rather than errors.
- Relationship to quality: rate limits pair with caching — good caching reduces the request rate that limits must absorb.

## Related
- [[wiki/api-protocols/retry-backoff|Retry & Backoff]] — correct behavior after a 429
- [[wiki/api-protocols/http-caching|HTTP Caching]] — fewer origin requests, less limiting pressure
- [[wiki/api-protocols/circuit-breaker|Circuit Breaker]] — stops hammering a failing downstream
- [[wiki/security/oauth2|OAuth 2.0]] — token-based identity lets limits attach to principals
- [[wiki/devops-infra/envoy|Envoy]] — gateway-level rate limit filters
- [[wiki/concepts/mykb-analysis|Mykb Analysis]] — daemon calls to embedding APIs need budgets
- [[wiki/concepts/triad-architecture|Triad Architecture]] — rate budgets for the daemon bridge
