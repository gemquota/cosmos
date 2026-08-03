---
type: "concept"
title: "Interrupt Handlers & Workqueues"
description: "Deferring work from interrupt context to kernel threads"
tags: ["interrupts", "workqueue", "kernel", "irq"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# Interrupt Handlers & Workqueues

## Summary
Interrupt handlers run in a restricted context where sleeping is forbidden, so real work must be deferred. The kernel's deferral machinery — softirqs, tasklets (legacy), and especially workqueues — moves that work into process context, where it can sleep, block on locks, and run on dedicated kernel threads. Understanding the split between "top half" (interrupt handler) and "bottom half" (deferred work) is the foundation of driver design.

## Details
- Mechanism: when hardware raises an interrupt, the kernel runs the registered handler (top half) in interrupt context: interrupts are masked, no sleeping or locking is allowed, and the handler must be fast — typically just acknowledging the device and recording state. Deferred processing (bottom half) happens in one of several forms: softirqs run in interrupt-like context with limited preemption; tasklets build on softirqs with per-CPU queues; and workqueues run in process context on kernel threads (`kworker`), where the code may sleep, allocate memory, and take mutexes. The API is `INIT_WORK`/`queue_work`/`schedule_work`, and drivers defer everything from "process the received packet" to "complete the USB transfer" this way.
- Concrete examples: a network driver's interrupt handler copies the ring-buffer index and schedules a softirq (`napi_schedule`) to process packets; an NVMe driver's handler acknowledges the completion and defers callback processing to a workqueue; a USB driver queues work to complete a read request that needs to copy data to user space; drivers use `request_irq` with `IRQF_SHARED` for shared lines and threadable IRQs (`request_threaded_irq`) when the entire handler can run as a kernel thread.
- Failure modes: the classic failures are doing too much in interrupt context — sleeping in a handler (`kmalloc(GFP_KERNEL)` or a mutex there causes a kernel oops/BUG), unbounded loops that starve other interrupts, and races between the top half and the workqueue that accesses the same state without proper synchronization (the workqueue runs later on a possibly different CPU). Workqueue misuse — scheduling the same work item while it is pending, unbounded queuing under load — causes pile-ups; and latency-sensitive drivers that defer too much add unacceptable delay.
- Operational tradeoffs: the tradeoff is latency versus safety: interrupt context is fast but severely restricted; softirqs are faster than workqueues but cannot sleep; workqueues are flexible but add scheduling latency and context-switch cost. Modern guidance: keep handlers minimal, use threaded IRQs or workqueues for anything nontrivial, and use per-CPU or bound workqueues where cache locality matters. RSIS3/mykb relevance: the top-half/bottom-half split is the kernel's version of fast-path/slow-path decomposition — handle the urgent acknowledgment inline, defer the expensive processing to a supervised queue, the same structure RSIS3 uses for L1 (fast corrections) versus L2/L3 (deep improvements).

## Related
- [[wiki/os-shell/shell-trap-handlers|Trap Handlers]]
- [[wiki/os-shell/kernel-architecture|Kernel Architecture]]
- [[wiki/os-shell/memory-management-paging|Memory Management & Paging]]
- [[wiki/syntheses/knowledge-acquisition-workflow|Knowledge Acquisition Workflow]] — how stubs grow into full articles in mykb
- [[wiki/syntheses/mykb-acquisition-curation-and-practices|Acquisition, Curation & Practices]] — the curation loop this stub belongs to
