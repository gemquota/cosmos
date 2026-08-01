---
type: "concept"
title: "NAT Gateways"
description: "Managed network address translation that gives private resources outbound internet access without inbound exposure"
tags: ["nat", "networking", "egress", "cloud"]
timestamp: "2026-08-01T00:00:00Z"
status: "stub"
---

# NAT Gateways

## Summary
A NAT gateway lets instances in private subnets reach the internet for updates and outbound calls while keeping them unreachable from outside.

## Details
- NAT translates private source IPs to a public IP, so outbound works and inbound connections cannot be initiated.
- Managed NAT gateways are highly available but cost per hour plus per-GB data processing; a single gateway is a bottleneck and SPOF.
- Place one per availability zone to avoid cross-AZ traffic and zonal failure.
- Alternatives: NAT instances, egress-only gateways for IPv6, and private-link-style endpoints for specific services.

## Related
- [[wiki/cloud-infra/subnet-design|Subnet Design]] — private subnets need NAT
- [[wiki/cloud-infra/vpc-networking|VPC Networking]] — routing context for NAT
- [[wiki/cloud-infra/virtual-machines|Virtual Machines]] — the workloads that need egress
