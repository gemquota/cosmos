---
type: "concept"
title: "tcpdump & Wireshark"
description: "Capture and analysis workflow from CLI filters to GUI dissection"
tags: ["tcpdump", "wireshark", "capture", "analysis"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# tcpdump & Wireshark

## Summary
tcpdump and Wireshark form the canonical packet-analysis workflow: tcpdump captures and filters packets on the CLI, and Wireshark (or its terminal sibling tshark) dissects, follows, and visualizes them. Together they turn "the network is slow" into a specific, reproducible sequence of packets.

## Details
- Mechanism: both tools read packets through libpcap, which taps the interface at the data-link layer; tcpdump applies BPF filter expressions before capture to keep only relevant traffic, while Wireshark dissects the full capture with protocol decoders that reconstruct conversations.
- Typical workflow: capture on the server with a narrow filter (`tcpdump -i eth0 -w server.pcap host 10.0.0.5 and tcp port 443`), capture at both ends if possible, then open the file in Wireshark, use "Follow TCP Stream" to see the conversation, and use statistics (conversations, endpoints, IO graphs) to find retransmissions and gaps.
- Concrete example: a user reports intermittent latency to an API. A capture shows TCP retransmissions and duplicate ACKs on the receive side while the send side shows nothing unusual, pointing to packet loss on the path rather than application slowness — confirmed by checking drop counters and switch errors.
- Failure modes: capturing on the wrong interface or missing VLAN tags and tunnels makes filters miss traffic; buffer overruns drop packets silently (`tcpdump: dropped packets`); timestamps without sub-second precision or with clock skew corrupt RTT analysis; and running a verbose capture on a busy production interface adds load and perturbs the very behavior being measured.
- Tradeoffs: tcpdump is fast, scriptable, and available everywhere, but its output is hard to read for complex protocols; Wireshark's GUI and decoders are powerful but heavyweight for automation — tshark fills the middle ground. Capture files are also a privacy and compliance concern: packet payloads may contain credentials or PII.
- Operational practice: cap capture file size with rotation, use `-nn` to avoid DNS lookups, always record the capture time and interface, and prefer capturing at the endpoint closest to the suspected fault before adding taps.
- RSIS3/mykb relevance: packet-level evidence is the ground truth loops use to validate network hypotheses; this node keeps the capture-and-dissect workflow retrievable so telemetry claims can be checked against actual bytes.

## Related
- [[wiki/infrastructure/packet-analysis-with-tcpdump|Packet Analysis with tcpdump]]
- [[wiki/infrastructure/tcpdump-filters-and-capture|tcpdump Filters & Capture]]
- [[wiki/os-shell/tcpdump|tcpdump]]
- [[wiki/os-shell/wireshark-and-tshark|Wireshark & tshark]]
- [[wiki/infrastructure/storage-systems|Storage Systems]]
- [[wiki/syntheses/knowledge-acquisition-workflow|Knowledge Acquisition Workflow]] — how stubs grow into full articles in mykb
- [[wiki/syntheses/mykb-acquisition-curation-and-practices|Acquisition, Curation & Practices]] — the curation loop this stub belongs to
