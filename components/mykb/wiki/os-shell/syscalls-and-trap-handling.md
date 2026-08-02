---
type: "concept"
title: "Syscalls & Trap Handling"
description: "The user-to-kernel boundary and how calls are serviced"
tags: ["syscalls", "traps", "kernel", "userspace"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: [
  "https://man7.org/linux/man-pages/man2/syscalls.2.html",
  "https://docs.kernel.org/process/adding-syscalls.html",
]
---

# Syscalls & Trap Handling

## Summary
Syscalls are the controlled interface between user programs and the kernel, entered via trap instructions. The kernel validates arguments and performs the operation on the caller's behalf. Everything a program does with resources goes through this boundary, making it central to security and performance.

## Details
- A syscall traps into kernel mode, switches to the kernel stack, and dispatches by number.
- The man-pages project catalogs the Linux syscall ABI.
- Seccomp filters constrain which syscalls a process may make, hardening containers.
- Fast paths avoid full context-switch cost for common operations.
- Syscall auditing is the foundation of security monitoring.
- In mykb, syscalls connect to kernel architecture, processes, and container security.
- VDSO and vvar pages accelerate a few syscalls without crossing into kernel mode.
- New syscalls follow a formal process that includes man pages and selftests.
- Kernel and userspace behavior meet here; the related process, memory, and filesystem articles provide the implementation detail.
- Tuning this behavior in production relies on the system monitoring and resource utilization articles of this cluster.

## Related
- [[wiki/shell-environment/exit-codes-and-error-handling|Exit Codes & Error Handling]]
- [[wiki/os-shell/namespace-networking|Namespace Networking]]
- [[wiki/os-shell/shell-trap-handlers|Trap Handlers]]
- [[wiki/os-shell/syscalls|System Calls]]
