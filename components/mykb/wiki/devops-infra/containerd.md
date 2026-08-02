---
type: "concept"
title: "containerd"
description: "Industry-standard OCI container runtime managing image lifecycle and execution"
tags: ["containerd", "containers", "oci", "runtime", "kubernetes"]
timestamp: "2026-07-31T00:00:00Z"
status: "growing"
source: ["https://containerd.io/", "https://github.com/containerd/containerd"]
---

# containerd

## Summary
containerd is the CNCF container runtime that manages image pull, storage, and process execution. It is the default runtime inside Docker and most Kubernetes clusters.

## Details
- OCI-spec compliant: runs standard images with runc-style low-level runtimes.
- Exposes a gRPC API for image and container lifecycle; used headlessly by K8s via CRI.
- Security: namespace isolation and configurable seccomp/AppArmor profiles.

## Architecture

containerd is a daemon that splits container management into distinct concerns. The `containerd` daemon owns image and content stores, while each running container gets a `containerd-shim` process that keeps the container alive independently of its client and hands execution to a low-level runtime such as runc. This split means a client crash does not kill the workload, and the runtime can be swapped without changing the management surface.

## Image Lifecycle

- Images are pulled from registries, verified by digest, and stored content-addressably in the content store.
- Snapshotters materialize writable layers on top of read-only image layers using overlayfs or other filesystems.
- Containers are created from an image plus a runtime spec that defines mounts, namespaces, and capabilities.

## Operational Notes

- `crictl` and `nerdctl` are common clients for CRI and Docker-compatible workflows respectively.
- Runtime security is configured through namespaces, seccomp profiles, AppArmor or SELinux, and read-only root filesystems.
- The CRI plugin is what Kubernetes talks to, so runtime upgrades are coordinated with cluster versions.

## Related

- [[wiki/devops-infra/kubernetes|Kubernetes]] — CRI runtime integration
- [[wiki/devops-infra/podman|Podman]] — higher-level engine on similar runtimes
- [[wiki/security/container-hardening|Container Hardening]] — runtime security config
- [[wiki/devops-infra/docker-compose|Docker Compose]] — user-facing orchestration
- [[wiki/infrastructure/containerization|Containerization]] — the isolation model containerd runs
- [[wiki/infrastructure/container-registries|Container Registries]] — where images are pulled from

## Related
- [[wiki/devops-infra/kubernetes|Kubernetes]] — CRI runtime integration
- [[wiki/devops-infra/podman|Podman]] — higher-level engine on similar runtimes
- [[wiki/security/container-hardening|Container Hardening]] — runtime security config
- [[wiki/devops-infra/docker-compose|Docker Compose]] — user-facing orchestration
