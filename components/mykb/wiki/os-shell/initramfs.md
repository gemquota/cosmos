---
type: "concept"
title: "initramfs"
description: "Early userspace, root mounting, and rescue"
tags: ["initramfs", "boot", "initrd", "kernel"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://docs.kernel.org/filesystems/ramfs-rootfs-initramfs.html", "https://man7.org/linux/man-pages/man7/boot.7.html"]
---

# initramfs

## Summary
The initramfs is a small cpio archive the bootloader loads alongside the kernel; the kernel unpacks it into a tmpfs root so that early userspace can load drivers and mount the real root filesystem. It replaces the older initrd block-device scheme.

## Details
- The kernel always needs some root: initramfs is a cpio archive unpacked into rootfs, a special in-memory filesystem that cannot be unmounted.
- Early userspace runs /init, which may be a shell or a tool like systemd: it loads storage, RAID, and crypto modules, assembles devices, and finds root=.
- The real root is mounted read-only first, then switched with switch_root(8), which moves the mount, chroots, and execs init on the real filesystem.
- Generators: dracut (Fedora/RHEL), initramfs-tools (Debian/Ubuntu), mkinitcpio (Arch) build the archive from the running kernel's modules.
- Rescue value: booting with init=/bin/sh on the kernel line drops into a shell inside the initramfs for repair.
- Compressed and small (tens of MB), the initramfs lives in /boot and can be inspected with lsinitrd or unmkinitramfs.
- On UEFI systems the kernel and initramfs may be combined into a single EFI stub binary for secure, self-contained boot.

## Related
- [[wiki/os-shell/boot-process|Boot Process]] — where the initramfs sits in the chain
- [[wiki/os-shell/filesystem-mounts|Filesystem Mounts]] — mounting and switching roots
- [[wiki/os-shell/kernel-modules|Kernel Modules]] — what early userspace loads
- [[wiki/os-shell/block-devices-and-partitions|Block Devices & Partitions]] — finding the root device
- [[wiki/os-shell/kernel-space-vs-user-space|Kernel vs User Space]] — the boundary early userspace crosses
