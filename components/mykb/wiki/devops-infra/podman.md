---
type: "entity"
title: "Podman"
description: "Daemonless, rootless container engine compatible with OCI images and the Docker CLI"
tags: ["podman", "containers", "oci", "linux", "devops"]
timestamp: "2026-07-31T00:00:00Z"
status: "growing"
---

# Podman

## Summary
Podman is a daemonless container engine that runs OCI images with a Docker-compatible CLI. Rootless operation and systemd integration make it a popular Docker alternative on Linux, particularly where a central root daemon is undesirable.

## Details
- Pods group containers the way Kubernetes does, easing local-to-cluster transitions.
- `podman-compose` maps compose files onto Podman; no central daemon means fewer attack vectors.
- On Android/Termux-style environments, lightweight runtimes like Podman matter when Docker is unavailable.
- Podman forks a per-command process instead of talking to a daemon, so each invocation runs in the caller's context and respects that user's permissions.
- Rootless mode maps container UIDs to unprivileged user namespaces, so even a compromised container does not automatically gain host root.
- Pods share network, IPC, and PID namespaces among their containers, mirroring the Kubernetes pod abstraction without needing a cluster.
- Image and container storage uses OCI layout and overlayfs layers, and images can be pulled from Docker Hub or any registry speaking the Docker distribution protocol.
- systemd integration allows containers to run as systemd units, with socket activation and dependency ordering handled by the service manager.
- Builds are handled by buildah underneath, and `podman build` can produce images from Dockerfiles, keeping the workflow familiar to Docker users.
- Networking options include bridge, host, and rootless slirp4netns/pasta modes, each with different isolation and performance trade-offs.
- Quadlet files let `podman run` configurations be declared as systemd units, making container startup reproducible across reboots.
- Volumes persist data independently of container lifecycles, and SELinux labels keep labeled hosts from denying container access.
- Healthchecks declared in images or run flags let systemd and monitoring restart unhealthy containers automatically.

## Related
- [[wiki/devops-infra/containerd|containerd]] — the runtime layer beneath
- [[wiki/devops-infra/docker-compose|Docker Compose]] — compose compatibility
- [[wiki/devops-infra/kubernetes|Kubernetes]] — pod concept source
- [[wiki/security/container-hardening|Container Hardening]] — rootless by default
