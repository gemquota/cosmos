---
type: "concept"
title: "Process Priorities & Niceness"
description: "nice/renice, priority classes, and scheduler weighting"
tags: ["nice", "priority", "scheduler", "processes", "renice"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://man7.org/linux/man-pages/man1/nice.1.html", "https://man7.org/linux/man-pages/man2/setpriority.2.html"]
---

# Process Priorities & Niceness

## Summary
Linux separates scheduling classes from priority: nice values adjust the fair-share weighting of normal processes, while real-time classes use their own priority scale. nice(1) and renice(8) manage the former; chrt(1) manages the latter.

## Details
- nice values range from -20 (highest priority) to +19 (lowest), defaulting to 0; positive niceness means "be nice" to other processes.
- In CFS, each task gets a weight derived from its nice value, and CPU time is proportional to weight — a nice+19 task still gets a guaranteed slice.
- Only root may lower a nice value or raise a real-time priority; unprivileged users may only increase niceness, and even that is bounded by RLIMIT_NICE.
- Real-time priorities run from 1 to 99 under SCHED_FIFO and SCHED_RR; FIFO tasks run until they block or yield, RR tasks round-robin with a timeslice.
- A single misbehaving RT task can starve the whole system, which is why RT throttling (sched_rt_period_us) exists.
- The kernel reports dynamic priorities: ps shows NI and PRI, and /proc/<pid>/stat exposes the internal task_prio.
- Renice affects already-running processes; systemd services set CPUWeight instead, which maps to the same CFS weights in a cgroup.

## Related
- [[wiki/os-shell/process-scheduling|Process Scheduling]] — how priorities feed scheduler decisions
- [[wiki/os-shell/cgroups-and-resource-control|cgroups & Resource Control]] — group-level CPUWeight quotas
- [[wiki/os-shell/system-monitoring-tools|System Monitoring]] — reading priority columns in ps/top
- [[wiki/os-shell/process-management|Process Management]] — the lifecycle priorities modify
- [[wiki/os-shell/sudo-and-privilege-escalation|sudo & Privilege Escalation]] — root is required to lower nice values
