---
type: "concept"
title: "MTU & Fragmentation"
description: "Maximum transmission unit limits and how oversized packets get handled"
tags: ["mtu", "fragmentation", "networking", "tcp"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---
# MTU & Fragmentation

## Summary

MTU is the largest packet a link carries (typically 1500 bytes, jumbo 9000 on internal networks); fragmentation splits packets that exceed the next hop's MTU. Mismatches cause black holes, especially with encapsulation and IPv6, where routers do not fragment.

## Details
- Mechanism: IP fragmentation splits oversized packets (with reassembly at the destination); the DF (don't fragment) bit forces senders to learn the path MTU via ICMP; IPv6 removed router fragmentation entirely — only the source fragments, so PMTUD failures black-hole traffic. Encapsulation (VXLAN +36B, GRE, IPsec, tunnels) shrinks effective MTU, and MSS clamping on TCP is the standard workaround.
- Concrete example: a VXLAN overlay with 1500 MTU underlay needs 1450 or 1400 tenant MTU to fit headers; a VPN tunnel delivering 1500 MTU payloads but dropping ICMP packet-too-big messages silently stalls transfers — the classic MTU black hole; jumbo frames inside a datacenter cut CPU and latency for storage traffic but break at any legacy hop.
- Failure modes: assuming 1500 everywhere (tunnels, PPPoE, carrier networks reduce it); ICMP filtered, breaking PMTUD (allow ICMP type 3 code 4); inconsistent MTU across a path causing mystery packet loss at exactly the fragment threshold; and IPv6 deployments with no MSS clamping path.
- Operational tradeoffs: standardize on 1500 for internet-facing paths and 9000 internally where the whole path supports it; document MTU per segment and verify with ping -M do sweeps. When encapsulation is involved, set the tenant MTU deliberately rather than discovering black holes in production.
- RSIS3/mykb relevance: the wiki's tunneled lab networks would record per-link MTUs and MSS clamps, so the loop's connectivity tests start from known-good values.
- Verification: probe each segment with df-bit ping sweeps at decreasing sizes to find the path MTU; the sweep is minutes of work that prevents the classic black-hole outage. Record the discovered MTU per link in the wiki so later sweeps have a baseline to diff against.

## Related
- [[wiki/os-shell/memory-fragmentation|Memory Fragmentation]]
