---
type: "concept"
title: "Authoritative & Recursive Resolvers"
description: "The two resolver roles and how queries flow between them"
tags: ["dns", "resolver", "recursion", "networking"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---
# Authoritative & Recursive Resolvers

## Summary

Authoritative and recursive resolvers are the two halves of DNS: authoritative servers answer questions about zones they own; recursive resolvers walk the hierarchy on behalf of clients and cache answers. Confusing the roles causes the classic "my DNS changed but nobody sees it" failures.

## Details
- Mechanism: a recursive resolver (8.8.8.8, 1.1.1.1, your ISP's) starts at the root, follows referrals to TLD and authoritative servers, and caches the answer for the record's TTL; an authoritative server (Route 53, Cloudflare DNS, your own NSD/BIND) serves only its zones. Delegation happens via NS records and glue.
- Concrete example: changing an A record on the authoritative side is instant, but users see the old IP until caches expire — debugging means checking TTLs, not re-propagating (there is no push). Setting an NS record change requires glue updates at the parent (the registrar/registry), which is where DNSSEC keys and delegation errors live.
- Failure modes: authoritative servers that also resolve (recursion open) become amplifiers for DDoS; TTL=86400 making changes take a day; missing glue or mismatched NS at the parent breaking delegation entirely; and resolvers ignoring short TTLs, so monitoring must poll authoritative directly.
- Operational tradeoffs: run your own authoritative for control (anycast, DNSSEC) or use managed DNS for reliability; recursive caching is invisible but controls user latency — CDN-style tuning uses low TTLs for failover and higher TTLs for stability.
- RSIS3/mykb relevance: the cosmos deployment's DNS changes follow a TTL-first procedure recorded here, so the loop's release checklist staggers DNS cutovers safely.
- Monitoring: query authoritative servers directly (dig @ns) for propagation checks; resolver-side caching means user-visible results always lag TTLs.
- Security: keep recursion closed on authoritative hosts, run DNSSEC validation on resolvers, and use RPKI-aligned validation where available to blunt cache poisoning and hijacks.

## Related
- [[wiki/cloud-infra/networking-fundamentals|Networking Fundamentals]]
- [[wiki/cloud-infra/tcp-ip-stack|TCP/IP Stack]]
- [[wiki/syntheses/knowledge-acquisition-workflow|Knowledge Acquisition Workflow]]
- [[wiki/syntheses/mykb-acquisition-curation-and-practices|Acquisition, Curation & Practices]]
