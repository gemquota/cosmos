---
type: "concept"
title: "ICMP & Diagnostics"
description: "Echo/ping, error messages, and traceroute"
tags: ["icmp", "ping", "traceroute", "network", "diagnostics"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://www.rfc-editor.org/rfc/rfc792", "https://man7.org/linux/man-pages/man8/ping.8.html"]
---

# ICMP & Diagnostics

## Summary
ICMP is the control protocol of IP: it reports errors and provides diagnostics, most famously echo request/reply for ping. Traceroute exploits ICMP TTL-exceeded messages to map the path to a destination.

## Details
- ICMP message types: echo request (8)/reply (0), destination unreachable (3), TTL exceeded (11), and redirect (5).
- ping sends echo requests and times replies: latency, loss percentage, and TTL of replies (which hints at hop count).
- Destination unreachable splits into codes: network/host unreachable, port unreachable (useful with UDP), and "fragmentation needed" for MTU discovery.
- Traceroute sends packets with incrementing TTLs; each router that decrements to zero replies TTL-exceeded, revealing the path.
- mtr combines ping and traceroute in a continuous view; path changes and packet loss show per-hop.
- Path MTU discovery uses ICMP "fragmentation needed" to find the largest packet a path supports; firewalls dropping ICMP break it.
- ICMP is often rate-limited or blocked for security, which can hide useful errors — that is why PMTUD failures are confusing.

## Related
- [[wiki/os-shell/routing-and-forwarding|Routing & Forwarding]] — the path traceroute maps
- [[wiki/os-shell/packet-analysis-and-capture|Packet Analysis]] — capturing the ICMP exchange
- [[wiki/os-shell/tcpdump|tcpdump]] — filtering ICMP traffic live
- [[wiki/os-shell/osi-model-and-tcp-ip|OSI Model & TCP/IP]] — ICMP's place in the stack
- [[wiki/os-shell/nat-and-port-forwarding|NAT & Port Forwarding]] — NAT traversal and ICMP
