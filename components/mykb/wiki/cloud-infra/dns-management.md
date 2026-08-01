---
type: "concept"
title: "DNS Management"
description: "Operating the domain name system: zones, record types, TTLs, routing policies, and DNSSEC for production domains"
tags: ["dns", "domains", "routing", "network", "rfc1035"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://www.rfc-editor.org/rfc/rfc1035"]
---

# DNS Management

## Summary
DNS translates human-readable names into IP addresses and is the first hop of nearly every request, so its correctness and speed shape availability and latency. Managing DNS means owning zones, records, TTLs, and routing policies — from simple A records to failover and geo-aware resolution. Standards like RFC 1035 define the protocol that every resolver and server implements.

## Details
- Record types: A/AAAA (addresses), CNAME (aliases), MX (mail), TXT (verification and SPF/DKIM), NS and SOA (zone authority) — each serves a distinct purpose in production zones.
- Zones are delegated from parent domains; the SOA and NS records at the apex define authority, and TTLs on records control how long resolvers cache answers.
- Propagation is a caching phenomenon: lowering TTL before a change shortens the window of stale answers, then raising it back reduces resolver load.
- Managed DNS adds routing policies: weighted, latency-based, geolocation, and health-checked failover — the glue for multi-region and active-passive setups.
- DNSSEC signs zone data so resolvers can verify answers, preventing cache poisoning; it adds key management overhead and must be coordinated with the registrar.
- Worked example: mykb's wiki domain could use a CNAME for www, an MX for mail, TXT for verification, and an A record with a 60-second TTL behind the CDN for fast failover.
- Tools: Cloudflare DNS and Let's Encrypt's DNS-01 challenges pair well; certbot and TLS records (CAA) tighten the certificate lifecycle.

## Related
- [[wiki/cloud-infra/latency-optimization|Latency Optimization]] — DNS TTLs and resolver choice affect latency
- [[wiki/cloud-infra/vpc-networking|VPC Networking]] — private DNS inside cloud networks
- [[wiki/cloud-infra/peering-and-transit|Peering and Transit]] — how networks exchange routes beyond DNS
- [[wiki/devops-infra/cloudflare|Cloudflare]] — managed DNS and edge routing
- [[wiki/security/lets-encrypt|Let's Encrypt]] — DNS-01 challenges for certificate issuance
- [[wiki/security/tls|TLS]] — records like CAA that govern certificates
