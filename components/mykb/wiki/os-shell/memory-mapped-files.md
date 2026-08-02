---
type: "concept"
title: "Memory-Mapped Files"
description: "mmap semantics, file-backed and shared mappings"
tags: ["mmap", "files", "shared-memory", "page-cache"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://man7.org/linux/man-pages/man2/mmap.2.html"]
---

# Memory-Mapped Files

## Summary
mmap(2) maps a file's contents into a process's address space so reads and writes become ordinary memory operations backed by the page cache. It is the basis of shared memory, executable loading, and efficient large-file access.

## Details
- MAP_SHARED mappings propagate changes to the underlying file; MAP_PRIVATE mappings give the process a copy-on-write view that never writes back.
- MAP_ANONYMOUS creates zero-filled memory with no file behind it — the standard path for private scratch memory and POSIX shared memory objects.
- File pages are demand-paged: touching a mapped region faults in the page, and dirty pages are written back by the kernel, or immediately with msync(2).
- The page cache deduplicates: multiple processes mapping the same file share its pages in RAM, so mmap reads can beat read(2) for random access.
- Addresses must be page-aligned and lengths rounded up; partial pages are zero-filled beyond the file size.
- Truncating or extending a mapped file can produce SIGBUS or zero-filled new pages; concurrent writers need explicit synchronization.
- munmap(2) unmaps a range, and mappings disappear automatically on exec or process exit; map count limits (vm.max_map_count) can bite.

## Related
- [[wiki/os-shell/shared-memory|Shared Memory]] — mmap is the POSIX shared-memory backend
- [[wiki/os-shell/paging|Paging]] — demand paging drives mapping population
- [[wiki/os-shell/copy-on-write|Copy-on-Write]] — the MAP_PRIVATE semantics
- [[wiki/os-shell/file-descriptors|File Descriptors]] — the fd an mmap is created from
- [[wiki/os-shell/virtual-memory|Virtual Memory]] — the address space mappings occupy
