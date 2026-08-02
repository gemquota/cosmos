---
type: "concept"
title: "Containers vs VMs"
description: "Isolation boundaries, overhead, and hypervisors"
tags: ["containers", "virtualization", "hypervisor", "isolation"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://man7.org/linux/man-pages/man7/namespaces.7.html", "https://www.kernel.org/doc/html/latest/virt/kvm/index.html"]
---

# Containers vs VMs

## Summary
Containers isolate processes with kernel features — namespaces and cgroups — while sharing the host kernel; virtual machines run a complete guest OS on virtualized hardware under a hypervisor. Containers are lightweight and fast; VMs provide a hard isolation boundary.

## Details
- Containers share the kernel: a container escape is a kernel exploit, so the blast radius is the host kernel itself.
- VMs (KVM, VirtualBox, cloud instances) present virtual CPU, memory, disk, and NICs; each guest boots its own kernel.
- Overhead: containers add near-zero startup cost and share memory pages; VMs pay for guest kernel boot and device emulation.
- Hypervisor isolation: hardware virtualization (VT-x/AMD-V) lets the hypervisor run guests at near-native speed; type 1 (KVM, ESXi) runs directly on hardware.
- Hybrid approaches exist: Kata Containers and gVisor wrap containers in a lightweight VM or user-space kernel for stronger isolation.
- Packaging overlap: container images bundle an app and its userspace; VM images bundle a full OS, making them heavier but more self-contained.
- Orchestration reflects the difference: kubernetes schedules containers; cloud providers schedule VMs underneath.

## Related
- [[wiki/os-shell/linux-namespaces|Linux Namespaces]] — the isolation primitive behind containers
- [[wiki/os-shell/cgroups-and-resource-control|cgroups & Resource Control]] — container resource limits
- [[wiki/infrastructure/containerization|Containerization]] — packaging workflows
- [[wiki/cloud-infra/virtual-machines|Virtual Machines]] — VM lifecycle in the cloud
- [[wiki/devops-infra/kubernetes|Kubernetes]] — container orchestration at scale
