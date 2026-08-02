---
type: "concept"
title: "Syslog & Logging"
description: "Syslog protocol, facilities/severities, and backends"
tags: ["syslog", "logging", "rsyslog", "facilities"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://www.rfc-editor.org/rfc/rfc3164", "https://www.rfc-editor.org/rfc/rfc5424"]
---

# Syslog & Logging

## Summary
Syslog is the classic Unix logging framework: applications emit timestamped messages tagged with a facility and severity, and a daemon (rsyslog, syslog-ng) routes them to files, terminals, or remote collectors. RFC 5424 modernized the format; RFC 3164 defines the traditional one.

## Details
- Facilities classify the source (kern, user, mail, daemon, auth, cron, local0-7); severities rank from emerg (0) to debug (7).
- Applications call syslog(3) or write to /dev/log; journald also listens there and forwards to syslog if configured.
- rsyslog config routes by facility/severity selectors: *.info;mail.none -/var/log/messages, with -, meaning no sync per line.
- Remote logging ships over UDP 514 (traditional) or TLS/TCP 6514 (RELP or syslog-tls), centralizing fleet logs.
- logrotate compresses and rotates files by size or time, keeping disk bounded; configs live in /etc/logrotate.d/.
- Modern systems often use systemd-journal for structured local logs and forward selected streams to a syslog or cloud collector.
- Grep-ability is the contract: every daemon logs to a known file with timestamps and hostnames for correlation.

## Related
- [[wiki/os-shell/systemd-journal|systemd-journal]] — the structured local alternative
- [[wiki/devops-infra/log-aggregation|Log Aggregation]] — collecting syslog at scale
- [[wiki/os-shell/process-supervision|Process Supervision]] — logging from supervised daemons
- [[wiki/security-auth/audit-logging|Audit Logging]] — the security side of syslog
- [[wiki/devops-infra/observability|Observability]] — logs as one of three pillars
