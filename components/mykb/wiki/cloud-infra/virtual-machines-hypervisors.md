---
type: "concept"
title: "Virtual Machines & Hypervisors"
description: "Hardware virtualization and the software that provides it"
tags: ["vm", "hypervisor", "virtualization", "cloud"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: [
  "https://docs.kernel.org/virt/kvm/index.html",
  "https://en.wikipedia.org/wiki/Hypervisor",
]
---

# Virtual Machines & Hypervisors

## Summary
Virtual machines emulate hardware so a guest OS runs in isolation under a hypervisor. Hypervisors come in type-1 (bare-metal) and type-2 (hosted) flavors. VMs remain the dominant unit of cloud compute despite containers.

## Details
- Type-1 hypervisors such as KVM and ESXi run directly on hardware; type-2 hypervisors such as VirtualBox run on an operating system.
- Hardware virtualization extensions (VT-x/AMD-V) make guests run near native speed.
- The kernel documentation describes KVM, the Linux virtualization module, and its architecture in detail.
- Each VM includes a guest kernel, making isolation strong but boot and memory overhead heavier than containers.
- Live migration and snapshots are hypervisor capabilities that containers lack by default and must build separately.
- In mykb, VMs connect to KVM/QEMU, containers vs VMs, autoscaling, and dedicated host articles.
- Provider consoles and CLI workflows differ, so the provider-specific articles in this cluster record the concrete steps and gotchas.
- Cost and latency tradeoffs for this choice are quantified in the capacity planning and cost-of-bandwidth articles.

## Related
- [[wiki/infrastructure/virtual-switches|Virtual Switches]]
- [[wiki/cloud-infra/dns-over-https|DNS over HTTPS]]
- [[wiki/cloud-infra/virtual-machines|Virtual Machines]]
- [[wiki/infrastructure/warehouse-clusters-and-virtual-warehouses|Warehouse Clusters And Virtual Warehouses]]
