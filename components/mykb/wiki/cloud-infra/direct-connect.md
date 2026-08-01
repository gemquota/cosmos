---
type: "concept"
title: "Direct Connect"
description: "Dedicated private network links from on-premises data centers to cloud providers"
tags: ["direct-connect", "networking", "hybrid-cloud", "bandwidth"]
timestamp: "2026-08-01T00:00:00Z"
status: "stub"
---

# Direct Connect

## Summary
Direct Connect is a dedicated physical link between a data center and a cloud provider, bypassing the public internet for lower latency, stable bandwidth, and private routing.

## Details
- A dedicated circuit crosses a colocation facility to the provider's edge; traffic is private but still needs encryption for compliance.
- Benefits: predictable throughput, lower per-GB cost for large transfers, and no internet path variability.
- Costs: circuit fees, colocation cross-connects, and long lead times — it is an investment, not a quick fix.

## Related
- [[wiki/cloud-infra/vpn-tunnels|VPN Tunnels]] — the cheaper alternative
- [[wiki/cloud-infra/peering-and-transit|Peering and Transit]] — how dedicated links route
- [[wiki/cloud-infra/multi-cloud-strategy|Multi-Cloud Strategy]] — dedicated links per provider
