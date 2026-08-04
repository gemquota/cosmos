---
type: "entity"
title: "strace & Dynamic Tracing"
description: "Syscall tracing with strace/ltrace and bpftrace"
tags: ["strace", "tracing", "debugging", "bpftrace", "perf"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://man7.org/linux/man-pages/man1/strace.1.html", "https://man7.org/linux/man-pages/man1/ltrace.1.html"]
---

# strace & Dynamic Tracing

## Summary
strace records the syscalls a process makes, showing file opens, network calls, and failures with errno. ltrace does the same for library calls, and bpftrace/eBPF traces kernel events at scale. Together they turn opaque binaries into observable behavior.

## Details
- strace -f follows child processes; -e trace=open,read,write filters calls; -p PID attaches to a running process.
- The -c flag summarizes syscall counts and times — a fast way to spot pathological syscall storms.
- strace shows errno in human form (EACCES, ENOENT), which pins down permission and missing-file bugs instantly.
- ltrace -S traces library calls plus signals, handy when the bug hides inside a shared library call.
- Overhead matters: strace uses ptrace and slows programs dramatically, so it is for debugging, not production monitoring.
- bpftrace attaches to kernel tracepoints, kprobes, and uprobes with one-liners like bpftrace -e 'tracepoint:syscalls:sys_enter_open { print(comm) }'.
- eBPF tracing (bpf, bpftrace, and tools like bcc) runs safely in the kernel with low overhead, powering modern observability.

## Related
- [[wiki/os-shell/syscalls|System Calls]] — what strace observes
- [[wiki/dev-tools/debuggers|Debuggers]] — stepping code at the source level
- [[wiki/dev-tools/profilers|Profilers]] — where time actually goes
- [[wiki/devops-infra/observability|Observability]] — production-grade tracing systems
- [[wiki/os-shell/kernel-modules|Kernel Modules]] — what eBPF programs run alongside
