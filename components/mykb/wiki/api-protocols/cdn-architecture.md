---
type: "concept"
title: "CDN Architecture"
description: "Distributed edge caching and delivery networks that bring content closer to users"
tags: ["cdn", "caching", "performance", "network", "infrastructure"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://en.wikipedia.org/wiki/Content_delivery_network", "https://developer.mozilla.org/en-US/docs/Glossary/CDN"]
---
# CDN Architecture

## Summary
A content delivery network replicates static and dynamic content across edge servers worldwide. Clients hit the nearest edge, cutting latency and offloading origin traffic. CDNs also provide TLS termination, DDoS absorption, and edge compute.

## Details
- **Anycast and DNS steering** — DNS or BGP anycast routes each client to the closest edge; cache keys, TTLs, and purging control freshness.
- **Cacheability** — Cache-Control and Vary decide what edges may store; purging invalidates stale content after deploys.
- **Edge features** — image resizing, compression, HTTP/3, WAF rules, and workers/edge functions run near the user.
- **Origin protection** — edges shield origins from load and attacks; origin pull keeps content fresh.
- **Worked example** — the mykb wiki could be served as static files from a CDN with the API behind a gateway; the wiki records cache headers and purge flows for the deployment.
- **Relevance** — RSIS3's fetch-heavy pipeline benefits from CDN-cached sources and predictable edge latency.

## Related
- [[wiki/web-platforms/dns-prefetch|DNS Prefetch]] — adjacent concept in this wiki
- [[wiki/web-platforms/preconnect-practice|Preconnect Practice]] — adjacent concept in this wiki
- [[wiki/web-platforms/preload-practice|Preload Practice]] — adjacent concept in this wiki
- [[wiki/web-platforms/link-rel-attributes|Link rel Attributes]] — adjacent concept in this wiki
- [[wiki/api-protocols/http-caching|HTTP Caching]] — existing coverage
- [[wiki/api-protocols/load-balancing|Load Balancing]] — existing coverage
- [[wiki/api-protocols/dns-load-balancing|DNS Load Balancing]] — existing coverage
