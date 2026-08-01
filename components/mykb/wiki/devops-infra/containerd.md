---
type: "concept"
title: "containerd"
description: "Industry-standard OCI container runtime managing image lifecycle and execution"
tags: ["containerd", "containers", "oci", "runtime", "kubernetes"]
timestamp: "2026-07-31T00:00:00Z"
status: "stub"
---

# containerd

## Summary
containerd is the CNCF container runtime that manages image pull, storage, and process execution. It is the default runtime inside Docker and most Kubernetes clusters.

## Details
- OCI-spec compliant: runs standard images with runc-style low-level runtimes.
- Exposes a gRPC API for image and container lifecycle; used headlessly by K8s via CRI.
- Security: namespace isolation and configurable seccomp/AppArmor profiles.

## Related
- [[wiki/devops-infra/kubernetes|Kubernetes]] — CRI runtime integration
- [[wiki/devops-infra/podman|Podman]] — higher-level engine on similar runtimes
- [[wiki/security/container-hardening|Container Hardening]] — runtime security config
- [[wiki/devops-infra/docker-compose|Docker Compose]] — user-facing orchestration
