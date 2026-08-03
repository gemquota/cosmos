---
type: "concept"
title: "GCP VPC & Cloud NAT"
description: "Global VPCs, firewall rules, and managed NAT for GCP"
tags: ["gcp", "vpc", "nat", "cloud"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---
# GCP VPC & Cloud NAT

## Summary

GCP VPCs are global: one network spans regions with regional subnets, firewall rules, and routes; Cloud NAT provides managed outbound internet for private instances. The global-VPC model changes subnet, peering, and NAT design compared with AWS's regional VPCs.

## Details
- Mechanism: a GCP VPC (auto or custom mode) holds regional subnets; firewall rules are global, hierarchical, and default-deny with explicit allows; Cloud NAT allocates external IPs and translates private instance egress with per-NAT IPs and port ranges; VPC peering and Shared VPC connect networks; routes are implicit per subnet with optional custom routes.
- Concrete example: a multi-region app uses one custom-mode VPC with subnets in us-central1 and europe-west1, peered with a Shared VPC for centralized egress via Cloud NAT in one region; firewall rules reference network tags and service accounts so instance groups inherit policy without per-IP rules.
- Failure modes: auto-mode VPCs running out of the fixed /20 subnets; Cloud NAT port exhaustion under heavy concurrency (scale NAT IPs and ports deliberately); firewall tag mismatches (tags applied to instances vs rules referencing tags) silently opening or closing access; and regional subnet overlap breaking peering.
- Operational tradeoffs: global VPCs simplify multi-region routing but concentrate blast radius — use Shared VPC plus hierarchical firewalls to delegate; Cloud NAT costs per hour and per GB and adds a dependency, so evaluate Private Google Access and PSC for Google-API traffic. Keep subnet plans documented before regions multiply.
- RSIS3/mykb relevance: the wiki's GCP environments use a shared-VPC + Cloud NAT baseline from this note, so loop-provisioned projects inherit egress and isolation rules.
- NAT capacity: plan Cloud NAT IPs and port ranges from peak concurrent connections; port exhaustion under autoscaling is the classic GCP egress outage.

## Related
- [[wiki/cloud-infra/cloud-providers-aws-azure-gcp|Cloud Providers: AWS, Azure, GCP]]
- [[wiki/os-shell/nat-and-port-forwarding|NAT & Port Forwarding]]
- [[wiki/cloud-infra/cloud-security-groups|Cloud Security Groups]]
- [[wiki/cloud-infra/aws-vpc-design|AWS VPC Design]]
- [[wiki/syntheses/knowledge-acquisition-workflow|Knowledge Acquisition Workflow]]
- [[wiki/syntheses/mykb-acquisition-curation-and-practices|Acquisition, Curation & Practices]]
