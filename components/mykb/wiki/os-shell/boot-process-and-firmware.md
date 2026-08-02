---
type: "concept"
title: "Boot Process & Firmware"
description: "From power-on to kernel: firmware, bootloaders, and initrd"
tags: ["boot", "firmware", "uefi", "kernel"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: [
  "https://wiki.archlinux.org/title/Arch_boot_process",
  "https://wiki.archlinux.org/title/Unified_Extensible_Firmware_Interface",
]
---

# Boot Process & Firmware

## Summary
The boot process runs from power-on through firmware, bootloader, and kernel to userspace. UEFI replaced BIOS as the firmware standard, and bootloaders chain into the kernel with an initramfs. Boot debugging is a core Linux administration skill for datacenter and edge machines.

## Details
- UEFI firmware finds boot entries, loads a bootloader, and hands off to the kernel in protected mode.
- The Arch wiki documents the full boot flow and its configuration points.
- The initrd/initramfs provides early userspace with drivers needed to mount the real root.
- Secure Boot verifies the bootloader and kernel signatures.
- Failure symptoms (no display, kernel panic, missing root) map to distinct stages.
- In mykb, boot connects to firmware, systemd, and first-boot configuration.
- Boot logs and early console output identify which stage failed first.
- Network booting via PXE provisions bare metal without local media.
- Kernel and userspace behavior meet here; the related process, memory, and filesystem articles provide the implementation detail.

## Related
- [[wiki/devops-infra/first-boot-configuration|First-Boot Configuration]]
- [[wiki/os-shell/namespace-networking|Namespace Networking]]
- [[wiki/os-shell/boot-process|Boot Process]]
- [[wiki/infrastructure/data-rfc-process|Data Rfc Process]]
