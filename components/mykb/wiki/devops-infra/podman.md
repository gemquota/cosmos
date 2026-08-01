---
type: "concept"
title: "Podman"
description: "Daemonless, rootless container engine compatible with OCI images and the Docker CLI"
tags: ["podman", "containers", "oci", "linux", "devops"]
timestamp: "2026-07-31T00:00:00Z"
status: "stub"
---

# Podman

## Summary
Podman is a daemonless container engine that runs OCI images with a Docker-compatible CLI. Rootless operation and systemd integration make it a popular Docker alternative on Linux.

## Details
- Pods group containers the way Kubernetes does, easing local-to-cluster transitions.
- `podman-compose` maps compose files onto Podman; no central daemon means fewer attack vectors.
- On Android/Termux-style environments, lightweight runtimes like Podman matter when Docker is unavailable.

## Related
- [[wiki/devops-infra/containerd|containerd]] — the runtime layer beneath
- [[wiki/devops-infra/docker-compose|Docker Compose]] — compose compatibility
- [[wiki/devops-infra/kubernetes|Kubernetes]] — pod concept source
- [[wiki/security/container-hardening|Container Hardening]] — rootless by default
