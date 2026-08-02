---
type: "concept"
title: "Containerization Practice"
description: "Packaging software with its runtime into portable, isolated units"
tags: ["containers", "docker", "isolation", "practice"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://en.wikipedia.org/wiki/OS-level_virtualisation", "https://en.wikipedia.org/wiki/Docker_(software)"]
---

# Containerization Practice

## Summary
Containerization packages an application with its runtime, libraries, and config into a portable unit that runs the same way anywhere. Practice covers image construction, registry hygiene, resource limits, and the discipline of treating containers as immutable artifacts.

## Details
- Images are built from layered filesystems; multi-stage builds keep runtime images small and attack-surface lean.
- Pin base images by digest, scan them, and rebuild on a cadence so security fixes actually land.
- Containers isolate processes, not hostile workloads: rootless operation and seccomp/AppArmor matter for untrusted code.
- Resource limits (CPU, memory) are mandatory in shared environments; a container without limits is a neighbor problem.
- Immutable infrastructure: rebuild images rather than patching running containers.
- For the mykb bundle, the curation tooling ships as a container with pinned, scanned dependencies.
- Worked example — the wiki tool container: multi-stage build, distroless runtime, digest-pinned base, scanned in CI, and run rootless with a memory limit.

Worked example — the wiki tool container: multi-stage build, distroless runtime, digest-pinned base, scanned in CI, and run rootless with a memory limit.

## Related
- [[wiki/communities/multi-stage-builds|Multi-Stage Builds]]
- [[wiki/communities/base-image-management|Base Image Management]]
- [[wiki/communities/image-scanning|Image Scanning]]
- [[wiki/tooling/kubernetes-practice|Kubernetes Practice]]
- [[wiki/communities/registry-practice|Registry Practice]]
- [[wiki/communities/image-tagging|Image Tagging]]
- [[wiki/devops-infra/container-runtimes|Container Runtimes]]
- [[wiki/devops-infra/container-images-oci|Container Images (OCI)]]
