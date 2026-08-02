---
type: "concept"
title: "Kernel vs User Space"
description: "Privilege levels, syscall boundary, and isolation"
tags: ["kernel", "user-space", "privilege", "syscalls", "isolation"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://man7.org/linux/man-pages/man7/syscalls.7.html", "https://www.kernel.org/doc/html/latest/process/howto.html"]
---

# Kernel vs User Space

## Summary
Modern CPUs enforce two privilege worlds: the kernel runs at the highest privilege level with full hardware access, while user programs run restricted and must ask the kernel for anything privileged. The syscall interface is the controlled doorway between them.

## Details
- x86 privilege rings: the kernel executes at ring 0, user code at ring 3; rings 1-2 are largely unused on Linux.
- User code cannot touch I/O ports, page tables, or other processes' memory; the MMU enforces it via page permissions.
- Entering the kernel happens through syscalls, exceptions, and interrupts; the CPU switches to a kernel stack and privilege level.
- The kernel validates user pointers (copy_from_user/copy_to_user) before touching them, preventing user space from tricking it.
- Not everything needs a syscall: vDSO exposes gettimeofday and clock_gettime directly in user memory for speed.
- Isolation failures are catastrophic: Meltdown/Spectre showed side channels across the boundary, leading to KPTI page-table isolation.
- Kernel bugs can crash or compromise the whole machine; user-space bugs only hurt the process, which is why drivers move to user space when possible.

## Related
- [[wiki/os-shell/syscalls|System Calls]] — the crossing mechanism
- [[wiki/os-shell/kernel-modules|Kernel Modules]] — privileged code loaded on demand
- [[wiki/os-shell/context-switching|Context Switching]] — mode switches versus full switches
- [[wiki/os-shell/page-tables|Page Tables]] — the hardware isolation that guards the boundary
- [[wiki/os-shell/containers-vs-vms|Containers vs VMs]] — where the isolation line is drawn
