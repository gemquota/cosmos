---
type: "concept"
title: "Firewalls & netfilter"
description: "iptables/nftables chains, tables, and rules"
tags: ["firewall", "netfilter", "iptables", "nftables"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://wiki.nftables.org/wiki-nftables/index.php/Main_Page", "https://man7.org/linux/man-pages/man8/iptables.8.html"]
---

# Firewalls & netfilter

## Summary
netfilter is the kernel's packet-filtering framework, and iptables/nftables are the user-space front ends that program it. Packets pass through numbered hooks, where chains of rules decide accept, drop, reject, or redirect — the basis of Linux firewalling.

## Details
- Hooks: PREROUTING, INPUT, FORWARD, OUTPUT, POSTROUTING; routing decisions determine which hooks a packet crosses.
- Legacy iptables tables: filter (firewall rules), nat (SNAT/DNAT/masquerade), mangle (packet modifications), raw (pre-conntrack).
- Rules match fields (interface, source/dest IP, protocol, ports, state) and jump to targets: ACCEPT, DROP, REJECT, LOG, or a chain.
- Conntrack state: -m conntrack --ctstate NEW,ESTABLISHED,RELATED enables stateful filtering that allows replies automatically.
- Default policies matter: a firewall with default DROP and explicit allows is safer than default ACCEPT with denies.
- nftables is the modern replacement: one unified syntax (nft add rule inet filter input tcp dport 22 accept), atomic rule updates, and no separate tables.
- Front ends: ufw and firewalld generate rules from simple policies; cloud security groups apply the same ideas at the network edge.

## Related
- [[wiki/os-shell/nat-and-port-forwarding|NAT & Port Forwarding]] — nat chains at work
- [[wiki/os-shell/nmap-and-port-scanning|nmap & Port Scanning]] — testing firewall rules
- [[wiki/os-shell/tcp-ports-and-services|TCP Ports & Services]] — what rules match on
- [[wiki/security-auth/network-segmentation|Network Segmentation]] — firewalls as segmentation tools
- [[wiki/infrastructure/network-policy|Network Policy]] — the container-native equivalent
