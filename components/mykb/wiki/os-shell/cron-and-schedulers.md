---
type: "concept"
title: "Cron & Scheduling"
description: "crontab syntax, at, and scheduler comparisons"
tags: ["cron", "scheduling", "automation", "at", "timers"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://man7.org/linux/man-pages/man5/crontab.5.html", "https://man7.org/linux/man-pages/man8/cron.8.html"]
---

# Cron & Scheduling

## Summary
cron runs commands on a schedule defined by five time fields: minute, hour, day of month, month, and weekday. The at command schedules one-shot jobs, and systemd timers are the modern alternative with dependency and calendar syntax.

## Details
- crontab -e edits the user's table; fields are space-separated with ranges (1-5), lists (1,3), steps (*/15), and names (mon, jan).
- Special strings: @reboot, @daily, @weekly, @hourly, @yearly replace the five fields.
- Environment inside crontab: a minimal PATH by default — set PATH=... and MAILTO= to control delivery of output.
- System cron reads /etc/crontab, /etc/cron.d/, and /etc/cron.hourly|daily|weekly|monthly scripts; user crontabs live in /var/spool/cron/.
- cron does not catch up missed runs; anacron does, for machines off at schedule time.
- at 16:00 and batch queue one-shot commands; atq/atrm manage the queue.
- systemd timers add calendar expressions, persistent=true (catch-up), randomized delays, and run through the same unit system as services.

## Related
- [[wiki/os-shell/interactive-vs-noninteractive-shells|Interactive vs Non-Interactive Shells]] — cron's minimal environment
- [[wiki/os-shell/process-supervision|Process Supervision]] — long-running versus scheduled work
- [[wiki/os-shell/systemd-units|Systemd Units]] — timer units as the replacement
- [[wiki/devops-infra/scheduled-jobs|Scheduled Jobs]] — scheduler management at platform scale
- [[wiki/os-shell/shell-scripting|Shell Scripting]] — what cron jobs are usually written in
