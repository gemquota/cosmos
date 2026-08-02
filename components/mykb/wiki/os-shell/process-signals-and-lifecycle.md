---
type: "concept"
title: "Process Signals & Lifecycle"
description: "How processes are born, signaled, and reaped"
tags: ["signals", "process", "lifecycle", "kernel"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: [
  "https://man7.org/linux/man-pages/man7/signal.7.html",
  "https://man7.org/linux/man-pages/man2/fork.2.html",
]
---

# Process Signals & Lifecycle

## Summary
Signals are the kernel's asynchronous notifications to processes: termination, interruption, and user-defined events. Lifecycle spans fork, exec, exit, and reaping by the parent. Signal handling is a core systems programming and operations skill for services and supervisors.

## Details
- The signal man page catalogs each signal and its default disposition.
- SIGTERM asks for graceful shutdown; SIGKILL cannot be caught or ignored.
- fork creates a child, exec replaces its image, and exit notifies the parent via wait.
- The fork man page documents the full lifecycle contract.
- Daemons and supervisors translate signals into shutdown sequences.
- In mykb, process signals connect to systemd, job control, and container lifecycle hooks.
- Signal masks and handlers let processes defer or customize delivery.
- Double-fork daemonization and supervisor models change who reaps the child.
- Kernel and userspace behavior meet here; the related process, memory, and filesystem articles provide the implementation detail.
- Tuning this behavior in production relies on the system monitoring and resource utilization articles of this cluster.

## Related
- [[wiki/cloud-infra/snapshot-lifecycle-policies|Snapshot Lifecycle Policies]]
- [[wiki/cloud-infra/glacier-and-s3-lifecycle|Glacier & S3 Lifecycle]]
- [[wiki/os-shell/process-signals|Process Signals]]
- [[wiki/devops-infra/golden-signals|Golden Signals]]
