---
type: "concept"
title: "System Calls"
description: "The syscall interface, libc wrappers, and examples"
tags: ["syscalls", "kernel", "libc", "abi", "interface"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://man7.org/linux/man-pages/man2/syscalls.2.html", "https://man7.org/linux/man-pages/man7/syscalls.7.html"]
---

# System Calls

## Summary
System calls are the kernel's application programming interface: numbered entry points that user programs invoke to request privileged work such as opening files, allocating memory, and sending network packets. Libc wraps them, and every language runtime sits on top of them.

## Details
- Each architecture numbers its syscalls; on x86-64, syscall numbers live in /usr/include/asm/unistd_64.h and a table in the kernel.
- The calling convention passes arguments in registers; glibc wrappers handle the syscall instruction and return errno on failure.
- Modern x86-64 has about 500 syscalls: open/read/write/close, fork/exec/exit, mmap/munmap, socket/connect, and newer ones like io_uring.
- io_uring batches operations with shared rings, avoiding one syscall per I/O for high-performance servers.
- seccomp filters let sandboxes deny syscalls before they reach the kernel, a cornerstone of container and browser sandboxes.
- strace(1) and perf trace show the syscall stream; each call crosses the user/kernel boundary, so hot paths minimize them.
- SysV ABI vs vDSO: some calls (gettimeofday) never enter the kernel at all, executed from a kernel-provided shared page.

## Related
- [[wiki/os-shell/kernel-space-vs-user-space|Kernel vs User Space]] — the boundary syscalls cross
- [[wiki/os-shell/strace-and-dynamic-tracing|strace & Dynamic Tracing]] — observing the syscall stream
- [[wiki/os-shell/fork-exec-and-process-creation|Fork, Exec & Process Creation]] — process-related syscalls
- [[wiki/os-shell/file-descriptors|File Descriptors]] — what open/read/write operate on
- [[wiki/os-shell/process-signals|Process Signals]] — asynchronous events delivered via syscalls
