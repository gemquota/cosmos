---
type: "concept"
title: "IPv6 Link-Local Addresses"
description: "fe80:: addresses used for neighbor discovery and automatic configuration"
tags: ["ipv6", "link-local", "networking", "addressing"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---
# IPv6 Link-Local Addresses

## Summary

IPv6 link-local addresses (fe80::/10) are auto-generated, scope-limited addresses every interface must have; they handle neighbor discovery, routing protocol peering, and link-local-only services without global configuration. They are the quiet workhorse of IPv6 networks.

## Details
- Mechanism: every IPv6 interface derives a link-local address (EUI-64 or privacy-stable random) from its MAC or a random token; it is only valid on the link (packets with link-local sources are not routed); neighbor discovery (NDP), SLAAC, and router advertisements use it, as do routing protocols (OSPFv3, BGP sessions over link-locals) and link-local services like mDNS.
- Concrete example: two routers peer over a point-to-point link using their link-local addresses — no global addressing needed on the transit segment; a host SLAACs its global address using RA from the router's link-local; Docker/kubernetes pods talk to gateway via fe80::1. The link-local address is stable per link, so it is often the reliable way to address a neighbor.
- Failure modes: assuming link-local addresses are globally reachable (they are not — scope matters); duplicate detection failures causing address conflicts on misconfigured links; EUI-64-based addresses exposing MAC-derived identifiers (privacy extensions exist); and filtering fe80 traffic accidentally, breaking NDP and routing peering.
- Operational tradeoffs: link-local addressing simplifies configuration (auto, no state) at the cost of conceptual confusion about scope; the operational norm is to use them for infrastructure protocols and reserve global addresses for user-facing services.
- RSIS3/mykb relevance: the wiki's IPv6 lab notes document link-local peering, so the loop's network experiments start with correct scope expectations.
- Security scope: link-local traffic cannot cross routers, so NDP and peering are inherently link-bounded; keep that scoping in mind when filtering, and never filter fe80 wholesale.
- Stability benefit: use link-local addresses for neighbor services (routers, gateways) because they are stable per link even when global addresses change.

## Related
- [[wiki/cloud-infra/ipv6-adoption|IPv6 Adoption]]
- [[wiki/cloud-infra/private-link-and-private-endpoints|Private Link & Private Endpoints]]
- [[wiki/devops-infra/local-persistent-volumes|Local Persistent Volumes]]
- [[wiki/os-shell/ip-addresses-and-subnetting|IP Addressing & Subnetting]]
- [[wiki/cloud-infra/networking-fundamentals|Networking Fundamentals]]
- [[wiki/syntheses/knowledge-acquisition-workflow|Knowledge Acquisition Workflow]]
- [[wiki/syntheses/mykb-acquisition-curation-and-practices|Acquisition, Curation & Practices]]
