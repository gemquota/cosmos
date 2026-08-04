---
type: "entity"
title: "systemd & Init Systems"
description: "The first process and service supervision on Linux"
tags: ["init", "systemd", "services", "boot"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: [
  "https://systemd.io/",
  "https://www.freedesktop.org/software/systemd/man/latest/systemd.html",
]
---

# systemd & Init Systems

## Summary
Init systems start the userspace after the kernel boots and supervise services for the lifetime of the machine. systemd is the de facto standard on Linux, with units, sockets, and timers. Understanding init is prerequisite to understanding service lifecycle and boot failure diagnosis.

## Details
- PID 1 is the first userspace process: it mounts, starts services, and reaps orphans.
- systemd manages services declaratively through unit files with dependencies and ordering.
- The systemd project site documents its architecture and design goals.
- Timers replace cron for periodic work with better logging and dependency handling.
- Socket activation defers service start until connections arrive.
- In mykb, systemd connects to boot process, process lifecycle, and cron articles.
- Journald captures structured logs for every unit, replacing scattered log files.
- Systemd-resolved and networkd extend the same declarative model to DNS and networking.
- Kernel and userspace behavior meet here; the related process, memory, and filesystem articles provide the implementation detail.

## Related
- [[wiki/infrastructure/intrusion-detection-systems|Intrusion Detection Systems]]
- [[wiki/devops-infra/feature-flag-systems-revisited|Feature Flag Systems]]
- [[wiki/os-shell/init-systems-and-runlevels|Init Systems & Runlevels]]
- [[wiki/os-shell/systemd-journal|systemd-journal]]
