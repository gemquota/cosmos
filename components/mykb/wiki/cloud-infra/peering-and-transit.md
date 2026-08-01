---
type: "concept"
title: "Peering and Transit"
description: "Connecting separate networks — VPCs, clouds, or data centers — through direct peering or transit hubs"
tags: ["peering", "transit", "networking", "routing"]
timestamp: "2026-08-01T00:00:00Z"
status: "stub"
---

# Peering and Transit

## Summary
Peering connects two networks directly (VPC peering, inter-cloud peering), while transit routes traffic through a central hub network.

## Details
- VPC peering is a private, low-latency connection between VPCs with no transiting and no extra data charges in some providers.
- Transit gateways centralize routing: many spokes attach to one hub with route tables and inter-region peering.
- Multi-cloud and on-prem connectivity converge on transit-hub designs rather than a mesh of point-to-point links.
- Open questions: peering limits, route-table sprawl, and cost accounting for cross-network traffic.

## Related
- [[wiki/cloud-infra/vpc-networking|VPC Networking]] — the networks being peered
- [[wiki/cloud-infra/direct-connect|Direct Connect]] — on-prem links enter the hub
- [[wiki/cloud-infra/multi-cloud-strategy|Multi-Cloud Strategy]] — why clouds must interconnect
