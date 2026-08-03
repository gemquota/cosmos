---
type: "concept"
title: "Subnet Design"
description: "Dividing VPC address space into subnets for availability, tiers, and routing control"
tags: ["subnets", "vpc", "networking", "cloud"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
---
# Subnet Design

## Summary

Subnet design carves VPC address space into functional segments — public, private, data, management — sized for growth and aligned to availability zones. It is the foundation decision of cloud networking: CIDR choices outlive most other design decisions.

## Details
- Mechanism: a VPC CIDR (e.g. 10.0.0.0/16) is split into subnets per AZ and tier (public/private/data); route tables attach per subnet; sizes are planned with headroom (never run a subnet to 100%); IPAM documents the plan; reserved addresses (cloud platforms reserve the first few per subnet) and future growth drive the math.
- Concrete example: three AZs × (public 10.0.x.0/24, app 10.0.x.0/23, db 10.0.x.0/24) gives room to grow app tiers without renumbering; a /16 subdivided to /23s leaves space for new tiers (cache, worker) without a new VPC; a misplanned /28 for a future fleet forces a redesign exactly when it is most painful.
- Failure modes: CIDR collisions with on-prem/peered networks (renumbering is catastrophic — plan the whole space first); uneven AZ sizing (one AZ exhausted); single-tier-per-AZ assumptions broken by multi-AZ deployments; and subnet sprawl without an IPAM record, so no one knows what is free.
- Operational tradeoffs: bigger subnets buy flexibility at negligible cost (unused IPs are free); the trade is broadcast/management scale in theory, rarely in practice. The standard: document the plan, reserve headroom, align tiers to AZs, and treat the CIDR map as immutable after launch.
- RSIS3/mykb relevance: the wiki's VPC templates would ship with a documented CIDR map; this note records the plan so the loop's new environments never overlap existing ranges.
- Security segmentation: data-plane subnets should be private with egress via NAT/endpoints; keep management paths (bastion, VPN) on their own subnet for tighter NACLs.
- Future-proofing: reserve a contiguous block for new AZs and tiers in the IPAM plan so the next environment never renumbers an existing VPC.

## Related
- [[wiki/cloud-infra/vpc-networking|VPC Networking]] — the parent network subnets divide
- [[wiki/cloud-infra/nat-gateways|NAT Gateways]] — egress from private subnets
- [[wiki/cloud-infra/virtual-machines|Virtual Machines]] — instances placed by subnet tier
