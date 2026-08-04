---
type: "entity"
title: "tcpdump"
description: "Capture syntax, filters, and common patterns"
tags: ["tcpdump", "capture", "filters", "cli"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://www.tcpdump.org/manpages/tcpdump.1.html"]
---

# tcpdump

## Summary
tcpdump captures and prints packets from the command line using Berkeley Packet Filter (BPF) syntax. It is the first tool for live network debugging: checking that traffic flows, finding which host talks to which port, and dumping sessions to a file.

## Details
- Basics: tcpdump -i eth0 captures on an interface; -i any covers all; -n disables name resolution; -nn also skips port names.
- Filters: host 8.8.8.8, net 192.168.0.0/24, port 443, and combos like tcp port 80 and not host 10.0.0.5.
- -w file.pcap writes raw packets for later analysis; -r file.pcap reads them; -c N stops after N packets.
- Payload views: -A prints ASCII, -X hex+ASCII, -s 0 sets full snaplen (default is enough for headers).
- Common recipes: tcpdump -nn -i any port 53 (DNS), 'tcp[tcpflags] & tcp-syn != 0' (SYN scan detection), port 443 (TLS ClientHello).
- Reading output: the classic line shows timestamp, src > dst, flags (S for SYN, P push, F FIN), sequence numbers, and lengths.
- Privileges: capturing usually needs root or CAP_NET_RAW; dumpcap is the capture engine behind Wireshark/tshark.

## Related
- [[wiki/os-shell/packet-analysis-and-capture|Packet Analysis]] — the capture ecosystem
- [[wiki/os-shell/wireshark-and-tshark|Wireshark & tshark]] — richer analysis of the same files
- [[wiki/os-shell/tcp-connection-lifecycle|TCP Connections]] — interpreting the flags tcpdump prints
- [[wiki/os-shell/icmp-and-network-diagnostics|ICMP & Diagnostics]] — filtering ping and errors
- [[wiki/os-shell/dns-resolution|DNS Resolution]] — watching port 53 traffic
