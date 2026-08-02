---
type: "concept"
title: "Page Tables"
description: "Multi-level page tables, entries, and virtual-to-physical translation"
tags: ["page-tables", "mmu", "virtual-memory", "x86", "translation"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://docs.kernel.org/mm/index.html", "https://www.intel.com/content/www/us/en/developer/articles/technical/intel-sdm.html"]
---

# Page Tables

## Summary
Page tables are the per-process data structures that map virtual addresses to physical frames. To keep them compact, x86-64 uses a four-level hierarchy (PML4, PDPT, PD, PT); newer CPUs optionally add a fifth level, and each level is indexed by a slice of the virtual address.

## Details
- A page table entry (PTE) holds the physical frame number plus flags: present, read/write, user-accessible, dirty, accessed, no-execute (NX), and cache controls.
- The top-level PML4 page is per process and swapped at context switch; lower levels are allocated lazily so sparse address spaces cost little.
- A 4 KiB page requires all four levels; a 2 MiB huge page uses three levels and a 1 GiB page uses two, cutting memory and TLB pressure.
- The hardware MMU walks the hierarchy on a TLB miss; Linux also uses software walkers to fill PTEs under memory pressure (CONFIG_PTE_NUMA etc.).
- Kernel and user halves of the address space share the same PML4 but use different protection bits, isolating kernel memory.
- Page-table pages are themselves normal pages, counted per process; many small mappings increase both memory and walk depth.
- Invalidation matters: when a mapping changes, the kernel must flush the relevant TLB entries, including on other CPUs.

## Related
- [[wiki/os-shell/paging|Paging]] — the unit of memory these tables describe
- [[wiki/os-shell/tlb-cache|TLB & Caching]] — the cache that avoids repeated walks
- [[wiki/os-shell/virtual-memory|Virtual Memory]] — the layout the tables translate
- [[wiki/os-shell/memory-fragmentation|Memory Fragmentation]] — why contiguous frames are hard to find
- [[wiki/os-shell/kernel-space-vs-user-space|Kernel vs User Space]] — how the shared kernel half stays isolated
