---
type: "concept"
title: "SSH Tunneling & Port Forwarding"
description: "Local, remote, and dynamic forwards for encrypted service access"
tags: ["ssh", "tunneling", "port-forwarding", "security"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# SSH Tunneling & Port Forwarding

## Summary
SSH tunneling carries TCP traffic inside an encrypted SSH session, letting you reach services that are not directly exposed, encrypt protocols that are normally plaintext, or route traffic through a jump host. Local, remote, and dynamic forwards cover the three main shapes: pull a remote port to your machine, expose a local port to a remote host, or turn SSH into a SOCKS proxy.

## Details
- Local forwarding (`-L local:remote`): bind a port on your machine and forward it over the SSH session to a host reachable from the server. Example: `ssh -L 5432:db.internal:5432 bastion` lets a local psql client reach a database that only the bastion can see.
- Remote forwarding (`-R remote:local`): reverse the direction — a port on the SSH server is forwarded back to a port on your machine. Useful for exposing a local dev server to a colleague, or for receiving webhooks on a machine without a public address.
- Dynamic forwarding (`-D 1080`): SSH acts as a SOCKS proxy so any SOCKS-aware application routes traffic through the server, effectively a per-process VPN without admin rights.
- Failure modes: tunnels die silently when the SSH connection drops or the idle timeout fires, so production reliance needs `ServerAliveInterval`, autossh-style supervision, or systemd socket units; port collisions and binding to the wrong interface (0.0.0.0 vs 127.0.0.1) leak services; and forwarding with `AllowTcpForwarding yes` on bastions weakens the security boundary.
- Operational tradeoffs: tunnels are excellent for occasional, human-scale access but poor for production service discovery — they create stateful ad-hoc routes that monitoring cannot see and that break during failover. Prefer VPNs, service meshes, or managed port-forwarding where uptime matters.
- Security practice: always bind forwards to localhost unless explicitly intended for others, restrict `AllowTcpForwarding` on shared bastions, and audit open listeners, since a forgotten reverse tunnel is a common exfiltration path.
- RSIS3/mykb relevance: when loops need temporary encrypted access paths, this node reminds retrievals that tunnels are ephemeral transport, not durable architecture.

## Related
- [[wiki/os-shell/nat-and-port-forwarding|NAT & Port Forwarding]] — related coverage in the same cluster
- [[wiki/cloud-infra/vpn-split-tunneling|VPN Split Tunneling]] — related coverage in the same cluster
- [[wiki/infrastructure/ssh-key-management|SSH Key Management]] — related coverage in the same cluster
- [[wiki/os-shell/nmap-and-port-scanning|nmap & Port Scanning]] — related coverage in the same cluster
- [[wiki/infrastructure/storage-systems|Storage Systems]] — related coverage in the same cluster
- [[wiki/syntheses/knowledge-acquisition-workflow|Knowledge Acquisition Workflow]] — how stubs grow into full articles in mykb
- [[wiki/syntheses/mykb-acquisition-curation-and-practices|Acquisition, Curation & Practices]] — the curation loop this stub belongs to
