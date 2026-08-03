---
type: "concept"
title: "NVIDIA Container Toolkit"
description: "Exposing GPUs to containers with driver injection and CDI"
tags: ["nvidia", "containers", "gpu", "cdi"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# NVIDIA Container Toolkit

## Summary
The NVIDIA Container Toolkit is the software that makes GPUs usable inside containers: it injects the NVIDIA driver's user-space libraries and creates the device nodes a container needs, so a containerized workload can access the host's GPU without shipping a driver in the image. It is the standard mechanism behind GPU workloads on Docker and Kubernetes (via the device plugin), and its design reflects the core rule of GPU containers: the driver stays on the host, the toolkit bridges it into the container.

## Details
- The mechanism: the toolkit (nvidia-container-toolkit, formerly nvidia-docker2) works through the container runtime — when a container requests GPUs (via `--gpus all` or a resource request), the toolkit's runtime hook inspects the request, mounts the host's NVIDIA libraries (libcuda, libnvidia-ml, the CUDA userspace stack) and the device nodes (/dev/nvidia0, /dev/nvidiactl, /dev/nvidia-uvm) into the container, and sets the environment (CUDA paths, visibility). The container image only needs the CUDA runtime/libraries matching the host driver's supported version range — never the kernel driver itself, which must match the host kernel and cannot be containerized. The failure mode this design prevents: the "driver in the image" trap, where a container ships a driver that conflicts with the host kernel — the classic source of "CUDA driver version is insufficient" and module-load failures.
- The version contract: the host driver is backward-compatible with older CUDA toolkits (a newer driver runs older CUDA runtime libraries), and each CUDA version requires a minimum driver version. The practical rule: pin the driver at the node level, build images against a CUDA base within the supported range, and validate with nvidia-smi inside the container. The failure mode is the mismatch: an image built with a CUDA newer than the host driver fails at load time with a cryptic driver-version error — which is why the toolkit's job includes surfacing a clean diagnostic.
- CDI (Container Device Interface) is the modern refinement: instead of the runtime hook, the toolkit generates CDI specifications that declare the devices, mounts, and environment for GPU access, and runtimes with CDI support consume them natively — making GPU containers declarative and removing the toolkit's runtime-hook dependency. Kubernetes uses the device plugin (nvidia-device-plugin) to advertise GPUs as allocatable resources and the toolkit's CDI specs to wire the allocation.
- The operational practices: install the toolkit on every GPU node, configure the default runtime (or the CDI spec), run `nvidia-smi` in a test container to validate, and keep driver and toolkit versions aligned across the fleet — the version matrix is the single biggest source of GPU-container incidents.
- For mykb: the toolkit is the containerization layer under GPU infrastructure — it connects container runtimes, OCI images, and the device-plugin story.

## Related
- [[wiki/devops-infra/container-runtimes|Container Runtimes]]
- [[wiki/devops-infra/container-images-oci|Container Images (OCI)]]
- [[wiki/devops-infra/container-network-interfaces|Container Network Interfaces]]
- [[wiki/devops-infra/container-storage-interfaces|Container Storage Interfaces]]
- [[wiki/syntheses/knowledge-acquisition-workflow|Knowledge Acquisition Workflow]] — how stubs grow into full articles in mykb
- [[wiki/syntheses/mykb-acquisition-curation-and-practices|Acquisition, Curation & Practices]] — the curation loop this stub belongs to
