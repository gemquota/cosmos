---
type: "concept"
title: "Packet Analysis"
description: "Capture, filtering, and protocol decoding"
tags: ["packet", "capture", "pcap", "network"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://www.tcpdump.org/manpages/pcap.3pcap.html", "https://wiki.wireshark.org/CaptureSetup"]
---

# Packet Analysis

## Summary
Packet capture records raw traffic off an interface for inspection. The pcap library is the capture standard, tcpdump and tshark are the CLI readers, and Wireshark adds interactive dissection — together they turn network behavior into evidence.

## Details
- Capture basics: interfaces must be in promiscuous mode to see all traffic; capture filters (BPF) reduce what is recorded.
- BPF filters: tcp port 443, host 10.0.0.1, or combinations with and/or/not — compiled in the kernel for efficiency.
- Files: pcap and pcapng formats store packets with timestamps; tcpdump -w writes, -r reads, and both tools interoperate.
- Offload complications: NIC checksum and segmentation offloads make captured packets look malformed; tools can compensate.
- Decoding: dissectors parse protocols up the stack — Ethernet, IP, TCP, HTTP, TLS — and highlight anomalies.
- Capture points: SPAN ports and TAPs mirror traffic; on the host, loopback captures miss nothing since traffic never leaves the NIC.
- Privacy and security: captures contain payloads; rotate and protect files, and capture only the fields needed.

## Related
- [[wiki/os-shell/tcpdump|tcpdump]] — the capture CLI
- [[wiki/os-shell/wireshark-and-tshark|Wireshark & tshark]] — interactive dissection
- [[wiki/os-shell/link-layer-ethernet-and-arp|Link Layer, Ethernet & ARP]] — the frames being captured
- [[wiki/os-shell/tcp-connection-lifecycle|TCP Connections]] — the flows to analyze
- [[wiki/security-auth/indicators-of-compromise|Indicators of Compromise]] — packet evidence in incident response
