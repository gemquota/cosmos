---
type: "concept"
title: "AWS VPC Design"
description: "Subnets, route tables, IGW, and NAT layout for production AWS networks"
tags: ["vpc", "aws", "networking", "cloud"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---
# AWS VPC Design

## Summary

AWS VPC design turns a flat network into a structured set of subnets, routes, and gateways: public/private tiers, NAT for egress, peering/transit for connectivity, and security groups as the enforcement layer. Good design keeps blast radius small and growth cheap.

## Details
- Mechanism: a VPC is an isolated CIDR block (e.g. 10.0.0.0/16); subnets carve it per AZ; route tables decide egress (IGW for public, NAT for private egress, transit gateway for hub traffic); security groups filter at the instance level, NACLs at the subnet level. Design decisions: subnet size planning (reserve space), AZ spread, and where shared services live — leave roughly 50% headroom per AZ for growth.
- Concrete example: a three-tier app uses public subnets for load balancers and NAT, private subnets for app servers and databases, each service in its own security group referenced by group ID — so the app SG allows 443 from the LB SG only; peering/transit connects to shared services without overlapping CIDRs.
- Failure modes: CIDR collisions with on-prem or peered networks; running out of IP space in an AZ (reserve headroom); single-AZ dependencies hidden by spread-out subnets; SG rules that reference IPs instead of groups (drift); and centralizing everything through a transit hub until bandwidth/latency suffers.
- Operational tradeoffs: per-team VPCs isolate blast radius but multiply overhead; a shared landing zone with clearly delegated subnets scales better. Prefer security groups as the primary filter, NACLs as a coarse second layer, and document CIDR reservations before they fill up.
- RSIS3/mykb relevance: experiment environments get disposable VPCs from a shared template; this note records the CIDR/route conventions the loop's provisioning tooling reuses.
- Documentation: maintain a CIDR map and subnet manifest as code; the network plan is the contract every future peering and migration reads. Include planned growth in the map, since retrofitting CIDR space after exhaustion is a migration, not an edit.

## Related
- [[wiki/os-shell/filesystem-design|Filesystem Design]]
- [[wiki/cloud-infra/cloud-providers-aws-azure-gcp|Cloud Providers: AWS, Azure, GCP]]
- [[wiki/cloud-infra/gcp-vpc-and-cloud-nat|GCP VPC & Cloud NAT]]
- [[wiki/cloud-infra/vpc-peering-and-transit-gateways|VPC Peering & Transit Gateways]]
