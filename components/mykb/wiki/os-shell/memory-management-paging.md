---
type: "concept"
hub: true
title: "Memory Management & Paging"
description: "Virtual memory, page tables, and the MMU"
tags: ["memory", "paging", "virtual-memory", "kernel"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: [
  "https://docs.kernel.org/mm/index.html",
  "https://en.wikipedia.org/wiki/Paging",
]
---

# Memory Management & Paging

## Summary
Memory management virtualizes physical RAM with page tables and the MMU, giving each process an isolated address space. Paging, swapping, and the page cache make memory transparent to applications. It is the foundation of process isolation, performance, and system stability.

## Details
- Page tables map virtual pages to physical frames; the MMU caches translations in TLBs.
- The kernel documentation covers memory-management internals and concepts.
- Demand paging loads pages on first access, making virtual memory sparse and lazy.
- Swapping moves cold pages to disk; OOM handling reclaims under pressure.
- Transparent huge pages and NUMA policies tune performance.
- In mykb, memory management connects to swap, OOM killer, and process scheduling.
- Kernel memory accounting tracks allocations per cgroup for fair sharing.
- Memory hotplug and huge pages are important levers on large servers.
- Kernel and userspace behavior meet here; the related process, memory, and filesystem articles provide the implementation detail.
- Tuning this behavior in production relies on the system monitoring and resource utilization articles of this cluster.

## Related
- [[wiki/infrastructure/ssh-key-management|SSH Key Management]]
- [[wiki/infrastructure/security-information-and-event-management|SIEM]]
- [[wiki/cloud-infra/dns-management|DNS Management]]
- [[wiki/cloud-infra/quota-management|Quota Management]]
