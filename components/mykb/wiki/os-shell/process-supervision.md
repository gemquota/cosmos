---
type: "concept"
title: "Process Supervision"
description: "Supervisors, restart policies, and daemon management"
tags: ["supervision", "daemons", "restart", "systemd", "supervisor"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://man7.org/linux/man-pages/man8/supervise.8.html", "https://www.freedesktop.org/software/systemd/man/latest/systemd.service.html"]
---

# Process Supervision

## Summary
A process supervisor keeps services running: it starts them at boot, restarts them on failure, captures their logs, and enforces limits. systemd, runit, s6, and supervisord are the common supervisors, differing in lifecycle model and restart policy.

## Details
- systemd services use Restart= (no, on-failure, always, on-abnormal) plus RestartSec backoff; Restart=always survives any exit.
- Type=simple means the main process is the service; Type=forking waits for a pidfile — prefer simple for new daemons.
- runit's run scripts and s6's supervision tree follow the daemontools model: a supervise process restarts a foreground run script.
- supervisord manages many user processes with [program:x] sections, common in containers and Python deployments.
- Watchdogs: systemd's WatchdogSec + sd_notify let a service prove liveness; failing to ping triggers restart.
- Logging is part of supervision: stderr is captured to the journal or log files, so restart loops are diagnosable.
- Restart storms need protection — backoff, start limits (StartLimitIntervalSec), and circuit-breaking are part of the discipline.

## Related
- [[wiki/os-shell/daemon-processes|Daemon Processes]] — what supervisors replace
- [[wiki/os-shell/systemd-units|Systemd Units]] — the unit files defining supervision
- [[wiki/os-shell/systemd-journal|systemd-journal]] — where supervised output lands
- [[wiki/os-shell/process-signals|Process Signals]] — how supervisors stop and restart
- [[wiki/infrastructure/graceful-termination|Graceful Termination]] — clean shutdown under supervision
