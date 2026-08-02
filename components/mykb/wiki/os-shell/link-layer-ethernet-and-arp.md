---
type: "concept"
title: "Link Layer, Ethernet & ARP"
description: "Frames, MAC addressing, and ARP"
tags: ["ethernet", "arp", "mac", "link-layer"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://www.rfc-editor.org/rfc/rfc826", "https://man7.org/linux/man-pages/man7/arp.7.html"]
---

# Link Layer, Ethernet & ARP

## Summary
The link layer moves frames between directly connected devices. Ethernet frames carry 48-bit MAC addresses, and the Address Resolution Protocol (ARP) maps IPv4 addresses to the MAC addresses needed to deliver them on a local network.

## Details
- The Ethernet II frame: destination MAC, source MAC, EtherType (0x0800 IPv4, 0x86DD IPv6), payload, and FCS checksum.
- MAC addresses are burned into NICs (or assigned by drivers) in the OUI/vendor format; switches learn which MAC is behind which port.
- Switches forward frames by MAC table, not IP; broadcasts flood to all ports, which is how ARP requests work.
- ARP: a host asks "who has 192.168.1.1?" by broadcast; the owner replies unicast; answers populate the neighbor cache.
- ip neigh and arp -n show the cache; gratuitous ARP announces address changes; ARP spoofing is a classic MITM attack.
- IPv6 replaces ARP with Neighbor Discovery (ND): ICMPv6 messages, multicast solicitation, and no broadcast.
- Troubleshooting: ping failure on-link usually means an ARP failure; tcpdump arp reveals the whole exchange.

## Related
- [[wiki/os-shell/ip-addresses-and-subnetting|IP Addressing & Subnetting]] — the addresses ARP resolves
- [[wiki/os-shell/routing-and-forwarding|Routing & Forwarding]] — the next hop is resolved by ARP
- [[wiki/os-shell/packet-analysis-and-capture|Packet Analysis]] — watching ARP and frame traffic
- [[wiki/os-shell/osi-model-and-tcp-ip|OSI Model & TCP/IP]] — the bottom layers of the stack
- [[wiki/os-shell/dhcp-and-ip-allocation|DHCP & IP Allocation]] — lease discovery uses MAC addresses
