---
type: "concept"
title: "tcpdump Filters & Capture"
description: "BPF filter expressions and capture files for packet analysis"
tags: ["tcpdump", "capture", "bpf", "packets"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# tcpdump Filters & Capture

## Summary
tcpdump filters are Berkeley Packet Filter (BPF) expressions that select which packets get captured or printed, keeping the capture narrow enough to be useful on busy interfaces. Mastering filter expressions and capture-file mechanics is what separates targeted debugging from drowning in traffic.

## Details
- Filter syntax: expressions combine primitives with logical operators — `host 10.0.0.5`, `tcp port 443`, `net 192.168.1.0/24`, `tcp[tcpflags] & tcp-syn != 0` — joined by `and`, `or`, `not`. Parentheses group conditions, and quoting protects them from the shell.
- Capture mechanics: `-i` selects the interface, `-w file.pcap` writes raw packets, `-c N` stops after N packets, `-s 0` captures full frames instead of truncated headers, and `-n` disables name resolution. Use `-Z` to drop privileges and `-B` to tune the kernel buffer for bursty traffic.
- Concrete examples: capture only new connections to a host (`tcp and host db01 and tcp[tcpflags] & tcp-syn != 0 and tcp[tcpflags] & tcp-ack == 0`); capture DNS queries to one resolver (`udp port 53 and host 1.1.1.1`); or capture a full web conversation excluding health checks (`tcp port 443 and not host 127.0.0.1`).
- Failure modes: filters that are too broad produce huge files and drop packets at the kernel buffer; filters that are too narrow miss the packets you need, and you cannot re-filter what you did not capture — BPF filters discard before capture, while display filters in Wireshark only hide afterward.
- Tradeoffs: filter early to keep captures small and cheap, but keep a "capture everything, filter on display" copy for complex investigations where you do not yet know the signature; the cost is disk and processing time.
- Operational practice: always record `-nn` to keep IPs readable, capture with timestamps enabled for later RTT analysis, and use `-w` files rather than screen output for anything beyond a quick look, since printing itself drops packets under load.
- RSIS3/mykb relevance: precise capture is the observability primitive that validates network claims; this node supplies the filter vocabulary loops need to define what "the right packets" means before starting a capture.

## Related
- [[wiki/infrastructure/egress-and-ingress-filters|Egress & Ingress Filters]]
- [[wiki/infrastructure/packet-analysis-with-tcpdump|Packet Analysis with tcpdump]]
- [[wiki/infrastructure/egress-proxies-and-filters|Egress Proxies & Filters]]
- [[wiki/infrastructure/tcpdump-and-wireshark|tcpdump & Wireshark]]
