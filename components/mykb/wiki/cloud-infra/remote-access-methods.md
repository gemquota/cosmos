---
type: "concept"
title: "Remote Access Methods"
description: "SSH, VPNs, RDP, and bastions as ways into private networks"
tags: ["remote-access", "ssh", "vpn", "security"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---
# Remote Access Methods

## Summary

Remote access methods — bastion/jump hosts, VPNs, client VPNs, SSH tunnels, and modern zero-trust connectors — all solve reaching private infrastructure. They trade convenience, security posture, and auditability differently; the trend is from broad network access to per-resource, identity-based access.

## Details
- Mechanism: bastion hosts concentrate SSH/RDP entry (hardened, monitored, with key management); site-to-site VPNs connect networks; client VPNs give users a network foothold; SSH tunnels/port-forwarding give narrow, short-lived paths; zero-trust (Tailscale, Teleport, BeyondCorp-style) brokers identity-aware access to specific resources without a network presence.
- Concrete example: an admin reaches a database via bastion → SSH tunnel to avoid exposing 5432; a contractor gets a short-lived, resource-scoped session through a zero-trust broker with full audit; a branch office connects via site-to-site VPN to the hub VPC. The failure pattern is broad VPN access + stale credentials = lateral movement.
- Failure modes: jump hosts with world-accessible SGs; long-lived credentials or keys that survive offboarding; VPN full-tunnel hairpinning (all traffic through HQ) degrading performance; unlogged access paths making incidents untraceable; and zero-trust rollouts that skip the last mile (server-side agent coverage), leaving legacy paths open.
- Operational tradeoffs: zero-trust per-resource access is the strongest posture with the highest adoption cost; bastion+VPN remains pragmatic for small teams. Whatever the method: short-lived credentials, MFA, session logging, and a deprovisioning path are non-negotiables. Pick one primary method and retire legacy entry points — parallel paths double the audit surface.
- RSIS3/mykb relevance: the wiki's admin access would use short-lived, audited sessions via a zero-trust broker, with bastion fallback documented; this note is the access-matrix reference for loop infrastructure changes.
- Session audit: log every remote session (who, what, when) and review access regularly; an unaudited access path is invisible until the incident that uses it. Rotate jump-host keys on a schedule, revoke VPN profiles promptly on offboarding, and spot-check logs monthly.

## Related
- [[wiki/devops-infra/zero-trust-access-proxies|Zero Trust Access Proxies]]
- [[wiki/cloud-infra/network-access-control-lists|Network Access Control Lists]]
- [[wiki/os-shell/ssh-and-remote-access|SSH & Remote Access]]
- [[wiki/devops-infra/remote-development-vscode-ssh|Remote Development: VS Code & SSH]]
