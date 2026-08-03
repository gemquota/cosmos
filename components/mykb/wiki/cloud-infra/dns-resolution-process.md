---
type: "concept"
title: "DNS Resolution Process"
description: "From resolver to authoritative server: how names become addresses"
tags: ["dns", "resolution", "networking", "protocol"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: [
  "https://www.rfc-editor.org/rfc/rfc1035",
  "https://www.rfc-editor.org/rfc/rfc8499",
]
---

# DNS Resolution Process

## Summary
DNS resolution turns human-readable names into the addresses applications can use. A query walks from a stub resolver through recursive resolvers to authoritative servers, caching at every step. This process is invisible to users but critical to nearly every request on the Internet.

## Details
- A stub resolver (in the OS or application) sends a recursive query to a configured resolver, typically provided by DHCP.
- The recursive resolver follows the delegation chain: root servers, then TLD servers, then the authoritative server for the zone, using NS records to navigate.
- RFC 1035 defines the original DNS message format; RFC 8499 clarifies the modern terminology of resolvers, zones, and caching.
- Answers are cached with TTLs, which is why DNS changes propagate slowly and why short TTLs are used ahead of migrations.
- The process adds the first network latency to most connections, which is why DNS performance, pre-resolution, and CDN-based answers matter.
- Failures cascade: a broken resolver, a poisoned cache, or a missing zone file each produces a distinct symptom pattern worth documenting in runbooks.

## Related
- [[wiki/os-shell/path-resolution|Path Resolution]]
- [[wiki/cloud-infra/dns-over-https|DNS over HTTPS]]
- [[wiki/os-shell/dns-resolution|DNS Resolution]]
- [[wiki/cloud-infra/dns-management|DNS Management]]
