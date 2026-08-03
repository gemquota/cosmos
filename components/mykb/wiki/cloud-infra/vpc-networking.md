---
type: "concept"
title: "VPC Networking"
description: "Private virtual networks in the cloud: CIDR ranges, subnets, routing, and isolation"
tags: ["vpc", "networking", "cloud", "security"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
---
# VPC Networking

## Summary

VPC networking is the umbrella discipline over CIDR planning, subnets, routing, gateways, DNS, and security in cloud private networks. It is where most cloud security and availability incidents originate — and where careful up-front design pays off for years.

## Details
- Mechanism: a VPC (AWS/Azure) or project network (GCP) owns a private CIDR, subdivided into subnets per AZ/tier; route tables direct traffic (local, internet via IGW/NAT, peered, transit); DNS (private hosted zones) resolves internal names; security groups/NACLs/firewalls enforce policy. All cloud services hang off this fabric: instances, LB, databases, serverless.
- Concrete example: a three-tier app in a VPC with public subnets for LBs, private app subnets with NAT egress, and data subnets with no egress; private hosted zones resolve app.internal; flow logs feed security analysis. The failure pattern: organic growth without a plan — overlapping CIDRs, no headroom, ad-hoc rules — that makes every future change risky.
- Failure modes: CIDR collisions that block peering/hybrid; subnet exhaustion in one AZ; routing asymmetries (NAT on one path only); DNS split-horizon mistakes; and security drift from console edits bypassing review.
- Operational tradeoffs: centralized network teams with standardized templates scale better than per-team ad-hoc VPCs; the trade is bureaucracy vs isolation. The standard is a documented plan (CIDR map, route conventions, DNS policy), IaC-managed networks, and flow-log-backed visibility.
- RSIS3/mykb relevance: the wiki's network blueprints encode these conventions; this node is the entry point the loop uses when designing new environments.
- Visibility: flow logs per subnet and VPC metrics (packet drop, rejected traffic) are the minimum observability; add them before workloads, not after incidents.
- Lifecycle: network changes are high-blast-radius — require peer review and IaC diffs, and keep a rollback plan (previous route table, prior SG set) for every change.

## Related
- [[wiki/cloud-infra/dns-management|DNS Management]] — private DNS in the VPC
- [[wiki/cloud-infra/virtual-machines|Virtual Machines]] — compute placed inside VPCs
- [[wiki/infrastructure/network-policy|Network Policy]] — in-cluster complement to VPC rules
