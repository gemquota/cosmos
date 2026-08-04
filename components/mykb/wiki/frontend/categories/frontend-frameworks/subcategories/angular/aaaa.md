---
type: "entity"
title: "AAAA"
description: "AAAA: IPv6 address records and their role in DNS resolution"
tags: ["entity", "acronym", "ajax", "android", "angular", "api", "ipv6", "dns"]
timestamp: "2026-07-19T22:41:42Z"
resource: ""
---

# AAAA

## Summary

AAAA is the frontend entity for the IPv6 AAAA DNS record type, which maps hostnames to 128-bit IPv6 addresses. It complements the A record's IPv4 role and is essential as networks migrate to IPv6. It matters because connectivity failures often trace to missing or incorrect AAAA records. Understanding record types turns DNS from a mystery into a debuggable system.

## Details

- **Definition** — An AAAA record associates a domain name with an IPv6 address, analogous to how an A record associates it with IPv4.
- **Resolution flow** — Resolvers query AAAA alongside A records and choose an address family based on network capability and policy.
- **Dual stack** — Most services publish both record types so clients on either protocol family can connect.
- **Failure modes** — Missing AAAA records strand IPv6-only clients; stale records send traffic to dead addresses with no fallback.
- **Debugging** — DNS lookup tools reveal which record types exist and what address family a host resolves to.
- **Worked example** — A web app's host has an AAAA record pointing at its IPv6 address; an IPv6-only mobile client connects without translation.
- **Practical relevance** — Frontend tooling that hits APIs over IPv6 depends on correct records, so DNS hygiene is part of app reliability.
- **Operational notes** — Record TTLs control how quickly changes propagate, balancing failover speed against resolver load.
- **Propagation** — DNS changes propagate according to TTLs, so planned AAAA updates need lead time.
- **Fallback behavior** — Clients attempt address families in order; broken records cause timeouts that fallback masks.
- **Verification** — Lookup and connectivity checks after changes confirm records before relying on them.
- **Monitoring** — DNS health checks that verify resolution and reachability catch record rot before users do.

## Related

- [[wiki/frontend/categories/frontend-frameworks/subcategories/angular/addr|ADDR]] — address resolution and addressing
- [[wiki/frontend/categories/frontend-frameworks/subcategories/angular/area|AREA]] — cluster acronym neighbor
- [[wiki/frontend/categories/frontend-frameworks/subcategories/angular/build|BUILD]] — deployment target connectivity
- [[wiki/frontend/categories/frontend-frameworks/subcategories/angular/00-index|Angular Index]] — cluster index page
