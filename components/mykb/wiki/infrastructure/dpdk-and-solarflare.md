---
type: "concept"
title: "DPDK & Solarflare"
description: "Userspace packet processing bypassing the kernel stack"
tags: ["dpdk", "userspace", "networking", "performance"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# DPDK & Solarflare

## Summary
DPDK (Data Plane Development Kit) and Solarflare/Onload are technologies for userspace packet processing that bypass the kernel networking stack. The kernel stack — interrupts, softirqs, per-packet locking, syscall boundaries — can only process a few million packets per second per core; DPDK-style designs push tens of millions, by letting applications own the NIC directly. This is the hardware base under kernel-bypass networking, low-latency trading, and high-performance packet processing.

## Details
- The kernel's cost structure: each packet traverses the NIC driver, interrupt handling, the protocol stack (TCP/IP), and the socket layer — with locks, copies, and context switches along the way. At high packet rates (small packets, high pps), the per-packet overhead dominates and throughput collapses far below the link rate. The kernel-bypass answer: remove the kernel from the path entirely.
- DPDK works by giving the application direct, safe access to the NIC: a userspace driver (poll-mode driver, PMD) maps NIC queues into application memory, the app polls those queues continuously (no interrupts — busy polling), and packets are processed in the application's own loops with its own memory pools and lock-free ring buffers. The wins: no syscalls, no interrupts, no kernel copies, no per-packet locks — just an application loop reading and writing packet buffers. The costs: the application owns the NIC (the kernel stack on that interface is bypassed, so normal networking tools stop seeing the traffic), CPU cores are burned on polling (the latency win comes from never sleeping), and the stack must be reimplemented by the application (TCP is hard; most DPDK users run user-space TCP stacks or offload to hardware).
- Solarflare (Onload) took a different route to the same goal: the NIC's firmware accelerates the kernel stack — full TCP offload in silicon, with the kernel's data structures implemented in the card, so applications use normal sockets (no rewrite) and get kernel-bypass performance. The tradeoff: the magic lives in proprietary silicon with limited generality, while DPDK is open and flexible but demands application rewrites.
- The operational tradeoffs: kernel-bypass networking breaks the standard tooling (tcpdump sees nothing, the OS thinks the NIC is idle), complicates multi-tenancy (the app owns the hardware), and requires careful CPU pinning and NUMA awareness; in exchange it delivers the deterministic microsecond-scale latency that trading and network-function workloads need.
- For mykb: DPDK/Solarflare sit under the kernel-bypass, packet-capture-performance, and high-performance networking nodes — the hardware layer that makes those techniques possible.

## Related
- [[wiki/infrastructure/storage-systems|Storage Systems]] — related coverage in the same cluster
- [[wiki/infrastructure/ospf-protocols|OSPF Protocols]] — related coverage in the same cluster
- [[wiki/syntheses/knowledge-acquisition-workflow|Knowledge Acquisition Workflow]] — how stubs grow into full articles in mykb
- [[wiki/syntheses/mykb-acquisition-curation-and-practices|Acquisition, Curation & Practices]] — the curation loop this stub belongs to
