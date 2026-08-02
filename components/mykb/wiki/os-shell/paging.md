---
type: "concept"
title: "Paging"
description: "Page-based memory management, page faults, and demand paging"
tags: ["paging", "page-faults", "memory", "demand-paging", "page-cache"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://docs.kernel.org/admin-guide/mm/index.html"]
---

# Paging

## Summary
Paging is the memory-management scheme in which virtual and physical memory are divided into fixed-size pages, typically 4 KiB on x86. Pages are the unit of mapping, protection, and transfer to and from swap, and they enable demand paging: memory is only brought in when actually touched.

## Details
- A page fault occurs when a process accesses an address whose page is not present in its page table; the kernel handles it by allocating a frame, reading from disk, or killing the process if the access was invalid.
- Minor faults resolve without disk I/O (zero-filled or already-cached pages); major faults involve reading from storage and are far more expensive.
- Demand paging means executable text and mapped files load lazily, page by page, so programs start without reading their entire binary.
- The page cache reuses pages of file data across processes, so repeated reads and mapped-file faults hit RAM.
- Reclaim: when memory is short, the kernel evicts clean file pages and writes back dirty ones, and moves anonymous pages to swap.
- Huge pages (2 MiB, 1 GiB) reduce page-table and TLB overhead for large workloads, managed via THP or explicit hugetlbfs.
- Accounting lives in /proc/meminfo and /proc/vmstat; pgfault and pgmajfault counters show fault behavior over time.

## Related
- [[wiki/os-shell/virtual-memory|Virtual Memory]] — the abstraction paging implements
- [[wiki/os-shell/page-tables|Page Tables]] — the structures that record present pages
- [[wiki/os-shell/swap-space|Swap Space]] — the disk store for evicted anonymous pages
- [[wiki/os-shell/memory-mapped-files|Memory-Mapped Files]] — file pages delivered on demand
- [[wiki/os-shell/tlb-cache|TLB & Caching]] — caching page translations to avoid walks
