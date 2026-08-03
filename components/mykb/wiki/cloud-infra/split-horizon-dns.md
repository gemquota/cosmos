---
type: "concept"
title: "Split-Horizon DNS"
description: "Serving different answers for internal and external clients"
tags: ["dns", "split-horizon", "networking", "internal"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---
# Split-Horizon DNS

## Summary

Split-horizon DNS serves different answers for the same name depending on where the query comes from — internal users get private IPs, external users get public ones. It enables NAT traversal, internal service naming, and privacy, but its failure modes are the classic "works in the office, breaks from home" bugs.

## Details
- Mechanism: the same zone (example.com) is served differently by an internal resolver (10.x addresses, internal services) vs public authoritative DNS (public IPs); implementations include separate views in BIND, cloud split-horizon (AWS Route 53 private hosted zones, Azure private DNS zones), or separate zones for internal names (internal.example.com).
- Concrete example: an app resolves api.example.com to a private IP on the office network and the public IP externally; a VPC private hosted zone overrides public resolution for resources inside the VPC so database calls stay internal; an employee at home hits the public endpoint through the VPN, which routes correctly.
- Failure modes: overlapping zones shadowing each other (the wrong resolver wins); a private zone that forgets to include public names, breaking external access from inside; cache poisoning between views when resolvers are shared; and split-brain documentation where the internal and public records diverge silently.
- Operational tradeoffs: split-horizon buys clean internal naming and traffic containment at the cost of operational complexity — every record exists twice, and resolver selection decides which view users get. Keep views in sync (pipeline), test from both sides, and document which resolver each network uses.
- RSIS3/mykb relevance: the wiki's VPC uses private hosted zones with split views; this note records the sync procedure the loop follows when records change.
- Synchronization: generate internal and external views from the same source of truth; manual dual maintenance is how the two views diverge. Add a drift check that compares both views after every zone edit.

## Related
- [[wiki/cloud-infra/dns-resolution-process|DNS Resolution Process]]
- [[wiki/cloud-infra/dns-over-https|DNS over HTTPS]]
- [[wiki/cloud-infra/vpn-split-tunneling|VPN Split Tunneling]]
- [[wiki/cloud-infra/dns-management|DNS Management]]
- [[wiki/cloud-infra/networking-fundamentals|Networking Fundamentals]]
