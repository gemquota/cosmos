---
type: "concept"
title: "VPN Tunnels"
description: "Encrypted site-to-site connections between on-premises networks and cloud VPCs"
tags: ["vpn", "networking", "encryption", "hybrid-cloud"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
---
# VPN Tunnels

## Summary

VPN tunnels are encrypted point-to-point links (IPsec, WireGuard, OpenVPN) carrying private traffic over public networks. They are the connective tissue of hybrid and branch architectures — simple in concept, subtle in the details: MTU, routing, redundancy, and tunnel drift.

## Details
- Mechanism: IPsec pairs (IKEv2 + ESP, often with AES-GCM) create SA pairs per direction; multiple tunnels per connection give redundancy (AWS VPN runs two per connection with failover); BGP runs over the tunnels for dynamic routing; WireGuard uses simpler crypto-key pairing with roaming; OpenVPN adds userspace flexibility at performance cost. All are subject to MTU reduction (encapsulation overhead).
- Concrete example: a branch office runs two IPsec tunnels to the cloud hub with BGP preferring the primary; an MTU mismatch silently drops large packets until MSS clamping is applied (the classic tunnel black hole); a WireGuard mesh connects remote workers directly, peer-to-peer, without a central concentrator.
- Failure modes: MTU/fragmentation black holes; dead-peer detection failures leaving one-way tunnels; key/SA expiry without rekeying (silent outages); routing loops or asymmetric paths when BGP and static routes mix; and tunnel software versions drifting from the policy baseline.
- Operational tradeoffs: tunnels are cheap and fast to deploy but add latency, complexity, and internet dependence; dedicated links beat them for latency-critical traffic. Monitor tunnel status, rekey health, and MTU per link, and keep the tunnel configuration versioned.
- RSIS3/mykb relevance: the wiki's hybrid links would use dual IPsec tunnels with BGP and recorded MTU clamps; this node is the reference for the loop's connectivity troubleshooting.
- Key management: prefer IKEv2 with certificates or strong PSKs, rotate them on a schedule, and store tunnel credentials in the parameter store, not in config files.
- Failover testing: rehearse tunnel failover quarterly by disabling the primary; an untested failover is a future outage with a two-hour postmortem attached.

## Related
- [[wiki/cloud-infra/peering-and-transit|Peering and Transit]] — routing between networks
- [[wiki/cloud-infra/direct-connect|Direct Connect]] — dedicated alternative to VPN
- [[wiki/cloud-infra/multi-cloud-strategy|Multi-Cloud Strategy]] — VPNs as the glue between clouds
