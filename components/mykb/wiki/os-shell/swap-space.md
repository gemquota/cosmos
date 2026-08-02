---
type: "concept"
title: "Swap Space"
description: "Swap devices/files, swapping vs paging, and swappiness"
tags: ["swap", "swapping", "memory", "swappiness", "zram"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://docs.kernel.org/admin-guide/sysctl/vm.html", "https://man7.org/linux/man-pages/man8/swapon.8.html"]
---

# Swap Space

## Summary
Swap extends physical memory onto disk, letting the kernel evict idle anonymous pages and later fault them back in. Strictly, modern Linux pages (moves individual pages) rather than swaps whole processes, but the term "swap" persists for both the storage and the mechanism.

## Details
- Swap lives on dedicated partitions or swap files, both set up with mkswap and activated with swapon; files need no separate partition and are resizable.
- vm.swappiness (0-100, default 60) biases reclaim: higher values favor evicting anonymous pages to swap, lower values prefer reclaiming file cache.
- Anonymous memory (heap, stack, MAP_ANONYMOUS) must be swapped; file-backed pages are simply dropped and re-read, so swap only matters for anonymous data.
- zram creates a compressed RAM block device used as swap, common on embedded and Android devices to avoid wearing flash.
- swapoff(8) drains swap by moving pages back to RAM; it fails if memory is insufficient, making it a useful memory-pressure probe.
- Hibernation writes a memory image to swap (resume= kernel parameter), a different use from ordinary paging.
- Monitoring: /proc/swaps lists devices and usage; vmstat si/so columns show swap-in and swap-out rates.

## Related
- [[wiki/os-shell/paging|Paging]] — the mechanism swap participates in
- [[wiki/os-shell/virtual-memory|Virtual Memory]] — the address space that overflows to swap
- [[wiki/os-shell/memory-allocation|Memory Allocation]] — what happens when the heap is idle
- [[wiki/os-shell/system-monitoring-tools|System Monitoring]] — reading vmstat si/so and /proc/swaps
- [[wiki/os-shell/block-devices-and-partitions|Block Devices & Partitions]] — where swap partitions live
