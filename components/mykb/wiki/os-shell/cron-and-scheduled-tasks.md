---
type: "concept"
title: "Cron & Scheduled Tasks"
description: "Scheduling recurring jobs with cron, systemd timers, and anacron"
tags: ["cron", "scheduling", "systemd", "automation"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# Cron & Scheduled Tasks

## Summary
Scheduling recurring jobs is the operating system's oldest automation problem, and Linux has three generations of answers: classic cron (with crontabs and `cron.d`), anacron (which catches jobs missed while the machine was off), and systemd timers (which integrate with units, dependencies, and logging). Modern distributions increasingly standardize on systemd timers for new services while cron remains ubiquitous for user crontabs.

## Details
- Mechanism: cron reads crontabs and runs jobs when the wall-clock time matches the five fields (minute, hour, day of month, month, day of week): `30 2 * * * /usr/local/bin/backup.sh` runs daily at 02:30. Vixie cron checks every minute; `anacron` instead stores the last run time per job and runs it at the next opportunity if the system was asleep or off at the scheduled moment — essential for laptops and desktops that are not always on. systemd timers replace the crontab with unit files: `OnCalendar=*-*-* 02:30:00` plus `Persistent=true` (catch up after downtime), and they add real features: dependency ordering, resource limits, on-boot and on-active triggers, randomized delays, and unified journal logging via `journalctl -u backup.timer`.
- Concrete examples: `crontab -e` for a user's daily backups; `/etc/cron.d/` drop-ins for packaged jobs; `systemd-run --on-calendar='daily'` to schedule ad hoc jobs without writing unit files; `systemctl list-timers` to see the next fire times; `OnBootSec=5min` plus `RandomizedDelaySec` to spread post-boot jobs; `Persistent=true` on a laptop timer so a missed nightly sync runs at next power-on.
- Failure modes: the classic failures are environment surprises — cron jobs run with a minimal `PATH` and no interactive shell environment, so scripts that work in your terminal fail under cron until `PATH` and environment are set explicitly — and silent failures, because cron emails or logs output only if configured, so a failing job can go unnoticed for weeks. The same job started by both cron and anacron (or a timer and a crontab) runs twice; wall-clock scheduling is also naive about daylight saving transitions and machine sleep, which is precisely what `Persistent=true` timers and anacron fix.
- Operational tradeoffs: cron is simple, ubiquitous, and fine for fixed-schedule jobs on always-on servers; systemd timers win on integration (logging, dependencies, failure notifications, catch-up semantics) at the cost of more ceremony; anacron bridges the gap for machines that sleep. The modern rule: use systemd timers for new services and anything needing failure visibility, keep user crontabs for quick personal jobs, and always capture job output (log file or journal) plus an alert on nonzero exit.
- RSIS3/mykb relevance: the wiki's snapshot and graph-rebuild jobs are scheduled tasks; treating them as systemd timers with `Persistent=true`, journal logging, and failure alerts mirrors RSIS3's checkpoint discipline — scheduled work must be observable and recoverable, not fire-and-forget.

## Related
- [[wiki/os-shell/job-control-and-background-tasks|Job Control & Background Tasks]]
- [[wiki/devops-infra/scheduled-jobs|Scheduled Jobs]]
- [[wiki/os-shell/cron-and-schedulers|Cron & Scheduling]]
- [[wiki/os-shell/kernel-architecture|Kernel Architecture]]
