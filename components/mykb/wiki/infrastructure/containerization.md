---
type: "concept"
title: "Containerization"
description: "Packaging applications with their runtime dependencies into portable, isolated units that share a host kernel"
tags: ["containers", "oci", "docker", "virtualization", "infrastructure"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://www.docker.com/resources/what-container/"]
---

# Containerization

## Summary
Containerization packages an application with its libraries, config, and runtime into a portable image that executes in isolated user-space namespaces on a shared host kernel. Containers standardize how software is built, shipped, and run, which makes deployments reproducible across laptops, CI, and production. They are the atomic unit of scheduling in Kubernetes and the default deployment model in modern cloud-native stacks.

## Details
- The OCI image and runtime specifications standardize image layout and execution; Docker popularized the toolchain, while containerd and CRI-O are the common production runtimes.
- Containers share the host kernel and rely on cgroups for resource limits and namespaces for isolation — weaker isolation than virtual machines but dramatically lower overhead and faster startup.
- Images are built from content-addressed layers, so registries and local caches can share base layers across many applications, making distribution cheap.
- Kubernetes treats containers as the scheduling unit: one or more containers form a pod, and the scheduler places pods onto nodes.
- Comparison: VMs virtualize hardware (own kernel, seconds-to-minutes boot), containers virtualize the OS (shared kernel, milliseconds-to-seconds boot, higher density per host).
- Worked example: RSIS3-side services can be built as multi-stage Docker images and run identically on a laptop and in a cluster, removing environment drift between dev and prod.
- Security posture depends on the image content and runtime: minimal images, read-only filesystems, and rootless runtimes reduce the attack surface.

## Related
- [[wiki/infrastructure/container-scheduling|Container Scheduling]] — how Kubernetes places containers onto nodes
- [[wiki/infrastructure/pod-lifecycle|Pod Lifecycle]] — lifecycle events for containerized workloads
- [[wiki/devops-infra/kubernetes|Kubernetes]] — orchestrates containers at scale
- [[wiki/devops-infra/containerd|containerd]] — production container runtime
- [[wiki/devops-infra/docker-compose|Docker Compose]] — multi-container orchestration for local and small deployments
- [[wiki/security/container-hardening|Container Hardening]] — securing images and runtimes
