---
type: "concept"
title: "TCP/IP Stack"
description: "How the Internet protocol suite carries data between applications"
tags: ["tcp-ip", "networking", "protocols", "internet"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: [
  "https://www.rfc-editor.org/rfc/rfc1180",
  "https://www.rfc-editor.org/rfc/rfc9293",
]
---

# TCP/IP Stack

## Summary
The TCP/IP stack is the protocol suite of the Internet: link, internet, transport, and application layers working together. TCP provides reliable byte streams, IP provides global addressing, and the layers above choose how the data is used. Understanding the stack is the prerequisite for every other networking article here.

## Details
- The four layers map to concrete protocols: Ethernet/Wi-Fi at the link layer, IPv4/IPv6 at the internet layer, TCP/UDP at the transport layer, and HTTP/DNS/SSH at the application layer.
- TCP (RFC 9293) offers connection-oriented, ordered, reliable delivery; UDP (RFC 768) offers connectionless datagrams with minimal overhead.
- IP is connectionless and best-effort: packets may take different paths, arrive out of order, or be dropped, and upper layers compensate.
- The stack exists on every host as a kernel implementation; Linux exposes it through sockets, which is why socket options appear throughout the OS-shell articles.
- Encapsulation means each layer only inspects its own headers, which is what makes middleboxes and packet capture tools work the way they do.
- Operationally, most network problems are diagnosed by reasoning about which layer is failing: cabling, addressing, routing, or application behavior.

## Related
- [[wiki/cloud-infra/tcp-retransmission|TCP Retransmission]]
- [[wiki/infrastructure/rack-and-stack-layout|Rack & Stack Layout]]
- [[wiki/os-shell/osi-model-and-tcp-ip|OSI Model & TCP/IP]]
- [[wiki/os-shell/dhcp-and-ip-allocation|DHCP & IP Allocation]]
