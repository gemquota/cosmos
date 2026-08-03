---
type: "concept"
title: "Device Drivers & udev"
description: "Kernel drivers and userspace device event handling"
tags: ["drivers", "udev", "kernel", "devices"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# Device Drivers & udev

## Summary
Device drivers are the kernel modules that make hardware usable, and udev is the userspace daemon that reacts when hardware appears: it receives kernel uevents, matches them against rules, and creates stable device nodes, symlinks, and permissions. Together they turn a raw PCI/USB device into something applications can open, like `/dev/sda` or a predictable `/dev/disk/by-uuid/...` path.

## Details
- Mechanism: a driver registers with a subsystem (PCI, USB, block, net) and binds to devices it matches; the kernel then exposes the device and generates uevents. udev (via `systemd-udevd`) listens, evaluates rules in `/etc/udev/rules.d/` (and `/usr/lib/udev/rules.d/`), and performs actions: creating nodes with the right owner/mode, adding symlinks, loading firmware, or running scripts. Rules match on attributes and environment: `SUBSYSTEM=="block", ATTR{size}=="...", SYMLINK+="disk/by-uuid/$attr{...}"`; `udevadm info` and `udevadm monitor` are the debugging tools.
- Concrete examples: a USB serial adapter appearing as `/dev/ttyUSB0`; a printer or audio device getting persistent ACLs so the logged-in user can access it (via `uaccess` tags); a storage device getting a stable `/dev/disk/by-uuid/` symlink so mounts survive drive letter changes; a GPU firmware loader that udev invokes at device arrival; `udevadm trigger` to re-run rules without replugging.
- Failure modes: the classic failures are race conditions at boot — udev must keep up with kernel events or devices appear "late", which historically caused flaky mount ordering (now solved by systemd's device units and `RequiresMountsFor`) — and overly broad or poorly matched rules that rename the wrong device or hang the boot on a slow script (rules should be short and synchronous; long work belongs in systemd services). Custom rules that assume an attribute that differs across kernel versions break silently on upgrade, and permissions mistakes (world-writable nodes) are a security hole.
- Operational tradeoffs: udev's predictability costs complexity — a rules engine plus event daemon is more moving parts than the old static `/dev` tree — but the payoff is stable device naming, dynamic permission management, and hotplug handling that static setups cannot provide. The practice rules: prefer existing distro rules and the `uaccess`/`seat` mechanism over custom scripts, keep custom rules minimal and well-commented, and validate with `udevadm test` before deploying. RSIS3/mykb relevance: the wiki's daemon and build tooling would depend on predictable device and mount paths; the same principle — stable names derived from attributes, not order of appearance — applies to how MyKB identifies articles by slug rather than by position.

## Related
- [[wiki/infrastructure/gpu-drivers-and-cuda|GPU Drivers & CUDA]]
- [[wiki/cloud-infra/block-device-mapping-gcp|Block Device Mapping on GCP]]
- [[wiki/os-shell/device-drivers|Device Drivers]]
- [[wiki/os-shell/kernel-architecture|Kernel Architecture]]
- [[wiki/os-shell/memory-management-paging|Memory Management & Paging]]
