---
type: "concept"
title: "cgroups & Resource Control"
description: "cgroup v1/v2, limits, and accounting"
tags: ["cgroups", "resource-control", "containers", "limits"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://docs.kernel.org/admin-guide/cgroup-v2.html", "https://man7.org/linux/man-pages/man7/cgroups.7.html"]
---

# cgroups & Resource Control

## Summary
Control groups (cgroups) group processes and limit, account, and prioritize their resource use — CPU time, memory, I/O, and process count. They are the resource half of containers, managed by systemd, Docker, and Kubernetes.

## Details
- cgroup v2 (the default on modern systems) organizes processes in a unified hierarchy mounted at /sys/fs/cgroup with a single "cgroup.controllers" file.
- Controllers: cpu (weights and quotas), memory (high/max limits plus usage), io (bandwidth), pids (process count), and cpuset (CPU pinning).
- memory.max kills or throttles the cgroup at its limit; memory.high signals pressure before the hard cap, and PSI files report stall times.
- CPU quota (cpu.max) limits usage to a fraction of cores; cpu.weight gives proportional share among siblings.
- systemd exposes this as service slices: user@.service, machine.slice, and per-service MemoryMax/CPUQuota settings.
- Containers get a cgroup each; Kubernetes kubelet writes limits into the container's cgroup and watches its usage.
- cgroup v1 is legacy but still seen on older systems: separate hierarchies per controller, which the v2 design replaced.

## Related
- [[wiki/os-shell/linux-namespaces|Linux Namespaces]] — isolation paired with cgroup limits
- [[wiki/os-shell/process-scheduling|Process Scheduling]] — how cpu.weight and quota feed the scheduler
- [[wiki/os-shell/containers-vs-vms|Containers vs VMs]] — the resource layer under containers
- [[wiki/os-shell/systemd-units|Systemd Units]] — slice/scope management of cgroups
- [[wiki/os-shell/ulimit-and-resource-limits|Resource Limits]] — the per-process complement to cgroups
