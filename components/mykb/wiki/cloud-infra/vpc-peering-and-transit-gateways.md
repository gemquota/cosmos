---
type: "concept"
title: "VPC Peering & Transit Gateways"
description: "Connecting VPCs directly or through central transit routing"
tags: ["vpc", "peering", "transit", "networking"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---
# VPC Peering & Transit Gateways

## Summary

VPC peering connects two VPCs directly; transit gateways connect many through a hub. Peering is simple and free but non-transitive (a-b-c does not connect a-c); transit gateways centralize routing, inspection, and inter-region connectivity at a cost and complexity premium.

## Details
- Mechanism: peering is a private connection between two VPCs with mutually added routes (non-transitive, per-pair); transit gateways (AWS TGW, Azure virtual WAN, GCP via shared VPC/cloud routers) route between many attachments (VPCs, VPN, Direct Connect, inter-region) with route tables and inspection attachment points.
- Concrete example: two VPCs that share a database peer directly — cheap and simple; ten VPCs needing a shared service hub use a transit gateway so each spoke peers once with the hub; a security requirement to inspect all east-west traffic routes everything through a firewall attachment on the TGW.
- Failure modes: CIDR overlap between peered VPCs (routes conflict or vanish); forgetting that peering is non-transitive and routing breaks at the third hop; TGW route-table misconfiguration black-holing spokes; and cost/bandwidth surprises — inter-region TGW traffic bills, and hub architectures concentrate failure and bandwidth.
- Operational tradeoffs: peering wins for few, stable pairs; transit hubs win for scale and inspection but add per-attachment pricing and a single routing authority. The pattern is peering for tight pairs and transit for hub-spoke, with CIDR uniqueness enforced across the estate.
- RSIS3/mykb relevance: the wiki's environment map would use peering for shared services and a transit hub for the fleet; this note records the routing model the loop preserves when adding VPCs.
- Route hygiene: document every peering route and TGW attachment in the IPAM/network map; an undocumented route is an incident waiting for a network change to expose it.
- Bandwidth note: TGW and peering have bandwidth ceilings per attachment; verify the ceiling against the workload before routing bulk traffic through the hub.

## Related
- [[wiki/cloud-infra/peering-and-transit|Peering & Transit]]
- [[wiki/devops-infra/api-gateways|API Gateways]]
- [[wiki/cloud-infra/aws-vpc-design|AWS VPC Design]]
- [[wiki/cloud-infra/gcp-vpc-and-cloud-nat|GCP VPC & Cloud NAT]]
