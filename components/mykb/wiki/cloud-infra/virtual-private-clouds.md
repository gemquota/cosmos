---
type: "concept"
title: "Virtual Private Clouds"
description: "Isolated network slices inside public cloud regions"
tags: ["vpc", "cloud", "networking", "isolation"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: [
  "https://docs.aws.amazon.com/vpc/latest/userguide/what-is-amazon-vpc.html",
  "https://cloud.google.com/vpc/docs/vpc",
]
---

# Virtual Private Clouds

## Summary
A VPC is an isolated virtual network inside a public cloud region, with its own address space, subnets, and routing. It gives tenants the control of a private network without owning hardware. VPC design is the foundation of cloud infrastructure.

## Details
- Each VPC owns a private CIDR block; subnets divide it per availability zone.
- Route tables direct traffic between subnets, to the internet gateway, or to virtual private gateways.
- Security groups and network ACLs provide instance-level and subnet-level filtering.
- AWS and GCP both implement VPCs (Amazon VPC and GCP VPC), with GCP using global VPCs across regions.
- Peering and transit connect VPCs, while private endpoints reach managed services without public exposure.
- VPC misconfigurations, such as overlapping CIDRs or missing routes, are among the most common production network incidents.
- Provider consoles and CLI workflows differ, so the provider-specific articles in this cluster record the concrete steps and gotchas.
- Cost and latency tradeoffs for this choice are quantified in the capacity planning and cost-of-bandwidth articles.

## Related
- [[wiki/infrastructure/virtual-switches|Virtual Switches]]
- [[wiki/cloud-infra/private-link-and-private-endpoints|Private Link & Private Endpoints]]
- [[wiki/cloud-infra/virtual-machines|Virtual Machines]]
- [[wiki/infrastructure/warehouse-clusters-and-virtual-warehouses|Warehouse Clusters And Virtual Warehouses]]
