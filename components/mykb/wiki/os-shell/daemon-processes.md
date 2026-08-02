---
type: "concept"
title: "Daemon Processes"
description: "Detaching from terminals, setsid/double-fork, and service-style background processes"
tags: ["daemons", "background", "setsid", "supervision", "services"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://man7.org/linux/man-pages/man7/daemon.7.html", "https://man7.org/linux/man-pages/man3/daemon.3.html"]
---

# Daemon Processes

## Summary
A daemon is a long-running background process deliberately detached from the terminal so it survives session logout and never gets stray signals from keyboard input. Traditional Unix daemons are produced by forking, calling setsid, and redirecting standard streams; modern services are often simple foreground processes supervised by systemd.

## Details
- The classic recipe: fork, have the parent exit, then call setsid() so the child becomes session leader with no controlling terminal.
- A second fork prevents the process from ever reacquiring a controlling terminal, since a session leader that opens a terminal device may get one.
- Daemons change directory to /, set umask to 0, and redirect stdin, stdout, and stderr to /dev/null or a log file.
- PID files (/run/<name>.pid) let administrators find and signal the daemon; systemd tracks processes via cgroups instead.
- systemd services commonly run in the foreground (Type=simple) and let the supervisor handle forking, restart, and logging.
- The daemon(3) library function wraps the classic steps, but modern advice is to skip double-forking entirely under a supervisor.
- Detachment tradeoffs: losing the terminal means losing job control, interactive prompts, and easy stderr inspection.

## Related
- [[wiki/os-shell/process-groups-and-sessions|Process Groups & Sessions]] — setsid is the key detachment call
- [[wiki/os-shell/process-supervision|Process Supervision]] — how modern systems manage daemon lifecycles
- [[wiki/os-shell/systemd-units|Systemd Units]] — Type=forking versus simple service definitions
- [[wiki/os-shell/stdin-stdout-stderr|Stdin, Stdout & Stderr]] — the redirected streams daemons use
- [[wiki/os-shell/syslog-and-logging|Syslog & Logging]] — where detached daemons report errors
