---
type: "concept"
title: "IPsec Tunnels"
description: "Suite-based VPN protection for IP packets with IKE negotiation"
tags: ["ipsec", "vpn", "ike", "security"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: [
  "https://www.rfc-editor.org/rfc/rfc7296",
  "https://www.rfc-editor.org/rfc/rfc6071",
]
---

# IPsec Tunnels

## Summary
IPsec protects IP traffic with encryption and authentication at the packet level, negotiated by IKE. It is the standard for site-to-site VPNs and remains widely used in cloud and enterprise connectivity. Its flexibility comes with configuration complexity.

## Details
- IPsec has two protocols: AH for authentication and ESP for encryption plus authentication, with ESP being the practical default.
- Tunnel mode wraps the whole original IP packet; transport mode protects only the payload between hosts.
- IKE (RFC 7296 for IKEv2) negotiates algorithms, authenticates peers, and establishes the security associations used by the data path.
- The suite must agree on ciphers, hashes, DH groups, and lifetimes, which is where interop problems arise between vendors.
- NAT traversal (NAT-T) lets ESP survive address translation by encapsulating in UDP port 4500.
- Cloud site-to-site VPN gateways, such as AWS VPN and Azure VPN Gateway, are configured largely in IKE terms.
- Provider consoles and CLI workflows differ, so the provider-specific articles in this cluster record the concrete steps and gotchas.

## Related
- [[wiki/cloud-infra/dns-over-https|DNS over HTTPS]]
- [[wiki/cloud-infra/anycast-routing|Anycast Routing]]
- [[wiki/cloud-infra/vpn-tunnels|VPN Tunnels]]
- [[wiki/cloud-infra/autoscaling|Autoscaling]]
