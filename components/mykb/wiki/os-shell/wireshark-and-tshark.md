---
type: "concept"
title: "Wireshark & tshark"
description: "GUI/CLI dissection and follow-stream workflows"
tags: ["wireshark", "tshark", "analysis", "pcap"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://www.wireshark.org/docs/man-pages/tshark.html", "https://www.wireshark.org/docs/wsug_html_chunked/"]
---

# Wireshark & tshark

## Summary
Wireshark is the interactive packet analyzer: it dissects protocols into browsable trees, follows TCP streams, and filters with a display language far richer than BPF. tshark is its command-line twin for scripting and bulk analysis.

## Details
- The GUI shows packets in three panes: summary list, protocol tree, and raw bytes; clicking a field highlights the corresponding bytes.
- Display filters (vs capture filters): http.request, tcp.port==443, ip.addr==10.0.0.1, and field comparisons like tcp.flags.syn==1.
- Follow TCP Stream reassembles a connection's payload — the fastest way to read an HTTP or TLS exchange (TLS needs keys).
- Decrypt TLS with (Pre)-Master-Secret logs: set the SSLKEYLOGFILE env var in browsers/curl and point Wireshark at it.
- tshark -r file.pcap -Y 'http' -T fields -e http.host -e http.request.uri prints structured output for scripts.
- Statistics menus produce endpoint tables, conversations, and protocol hierarchies for traffic characterization.
- Export Objects extracts files (images, executables) transferred over HTTP or SMB from a capture.

## Related
- [[wiki/os-shell/tcpdump|tcpdump]] — the capture partner
- [[wiki/os-shell/packet-analysis-and-capture|Packet Analysis]] — the pcap workflow
- [[wiki/os-shell/http-basics|HTTP Basics]] — the protocol most commonly dissected
- [[wiki/os-shell/tls-and-https|TLS & HTTPS]] — decrypting TLS sessions
- [[wiki/security-auth/indicators-of-compromise|Indicators of Compromise]] — hunting in captures
