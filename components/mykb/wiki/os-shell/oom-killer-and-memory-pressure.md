---
type: "concept"
title: "OOM Killer & Memory Pressure"
description: "How the kernel reclaims memory and selects victims under pressure"
tags: ["oom", "memory", "kernel", "linux"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# OOM Killer & Memory Pressure

## Summary
When a Linux system runs out of reclaimable memory, the kernel's OOM killer picks a process to kill so the system can continue. Understanding memory pressure — the reclaim path, `overcommit`, cgroup limits, and the OOM score — is what separates "the OOM killer is evil" from "the OOM killer was the only reasonable option and I know why it chose what it did."

## Details
- Mechanism: memory is demand-paged and overcommitted: `malloc` succeeds even when physical memory is short, and pages are committed on first touch. Under pressure, the kernel first reclaims clean page cache, then tries swapping and shrinking caches; if that is insufficient, it invokes the OOM killer, which scores processes (oom_score: memory footprint, `oom_score_adj`, whether it is a root process, and how long it has lived) and kills the worst offender, logging to `dmesg`/`journald`. cgroups add scoped pressure: a container's memory cgroup can hit its `memory.limit` and trigger its own OOM kill (the container is killed, not the host), and `memory.high`/`low` provide softer throttling. `vm.overcommit_memory`, `vm.swappiness`, and `vm.oom_kill_allocating_task` tune the whole policy.
- Concrete examples: a Java service with `-Xmx` larger than the cgroup limit gets OOM-killed at startup or under peak load; a `ps aux --sort=-rss` audit finds a memory hog right before the kill; setting `oom_score_adj` to -1000 on a database makes the killer prefer other processes (with `OOM_SCORE_ADJ_MIN` requiring root); a CI runner hits `memory.limit_in_bytes` and the whole job dies; `sysctl vm.panic_on_oom=1` turns OOM into a kernel panic for fail-loud servers; `earlyoom` or systemd-oomd kill based on pressure *before* the kernel's last resort, giving cleaner shutdowns.
- Failure modes: the classic failure is misreading the OOM kill as a bug in the victim: the killer targets the process with the worst score, which is often the biggest process — if your database is the biggest process, it dies even when a leak elsewhere triggered the pressure. Silent memory leaks that only manifest under load, overcommitted `malloc` succeeding until first touch, and swap misconfiguration (`swappiness` too high thrashing swap, too low causing OOM) are the recurring causes. cgroup OOM with `memory.oom_control` disabled makes the allocating task hang instead of being killed — a worse failure mode that looks like a deadlock.
- Operational tradeoffs: the kernel's job is to keep the system alive, and the OOM killer is the last resort — the tradeoff is between predictability (tune `oom_score_adj`, use systemd-oomd/earlyoom for early, cleaner kills) and the kernel's raw survival instinct. The practice rules: size workloads to memory with headroom, monitor pressure via cgroup v2 `memory.pressure` before kills happen, set `oom_score_adj` deliberately on critical services, and treat OOM kills as a capacity/leak signal, not a process bug.
- RSIS3/mykb relevance: RSIS3's batch loops are exactly the kind of workload that gets OOM-killed under pressure; the discipline of bounding per-loop memory (like cgroup limits and `oom_score_adj` on the daemon) mirrors the loop-hygiene rule that one runaway worker must not take down the knowledge store.

## Related
- [[wiki/os-shell/memory-management-paging|Memory Management & Paging]]
- [[wiki/os-shell/memory-allocation|Memory Allocation]]
- [[wiki/os-shell/memory-fragmentation|Memory Fragmentation]]
- [[wiki/os-shell/memory-mapped-files|Memory-Mapped Files]]
- [[wiki/os-shell/kernel-architecture|Kernel Architecture]]
- [[wiki/syntheses/knowledge-acquisition-workflow|Knowledge Acquisition Workflow]] — how stubs grow into full articles in mykb
- [[wiki/syntheses/mykb-acquisition-curation-and-practices|Acquisition, Curation & Practices]] — the curation loop this stub belongs to
