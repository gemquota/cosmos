---
type: "concept"
title: "Subnet Design"
description: "Dividing VPC address space into subnets for availability, tiers, and routing control"
tags: ["subnets", "vpc", "networking", "cloud"]
timestamp: "2026-08-01T00:00:00Z"
status: "stub"
---

# Subnet Design

## Summary
Subnet design splits a VPC's CIDR into smaller ranges so different tiers of infrastructure get distinct routing, security, and failure behavior.

## Details
- Tiers: public subnets host load balancers and gateways; private subnets hold application and data layers with no direct internet route.
- Place one subnet per availability zone to keep each tier multi-AZ and resizable.
- Reserve address space for growth (databases, new services) before you need it; renumbering is painful.
- Open questions: subnet size policy, NAT placement per AZ, and IPv6 planning.

## Related
- [[wiki/cloud-infra/vpc-networking|VPC Networking]] — the parent network subnets divide
- [[wiki/cloud-infra/nat-gateways|NAT Gateways]] — egress from private subnets
- [[wiki/cloud-infra/virtual-machines|Virtual Machines]] — instances placed by subnet tier
