---
type: "concept"
title: "Container Runtimes"
description: "The software that actually runs containerized processes"
tags: ["containers", "runtimes", "oci", "kubernetes"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: [
  "https://opencontainers.org/",
  "https://kubernetes.io/docs/setup/production-environment/container-runtimes/",
]
---

# Container Runtimes

## Summary
Container runtimes are the software that turns an OCI image into a running process with namespaces, cgroups, and a root filesystem. The Kubernetes CRI abstracts them behind one interface. Runtime choice affects isolation, performance, and security.

## Details
- The OCI runtime spec defines how a container bundle is created and run, including mounts, namespaces, and hooks.
- The CRI (Container Runtime Interface) lets Kubernetes talk to runtimes such as containerd and CRI-O.
- Low-level runtimes like runc and crun execute the container process; high-level runtimes manage images and lifecycle.
- Kubernetes documents supported runtimes and their configuration through the CRI and kubelet settings.
- Isolation varies by runtime: runc uses kernel namespaces, while gVisor and Kata add extra guest boundaries.
- In mykb, container runtimes link to OCI images, runc/crun, cgroups, and Kubernetes scheduling.
- Operationally, alerting thresholds and runbook steps for this concept belong in the SLO, incident, and runbook articles of this cluster.
- Pipelines and GitOps practices in the delivery articles show how this concept is deployed and promoted safely.

## Related
- [[wiki/devops-infra/container-network-interfaces|Container Network Interfaces]]
- [[wiki/devops-infra/container-storage-interfaces|Container Storage Interfaces]]
- [[wiki/infrastructure/container-registries|Container Registries]]
- [[wiki/infrastructure/container-scanning|Container Scanning]]
