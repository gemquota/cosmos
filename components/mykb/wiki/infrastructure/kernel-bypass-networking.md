---
type: "concept"
title: "Kernel-Bypass Networking"
description: "Direct NIC access from userspace for extreme throughput"
tags: ["bypass", "kernel", "nic", "networking"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# Kernel-Bypass Networking

## Summary
Kernel-bypass networking gives applications direct access to the NIC from userspace, removing the kernel's networking stack from the data path. It exists because the kernel stack — however well engineered — pays a per-packet cost (interrupts, locking, copies, syscalls) that caps throughput around a few million packets per second per core, far below what modern NICs can deliver; bypass designs push tens of millions of packets per second by letting the application own the hardware.

## Details
- The kernel's cost structure, in detail: each packet triggers an interrupt (or busy-poll wakeup), the driver copies the packet into kernel memory (or DMA's it), the protocol stack processes it through socket buffers with locks, and the application receives it through a syscall boundary that may copy again. Small packets — 64-256 bytes, the worst case for pps rates — make the per-packet overhead dominate: the kernel can be the bottleneck at a fraction of the link's bandwidth. Bypass removes the stack from the path: the NIC DMA's packets into application-owned memory, and the application polls the queues directly.
- The implementation families: DPDK (open, userspace drivers with poll-mode — the application takes full ownership of NIC queues, memory pools, and the processing loop; the kernel stack on that interface is bypassed entirely), RDMA (the NIC offloads the transport — data is placed directly into application memory by hardware, with kernel involvement only for connection setup), XDP (the in-kernel compromise — a BPF program runs on the packet in the driver context, before the stack, delivering most of the performance win while keeping kernel safety and tooling), and SmartNICs (the NIC itself runs the packet-processing program, offloading even the application CPU). Each trades control, complexity, and ecosystem compatibility differently.
- The costs: the application reimplements what the kernel gave for free — TCP is genuinely hard in userspace (the reason most DPDK deployments run UDP, or a userspace TCP stack, or offload TCP to hardware); normal tooling stops working (tcpdump sees nothing on a bypassed interface, the OS reports the NIC idle); the application owns the hardware (multi-tenancy and sharing become the app's problem); and CPU cores are consumed polling (the latency win comes from never sleeping — busy-polling burns a core).
- The decision framework: use kernel-bypass when the workload is packet-rate-bound and the latency/throughput targets cannot be met through the kernel (trading, packet brokers, network functions, storage data paths); otherwise the kernel — with modern tuning (multi-queue, RSS, busy polling, XDP where it fits) — is almost always the right choice: simpler, safer, and compatible with everything.
- For mykb: kernel bypass is the mechanism under the high-performance networking cluster — DPDK, RDMA/RoCE, and packet-capture performance all build on this tradeoff.

## Related
- [[wiki/cloud-infra/networking-fundamentals|Networking Fundamentals]]
- [[wiki/infrastructure/vlan-networking|VLAN Networking]]
- [[wiki/cloud-infra/multicast-networking|Multicast Networking]]
- [[wiki/infrastructure/software-defined-networking|Software-Defined Networking]]
- [[wiki/syntheses/knowledge-acquisition-workflow|Knowledge Acquisition Workflow]] — how stubs grow into full articles in mykb
- [[wiki/syntheses/mykb-acquisition-curation-and-practices|Acquisition, Curation & Practices]] — the curation loop this stub belongs to
