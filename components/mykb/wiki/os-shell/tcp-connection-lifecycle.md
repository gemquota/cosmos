---
type: "concept"
title: "TCP Connections"
description: "Handshake, state machine, and teardown"
tags: ["tcp", "connections", "handshake", "state-machine"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://www.rfc-editor.org/rfc/rfc9293"]
---

# TCP Connections

## Summary
TCP provides reliable, ordered, byte-stream connections over IP, built around a handshake, sequence numbers, acknowledgments, and an explicit teardown. Its state machine — visible in tools like ss and netstat — explains most connectivity mysteries.

## Details
- The three-way handshake: client sends SYN, server replies SYN-ACK, client sends ACK; sequence numbers are chosen per side (ISN) to protect against stale segments.
- Established state tracks sent-but-unacknowledged data in a send window and received data in a receive window; ACKs are cumulative.
- Flow control: the receiver advertises a window; congestion control (cubic, BBR) paces the sender independently.
- Teardown is four-way: each side sends FIN and receives ACK; the side receiving FIN enters CLOSE_WAIT and must close its own half.
- TIME_WAIT holds closed connections for 2*MSL (about 60s) so delayed segments cannot corrupt new connections; too many TIME_WAIT sockets can exhaust ports.
- Half-open connections die via keepalive or timeout; /proc/net/tcp and ss -tan show all states and local/remote endpoints.
- New connections queue in the listen backlog; a full backlog causes SYN drops or RSTs under load.

## Related
- [[wiki/os-shell/udp-and-datagrams|UDP & Datagrams]] — the connectionless alternative
- [[wiki/os-shell/tcp-ports-and-services|TCP Ports & Services]] — endpoints and well-known ports
- [[wiki/os-shell/network-sockets|Network Sockets]] — the API driving the state machine
- [[wiki/os-shell/tcpdump|tcpdump]] — watching handshakes and teardown on the wire
- [[wiki/os-shell/osi-model-and-tcp-ip|OSI Model & TCP/IP]] — where TCP sits in the stack
