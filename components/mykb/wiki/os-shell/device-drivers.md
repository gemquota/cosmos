---
type: "concept"
title: "Device Drivers"
description: "Driver model, char/block devices, and major/minor numbers"
tags: ["device-drivers", "kernel", "char-devices", "block-devices"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://docs.kernel.org/driver-api/index.html", "https://www.kernel.org/doc/html/latest/admin-guide/devices.html"]
---

# Device Drivers

## Summary
Device drivers are kernel code that makes hardware usable: they translate standardized kernel operations into the register and protocol dances of specific devices. Linux's driver model ties drivers to devices through bus matching, and exposes them as device nodes under /dev.

## Details
- Devices appear to user space as files: character devices (terminals, serial ports, mice) transfer byte streams; block devices transfer fixed-size blocks.
- Each device node has a major number identifying the driver and a minor number identifying the instance, registered via alloc_chrdev_region.
- The driver core matches devices on buses (PCI, USB, platform) to drivers by ID tables, then calls the driver's probe function.
- User space reaches drivers through read/write/ioctl on the node; ioctl(2) is the escape hatch for device-specific operations.
- udev listens for uevents from sysfs and creates, names, and permissions device nodes dynamically (e.g., /dev/sda, /dev/input/mouse0).
- Modules make drivers loadable at runtime, but built-in drivers are required for the storage that mounts the real root.
- Driver bugs run in kernel context, so many drivers move complexity to user space (usbfs, vfio, uio) or use robust frameworks like devicetree overlays.

## Related
- [[wiki/os-shell/kernel-modules|Kernel Modules]] — the packaging of most drivers
- [[wiki/os-shell/block-devices-and-partitions|Block Devices & Partitions]] — block drivers in action
- [[wiki/os-shell/procfs-and-sysfs|procfs & sysfs]] — the device model exposed to user space
- [[wiki/os-shell/syscalls|System Calls]] — the operations drivers implement
- [[wiki/os-shell/kernel-space-vs-user-space|Kernel vs User Space]] — where drivers execute
