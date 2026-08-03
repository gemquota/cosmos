---
type: "concept"
title: "Kernel Modules & Loading"
description: "Loadable kernel objects, module parameters, and udev integration"
tags: ["kernel", "modules", "kmod", "linux"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# Kernel Modules & Loading

## Summary
Loadable kernel modules (LKMs) let the kernel gain functionality without a reboot: drivers, filesystems, and netfilter helpers ship as `.ko` files that `modprobe`/`insmod` load into the running kernel. Module parameters, dependency resolution, and udev-driven auto-loading turn a monolithic core into a composable system where hardware arrival triggers the right driver automatically.

## Details
- Mechanism: modules are relocatable ELF objects linked against kernel symbols (`EXPORT_SYMBOL`); `insmod` loads a specific file, `modprobe` resolves dependencies via `modules.dep` and handles parameters from `modprobe.conf` and `modprobe.d`. Modules declare `module_init`/`module_exit` entry points and `MODULE_LICENSE`, `MODULE_ALIAS`, and `MODULE_PARM_DESC` metadata; aliases are how udev maps a device (e.g., a PCI vendor/device ID) to a module name, triggering `modprobe` on hotplug. The module loader also handles module signing (enforced when `CONFIG_MODULE_SIG_FORCE` is set, in which case unsigned modules fail to load) and, since lockdown mode, restricts which modules may be loaded based on integrity policy.
- Concrete examples: inserting a USB WiFi adapter causes udev to load `rtl8xxxu`; `modprobe vfio-pci` with `options vfio-pci ids=10de:1db6` binds a GPU to VFIO for passthrough; `modprobe nbd max_part=8` passes a parameter; `lsmod` shows loaded modules and their users; `modinfo` prints a module's description, author, and dependencies; `/etc/modprobe.d/blacklist.conf` blocks problematic drivers; `modprobe -r` unloads when the refcount drops to zero.
- Failure modes: the classic failures are loading a module for the wrong kernel version (vermagic mismatch — "invalid module format"), unresolved symbols (a module built against a different config), and unloading a module that is still in use (refcount prevents it, or `rmmod -f` corrupts the kernel by force-removing a module with active users). Blacklisting the wrong module can silently disable hardware; and signing/lockdown enforcement means distribution modules fail with a signature error on a system with secure boot unless they are signed.
- Operational tradeoffs: modules keep the base kernel small and hardware support dynamic, at the cost of a larger attack surface (a buggy module can panic the kernel) and boot-time complexity (initramfs must contain the modules needed before the root filesystem mounts). The practice rules: rely on distribution-built modules and `modprobe` rather than hand-built ones, keep module signing and secure boot enabled where possible, blacklist deliberately and document why, and treat "module not found for this device" as a version/config diagnosis, not a reboot solution.
- RSIS3/mykb relevance: module loading is dependency resolution with a registry (modprobe alias tables, modules.dep) — the same discipline as the wiki's link graph, where a new capability (driver, article) registers aliases so lookup by identifier (device ID, concept name) finds the right implementation automatically.

## Related
- [[wiki/os-shell/kernel-architecture|Kernel Architecture]] — related coverage in the same cluster
- [[wiki/devops-infra/terraform-workspaces-and-modules|Terraform Workspaces & Modules]] — related coverage in the same cluster
- [[wiki/infrastructure/kernel-bypass-networking|Kernel-Bypass Networking]] — related coverage in the same cluster
- [[wiki/os-shell/kernel-modules|Kernel Modules]] — related coverage in the same cluster
- [[wiki/os-shell/memory-management-paging|Memory Management & Paging]] — related coverage in the same cluster
- [[wiki/syntheses/knowledge-acquisition-workflow|Knowledge Acquisition Workflow]] — how stubs grow into full articles in mykb
- [[wiki/syntheses/mykb-acquisition-curation-and-practices|Acquisition, Curation & Practices]] — the curation loop this stub belongs to
