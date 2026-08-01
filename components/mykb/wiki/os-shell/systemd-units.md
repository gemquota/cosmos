---
type: "concept"
title: "Systemd Units"
description: "The declarative service, socket, timer, and mount definitions supervised by systemd"
tags: ["systemd", "services", "init", "supervision"]
timestamp: "2026-08-01T00:00:00Z"
status: "stub"
---

# Systemd Units

## Summary
systemd units are declarative files that define what to run and how: services, timers, sockets, mounts, targets. `systemctl` starts, stops, enables, and inspects them, giving Linux a unified supervision model.

## Details
- A unit file declares ExecStart, dependencies, restart policies, and environment.
- Timers replace cron for most scheduled jobs with richer semantics.
- RSIS3 relevance: long-running daemons (memory bridge, dashboards) are systemd-shaped services.

## Related
- [[wiki/os-shell/process-management|Process Management]] — systemd supervises process lifecycles
- [[wiki/os-shell/process-signals|Process Signals]] — units define how signals are delivered
- [[wiki/devops-infra/observability|Observability]] — journald collects unit logs
- [[wiki/api-protocols/health-checks|Health Checks]] — service health maps to unit state
