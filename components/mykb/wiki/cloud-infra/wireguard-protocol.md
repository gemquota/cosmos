---
type: "entity"
title: "WireGuard Protocol"
description: "A minimal, auditable VPN protocol built on modern cryptography"
tags: ["wireguard", "vpn", "crypto", "protocol"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: [
  "https://www.wireguard.com/protocol/",
  "https://www.wireguard.com/install/",
]
---

# WireGuard Protocol

## Summary
WireGuard is a modern VPN protocol built from a small set of well-audited cryptographic primitives. Its minimal design makes configuration, performance, and security review tractable. It has become the default choice for new tunnel deployments in many teams.

## Details
- WireGuard uses Curve25519 for key exchange, ChaCha20-Poly1305 for encryption, and BLAKE2s for hashing, all standard primitives.
- The protocol keeps a persistent handshake and session key rotation, with roaming built in by default.
- Configuration is declarative: peers are identified by public keys, and interfaces are configured with simple sections.
- The official protocol documentation and install guides cover both design and deployment.
- Performance is strong because the data path is a simple encrypt/decrypt transform with no negotiation on every packet.
- WireGuard integrates into the Linux kernel, which is why it appears in the OS-shell cluster as well as the VPN and remote access articles.
- Provider consoles and CLI workflows differ, so the provider-specific articles in this cluster record the concrete steps and gotchas.

## Related
- [[wiki/infrastructure/network-time-protocol|Network Time Protocol]]
- [[wiki/infrastructure/precision-time-protocol|Precision Time Protocol]]
- [[wiki/cloud-infra/autoscaling|Autoscaling]]
- [[wiki/cloud-infra/availability-zones|Availability Zones]]
