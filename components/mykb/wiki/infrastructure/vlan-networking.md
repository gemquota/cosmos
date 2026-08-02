---
type: "concept"
title: "VLAN Networking"
description: "Segmenting broadcast domains with 802.1Q tags"
tags: ["vlan", "switching", "802.1q", "networking"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: [
  "https://www.rfc-editor.org/rfc/rfc5517",
  "https://en.wikipedia.org/wiki/IEEE_802.1Q",
]
---

# VLAN Networking

## Summary
VLANs segment a physical Ethernet network into isolated broadcast domains using 802.1Q tags. They are the basic unit of network partitioning in campus, datacenter, and virtualized environments. Correct VLAN design simplifies security, traffic engineering, and troubleshooting.

## Details
- IEEE 802.1Q inserts a 12-bit VLAN identifier and priority bits into Ethernet frames, allowing trunk links to carry many VLANs.
- Access ports assign untagged traffic to one VLAN; trunk ports carry tagged traffic for many VLANs between switches.
- Each VLAN behaves like its own LAN: broadcasts, ARP, and multicast stay inside the VLAN, which limits blast radius.
- Inter-VLAN routing moves traffic through a router or layer-3 switch, which is where firewalls and policies apply.
- Common failure modes are trunk misconfiguration (VLAN leaks), MTU overhead from the extra tag, and duplicate IP addresses across VLANs.
- Virtual switches in hypervisors and cloud VPCs apply the same tagging concept, so VLAN knowledge transfers directly to virtual networking.

## Related
- [[wiki/cloud-infra/multicast-networking|Multicast Networking]]
- [[wiki/infrastructure/software-defined-networking|Software-Defined Networking]]
- [[wiki/cloud-infra/vpc-networking|VPC Networking]]
- [[wiki/infrastructure/ambassador-pattern|Ambassador Pattern]]
