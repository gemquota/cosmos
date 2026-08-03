---
type: "concept"
title: "Hardware RAID vs Software RAID"
description: "Controller-based versus OS-based redundancy and performance"
tags: ["raid", "hardware", "software", "storage"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# Hardware RAID vs Software RAID

## Summary
Hardware RAID implements the RAID array on a dedicated controller card (with its own processor and cache), while software RAID implements it in the operating system, using the host CPU and memory. The decision is about where the redundancy and performance logic lives — and the modern answer has shifted decisively from hardware to software as CPUs got fast enough to do the work without the controller tax.

## Details
- Hardware RAID: a controller card sits between the drives and the host. It owns the RAID math (parity computation, striping, rebuilding), presents the array to the OS as one clean disk, and typically carries a battery-backed or flash-backed write cache that absorbs writes and dramatically improves write latency. The OS sees a single device and never knows (or manages) the individual drives. The benefits: CPU offload (relevant when RAID compute was expensive), the write cache (the reason hardware RAID was the enterprise default for databases), and OS independence (the array works regardless of OS — including when the OS cannot boot). The costs: the controller is a single point of failure (a dead controller can make the array unreadable without an identical replacement), proprietary formats (recovery tools must understand the vendor's metadata), and the controller's own firmware bugs.
- Software RAID: the OS implements the array — Linux mdraid and ZFS/Btrfs are the standards — using host CPU for parity and host memory for cache. The benefits: portability (the array metadata is open and understood, so arrays survive OS and hardware changes), flexibility (reshape, mixed drive sizes, and per-filesystem integration), observability (the OS sees every drive and every rebuild event), and cost. The costs: CPU and memory overhead (parity computation for RAID5/6, and the RAM that filesystem caches demand), and the fact that a host failure is the array failure (the drives and the RAID logic die together).
- The write-cache argument used to decide the debate: hardware RAID's battery-backed cache made it the choice for databases that could not absorb write latency. Modern software stacks closed the gap — ZFS with a fast SLOG/ZIL device, mdraid with proper write-intent bitmap and journaling filesystems, and NVMe drives with their own power-loss protection — so the latency advantage of the hardware controller has largely evaporated.
- The modern recommendation: software RAID (especially ZFS for its checksumming, snapshots, and scrub capabilities) for virtually all new systems, with hardware RAID reserved for legacy environments, boot-array requirements, or workloads that need the controller's cache and can justify the vendor lock-in. The failure modes to design around in both: rebuild time under load (a degraded array is vulnerable until rebuild completes), and the array itself being the single point of failure — RAID protects against drive loss, not against losing the whole machine, which is what backups are for.
- For mykb: the node connects RAID levels, storage systems, and the SDN analogy — the same "where does the intelligence live" question that the software-defined movement answers everywhere.

## Related
- [[wiki/os-shell/raid-levels|RAID Levels]]
- [[wiki/infrastructure/software-defined-networking|Software-Defined Networking]]
- [[wiki/infrastructure/storage-systems|Storage Systems]]
- [[wiki/syntheses/knowledge-acquisition-workflow|Knowledge Acquisition Workflow]] — how stubs grow into full articles in mykb
- [[wiki/syntheses/mykb-acquisition-curation-and-practices|Acquisition, Curation & Practices]] — the curation loop this stub belongs to
