---
type: "concept"
title: "DNS Fundamentals"
description: "The hierarchical naming system translating hostnames to addresses, records, and service endpoints"
tags: ["dns", "network", "infrastructure", "http", "standards"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://www.rfc-editor.org/rfc/rfc1035", "https://en.wikipedia.org/wiki/Domain_Name_System"]
---
# DNS Fundamentals

## Summary
DNS is a distributed, hierarchical database that maps names like `api.example.com` to IP addresses and service metadata. Resolvers walk the hierarchy from root to authoritative servers, caching results along the way. DNS underpins every HTTP request, load-balanced service, and CDN edge selection.

## Details
- **Record types** — A/AAAA map names to addresses; CNAME aliases names; MX routes mail; TXT carries verification and policy; SRV locates services by port.
- **Resolution flow** — a stub resolver queries recursive resolvers, which follow referrals from root to TLD to authoritative nameservers, then cache TTL-bounded answers.
- **TTL and caching** — low TTLs speed failover but increase query volume; CDNs use DNS to steer clients to nearby edges.
- **Security** — DNSSEC signs records; DoH/DoT encrypt queries; cache poisoning motivates both.
- **Worked example** — mykb's local dev uses hosts-file entries while production uses managed DNS with CNAMEs to the CDN and TXT records for verification.
- **Relevance** — RSIS3's knowledge graph can record DNS topology (CNAME chains, TTLs) as operational context for deployments.

## Related
- [[wiki/api-protocols/ipv4-vs-ipv6|IPv4 vs IPv6]] — adjacent concept in this wiki
- [[wiki/api-protocols/tcp-vs-udp|TCP vs UDP]] — adjacent concept in this wiki
- [[wiki/api-protocols/http-keep-alive|HTTP Keep-Alive]] — existing coverage
- [[wiki/api-protocols/dns-load-balancing|DNS Load Balancing]] — existing coverage
- [[wiki/api-protocols/load-balancing|Load Balancing]] — existing coverage
