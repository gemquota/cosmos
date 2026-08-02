---
type: "concept"
title: "System Monitoring"
description: "top/htop/ps/vmstat/iostat usage patterns"
tags: ["monitoring", "top", "htop", "vmstat", "ps"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://man7.org/linux/man-pages/man1/top.1.html", "https://man7.org/linux/man-pages/man8/vmstat.8.html"]
---

# System Monitoring

## Summary
System monitoring starts with a handful of text tools: ps for process snapshots, top/htop for live CPU and memory, vmstat for paging and runqueue trends, and iostat for I/O. Each reads the same kernel counters through procfs and presents them differently.

## Details
- ps aux gives a full snapshot; ps -eo pid,ppid,cmd --sort=-%mem sorts; ps -L shows threads, and ps -o customizes columns.
- top refreshes periodically with CPU per-process and load average; htop adds color, trees, and mouse-friendly interaction.
- vmstat 1 samples every second: r (runnable), b (blocked), si/so (swap), us/sy/id/wa (CPU breakdown) reveal bottlenecks at a glance.
- iostat -x shows per-device utilization, await, and queue depth; mpstat per-CPU; free -h and sar for historical records.
- Load average (uptime) is a one-minute smoothed runnable+uninterruptible count, not CPU percent — context matters.
- For containers and cgroups, /sys/fs/cgroup and cgroup-aware tools (systemd-cgtop, docker stats) report per-group usage.
- Production monitoring builds on these primitives with exporters and dashboards, but the same counters underlie them.

## Related
- [[wiki/os-shell/procfs-and-sysfs|procfs & sysfs]] — the data source for all these tools
- [[wiki/os-shell/process-scheduling|Process Scheduling]] — what the r column means
- [[wiki/os-shell/context-switching|Context Switching]] — vmstat cs and top %cpu
- [[wiki/devops-infra/observability|Observability]] — extending to distributed systems
- [[wiki/devops-infra/monitoring-dashboards|Monitoring Dashboards]] — visualizing the same counters
