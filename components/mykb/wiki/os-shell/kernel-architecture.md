---
type: "concept"
title: "Kernel Architecture"
description: "The monolithic kernel and its core subsystems"
tags: ["kernel", "architecture", "linux", "subsystems"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: [
  "https://docs.kernel.org/",
  "https://en.wikipedia.org/wiki/Linux_kernel",
]
---

# Kernel Architecture

## Summary
The Linux kernel is a monolithic core with modular subsystems: scheduling, memory, filesystems, networking, and device drivers. Its design trades isolation for performance, with modules and eBPF adding extensibility. This node anchors the OS-shell kernel cluster in the mykb graph.

## Details
- Monolithic design runs most services in kernel space for speed, with modules for hardware support.
- The kernel documentation portal catalogs every subsystem's documentation.
- Process, memory, VFS, networking, and block layers communicate through well-defined APIs.
- Loadable modules and eBPF extend the kernel without rebooting.
- Kernel versions drive feature availability: security, scheduling, and I/O improvements land every release.
- In mykb, kernel architecture connects to syscalls, scheduling, memory, and filesystem articles.
- Subsystem interaction is mediated by kernel APIs, keeping the whole system testable and coherent.
- Debugging infrastructure such as ftrace and kprobes exposes kernel behavior to operators.
- Kernel and userspace behavior meet here; the related process, memory, and filesystem articles provide the implementation detail.

## Related
- [[wiki/devops-infra/node-storage-architecture|Node Storage Architecture]]
- [[wiki/os-shell/kernel-modules-and-loading|Kernel Modules & Loading]]
- [[wiki/infrastructure/bigquery-architecture|Bigquery Architecture]]
- [[wiki/infrastructure/pulsar-architecture-and-tiers|Pulsar Architecture And Tiers]]
