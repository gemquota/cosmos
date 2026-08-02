---
type: "concept"
title: "Cgroups & Namespaces"
description: "Kernel primitives for resource control and isolation"
tags: ["cgroups", "namespaces", "containers", "isolation"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: [
  "https://man7.org/linux/man-pages/man7/namespaces.7.html",
  "https://docs.kernel.org/admin-guide/cgroup-v2.html",
]
---

# Cgroups & Namespaces

## Summary
Cgroups limit and account resources per process group, while namespaces isolate views of the system. Together they are the kernel primitives behind containers and systemd services. Understanding them explains both container behavior and multi-tenant isolation in the mykb graph.

## Details
- Namespaces isolate process, network, mount, UTS, IPC, and user IDs; the man page documents each.
- cgroup v2 provides a unified hierarchy for CPU, memory, and I/O control.
- Containers are processes confined by namespaces and limited by cgroups, nothing more.
- Systemd organizes services into cgroup slices, making the host a tree of scopes.
- Breakout risk is kernel-wide: a namespace escape is a host compromise.
- In mykb, cgroups and namespaces connect to container runtimes, capabilities, and scheduling.
- Cgroup v2 delegation lets unprivileged users manage their own subtrees safely.
- Pressure stall information exposes memory and I/O contention directly to userspace.
- Kernel and userspace behavior meet here; the related process, memory, and filesystem articles provide the implementation detail.

## Related
- [[wiki/os-shell/namespace-networking|Namespace Networking]]
- [[wiki/os-shell/kernel-modules-and-loading|Kernel Modules & Loading]]
- [[wiki/os-shell/cgroups-and-resource-control|cgroups & Resource Control]]
- [[wiki/os-shell/linux-namespaces|Linux Namespaces]]
