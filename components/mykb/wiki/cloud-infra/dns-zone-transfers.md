---
type: "concept"
title: "DNS Zone Transfers"
description: "AXFR/IXFR replication between authoritative name servers"
tags: ["dns", "zone-transfer", "axfr", "networking"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---
# DNS Zone Transfers

## Summary

DNS zone transfers (AXFR/IXFR) replicate a zone from a primary to secondary nameservers: AXFR sends the whole zone, IXFR only changes. They are how multi-server DNS stays consistent — and a classic information-leak and poisoning vector when left open.

## Details
- Mechanism: the primary sends the zone (AXFR) or incremental deltas (IXFR) to secondaries that request it with a matching TSIG key or allow-list; secondaries then answer authoritatively. Anycast or load-balanced secondaries spread query load and add resilience; serial numbers (SOA) coordinate freshness.
- Concrete example: a zone hosted on two nameservers syncs via IXFR every few minutes so record changes propagate without manual copying; a monitoring tool triggers an alert when secondary serial lags the primary. Misconfigured servers that allow anonymous AXFR let anyone dump every hostname — reconnaissance gold for attackers.
- Failure modes: open AXFR leaking internal hostnames (always restrict by IP/TSIG); TSIG keys mishandled (shared, unrotated) enabling zone injection; SOA serials that never advance, silently desyncing secondaries; and transfer failures during DNS cutovers causing stale answers at the exact moment of change.
- Operational tradeoffs: managed DNS (Route 53, Cloudflare) hides transfers behind the provider; self-hosted DNS needs disciplined allow-lists, TSIG, and monitoring. Prefer managed DNS where compliance cost is low, and document the transfer policy when self-hosting.
- RSIS3/mykb relevance: the cosmos DNS self-hosting notes record the TSIG and allow-list policy here, so the loop's nameserver changes do not open transfers.
- Hidden primary pattern: keep the authoritative primary unreachable from the internet (private or firewalled) so secondaries are the only public nameservers — a standard hardening that also simplifies TSIG key distribution.
- Transfer monitoring: alert on serial lag and on failed transfers; a secondary silently serving stale records is worse than an outage because it is invisible until users hit it.

## Related
- [[wiki/cloud-infra/dns-resolution-process|DNS Resolution Process]]
- [[wiki/cloud-infra/availability-zone-architectures|Availability Zone Architectures]]
- [[wiki/cloud-infra/dns-over-https|DNS over HTTPS]]
- [[wiki/cloud-infra/split-horizon-dns|Split-Horizon DNS]]
- [[wiki/syntheses/knowledge-acquisition-workflow|Knowledge Acquisition Workflow]]
- [[wiki/syntheses/mykb-acquisition-curation-and-practices|Acquisition, Curation & Practices]]
