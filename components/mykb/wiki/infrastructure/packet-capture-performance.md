---
type: "concept"
title: "Packet Capture Performance"
description: "Capture at line rate with ring buffers, offloads, and filters"
tags: ["capture", "performance", "tcpdump", "packets"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# Packet Capture Performance

## Summary
Packet capture performance is the art of capturing every packet at line rate without dropping any — which is much harder than it sounds. A busy 10/25/40G interface can generate millions of packets per second, and the default capture path (kernel → socket → userspace → file) drops packets once the pipeline saturates; the discipline is the set of mechanisms — ring buffers, offloads, and filters — that keep the capture pipeline ahead of the traffic.

## Details
- The drop point is the bottleneck. Packets arrive at the NIC; the driver places them in a ring buffer (RX ring); the kernel processes them and delivers to the capture socket (AF_PACKET); the application (tcpdump/Wireshark) writes them to disk. Drops happen when any stage is slower than the arrival rate: the RX ring overflows (NIC drops, counted in `ethtool -S` as rx_fifo_errors or the driver's dropped counter), the socket buffer overflows (the kernel drops before userspace reads), or the application cannot write fast enough (disk throughput). The captured count can look fine while captures are silently incomplete — which is why the discipline starts with knowing which drop counter to watch.
- The mechanisms, in order of impact: filter at the earliest point (a BPF filter runs in the kernel — or on the NIC with hardware filters — so packets that do not match never enter the capture pipeline; filtering on a 10G link can reduce the capture load by orders of magnitude); enlarge the ring buffers (bigger RX rings and socket buffers absorb bursts — the first fix to try); use zero-copy capture (AF_PACKET with PACKET_MMAP, or PF_RING — the kernel DMA's directly into the application's mapped ring, removing a copy and the syscall per packet); and capture to fast storage (dedicated NVMe, or a RAM buffer with background flush — disk is usually the final bottleneck).
- The measurement: the packet rate, not the bit rate, is the stressor — 1G of 64-byte packets is ~1.5M pps (hard for the default path); 10G of 64-byte packets is ~14.9M pps (impossible without zero-copy and careful tuning). The counters to watch: the NIC's dropped counter, the kernel's packet socket drops (`netstat -s`), and the application's own count — and the rule: if the drop counters are nonzero, the capture is incomplete and the analysis is suspect.
- The failure modes: the capture tool itself distorting the traffic (a capture that consumes CPU on the very host being measured), disk exhaustion mid-capture (the classic "the capture stopped at 3am"), and the filter mistake (a too-narrow BPF filter that silently captures nothing interesting).
- For mykb: capture performance is the engineering layer under the tcpdump cluster — filters, packet analysis, and the capture tooling all build on getting packets to disk losslessly.

## Related
- [[wiki/infrastructure/packet-analysis-with-tcpdump|Packet Analysis with tcpdump]]
- [[wiki/infrastructure/tcpdump-filters-and-capture|tcpdump Filters & Capture]]
- [[wiki/cloud-infra/tls-performance|TLS Performance]]
- [[wiki/os-shell/packet-analysis-and-capture|Packet Analysis]]
- [[wiki/infrastructure/storage-systems|Storage Systems]]
