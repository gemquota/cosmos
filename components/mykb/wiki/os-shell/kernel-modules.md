---
type: "concept"
title: "Kernel Modules"
description: "Loadable modules, modprobe, and dependency resolution"
tags: ["kernel-modules", "modprobe", "drivers", "lsmod", "kernel"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://man7.org/linux/man-pages/man8/modprobe.8.html", "https://docs.kernel.org/kbuild/modules.html"]
---

# Kernel Modules

## Summary
Kernel modules are loadable chunks of kernel code — usually device drivers and filesystems — that can be inserted and removed at runtime. modprobe resolves their dependencies and parameters, keeping the base kernel small while still supporting arbitrary hardware.

## Details
- Modules live in /lib/modules/$(uname -r)/ as .ko files; modinfo displays their description, license, and parameters.
- modprobe reads modules.dep, which records dependencies, and loads the full closure; insmod loads a single module and rmmod unloads it.
- lsmod lists loaded modules with their use counts; a module with dependents refuses to unload until they are removed.
- Kernel parameters configure modules at load time (e.g., modprobe bonding mode=1) or via /etc/modprobe.d/*.conf.
- Modules are either built-in (=y), modular (=m), or absent; built-ins cannot be unloaded and boot without initramfs help.
- Firmware files (request_firmware) are loaded from /lib/firmware when a module initializes hardware.
- Security: module loading is root-only; Secure Boot requires signed modules, and kernel lockdown restricts insertion.

## Related
- [[wiki/os-shell/device-drivers|Device Drivers]] — the primary content of modules
- [[wiki/os-shell/boot-process|Boot Process]] — early module loading from initramfs
- [[wiki/os-shell/initramfs|initramfs]] — where boot-time modules are bundled
- [[wiki/os-shell/procfs-and-sysfs|procfs & sysfs]] — module state under /proc/modules
- [[wiki/security-auth/patch-management|Patch Management]] — updating modules with the kernel
