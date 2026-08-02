---
type: "concept"
title: "Resource Limits"
description: "ulimit/rlimits for files, processes, and memory"
tags: ["ulimit", "rlimits", "resources", "security"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://man7.org/linux/man-pages/man2/getrlimit.2.html", "https://man7.org/linux/man-pages/man1/ulimit.1.html"]
---

# Resource Limits

## Summary
Resource limits (rlimits) cap what a process and its children may consume: open files, address space, CPU time, core dumps, and process count. The ulimit builtin reads and sets them, and every limit has a soft and hard value.

## Details
- RLIMIT_NOFILE bounds open file descriptors (the "too many open files" error); RLIMIT_NPROC bounds processes per user.
- RLIMIT_AS caps total virtual address space; RLIMIT_DATA caps data segment; RLIMIT_STACK caps stack size.
- RLIMIT_CORE controls core dump size — 0 disables dumps, ulimit -c unlimited enables debugging dumps.
- Soft limits can be raised up to the hard limit by the process itself; only root raises hard limits, and they inherit across fork/exec.
- Persistent configuration: /etc/security/limits.conf with pam_limits, and systemd services use LimitNOFILE, LimitNPROC, LimitAS directly.
- prlimit(1) inspects and changes limits of running processes; /proc/<pid>/limits shows the effective values.
- Contrast with cgroups: rlimits are per-process ceilings with hard failure, cgroups are per-group with accounting and reclaim.

## Related
- [[wiki/os-shell/file-descriptors|File Descriptors]] — the table RLIMIT_NOFILE bounds
- [[wiki/os-shell/cgroups-and-resource-control|cgroups & Resource Control]] — group-level resource control
- [[wiki/os-shell/systemd-units|Systemd Units]] — Limit* directives in unit files
- [[wiki/os-shell/system-monitoring-tools|System Monitoring]] — spotting limit exhaustion
- [[wiki/dev-tools/debuggers|Debuggers]] — core dumps need RLIMIT_CORE
