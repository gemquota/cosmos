---
type: "concept"
title: "TLB & Caching"
description: "Translation lookaside buffer hits, misses, and invalidation"
tags: ["tlb", "cache", "mmu", "performance", "translation"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://docs.kernel.org/mm/page_tables.html", "https://www.intel.com/content/www/us/en/developer/articles/technical/intel-sdm.html"]
---

# TLB & Caching

## Summary
The translation lookaside buffer (TLB) caches virtual-to-physical page translations so the MMU does not walk page tables for every memory access. Its hit rate is one of the strongest predictors of memory performance, since a miss can cost dozens of cycles and extra memory loads.

## Details
- The TLB is split on most x86 CPUs into separate instruction and data TLBs, often multi-level like other caches.
- A miss forces a hardware page-table walk; deep page-table hierarchies mean several memory loads, which is why huge pages reduce miss cost.
- On context switch, address spaces change, so stale entries must be invalidated; x86 uses PCID/ASID tags to keep valid entries across switches.
- TLB shootdowns: when the kernel unmaps a page, it must invalidate that entry on every CPU that may hold it, using inter-processor interrupts.
- Huge pages (2 MiB/1 GiB) map far more memory per TLB entry, dramatically raising effective coverage for databases and JVMs.
- Linux exposes counters via perf (dTLB-load-misses) and /proc/interrupts shows TLB shootdowns as function-call interrupts.
- Meltdown-era mitigations (KPTI) added cost to user/kernel transitions by isolating kernel page tables, trading TLB pressure for security.

## Related
- [[wiki/os-shell/page-tables|Page Tables]] — what the TLB caches translations from
- [[wiki/os-shell/context-switching|Context Switching]] — switches flush or tag TLB state
- [[wiki/os-shell/paging|Paging]] — the page granularity of TLB entries
- [[wiki/os-shell/virtual-memory|Virtual Memory]] — the abstraction the TLB accelerates
- [[wiki/os-shell/system-monitoring-tools|System Monitoring]] — perf counters for TLB misses
