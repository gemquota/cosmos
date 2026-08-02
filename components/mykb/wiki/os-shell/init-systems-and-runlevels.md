---
type: "concept"
title: "Init Systems & Runlevels"
description: "sysvinit, systemd targets, and boot ordering"
tags: ["init", "systemd", "runlevels", "sysvinit", "boot"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://www.freedesktop.org/software/systemd/man/latest/systemd.html", "https://man7.org/linux/man-pages/man7/boot.7.html"]
---

# Init Systems & Runlevels

## Summary
The init system is PID 1: the first userspace process, responsible for starting and supervising everything else. sysvinit used runlevels and sequential shell scripts; systemd uses parallel unit dependencies and targets, and nearly every modern distribution has adopted it.

## Details
- sysvinit defines runlevels 0-6: 0 halt, 1 single-user, 2-5 multiuser variants, 6 reboot; /etc/rc?.d/ holds start/stop scripts.
- systemd replaces runlevels with targets: multi-user.target for text login, graphical.target adding the display manager.
- Units (.service, .socket, .mount, .timer) declare dependencies; systemd starts independent units in parallel, cutting boot time.
- Socket activation defers service startup until a connection arrives; cgroups track service processes for clean shutdown.
- systemd-analyze blame shows per-unit startup time; systemctl isolate target switches modes like old runlevels.
- Compatibility layers run legacy init scripts, and distributions still ship rc-local hooks for one-off startup commands.
- Alternatives exist (OpenRC, runit, s6) but the unit model and journal integration make systemd the ecosystem default.

## Related
- [[wiki/os-shell/boot-process|Boot Process]] — PID 1 takes over from the kernel
- [[wiki/os-shell/systemd-units|Systemd Units]] — the unit files this system runs
- [[wiki/os-shell/systemd-journal|systemd-journal]] — logging owned by the init system
- [[wiki/os-shell/process-supervision|Process Supervision]] — what init does for services
- [[wiki/os-shell/containers-vs-vms|Containers vs VMs]] — init also runs inside containers
