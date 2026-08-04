---
type: "entity"
title: "eBPF & XDP"
description: "In-kernel programmable packet and tracing paths"
tags: ["eBPF", "XDP", "kernel", "observability"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: [
  "https://ebpf.io/what-is-ebpf/",
  "https://docs.kernel.org/bpf/index.html",
]
---

# eBPF & XDP

## Summary
eBPF runs sandboxed programs inside the Linux kernel for observability, networking, and security, while XDP processes packets at the earliest driver stage. Together they enable high-performance programmable infrastructure. They are a defining technology of modern Linux networking.

## Details
- eBPF programs attach to kernel hooks and are verified before loading, preventing unsafe memory access and unbounded loops before they can ever run.
- XDP attaches eBPF programs to network drivers, handling packets before the kernel stack and reaching millions of packets per second.
- Use cases include packet filtering, DDoS mitigation, load balancing, and fine-grained tracing with minimal overhead.
- The kernel documentation covers the BPF infrastructure, including maps for sharing data with userspace.
- Tools such as bpftrace and Cilium build on eBPF to deliver tracing and Kubernetes networking.
- For mykb, eBPF connects kernel, networking, and observability clusters, and it is how modern security agents see traffic.
- Kernel and userspace behavior meet here; the related process, memory, and filesystem articles provide the implementation detail.

## Related
- [[wiki/os-shell/namespace-networking|Namespace Networking]]
- [[wiki/os-shell/kernel-modules-and-loading|Kernel Modules & Loading]]
- [[wiki/os-shell/access-control-lists|Access Control Lists]]
- [[wiki/os-shell/ansi-escape-sequences|ANSI Escape Sequences]]
