---
type: "concept"
title: "UDP & Datagrams"
description: "Connectionless delivery, checksums, and use cases"
tags: ["udp", "datagrams", "networking", "checksum"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://www.rfc-editor.org/rfc/rfc768", "https://man7.org/linux/man-pages/man7/udp.7.html"]
---

# UDP & Datagrams

## Summary
UDP is the connectionless transport: applications send self-contained datagrams with no handshake, no retransmission, and no ordering guarantees. Its 8-byte header is minimal, which is why latency-sensitive and simple protocols prefer it.

## Details
- The UDP header carries source port, destination port, length, and checksum; IPv4 makes the checksum optional, IPv6 requires it.
- Datagram boundaries survive: each send becomes one recv, so message framing is built in — unlike TCP's byte stream.
- No congestion control means a sender can flood a receiver or network; applications (QUIC, media) add their own control or tolerate loss.
- Drop behavior: when a socket buffer fills, the kernel drops datagrams and increments UDP receive error counters (ss -u shows drops).
- Use cases: DNS queries, NTP, DHCP, VoIP, multicast streaming, and QUIC which runs over UDP with congestion control in user space.
- Server pattern: bind to a port, then recvfrom answers each datagram from the source address; one socket serves many clients.
- For local IPC, UDP-over-Unix-sockets (SOCK_DGRAM on AF_UNIX) gives message semantics without the network stack.

## Related
- [[wiki/os-shell/tcp-connection-lifecycle|TCP Connections]] — the reliable contrast
- [[wiki/os-shell/dns-resolution|DNS Resolution]] — the classic UDP consumer
- [[wiki/os-shell/network-sockets|Network Sockets]] — SOCK_DGRAM in the socket API
- [[wiki/os-shell/packet-analysis-and-capture|Packet Analysis]] — seeing datagrams on the wire
- [[wiki/os-shell/osi-model-and-tcp-ip|OSI Model & TCP/IP]] — transport layer in context
