---
type: "concept"
title: "DNS over HTTPS"
description: "Encrypting DNS queries inside HTTPS to resist snooping and injection"
tags: ["dns", "https", "privacy", "security"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---
# DNS over HTTPS

## Summary

DNS-over-HTTPS (DoH) encrypts DNS queries inside HTTPS, hiding them from network observers and preventing on-path tampering. It is the mainstream encrypted-DNS protocol (with DoT for the transport layer), and it changes enterprise filtering and ISP visibility.

## Details
- Mechanism: the client sends DNS queries to a DoH resolver (Cloudflare 1.1.1.1, Google 8.8.8.8, NextDNS, or a private resolver) over HTTP/2 or HTTP/3; responses come back inside TLS, so intermediaries see only the resolver hostname. DoT wraps DNS in TLS on port 853; both address the same threat (DNS spoofing, snooping) with different operational profiles.
- Concrete example: a user on airport Wi-Fi resolves through DoH and an attacker cannot inject fake DNS answers or log the domains; a company with compliance filtering must either deploy its own DoH resolver or block third-party DoH endpoints to keep DNS policy enforced; browsers negotiate DoH with fallback to plain DNS when the resolver fails.
- Failure modes: DoH breaking split-horizon and local resolution (intranet names fail when queries go to public resolvers — enterprise deployments must route private names separately); blocking all DoH also breaking legit services that rely on it; performance overhead of a second connection unless connection reuse applies; and misconfigured resolvers leaking metadata despite encryption.
- Operational tradeoffs: DoH buys privacy and integrity at the cost of visibility (for ISPs and enterprises) and a small dependency on the resolver provider; browsers now bundle DoH, so networks that filter must actively manage it rather than ignore it.
- RSIS3/mykb relevance: the wiki's admin tooling uses a private DoH resolver for internal names; this note records the resolver policy and fallbacks the loop must preserve.
- Enterprise path: run a private DoH resolver for split-horizon names and enforce it via policy; blocking public DoH without a replacement breaks both privacy and filtering.

## Related
- [[wiki/cloud-infra/dns-resolution-process|DNS Resolution Process]]
- [[wiki/cloud-infra/https-and-tls|HTTPS & TLS]]
- [[wiki/cloud-infra/dns-zone-transfers|DNS Zone Transfers]]
- [[wiki/cloud-infra/split-horizon-dns|Split-Horizon DNS]]
- [[wiki/syntheses/knowledge-acquisition-workflow|Knowledge Acquisition Workflow]]
- [[wiki/syntheses/mykb-acquisition-curation-and-practices|Acquisition, Curation & Practices]]
