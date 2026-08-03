---
type: "concept"
title: "IPv4 vs IPv6"
description: "Address families, exhaustion, and the practical gaps in dual-stack APIs"
tags: ["networking", "ip", "protocols", "infra"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---
# IPv4 vs IPv6

## Summary
IPv4 offers 32-bit addresses; IPv6 offers 128-bit addresses with built-in features like autoconfiguration and mandatory IPsec-era header extensions. The practical API question is dual-stack behavior: which family clients use, and how that changes logging, rate limiting, and access control.

## Details
IPv4 addresses are 32 bits (4.3 billion theoretical, far fewer usable), which is why NAT exists and why address scarcity drives proxy and carrier-grade NAT designs. IPv6 addresses are 128 bits, eliminating scarcity, and bring stateless address autoconfiguration (SLAAC), larger subnet standards (a /64 per network), and a redesigned header with no checksum and optional extension headers. The wire formats are incompatible, so coexistence uses dual-stack (both families on one host) and transition mechanisms like NAT64/DNS64.

The mechanism: a dual-stack host resolves DNS (A for IPv4, AAAA for IPv6) and prefers IPv6 when available per RFC 6724, with Happy Eyeballs (RFC 6555/8305) racing both families to avoid slow fallback. Behind the scenes, an IPv6 request may traverse completely different network paths than IPv4, and a misconfigured AAAA record or broken IPv6 path can silently degrade connectivity — the reason clients implement connection racing.

Concrete example: an API serves dual-stack. Analytics shows 30% of clients arrive over IPv6. If rate limiting keys on IP, the same NATed IPv4 user and their IPv6 self look like different clients (or worse, a shared IPv6 /64 looks like one client), skewing quotas and abuse detection. Logs must record the family, and allowlists or geo logic must handle both forms of the same entity.

Failure modes: publishing AAAA records for a host that can't route IPv6 causes connection hangs (mitigated by Happy Eyeballs); treating IPv6 as "more anonymous" breaks abuse models; storing addresses in 32-bit-only columns truncates IPv6; and DNS without AAAA (or with broken AAAA) forces everyone through NAT64 or IPv4-only paths. Security tooling that doesn't parse IPv6 literals (with brackets in URLs and port syntax) mis-handles them.

Operational tradeoffs: IPv6 requires no NAT and simplifies addressing at scale, but monitoring, firewalls, and rate limiters must be family-aware; IPv4-only operation is simpler operationally but inherits NAT-related rate-limit and geo issues. The baseline for new services: dual-stack with family-tagged logging, IPv6-compatible storage (128-bit fields or text), and rate limiting keyed on identity rather than raw address where possible.

RSIS3/mykb relevance: the wiki's hosted services would sit behind GitHub Pages' CDN; documenting the family handling (CDN terminates both, app sees one) keeps RSIS3's network notes honest about what the app actually observes.

## Related
- [[wiki/api-protocols/dns-fundamentals|DNS Fundamentals]]
- [[wiki/api-protocols/tcp-vs-udp|TCP vs UDP]]
- [[wiki/api-protocols/http-keep-alive|HTTP Keep-Alive]]
- [[wiki/api-protocols/dns-load-balancing|DNS Load Balancing]]
- [[wiki/api-protocols/load-balancing|Load Balancing]]
