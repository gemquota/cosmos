---
type: "concept"
title: "Linux Capabilities & SELinux"
description: "Discretionary privilege splitting and mandatory access control"
tags: ["capabilities", "selinux", "security", "linux"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: [
  "https://man7.org/linux/man-pages/man7/capabilities.7.html",
  "https://en.wikipedia.org/wiki/Security-Enhanced_Linux",
]
---

# Linux Capabilities & SELinux

## Summary
Linux capabilities split root's power into fine-grained privileges, while SELinux enforces mandatory access control with policies. Both reduce the blast radius of compromised processes beyond traditional permissions. They are the main hardening layers for Linux workloads and containers.

## Details
- Capabilities give processes specific privileges (CAP_NET_BIND_SERVICE, CAP_SYS_ADMIN) instead of all-or-nothing root.
- The capabilities man page defines every capability and its effect.
- SELinux labels processes and files and enforces type-enforcement rules.
- Policies must cover the application's actual needs, which is the adoption cost.
- Containers drop capabilities and run with seccomp to minimize kernel attack surface.
- In mykb, capabilities and SELinux connect to container security, permissions, and egress filtering.
- Capability bounding sets and ambient capabilities constrain what containers can gain.
- SELinux booleans and audit logs make policy tuning observable in production.
- Kernel and userspace behavior meet here; the related process, memory, and filesystem articles provide the implementation detail.
- Tuning this behavior in production relies on the system monitoring and resource utilization articles of this cluster.

## Related
- [[wiki/infrastructure/loopback-vs-linux-bridge|Loopback vs Linux Bridge]]
- [[wiki/os-shell/namespace-networking|Namespace Networking]]
- [[wiki/os-shell/linux-namespaces|Linux Namespaces]]
- [[wiki/os-shell/access-control-lists|Access Control Lists]]
