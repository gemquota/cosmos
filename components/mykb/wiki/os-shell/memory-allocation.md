---
type: "concept"
title: "Memory Allocation"
description: "malloc/brk/mmap paths, heap growth, and allocator behavior"
tags: ["malloc", "heap", "allocator", "memory", "brk"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://man7.org/linux/man-pages/man3/malloc.3.html", "https://man7.org/linux/man-pages/man2/brk.2.html"]
---

# Memory Allocation

## Summary
User programs rarely call the kernel for memory directly: libc malloc(3) manages the heap on top of two kernel mechanisms — brk(2), which grows the heap segment, and mmap(2), which creates anonymous mappings. The allocator batches requests to keep syscalls rare.

## Details
- Small allocations are served from bins and the per-thread tcache, making malloc cheap; large allocations (above about 128 KiB) go straight to mmap and are unmapped on free.
- brk moves the program break, the top of the heap; it only works for the main arena and cannot return memory when later allocations pin the top.
- glibc malloc maintains multiple arenas to reduce lock contention between threads; arena count scales with CPU count.
- Freeing does not return memory to the OS immediately: the allocator keeps chunks for reuse, and malloc_trim(3) can release top-of-heap pages.
- Overcommit means malloc can succeed with no physical memory behind it; the OOM killer fires only when pages are actually touched.
- Fragmentation costs: the allocator rounds sizes to chunk boundaries (16-byte granularity) and may fail to reuse scattered free chunks.
- Tools for diagnosis: valgrind/massif, glibc tunables (MALLOC_ARENA_MAX), and /proc/<pid>/statm to observe RSS and heap growth.

## Related
- [[wiki/os-shell/virtual-memory|Virtual Memory]] — the address space malloc operates in
- [[wiki/os-shell/memory-mapped-files|Memory-Mapped Files]] — mmap is also the large-allocation path
- [[wiki/os-shell/memory-fragmentation|Memory Fragmentation]] — the allocator's core problem
- [[wiki/os-shell/ulimit-and-resource-limits|Resource Limits]] — RLIMIT_AS bounds total address space
- [[wiki/os-shell/swap-space|Swap Space]] — where idle anonymous pages end up
