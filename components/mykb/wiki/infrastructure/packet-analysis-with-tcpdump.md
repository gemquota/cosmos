---
type: "concept"
title: "Packet Analysis with tcpdump"
description: "Capturing and interpreting packets to debug networks"
tags: ["tcpdump", "packets", "analysis", "debugging"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: [
  "https://www.tcpdump.org/manpages/tcpdump.1.html",
  "https://www.tcpdump.org/",
]
---

# Packet Analysis with tcpdump

## Summary
tcpdump captures and decodes packets at the interface, the first tool for network debugging. Filters select traffic with BPF expressions, and captures can be saved for deeper analysis. Reading tcpdump output is a core infrastructure skill.

## Details
- tcpdump attaches to an interface or pcap file, printing one line per packet with protocol-specific decoding.
- BPF filters such as 'host 10.0.0.1 and tcp port 443' run in the kernel, dropping non-matching packets before userspace sees them.
- Key flags: -i for interface, -n to disable name resolution, -w to write capture files, -c to limit packet count.
- Common workflows: SYN retransmission spotting, TLS ClientHello inspection, and verifying load balancer source IPs.
- The official man page documents every flag and example expression.
- In this cluster, tcpdump pairs with flow logs and network observability to complete the debugging toolkit.
- Physical and virtual layers interact here; the cabling, power, and rack articles document the physical side of these decisions.

## Related
- [[wiki/os-shell/resource-utilization-analysis|Resource Utilization Analysis]]
- [[wiki/infrastructure/tcpdump-filters-and-capture|tcpdump Filters & Capture]]
- [[wiki/os-shell/packet-analysis-and-capture|Packet Analysis]]
- [[wiki/devops-infra/root-cause-analysis|Root Cause Analysis]]
