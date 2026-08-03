---
type: "concept"
title: "VPN Split Tunneling"
description: "Sending only some traffic through the VPN tunnel"
tags: ["VPN", "tunneling", "routing", "security"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---
# VPN Split Tunneling

## Summary

Split tunneling routes only specified traffic through the VPN while the rest uses the local internet; full tunneling sends everything through the VPN. Split saves bandwidth and latency; full tunneling centralizes inspection and compliance. The choice is a security-vs-performance policy.

## Details
- Mechanism: client VPN configs carry route lists: split lists internal ranges (10.0.0.0/8) through the tunnel, leaving everything else local; full tunnel sets 0.0.0.0/0 (and IPv6) through the VPN with default-route injection. DNS handling matters: split configs should send only internal domains to the VPN resolver to avoid DNS leaks.
- Concrete example: a developer VPN splits out only the internal CIDR — video calls and web browsing stay local, fast; a regulated team forces full tunnel so all egress passes through the corporate filter and logs; a misconfigured split tunnel leaks internal DNS or routes, sending confidential lookups to the ISP resolver.
- Failure modes: DNS leaks (queries for internal names going to public resolvers); split-route gaps (a new internal subnet not in the list breaks access); full-tunnel performance complaints (all traffic hairpins through HQ); and policy bypass when users can toggle tunneling or the client is not enforced.
- Operational tradeoffs: split tunneling is the UX and performance winner for general use; full tunneling is the compliance winner where inspection is mandatory. The middle path: split by default with enforced full-tunnel profiles for sensitive roles, and DNS explicitly scoped in both.
- RSIS3/mykb relevance: the wiki's admin VPN would split out only management ranges with scoped DNS; this note records the route/DNS policy the loop checks when access issues surface.
- Policy enforcement: manage split/full tunneling through the client configuration and prevent user overrides where compliance requires inspection; a toggle is a policy bypass. Document the split route list wherever it changes, since a missing subnet is an outage that looks like DNS, and verify the client route table after every profile update.

## Related
- [[wiki/cloud-infra/vpn-technologies|VPN Technologies]]
- [[wiki/cloud-infra/site-to-site-vpn|Site-to-Site VPN]]
- [[wiki/cloud-infra/client-vpn-profile|Client VPN Profiles]]
- [[wiki/cloud-infra/vpn-tunnels|VPN Tunnels]]
- [[wiki/cloud-infra/networking-fundamentals|Networking Fundamentals]]
