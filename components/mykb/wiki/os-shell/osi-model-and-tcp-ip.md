---
type: "concept"
title: "OSI Model & TCP/IP"
description: "Layer stacks and encapsulation"
tags: ["osi", "tcp-ip", "networking", "layers"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://www.rfc-editor.org/rfc/rfc1122", "https://www.rfc-editor.org/rfc/rfc1180"]
---

# OSI Model & TCP/IP

## Summary
The OSI model describes networking in seven layers, from physical media to applications; the TCP/IP model condenses it to four: link, internet, transport, and application. Each layer encapsulates the one above it, wrapping data in headers as it travels down the stack.

## Details
- The seven OSI layers: physical, data link, network, transport, session, presentation, application — a teaching frame more than a protocol spec.
- TCP/IP's four layers map onto it: link (Ethernet/Wi-Fi), internet (IP), transport (TCP/UDP), application (HTTP, DNS, SSH).
- Encapsulation: an HTTP request becomes a TCP segment inside an IP packet inside an Ethernet frame, each adding its own header.
- Each layer is independent by contract: transport doesn't care whether the link is Ethernet or Wi-Fi, which is why stacks interoperate.
- PDUs have names per layer: frame (link), packet (network), segment (transport); RFC 1122 defines the host requirements.
- Troubleshooting follows the layers: physical (cable/link), link (ARP), network (ping), transport (ports), application (HTTP status).
- The OSI presentation and session layers live folded into applications in practice — TLS covers encryption, sockets handle sessions.

## Related
- [[wiki/os-shell/tcp-connection-lifecycle|TCP Connections]] — the transport layer's state machine
- [[wiki/os-shell/udp-and-datagrams|UDP & Datagrams]] — the connectionless transport
- [[wiki/os-shell/network-sockets|Network Sockets]] — the API at the transport boundary
- [[wiki/os-shell/routing-and-forwarding|Routing & Forwarding]] — the internet layer's job
- [[wiki/os-shell/link-layer-ethernet-and-arp|Link Layer, Ethernet & ARP]] — the bottom of the stack
