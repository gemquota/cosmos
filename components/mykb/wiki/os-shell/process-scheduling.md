---
type: "concept"
title: "Process Scheduling"
description: "CPU scheduler policies, preemption, and run queues across processes and threads"
tags: ["scheduling", "kernel", "cpu", "preemption", "runqueues"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://docs.kernel.org/scheduler/index.html", "https://man7.org/linux/man-pages/man7/sched.7.html"]
---

# Process Scheduling

## Summary
The CPU scheduler decides which runnable task gets the processor and for how long, balancing throughput, latency, and fairness. Linux's scheduler is priority-based: the Completely Fair Scheduler (CFS) serves normal tasks, while SCHED_FIFO, SCHED_RR, and SCHED_DEADLINE classes serve real-time and deadline workloads.

## Details
- Each CPU keeps a runqueue of runnable tasks; periodic load balancing migrates tasks between queues so cores stay busy.
- CFS stores tasks in a red-black tree keyed by virtual runtime (vruntime) and always dispatches the task with the smallest vruntime, giving every task a fair share.
- Preemption happens when a higher-priority task becomes runnable or a timeslice expires; preemptible kernels also allow switching inside kernel code paths.
- nice values from -20 to +19 only weight the fair-share class; CFS guarantees a minimum share so nice never starves a task outright.
- The kernel schedules threads, not processes: threads of one process are independent schedulable entities sharing a signal and memory context.
- Every switch pays real costs, including TLB flushes and cache cold misses, so the scheduler batches work with timeslices and wakeup heuristics.
- cgroup cpu controllers group tasks for bandwidth and quota limits, which containers and systemd slices rely on.

## Related
- [[wiki/os-shell/context-switching|Context Switching]] — the hardware cost paid on every scheduler decision
- [[wiki/os-shell/process-priorities-and-nice|Process Priorities & Niceness]] — how nice values feed CFS weight calculations
- [[wiki/os-shell/threads-and-concurrency|Threads & Concurrency]] — the schedulable entity the kernel dispatches
- [[wiki/os-shell/cgroups-and-resource-control|cgroups & Resource Control]] — group-level CPU bandwidth and quota limits
- [[wiki/os-shell/process-management|Process Management]] — the lifecycle of the tasks being scheduled
