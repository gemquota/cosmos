---
type: "concept"
title: "Routing & Forwarding"
description: "Routing tables, next hops, and protocols"
tags: ["routing", "forwarding", "routing-tables", "ip"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://man7.org/linux/man-pages/man8/ip-route.8.html", "https://www.rfc-editor.org/rfc/rfc1812"]
---

# Routing & Forwarding

## Summary
Routing is the process of choosing paths for packets across networks: each host and router consults a routing table and forwards each packet to the best next hop. The default route catches everything not otherwise matched.

## Details
- The routing table maps destination prefixes to next hops and interfaces; ip route show and route -n display it.
- Longest prefix match decides: the most specific route wins, so a /32 host route beats a /24, which beats the default /0.
- The default route (0.0.0.0/0) is the gateway of last resort, usually the LAN router or the container's bridge.
- A route entry needs a gateway only for non-directly-connected destinations; link-local routes resolve next hops via ARP.
- Policy routing (ip rule) adds tables beyond main: source-based routing and per-mark routing for VPNs and multi-homed hosts.
- ECMP balances across equal-cost next hops; metrics prefer lower values when multiple routes exist.
- Dynamic routing (BGP for the internet, OSPF/IS-IS inside networks) distributes routes; kernel forwarding (ip_forward) turns a host into a router.

## Related
- [[wiki/os-shell/ip-addresses-and-subnetting|IP Addressing & Subnetting]] — the prefixes routes match
- [[wiki/os-shell/nat-and-port-forwarding|NAT & Port Forwarding]] — what happens at routing boundaries
- [[wiki/os-shell/link-layer-ethernet-and-arp|Link Layer, Ethernet & ARP]] — resolving the next hop
- [[wiki/cloud-infra/peering-and-transit|Peering & Transit]] — internet-scale routing relationships
- [[wiki/os-shell/icmp-and-network-diagnostics|ICMP & Diagnostics]] — TTL errors expose routing loops
