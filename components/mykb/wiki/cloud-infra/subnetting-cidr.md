---
type: "concept"
title: "Subnetting & CIDR"
description: "Prefix math that carves networks into addressable subnets"
tags: ["subnet", "cidr", "addressing", "networking"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: [
  "https://www.rfc-editor.org/rfc/rfc4632",
  "https://www.rfc-editor.org/rfc/rfc1519",
]
---

# Subnetting & CIDR

## Summary
Subnetting divides IP address space with prefix-length notation, and CIDR made that notation the universal standard. Every VPC, firewall rule, and routing table in cloud infrastructure is expressed in CIDR form. Prefix math is a daily skill for infrastructure engineers.

## Details
- CIDR (RFC 4632) expresses a network as address plus prefix length, such as 10.0.0.0/16, replacing classful addressing.
- The prefix length determines the number of hosts: 2^(32-prefix) addresses per subnet, minus network and broadcast addresses for IPv4.
- Subnetting creates hierarchy: a /16 can be split into /24s, letting routing aggregate routes and reducing table size.
- Cloud VPCs require planning: each subnet maps to an availability zone, and reserved addresses are consumed by gateways and load balancers.
- Misplanning causes exhaustion: too-small subnets block autoscaling, overlapping CIDRs block peering and VPNs.
- IPv6 subnetting is simpler because a /64 per subnet is the norm, leaving no host-count arithmetic.
- Provider consoles and CLI workflows differ, so the provider-specific articles in this cluster record the concrete steps and gotchas.

## Related
- [[wiki/cloud-infra/dns-over-https|DNS over HTTPS]]
- [[wiki/cloud-infra/anycast-routing|Anycast Routing]]
- [[wiki/os-shell/ip-addresses-and-subnetting|IP Addressing & Subnetting]]
- [[wiki/cloud-infra/autoscaling|Autoscaling]]
