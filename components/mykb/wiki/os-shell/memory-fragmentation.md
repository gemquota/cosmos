---
type: "concept"
title: "Memory Fragmentation"
description: "Internal vs external fragmentation, compaction, and impact"
tags: ["fragmentation", "memory", "allocator", "compaction"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://docs.kernel.org/admin-guide/mm/index.html"]
---

# Memory Fragmentation

## Summary
Fragmentation is wasted memory: internal fragmentation pads allocations beyond what is needed, while external fragmentation leaves scattered free chunks too small to satisfy a large request. Both lower effective capacity and can force expensive cleanup work.

## Details
- Internal fragmentation is the slack inside an allocated unit — a slab rounding a 33-byte object to 64 bytes, or a page partially used by a small file.
- External fragmentation is the checkerboard problem: total free memory exists, but no contiguous run is large enough for the request.
- The buddy allocator splits and merges power-of-two page blocks, which makes merging easy but can strand blocks when pages are pinned in the wrong order.
- Slab allocators (kmalloc, SLUB) serve same-size kernel objects from caches, trading internal slack for speed and reduced fragmentation.
- Compaction migrates movable pages to create contiguous blocks, used by hugepage allocation and CMA regions.
- Long-lived processes with scattered dirty pages make compaction expensive; /proc/buddyinfo shows the free-block histogram per zone.
- Userspace can't easily avoid external fragmentation, but jemalloc-style arenas and explicit arenas reduce internal waste in hot allocators.

## Related
- [[wiki/os-shell/memory-allocation|Memory Allocation]] — where fragmentation originates
- [[wiki/os-shell/paging|Paging]] — page granularity defines the smallest free unit
- [[wiki/os-shell/swap-space|Swap Space]] — evicting pages can free up movable memory
- [[wiki/os-shell/virtual-memory|Virtual Memory]] — virtual contiguity hides physical fragmentation
- [[wiki/os-shell/page-tables|Page Tables]] — huge pages need physically contiguous memory
