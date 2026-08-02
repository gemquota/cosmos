---
type: "concept"
title: "DHCP & IP Allocation"
description: "DORA exchange, leases, and static vs dynamic"
tags: ["dhcp", "ip", "leases", "network"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://www.rfc-editor.org/rfc/rfc2131", "https://man7.org/linux/man-pages/man8/dhclient.8.html"]
---

# DHCP & IP Allocation

## Summary
DHCP hands out IP configuration automatically: address, netmask, gateway, DNS servers, and more. A client discovers a server, receives an offer, requests the address, and gets an acknowledgment — the DORA exchange — then renews the lease before it expires.

## Details
- DORA: Discover (broadcast), Offer (available config), Request (accept the offer), Ack (final lease); the client may also decline conflicts.
- Leases have a lifetime; the client renews at T1 (50%) and rebinds at T2 (87.5%) to any server before the lease expires.
- DHCP servers match clients by MAC (chaddr) or client ID, so reservations can pin stable addresses.
- Options carried in the exchange include routers, DNS servers, NTP, domain search, and boot files (PXE).
- DHCPv6 differs: stateful DHCPv6 assigns addresses, while SLAAC (RA messages) configures addresses automatically without a server.
- Static vs dynamic: servers and appliances get reserved or static addresses; workstations and IoT get leases from pools.
- Clients: dhclient, systemd-networkd, NetworkManager; dhcpcd is common on smaller systems and Termux-style environments.

## Related
- [[wiki/os-shell/ip-addresses-and-subnetting|IP Addressing & Subnetting]] — the addresses DHCP hands out
- [[wiki/os-shell/dns-resolution|DNS Resolution]] — DNS servers arrive via DHCP options
- [[wiki/os-shell/link-layer-ethernet-and-arp|Link Layer, Ethernet & ARP]] — the MAC addresses DHCP matches
- [[wiki/cloud-infra/vpc-networking|VPC Networking]] — cloud subnets and DHCP equivalents
- [[wiki/os-shell/tcp-ports-and-services|TCP Ports & Services]] — DHCP uses UDP 67/68
