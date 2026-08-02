---
type: "concept"
title: "Boot Process"
description: "Firmware to bootloader to kernel to init sequence"
tags: ["boot", "bootloader", "kernel", "firmware", "uefi"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://man7.org/linux/man-pages/man7/boot.7.html", "https://systemd.io/BOOT_LOADER_INTERFACE/"]
---

# Boot Process

## Summary
Booting Linux is a chain of increasingly capable stages: firmware initializes hardware, a bootloader loads the kernel and initramfs into memory, the kernel mounts a temporary root, and the first userspace process (init) brings up the real system.

## Details
- Firmware: BIOS performs POST and reads the boot sector; UEFI reads a FAT partition with an EFI system partition and can boot directly with Secure Boot validation.
- Bootloaders: GRUB reads /boot/grub/grub.cfg, loads kernel and initramfs, and can chain other operating systems; systemd-boot is the minimal UEFI alternative.
- The kernel decompresses itself, sets up page tables, memory management, and drivers, then unpacks the initramfs as its first root filesystem.
- initramfs runs early userspace: it loads storage drivers, assembles md/dm devices, decrypts LUKS, and finds the real root.
- switch_root (or pivot_root) replaces the initramfs root with the real one, then execs init — PID 1.
- PID 1 (systemd or sysvinit) mounts the real filesystem table, starts units in dependency order, and eventually reaches multi-user.target.
- Kernel command line (quiet, root=, console=) tunes the process; systemd-analyze plot and dmesg show where time goes.

## Related
- [[wiki/os-shell/initramfs|initramfs]] — early userspace before the real root
- [[wiki/os-shell/init-systems-and-runlevels|Init Systems & Runlevels]] — what PID 1 does next
- [[wiki/os-shell/kernel-modules|Kernel Modules]] — the drivers early boot must load
- [[wiki/os-shell/filesystem-mounts|Filesystem Mounts]] — mounting the real root
- [[wiki/os-shell/block-devices-and-partitions|Block Devices & Partitions]] — the disks boot reads
