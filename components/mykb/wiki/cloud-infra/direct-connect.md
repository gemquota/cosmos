---
type: "concept"
title: "Direct Connect"
description: "Dedicated private network links from on-premises data centers to cloud providers"
tags: ["direct-connect", "networking", "hybrid-cloud", "bandwidth"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://docs.aws.amazon.com/directconnect/latest/UserGuide/Welcome.html", "https://learn.microsoft.com/en-us/azure/expressroute/expressroute-introduction"]
---

# Direct Connect

## Summary
Direct Connect is a dedicated physical link between a data center and a cloud provider, bypassing the public internet for lower latency, stable bandwidth, and private routing.

## Details
- A dedicated circuit crosses a colocation facility to the provider's edge; traffic is private but still needs encryption for compliance.
- Benefits: predictable throughput, lower per-GB cost for large transfers, and no internet path variability.
- Costs: circuit fees, colocation cross-connects, and long lead times — it is an investment, not a quick fix.
- AWS Direct Connect is a dedicated network connection from an on-premises site to AWS, bypassing the public internet for lower latency, consistent bandwidth, and privacy.
- It requires physical infrastructure (cross-connects, routers, VLANs) and is a capacity commitment, not an on-demand service.
- The equivalent concept in Azure is ExpressRoute, with similar tradeoffs: predictable performance for predictable cost.
- Direct connections are justified by sustained traffic and hybrid architectures; occasional transfers are cheaper over the internet or VPN.
- **Worked example / comparison** — Comparison — a VPN uses the public internet and scales on demand but fluctuates; a dedicated connection is stable but has a floor cost, so the traffic profile decides which fits.
- For mykb, Direct Connect is documented as the dedicated-connectivity option in the hybrid-cloud cluster.

## Related
- [[wiki/cloud-infra/vpn-tunnels|VPN Tunnels]]
- [[wiki/cloud-infra/peering-and-transit|Peering and Transit]]
- [[wiki/cloud-infra/multi-cloud-strategy|Multi-Cloud Strategy]]
- [[wiki/concepts/promotion-readiness|Promotion Readiness]]
- [[wiki/dev-tools/global-link-check|Global Link Check]]
- [[wiki/concepts/decision-guides|Decision Guides]]
