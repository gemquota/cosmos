---
type: "entity"
title: "KVM & QEMU"
description: "The Linux hypervisor and the emulator that front-ends it"
tags: ["kvm", "qemu", "virtualization", "linux"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: [
  "https://www.qemu.org/documentation/",
  "https://docs.kernel.org/virt/kvm/index.html",
]
---

# KVM & QEMU

## Summary
KVM turns Linux into a type-1 hypervisor using hardware virtualization, while QEMU provides device emulation and user-facing tooling. Together they power most cloud VMs and local virtualization on Linux. The pairing is the reference open-source virtualization stack, and it anchors the virtualization articles in mykb.

## Details
- KVM exposes /dev/kvm and uses CPU virtualization extensions to run guest operating systems efficiently.
- QEMU emulates devices and machine types, and with KVM acceleration it approaches native performance for guests.
- QEMU documentation covers system emulation, networking, and storage options for full virtual machines.
- libvirt and virt-manager add management layers above QEMU/KVM for pools, networks, and domains.
- Live migration moves running VMs between hosts using shared storage and state transfer without downtime.
- In mykb, KVM/QEMU connect to hypervisors, containers vs VMs, and dedicated host articles.
- Kernel-based VMs benefit from mainline security and performance work, which is why KVM underlies most public cloud instances.
- Kernel and userspace behavior meet here; the related process, memory, and filesystem articles provide the implementation detail.

## Related
- [[wiki/os-shell/namespace-networking|Namespace Networking]]
- [[wiki/os-shell/kernel-modules-and-loading|Kernel Modules & Loading]]
- [[wiki/os-shell/access-control-lists|Access Control Lists]]
- [[wiki/os-shell/ansi-escape-sequences|ANSI Escape Sequences]]
