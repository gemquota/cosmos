---
type: "concept"
title: "IP Addressing & Subnetting"
description: "IPv4/IPv6 addresses, CIDR, and subnet math"
tags: ["ip", "subnetting", "cidr", "ipv4", "ipv6"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://www.rfc-editor.org/rfc/rfc4632", "https://man7.org/linux/man-pages/man8/ip.8.html"]
---

# IP Addressing & Subnetting

## Summary
IP addresses identify network interfaces: IPv4 uses 32 bits and IPv6 128 bits. CIDR notation (192.168.1.0/24) states the prefix length, and subnetting is the arithmetic of dividing address blocks into networks and hosts.

## Details
- IPv4: four octets, about 4.3 billion addresses; IPv6: eight 16-bit groups in hex, effectively inexhaustible, with :: for zero runs.
- CIDR: the /N suffix is the number of network bits; remaining bits address hosts within the subnet.
- Subnet math: for /24, the network address has host bits zero, broadcast has host bits one, and usable hosts are 2^(32-N) - 2.
- Private IPv4 ranges (RFC 1918): 10/8, 172.16/12, 192.168/16, never routed publicly; IPv6 has ULA (fc00::/7) and link-local fe80::/10.
- Special addresses: 127.0.0.1 loopback, 0.0.0.0 any/unspecified, 169.254.0.0/16 link-local (APIPA).
- Tools: ip addr show, ipcalc/prefix, and route lookups via ip route get; misconfigured masks cause "can't reach" symptoms.
- IPv6 specifics: global unicast, link-local for neighbor discovery, and no broadcast — multicast and anycast instead.

## Related
- [[wiki/os-shell/routing-and-forwarding|Routing & Forwarding]] — what the network bits select
- [[wiki/os-shell/dns-resolution|DNS Resolution]] — names instead of numbers
- [[wiki/os-shell/nat-and-port-forwarding|NAT & Port Forwarding]] — hiding private subnets
- [[wiki/cloud-infra/subnet-design|Subnet Design]] — planning address blocks in the cloud
- [[wiki/os-shell/tcp-ports-and-services|TCP Ports & Services]] — the endpoints on top of addresses
