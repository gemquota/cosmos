---
type: "entity"
title: "CACHE"
status: "growing"
description: "Cache"
tags: ["entity", "acronym", "android", "api", "ast", "auth"]
timestamp: "2026-07-19T22:41:41Z"
resource: ""
---

## Cache

Cache — temporary storage of frequently accessed data for performance. Sessions show Redis caching, in-memory caches, and cache invalidation patterns.

**Related topics:** android, api, auth

**Domain:** Mobile Platform › [[wiki/web-platforms/index|Android Core]] › [[wiki/web-platforms/index|Api Clients › Cache

## Overview

Caching stores frequently accessed data in a faster tier so repeated reads avoid expensive computation or slow backends. Sessions have exercised Redis caching, in-memory caches, and invalidation patterns. A cache's value depends on the read/write ratio, the cost of misses, and how tightly the application can tolerate staleness; the same mechanism that accelerates a hot path can silently serve stale data if expiration and invalidation are not designed deliberately.

## Cache Topologies

- In-process caches (per node) are fastest but duplicated across instances and lost on restart.
- Distributed caches such as Redis centralize state, support TTLs, and can back multiple services.
- Client and CDN caches sit closest to the user and rely on HTTP cache headers and validators.
- Popular policies include LRU and LFU eviction, TTL-based expiration, and cache-aside or write-through population strategies.

## Failure and Consistency

- Cache stampede occurs when many requests miss simultaneously; protect with locks or single-flight requests.
- Invalidate on write where consistency matters, and accept eventual consistency where it does not.
- Monitor hit rate and miss latency, and rehearse what happens when the cache tier goes down.

## Related Concepts

- [[wiki/api-protocols/http-caching|HTTP Caching]] — browser and CDN caching semantics
- [[wiki/api-protocols/redis-streams|Redis Streams]] — the distributed cache/data structure server seen in sessions
- [[wiki/api-protocols/circuit-breaker|Circuit Breaker]] — guarding callers when the backend degrades


## Practical Guidance

- Start with the slowest repeated query or computation and cache that; profile before adding layers.
- Measure the cache's value by miss cost and hit rate, and re-tune TTLs as traffic patterns change.
- Version cache keys when the schema or serialization changes so old data does not leak into new code paths.


## Related Entities

- [[wiki/web-platforms/supercategories/api-services/categories/api-rest/subcategories/rest-api/aap-2|Aap 2
- [[wiki/web-platforms/supercategories/api-services/categories/api-rest/subcategories/rest-api/aar|Aar
- [[wiki/web-platforms/supercategories/api-services/categories/api-rest/subcategories/rest-api/aarrr|Aarrr
- [[wiki/web-platforms/supercategories/api-services/categories/api-rest/subcategories/rest-api/abi|Abi
- [[wiki/web-platforms/supercategories/api-services/categories/api-rest/subcategories/rest-api/accr-2|Accr 2
- [[wiki/web-platforms/supercategories/api-services/categories/api-rest/subcategories/rest-api/ace-core|Ace Core
- [[wiki/web-platforms/supercategories/api-services/categories/api-rest/subcategories/rest-api/acid|Acid
- [[wiki/web-platforms/supercategories/api-services/categories/api-rest/subcategories/rest-api/acli|Acli
