---
type: "concept"
title: "Linux Namespaces"
description: "PID/net/mnt/user namespaces and isolation"
tags: ["namespaces", "containers", "isolation", "kernel"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://man7.org/linux/man-pages/man7/namespaces.7.html", "https://man7.org/linux/man-pages/man1/unshare.1.html"]
---

# Linux Namespaces

## Summary
Namespaces give processes their own view of the system: their own PID tree, network stack, mount table, hostname, user IDs, and more. They are the kernel feature that containers are built on, created with clone(3), unshare(2), or setns(2).

## Details
- Mount namespaces isolate the mount table, letting each container see its own root and filesystem layout.
- PID namespaces renumber PIDs: inside, PID 1 is the namespace's init, and processes in other namespaces are invisible.
- Network namespaces own their own interfaces, routes, and firewall rules; veth pairs and bridges connect them.
- UTS namespaces isolate hostname; IPC namespaces isolate SysV queues and shared memory; user namespaces remap UIDs.
- User namespaces grant a process root privileges inside the namespace without host root, powering rootless containers.
- Time and cgroup namespaces are newer; /proc/<pid>/ns/ shows a process's namespace set, and unshare -n gives a shell in a new netns.
- Commands: unshare(1) creates namespaces; nsenter enters an existing one; ip netns manages network namespaces.

## Related
- [[wiki/os-shell/containers-vs-vms|Containers vs VMs]] — what containers assemble from namespaces
- [[wiki/os-shell/cgroups-and-resource-control|cgroups & Resource Control]] — limits paired with namespaces
- [[wiki/os-shell/filesystem-mounts|Filesystem Mounts]] — mount namespaces in action
- [[wiki/infrastructure/network-policy|Network Policy]] — isolating namespaced traffic
- [[wiki/security-auth/network-segmentation|Network Segmentation]] — security boundaries at the netns level
