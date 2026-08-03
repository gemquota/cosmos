---
type: "concept"
title: "RoCE & RDMA over TCP"
description: "RDMA over converged Ethernet and TCP variants"
tags: ["roce", "rdma", "ethernet", "storage"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# RoCE & RDMA over TCP

## Summary
Remote Direct Memory Access (RDMA) lets one host read or write another host's memory without the source or destination CPU and OS kernel touching the data path. RoCE (RDMA over Converged Ethernet) and RDMA-over-TCP variants are the two main ways to run that capability on commodity Ethernet instead of InfiniBand, trading fabric guarantees for lower cost and familiar tooling.

## Details
- Mechanism: hosts register memory regions with the NIC, exchange queue pairs (QPs) and memory keys, then let the adapter DMA data directly between buffers. Verbs such as send/recv, RDMA read, and RDMA write are issued from userspace, and completions land on a shared completion queue without syscalls or copies.
- RoCE: RoCEv1 operates on a single L2 Ethernet segment, while RoCEv2 wraps the RDMA payload in UDP/IP so it can route across L3 networks. Both assume a lossless or near-lossless fabric: RoCE has no built-in retransmission, so dropped packets can stall QPs for tens of seconds or push them into fatal error states.
- RDMA over TCP: iWARP and the NVMe/TCP stack carry RDMA-style semantics over TCP, inheriting congestion control and retransmission. The price is CPU overhead for segmentation, checksums, and copies, plus added latency, which is why it fits cloud environments that cannot guarantee lossless Ethernet.
- Failure modes: PFC (priority flow control) storms under head-of-line blocking, out-of-order delivery breaking older RoCEv2 NICs, memory-registration leaks, and QP timeouts tuned below the real fabric latency. On lossy fabrics RoCE tails degrade from microseconds to milliseconds.
- Operational tradeoffs: RoCE demands careful DCB/PFC configuration, dedicated lossless traffic classes, and isolation from bursty flows; RDMA over TCP tolerates shared networks but consumes more CPU per byte. Mixed fabrics often run RoCE for storage replication and TCP variants for control and management traffic.
- RSIS3/mykb relevance: when self-improvement cycles evaluate infrastructure choices, this node separates protocol choice from fabric guarantees so retrieval does not collapse RDMA into a single undifferentiated answer.

## Related
- [[wiki/cloud-infra/tcp-ip-stack|TCP/IP Stack]] — related coverage in the same cluster
- [[wiki/cloud-infra/udp-vs-tcp|UDP vs TCP]] — related coverage in the same cluster
- [[wiki/infrastructure/nvme-over-fabrics-tcp|NVMe over Fabrics (TCP)]] — related coverage in the same cluster
- [[wiki/cloud-infra/tcp-retransmission|TCP Retransmission]] — related coverage in the same cluster
- [[wiki/syntheses/knowledge-acquisition-workflow|Knowledge Acquisition Workflow]] — how stubs grow into full articles in mykb
- [[wiki/syntheses/mykb-acquisition-curation-and-practices|Acquisition, Curation & Practices]] — the curation loop this stub belongs to
