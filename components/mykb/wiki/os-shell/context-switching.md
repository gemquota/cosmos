---
type: "concept"
title: "Context Switching"
description: "How the kernel saves and restores process state, costs, and what triggers switches"
tags: ["context-switch", "kernel", "scheduling", "performance"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://docs.kernel.org/scheduler/index.html", "https://man7.org/linux/man-pages/man2/sched_yield.2.html"]
---

# Context Switching

## Summary
A context switch suspends one execution context and resumes another, saving enough state that the first can continue later. It is the fundamental cost of multitasking: the kernel must preserve registers, program counter, stack, and address-space state.

## Details
- A switch saves the CPU registers and instruction pointer, swaps kernel stacks, and updates the running task pointer before restoring the next task's state.
- Between processes, switch_mm installs the new address space, which can flush the TLB; PCID/ASID tags avoid full flushes on x86.
- Thread switches within one process skip the address-space change, which is why threads are cheaper to switch than processes.
- Voluntary switches happen when a task blocks on I/O, sleeps, or calls sched_yield; involuntary switches follow preemption or timeslice expiry.
- Interrupts and syscalls also enter the kernel but are not always full context switches — the user context is simply resumed.
- Costs include TLB misses, cache pollution, and kernel entry overhead; tools like vmstat (cs column) and perf sched measure switch rates.
- Excessive switching (thrashing) degrades throughput; batch sizes, I/O scheduling, and correct locking reduce unnecessary switches.

## Related
- [[wiki/os-shell/process-scheduling|Process Scheduling]] — the scheduler decides when switches happen
- [[wiki/os-shell/threads-and-concurrency|Threads & Concurrency]] — thread switches avoid address-space work
- [[wiki/os-shell/tlb-cache|TLB & Caching]] — TLB pressure dominates switch cost
- [[wiki/os-shell/system-monitoring-tools|System Monitoring]] — measuring context-switch rates
- [[wiki/os-shell/kernel-space-vs-user-space|Kernel vs User Space]] — the privilege boundary crossed on every switch
