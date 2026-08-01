---
type: "concept"
title: "VPN Tunnels"
description: "Encrypted site-to-site connections between on-premises networks and cloud VPCs"
tags: ["vpn", "networking", "encryption", "hybrid-cloud"]
timestamp: "2026-08-01T00:00:00Z"
status: "stub"
---

# VPN Tunnels

## Summary
VPN tunnels encrypt traffic between an on-premises network and a cloud VPC over the public internet.

## Details
- IPsec tunnels terminate at VPN gateways on both sides; traffic flows encrypted but shares public internet paths.
- Bandwidth and latency are bounded by the tunnel endpoints — fine for management traffic, risky for data-heavy replication.
- Failover: two tunnels to different endpoints give some redundancy; cloud VPNs integrate with route propagation for automatic failover.
- Open questions: tunnel throughput tuning, MTU issues, and when to graduate to dedicated connectivity.

## Related
- [[wiki/cloud-infra/peering-and-transit|Peering and Transit]] — routing between networks
- [[wiki/cloud-infra/direct-connect|Direct Connect]] — dedicated alternative to VPN
- [[wiki/cloud-infra/multi-cloud-strategy|Multi-Cloud Strategy]] — VPNs as the glue between clouds
