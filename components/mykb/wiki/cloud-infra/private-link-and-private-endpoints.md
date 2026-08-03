---
type: "concept"
title: "Private Link & Private Endpoints"
description: "Reaching cloud services over private IPs without public exposure"
tags: ["privatelink", "endpoints", "networking", "security"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---
# Private Link & Private Endpoints

## Summary

Private Link / private endpoints give services private IPs inside your VPC, so traffic to SaaS and other VPCs never touches the public internet: AWS PrivateLink/interface VPC endpoints, Azure Private Link, GCP Private Service Connect. They cut egress costs, simplify security, and complicate routing and DNS.

## Details
- Mechanism: a private endpoint is a NIC with an IP in your subnet backed by a service (SaaS, your own services, provider APIs); DNS resolution maps the service's public name to the private IP inside the VPC; traffic flows over the provider's backbone, not the internet. AWS interface endpoints support private DNS, Azure private endpoints integrate with private DNS zones, and PSC uses service attachment + forwarding rules.
- Concrete example: an app calls an SaaS API through a PrivateLink endpoint — no NAT, no public IP, no internet egress bill; a hub VPC exposes its internal service to spoke VPCs via PrivateLink, avoiding peering mesh; compliance requires no public exposure of database access, satisfied by endpoints instead of security-group gymnastics.
- Failure modes: DNS not switching to the private IP (the classic "still going to the internet" bug — private DNS zone must be linked and split-horizon correct); cross-region/on-prem resolution of private endpoints (needs custom DNS forwarding); per-endpoint pricing accumulating across many services; and service-side trust — endpoints are mutual: the consumer sees a private IP, but the service still authorizes by identity.
- Operational tradeoffs: endpoints buy privacy, lower egress cost, and simpler security groups at per-hour pricing and DNS complexity; use them for high-volume or compliance-sensitive traffic and document the DNS split so the loop's service discovery does not regress to public resolution.
- RSIS3/mykb relevance: the wiki's hub services are reached via private endpoints with documented DNS zones, so cross-service calls never traverse public egress.

## Related
- [[wiki/cloud-infra/virtual-private-clouds|Virtual Private Clouds]]
- [[wiki/cloud-infra/ipv6-link-local-addresses|IPv6 Link-Local Addresses]]
- [[wiki/os-shell/link-layer-ethernet-and-arp|Link Layer, Ethernet & ARP]]
