---
type: "concept"
title: "RDMA & InfiniBand"
description: "Remote memory access with ultra-low latency fabrics"
tags: ["rdma", "infiniband", "networking", "hpc"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# RDMA & InfiniBand

## Summary
RDMA (Remote Direct Memory Access) lets one computer read or write another computer's memory directly over the network — bypassing the remote CPU, its kernel, and its protocol stack entirely. InfiniBand is the original and highest-performance fabric for RDMA: a dedicated switched network with hardware transport offload, sub-microsecond latency, and lossless delivery. Together they are the interconnect of HPC and AI training clusters, where collective operations (all-reduce) over ordinary TCP would spend more time in protocol overhead than in useful work.

## Details
- The mechanism: RDMA works because the NIC (HCA — host channel adapter, in InfiniBand terms) does the work. The application registers memory regions (pinning them), the NIC reads/writes them directly via DMA, and the remote NIC places the data in the remote application's memory — no remote CPU involvement, no kernel on either side, no copies. The verbs API (ibverbs) exposes the operations: send/receive (like messages), RDMA read/write (direct memory access), and atomic operations. The latency profile: a single-digit-microsecond round trip, versus tens to hundreds of microseconds for TCP on the same hardware — because the protocol stack, the copies, and the remote CPU are all gone.
- InfiniBand as a fabric: dedicated switches and links (EDR 100G, HDR 200G, NDR 400G generations) with hardware flow control that makes the fabric lossless (no packet drops, so no retransmission, so latency stays flat) and congestion control for the all-to-all patterns of HPC workloads. The network is a separate physical plant — its own switches, cabling (active optical or copper), and management (subnet manager — the control plane that configures the fabric, computes paths, and handles failover). The tradeoff is total: InfiniBand delivers the best latency and throughput at the cost of a parallel network infrastructure that must be built, operated, and learned.
- RDMA beyond InfiniBand: RoCE (RDMA over Converged Ethernet — RDMA on ordinary Ethernet, with the lossless requirement delegated to PFC priority flow control) and iWARP (RDMA over TCP) let RDMA run on the existing fabric — cheaper, but with more tuning (RoCE's performance collapses if the Ethernet fabric drops packets, since RDMA does not retransmit). The GPU-to-GPU layer (GPUDirect RDMA, NVLink+InfiniBand in supercomputers) extends the model into accelerator memory, which is why the largest AI training runs use InfiniBand or RoCE rather than TCP.
- Failure modes: lossless-fabric misconfiguration (a PFC deadlock or a buffer that cannot absorb a burst — the fabric head-of-line blocks), subnet manager failure (the InfiniBand control plane dies — the fabric stops learning paths), and the observability gap: RDMA traffic is invisible to standard tools (tcpdump sees nothing), so monitoring requires the fabric's own counters.
- For mykb: RDMA/InfiniBand anchors the HPC-interconnect branch — RoCE (the Ethernet version), NVMe-oF (RDMA for storage), and kernel bypass (the same "remove the CPU" philosophy) connect here.

## Related
- [[wiki/infrastructure/roce-and-rdma-over-tcp|RoCE & RDMA over TCP]]
