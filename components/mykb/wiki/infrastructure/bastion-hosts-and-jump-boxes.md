---
type: "concept"
title: "Bastion Hosts & Jump Boxes"
description: "Hardened entry points for reaching private infrastructure"
tags: ["bastion", "ssh", "security", "access"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# Bastion Hosts & Jump Boxes

## Summary
Bastion hosts (jump boxes) are hardened, deliberately exposed entry points that provide the only path into a private network. The design idea: instead of opening SSH or RDP to every internal host, expose one tightly controlled host, and route all administrative access through it — so the network's attack surface for management traffic is a single, heavily defended door.

## Details
- The architecture: internal hosts have private addresses and no inbound exposure; the bastion sits in a public (or DMZ) subnet with a small, locked-down management port open; administrators connect to the bastion and then jump to internal hosts, either by running interactive SSH through it or by configuring SSH agent/proxy forwarding so the bastion relays connections without ever holding credentials. Cloud platforms formalize the pattern with managed bastion services (AWS Systems Manager Session Manager, Azure Bastion, GCP IAP), which remove the bastion host's own management burden entirely.
- Hardening is the whole point, and it is demanding: the bastion must run a minimal OS with auto-patching, SSH configured with key-only auth, no passwords, and rate limiting; it should carry no production credentials and no data; and every login should be audited. Managed services are usually the better choice because they eliminate the patch-and-harden treadmill and give identity-based access control (IAM/Entra policies) instead of a shared host account.
- The alternatives and tradeoffs: direct exposure of internal hosts is simpler but multiplies the attack surface; a VPN replaces the bastion with a network-level gate but shifts trust to the VPN client and endpoint security; zero-trust port knocking and ephemeral access (SSO-issued short-lived credentials, one-time host access) shrink the window further. The tradeoff for the bastion is operational friction — every administrative session traverses an extra hop, and the bastion itself is a critical single point of failure: if it is down or compromised, all management access is down or compromised.
- Failure modes: the unmaintained bastion (outdated packages, leftover accounts, default configs — the classic way bastions become the breach point), bastions holding real credentials (one compromise becomes full access), and unlogged bastion use (no audit trail for who touched what).
- For mykb: the node connects the access-control cluster — SSH key management, hardware keys, and session management all plug into the bastion pattern.

## Related
- [[wiki/cloud-infra/dedicated-hosts-and-instances|Dedicated Hosts & Instances]]
- [[wiki/infrastructure/storage-systems|Storage Systems]]
- [[wiki/infrastructure/ospf-protocols|OSPF Protocols]]
