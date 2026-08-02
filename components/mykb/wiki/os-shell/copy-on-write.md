---
type: "concept"
title: "Copy-on-Write"
description: "COW sharing for fork and page faults on write"
tags: ["copy-on-write", "fork", "memory", "optimization"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://man7.org/linux/man-pages/man2/fork.2.html", "https://docs.kernel.org/mm/index.html"]
---

# Copy-on-Write

## Summary
Copy-on-write (COW) defers copying: pages are shared read-only until someone writes, and only then is a private copy made. It makes fork(2) nearly free and underpins MAP_PRIVATE mappings, deduplication, and several copy-on-write filesystems.

## Details
- After fork, parent and child share all pages marked read-only; the page tables point to the same frames with the write bit cleared.
- The first write to a shared page traps a page fault; the kernel allocates a new frame, copies the old contents, and updates the faulting process's PTE.
- COW means fork cost scales with the number of pages in the page table, not their contents; big processes fork almost as fast as small ones.
- Exec-heavy programs still benefit because the child usually execs immediately, so few pages are ever duplicated.
- MAP_PRIVATE mmap uses the same trick: the file's cache pages are shared read-only until modified, then copied.
- Kernel samepage merging (KSM) and filesystem reflinks (cp --reflink, btrfs/ZFS) apply COW at different layers to save space.
- Pitfall: a forking process that writes heavily pays the copy cost later; tools like perf track COW faults via page-fault counters.

## Related
- [[wiki/os-shell/fork-exec-and-process-creation|Fork, Exec & Process Creation]] — COW is why fork is cheap
- [[wiki/os-shell/memory-mapped-files|Memory-Mapped Files]] — MAP_PRIVATE shares via COW
- [[wiki/os-shell/paging|Paging]] — the page faults COW relies on
- [[wiki/os-shell/filesystem-types|Filesystem Types]] — COW filesystems extend the idea to data blocks
- [[wiki/os-shell/page-tables|Page Tables]] — the write-protect bits that trigger COW
