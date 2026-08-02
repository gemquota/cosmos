---
type: "concept"
title: "runc & crun"
description: "Low-level OCI runtime implementations"
tags: ["oci", "runc", "crun", "containers"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: [
  "https://github.com/opencontainers/runc",
  "https://github.com/containers/crun",
]
---

# runc & crun

## Summary
runc and crun are the low-level OCI runtime implementations that actually launch container processes. They apply namespaces, cgroups, and seccomp to a prepared bundle. Most production containers run under one of these two engines.

## Details
- runc is the reference OCI runtime implementation, originally extracted from Docker and now maintained by the Open Containers Initiative under an open governance model.
- crun is a C implementation designed for lower memory use and faster startup, popular in minimal distributions.
- Both consume an OCI bundle: a config.json describing the process, mounts, and resource limits.
- High-level runtimes like containerd and CRI-O invoke runc or crun on their behalf to start and stop container processes.
- Differences matter at scale: crun's smaller footprint suits tiny nodes and edge devices.
- In mykb, runc/crun connect to container runtimes, cgroups, namespaces, and image articles.
- Kernel and userspace behavior meet here; the related process, memory, and filesystem articles provide the implementation detail.

## Related
- [[wiki/os-shell/namespace-networking|Namespace Networking]]
- [[wiki/os-shell/kernel-modules-and-loading|Kernel Modules & Loading]]
- [[wiki/os-shell/access-control-lists|Access Control Lists]]
- [[wiki/os-shell/ansi-escape-sequences|ANSI Escape Sequences]]
