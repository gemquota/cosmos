---
type: "concept"
title: "Virtual Memory"
description: "Address-space abstraction, mappings, and how processes view memory"
tags: ["virtual-memory", "address-space", "mmu", "kernel", "isolation"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://docs.kernel.org/admin-guide/mm/index.html", "https://man7.org/linux/man-pages/man2/mmap.2.html"]
---

# Virtual Memory

## Summary
Virtual memory gives every process its own private, contiguous-looking address space backed by physical memory managed by the kernel. The MMU translates virtual addresses to physical ones per page, so each process sees the same layout regardless of where its data actually lives in RAM.

## Details
- On 64-bit Linux, a process's address space is split: the lower region holds text, data, heap, and mmap areas; the top region holds the stack and kernel mappings.
- The kernel half of the address space is shared by all processes and is unmapped for user access, isolating kernel data from user code.
- Mappings are either file-backed (executables, mmap'd files) or anonymous (heap, stack, zero-fill pages); both are populated on first touch.
- The MMU walks page tables to translate addresses; every page carries permission bits, so a process cannot touch memory it was not given.
- Overcommit lets the kernel hand out more virtual memory than RAM plus swap exists; the OOM killer reclaims when actual use overshoots.
- vm.max_map_count limits the number of mappings a process may create; modern runtimes can exhaust it with many small mappings.
- ASLR randomizes base addresses of libraries, heap, and stack to blunt exploitation of fixed-layout bugs.

## Related
- [[wiki/os-shell/paging|Paging]] — the page-granular mechanism behind virtual memory
- [[wiki/os-shell/page-tables|Page Tables]] — the translation structures the MMU walks
- [[wiki/os-shell/memory-allocation|Memory Allocation]] — how the heap and mmap regions grow
- [[wiki/os-shell/swap-space|Swap Space]] — the backing store for evicted pages
- [[wiki/os-shell/tlb-cache|TLB & Caching]] — the cache that makes translation fast
