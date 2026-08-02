---
type: "entity"
status: "growing"
title: "ACH"
description: "Cache"
tags: ["acronym", "android", "api", "ast", "auth", "authentication", "entity"]
timestamp: "2026-07-19T22:41:40Z"
resource: ""
---

## Ach 2

Cache — temporary storage of frequently accessed data for performance. Sessions show Redis caching, in-memory caches, and cache invalidation patterns.

**Related topics:** android, api, auth, authentication

**Domain:** Mobile Platform › [[wiki/mobile-platform/supercategories/android-core/index|Android Core]] › [[wiki/web-platforms/supercategories/security-auth/categories/auth-security/index|Auth Security › Ach 2

## Overview

Caching trades a bounded amount of memory for lower latency and reduced backend load by keeping frequently accessed data closer to the consumer. In the authentication context represented by this entity, caches commonly hold session records, token-derived user profiles, rate-limit counters, and expensive lookups such as permission sets or signing keys. Two placements dominate practice: in-process caches, which are fast but local to a single process, and shared caches such as Redis, which every application instance can reach.

## Cache Placement and Data

- In-memory maps or LRU structures suit small, read-heavy data that tolerates per-process staleness.
- Redis adds a shared key-value store with time-to-live values, atomic counters, and pub/sub, which fits session and rate-limit data.
- Every entry should carry an expiry so stale data cannot outlive its usefulness, and eviction policy matters under memory pressure.

## Invalidation Patterns

- Write-through updates the cache when the source of truth changes, keeping reads consistent at some write cost.
- Write-behind defers persistence for throughput but risks losing updates on crash.
- TTL-based expiry bounds staleness without explicit notification and is the simplest approach to manage.
- Explicit invalidation deletes keys on known mutations; it is precise but easy to miss when several writers touch the same data.

## Auth-Specific Use

Authentication systems cache token revocation lists, JWKS keys, and session state. Because revocation must propagate promptly, short TTLs or explicit deletion matter more than raw hit rate. A cache that serves stale credentials can become a security hole, so authentication caches favor correctness over maximal hit ratio.

## Related Concepts

- [[wiki/data-storage/entities/cache|Cache]] — the general caching model
- [[wiki/data-storage/cache-eviction-policies|Cache Eviction Policies]] — LRU, LFU, and TTL trade-offs
- [[wiki/api-protocols/redis-streams|Redis Streams]] — Redis data structures beyond plain keys
- [[wiki/frontend/browser-caching|Browser Caching]] — client-side caching behavior

## Related Entities

- [[wiki/web-platforms/supercategories/security-auth/categories/auth-security/subcategories/authentication/abuseipdb-2|Abuseipdb 2
- [[wiki/web-platforms/supercategories/security-auth/categories/auth-security/subcategories/authentication/ac-2|Ac 2
- [[wiki/web-platforms/supercategories/security-auth/categories/auth-security/subcategories/authentication/access-denied|Access Denied
- [[wiki/web-platforms/supercategories/security-auth/categories/auth-security/subcategories/authentication/actionnode-2|Actionnode 2
- [[wiki/web-platforms/supercategories/security-auth/categories/auth-security/subcategories/authentication/addressfamily|Addressfamily
- [[wiki/web-platforms/supercategories/security-auth/categories/auth-security/subcategories/authentication/aec-2|Aec 2
- [[wiki/web-platforms/supercategories/security-auth/categories/auth-security/subcategories/authentication/agentconfig|Agentconfig
- [[wiki/web-platforms/supercategories/security-auth/categories/auth-security/subcategories/authentication/agentswitchrecord|Agentswitchrecord
