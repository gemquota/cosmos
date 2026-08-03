---
type: "concept"
title: "Cache Poisoning"
description: "Injecting malicious content into shared caches so victims receive attacker-served responses"
tags: ["security", "caching", "http", "attacks"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---
# Cache Poisoning

## Summary
Cache poisoning plants malicious or stale content into a shared cache so many users receive it. It combines attacker-controlled input with caches that key or store responses too loosely.

## Details
Cache poisoning occurs when a shared cache (CDN, reverse proxy, browser-adjacent cache) stores a response that was influenced by attacker input and then serves it to other users. The classic web-cache poisoning chain uses unkeyed inputs — headers or parameters that the origin uses to build the response but the cache doesn't include in its cache key — so an attacker-crafted request poisons the cached copy for everyone.

The mechanism: a cache key normally includes method, URL, and sometimes headers (Accept, Host). If the origin reflects an unkeyed header (X-Forwarded-Host, X-Forwarded-Proto, or a custom header) into the page or into a redirect Location, an attacker can request the URL with a poisoned value, get the cache to store it, and every subsequent request for that URL receives the attacker's content. Cache poisoning also covers storing 200s for attacker-controllable 404s, serving stale data after purge failures, and web cache deception — caching a private response under a public URL.

Concrete example: an origin echoes X-Forwarded-Host into canonical URLs and redirects. An attacker requests / with X-Forwarded-Host: evil.example, the cache stores the poisoned response, and all visitors to / are redirected to evil.example — a full phishing or defacement primitive with one request. The fix: only trust forwarded headers from known proxies, include them in the cache key if used, and never reflect unvalidated headers.

Failure modes: CDN configurations that key on too little — ignoring auth-relevant headers or cookies — cache private data publicly; purge APIs that are unauthenticated or slow allow poisoning to persist; and caching error pages (5xx, 404 with bodies) spreads outages. Vary headers that are too broad fragment the cache; too narrow cause cross-user leakage.

Operational tradeoffs: caching is essential for cost and latency, so the goal is not to disable it but to key it precisely: cache only safe methods (GET and HEAD), include auth indicators in the key when responses vary by them, never cache responses with Set-Cookie or per-user content unless explicitly designed, and validate forwarded headers. A cache-busting deployment flow and fast purge APIs are the operational half.

RSIS3/mykb relevance: dashboard asset caching is a small-scale instance; the standing rule "what the cache key excludes is attacker-visible" transfers directly to the wiki's static hosting setup.

## Related
- [[wiki/api-protocols/web-security-owasp|Web Security (OWASP)]] — related coverage in the same cluster
- [[wiki/api-protocols/request-smuggling|Request Smuggling]] — related coverage in the same cluster
- [[wiki/api-protocols/ssrf-practice|SSRF Attacks]] — related coverage in the same cluster
- [[wiki/api-protocols/idor-web|IDOR on the Web]] — related coverage in the same cluster
- [[wiki/security-auth/ssrf-prevention|SSRF Prevention]] — related coverage in the same cluster
- [[wiki/security-auth/deserialization-attacks|Deserialization Attacks]] — related coverage in the same cluster
- [[wiki/security-auth/privilege-escalation|Privilege Escalation]] — related coverage in the same cluster
