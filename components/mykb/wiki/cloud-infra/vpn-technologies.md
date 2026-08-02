---
type: "concept"
title: "VPN Technologies"
description: "Tunnels that extend private networks across untrusted links"
tags: ["vpn", "tunneling", "encryption", "networking"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: [
  "https://www.rfc-editor.org/rfc/rfc6071",
  "https://en.wikipedia.org/wiki/Virtual_private_network",
]
---

# VPN Technologies

## Summary
VPNs create private, encrypted tunnels across untrusted networks, connecting remote users and sites to internal resources. Modern options span IPsec, WireGuard, and TLS-based solutions. Choosing and operating a VPN requires balancing security, performance, and compatibility.

## Details
- A VPN encapsulates and encrypts traffic at a defined layer: IP packets for IPsec, UDP datagrams for WireGuard, or arbitrary TCP for TLS VPNs.
- RFC 6071 is the roadmap for IPsec and IKE, describing the building blocks used by enterprise VPN products.
- Tunnel mode protects whole packets between gateways; transport mode protects only the payload between endpoints.
- Split tunneling routes only some traffic through the VPN, improving performance while complicating security posture.
- Key management is the hard part: PSKs, certificates, and IKE negotiation all need rotation and monitoring.
- In the mykb graph, VPN technologies connect to tunnel protocols, remote access methods, and zero-trust access articles.
- Provider consoles and CLI workflows differ, so the provider-specific articles in this cluster record the concrete steps and gotchas.

## Related
- [[wiki/cloud-infra/vpn-split-tunneling|VPN Split Tunneling]]
- [[wiki/cloud-infra/site-to-site-vpn|Site-to-Site VPN]]
- [[wiki/cloud-infra/vpn-tunnels|VPN Tunnels]]
- [[wiki/cloud-infra/autoscaling|Autoscaling]]
