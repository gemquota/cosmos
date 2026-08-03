---
type: "concept"
title: "Swap & zram"
description: "Swap devices, zram compressed RAM swap, and pressure handling"
tags: ["swap", "zram", "memory", "linux"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# Swap & zram

## Summary
Swap gives the kernel a place to park cold pages when memory pressure rises: a disk swap device (partition or file) or zram, which compresses pages in RAM itself and uses that as a swap device. zram is the modern default for workstations and small systems — it avoids disk I/O entirely and typically expands effective memory by 1.5-3x — while disk swap remains the safety net for bursts of demand.

## Details
- Mechanism: the kernel's page-out path selects cold, cleanable pages under pressure and writes them to swap; on access, they fault back. `vm.swappiness` (0-100) biases how eagerly the kernel swaps anonymous pages versus reclaiming page cache — 0 avoids swapping until necessary, 100 swaps aggressively; default 60 on most distros. zram creates a compressed block device in RAM (`zramctl`/`modprobe zram`) used as swap, trading CPU (compression) for memory: compressible pages shrink to ~1/3, so 4GB of zram can hold what would be ~12GB of uncompressed anonymous pages. zswap is the hybrid: a compressed cache in front of a disk swap device, keeping hot-but-cold pages in compressed RAM and only spilling to disk under sustained pressure.
- Concrete examples: a laptop with 8GB RAM and a 4GB zram swap handles a dozen browser tabs without hitting disk thrash; a Raspberry Pi or embedded box uses zram exclusively because there is no swap disk; a server uses a 2x-RAM swap file plus `vm.swappiness=10` so bursts of build memory do not OOM; `zramctl` reports compression ratio (`zramctl -l`); `swapon`/`swapoff` manage devices; `free -h` shows swap usage; `vmstat 1` shows `si`/`so` (swap in/out) to detect thrashing.
- Failure modes: the classic failures are thrashing — heavy `si`/`so` with high disk utilization means the system is swapping continuously and throughput collapses (the fix is more RAM or lower pressure, not more swap); zram CPU overhead under sustained compression-heavy workloads (a CPU-bound box gets slower, not faster); and zram's fragility as a memory *overflow*: when zram itself cannot compress enough, the system OOMs — zram is not a substitute for actual capacity planning. Swap on a failing disk hides failures behind latency, and `swappiness=0` on a box with heavy page-cache workloads can cause OOM when cache reclaim would have sufficed.
- Operational tradeoffs: zram trades CPU for apparent memory and is nearly always a win on interactive and small systems; disk swap trades disk I/O for memory headroom and is the right safety net on servers, sized to worst-case burst (typically 1-2x RAM, or `swapfile` sized to the largest single process). The modern guidance: zram (or zswap) as the primary swap on desktops, a generous disk swap file with moderate `swappiness` on servers, and `vmstat`/`memory.pressure` monitoring to distinguish "swap used" (fine) from "swapping hard" (bad).
- RSIS3/mykb relevance: RSIS3's batch loops (indexing, graph rebuilds) are memory-spiky; giving the daemon a bounded cgroup with zram-backed swap and pressure alerts mirrors the loop-hygiene rule that bursts must be absorbed without taking down the knowledge store.

## Related
- [[wiki/os-shell/swap-space|Swap Space]]
- [[wiki/os-shell/kernel-architecture|Kernel Architecture]]
- [[wiki/os-shell/memory-management-paging|Memory Management & Paging]]
