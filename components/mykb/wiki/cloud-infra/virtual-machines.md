---
type: "concept"
title: "Virtual Machines"
description: "Hardware-virtualized compute instances that remain the unit of infrastructure-as-a-service (IaaS)"
tags: ["virtual-machines", "hypervisor", "iaas", "compute", "cloud"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/concepts.html"]
---

# Virtual Machines

## Summary
Virtual machines emulate complete computers on top of a hypervisor, giving each guest its own kernel, memory, and devices. They are the basic unit of IaaS compute, offered in families tuned for general, compute-, memory-, or GPU-heavy work. VMs trade density for stronger isolation compared with containers.

## Details
- Hypervisors virtualize hardware: type-1 hypervisors run directly on hardware (KVM, Xen); type-2 run as host applications. The hypervisor multiplexes CPUs, memory, and I/O between guests.
- Instance families tune vCPU/RAM ratios: general-purpose, compute-optimized, memory-optimized, storage-optimized, and GPU accelerators.
- Lifecycle: VMs boot from images (AMIs, cloud images), attach block storage, join networks, and can be snapshotted, migrated, or resized.
- Pricing models: on-demand, spot (interruptible, cheap), and reserved capacity (commitment discount) — see the related stubs for trade-offs.
- Comparison: VMs boot in seconds-to-minutes with their own kernel (strong isolation, full control), while containers share the host kernel and boot faster at higher density.
- Placement and resilience: VMs span availability zones; instance health is tied to host maintenance events, so workloads should be designed for replacement.
- Worked example: a mykb postgres replica on a memory-optimized VM in zone A, with nightly snapshots and a spot-capable worker pool for batch jobs.

## Related
- [[wiki/cloud-infra/availability-zones|Availability Zones]] — failure domains for VM placement
- [[wiki/devops-infra/kubernetes|Kubernetes]] — container orchestration that runs on VMs
- [[wiki/cloud-infra/spot-instances|Spot Instances]] — cheap interruptible VM capacity
- [[wiki/cloud-infra/reserved-capacity|Reserved Capacity]] — committed-use discounts
- [[wiki/cloud-infra/right-sizing|Right-Sizing]] — matching VM size to workload
- [[wiki/infrastructure/containerization|Containerization]] — the lighter-weight alternative
- [[wiki/devops-infra/terraform|Terraform]] — provisioning VMs as code
