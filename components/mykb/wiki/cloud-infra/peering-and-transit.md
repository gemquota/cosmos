---
type: "concept"
title: "Peering and Transit"
description: "Connecting separate networks — VPCs, clouds, or data centers — through direct peering or transit hubs"
tags: ["peering", "transit", "networking", "routing"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://docs.aws.amazon.com/vpc/latest/peering/what-is-vpc-peering.html", "https://docs.aws.amazon.com/vpc/latest/tgw/what-is-transit-gateway.html", "https://www.rfc-editor.org/rfc/rfc4271.html"]
---

# Peering and Transit

## Summary
Peering connects two networks directly (VPC peering, inter-cloud peering), while transit routes traffic through a central hub network. Cloud providers expose both as managed constructs: VPC peering for point-to-point private connectivity and transit gateways for hub-and-spoke routing at scale. Together they replace the ad-hoc mesh of VPN tunnels that early multi-cloud architectures relied on.

## Details
- VPC peering is a private, low-latency connection between VPCs with no transiting and no extra data charges in some providers.
- Transit gateways centralize routing: many spokes attach to one hub with route tables and inter-region peering.
- Multi-cloud and on-prem connectivity converge on transit-hub designs rather than a mesh of point-to-point links.
- **Direct peering** — a one-to-one relationship between two networks; traffic stays private and latency is minimal, but every new pair adds route-table entries and peering limits apply per account/region.
- **Transit hub** — a single gateway device that every spoke attaches to; route tables and attachments scale the design to many VPCs, and inter-region peering lets the hub forward traffic between regions.
- **Routing protocol reality** — at the internet backbone level, peering is governed by BGP (RFC 4271): ASes exchange routes over peering sessions, with transit providers selling reachability to the rest of the internet. Cloud transit gateways abstract this, but the same hub-and-spoke economics apply.
- **RSIS3 relevance** — the mykb graph itself is a peering problem: linking new domain clusters directly creates mesh sprawl, while synthesis and hub articles act as transit nodes that keep the graph navigable.
- **Open questions** — peering limits, route-table sprawl, cost accounting for cross-network traffic, and when to break a hub into multiple transit gateways for blast-radius isolation.

## Related
- [[wiki/cloud-infra/virtual-private-clouds|Virtual Private Clouds]] — the network containers peering connects
- [[wiki/cloud-infra/cdns-and-edge-networking|CDNs and Edge Networking]] — peering at the edge versus in the data center
- [[wiki/devops-infra/network-observability|Network Observability]] — measuring the flows these designs create
- [[wiki/devops-infra/service-meshes-istio-linkerd|Service Meshes]] — application-level peering on top of VPC peering
- [[wiki/infrastructure/bastion-hosts-and-jump-boxes|Bastion Hosts]] — secure entry points in peered topologies

## Related
- [[wiki/cloud-infra/vpc-networking|VPC Networking]] — the networks being peered
- [[wiki/cloud-infra/direct-connect|Direct Connect]] — on-prem links enter the hub
- [[wiki/cloud-infra/multi-cloud-strategy|Multi-Cloud Strategy]] — why clouds must interconnect
