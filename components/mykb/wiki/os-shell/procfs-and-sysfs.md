---
type: "concept"
title: "procfs & sysfs"
description: "Virtual filesystems exposing kernel and device state"
tags: ["procfs", "sysfs", "virtual-filesystem", "kernel"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://man7.org/linux/man-pages/man5/proc.5.html", "https://man7.org/linux/man-pages/man5/sysfs.5.html"]
---

# procfs & sysfs

## Summary
procfs (/proc) and sysfs (/sys) are virtual filesystems that expose kernel and device state as files. Reading them is how tools like ps, top, and lspci get their data; writing selected files tunes kernel parameters.

## Details
- /proc/<pid>/ contains per-process data: cmdline, environ, fd links, maps, stat, and status — the source for ps and lsof.
- Global files: /proc/meminfo, /proc/cpuinfo, /proc/loadavg, /proc/interrupts, /proc/partitions, and /proc/net/*.
- /proc/sys/ holds sysctl tunables (kernel.pid_max, vm.swappiness, net.ipv4.ip_forward); sysctl(8) is the friendly front end.
- procfs files are generated on read, so they never go stale like regular files; writing to them changes live kernel state.
- sysfs (/sys) models devices and drivers: /sys/class/net/ lists network interfaces, /sys/block/ block devices, with attributes readable and some writable.
- Udev reads sysfs events to create device nodes; systemd and monitoring tools read both filesystems continuously.
- Security: hidepid= mount options restrict /proc/<pid> visibility; some /proc/sys files are namespaced per container.

## Related
- [[wiki/os-shell/system-monitoring-tools|System Monitoring]] — the tools built on procfs
- [[wiki/os-shell/device-drivers|Device Drivers]] — what sysfs describes
- [[wiki/os-shell/filesystem-types|Filesystem Types]] — pseudo-filesystems with no disk
- [[wiki/os-shell/cgroups-and-resource-control|cgroups & Resource Control]] — a sibling virtual filesystem
- [[wiki/os-shell/kernel-modules|Kernel Modules]] — module state under /proc
