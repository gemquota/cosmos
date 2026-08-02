---
type: "concept"
title: "systemd-journal"
description: "journald, journalctl, and structured logs"
tags: ["systemd", "journald", "journalctl", "logs"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://www.freedesktop.org/software/systemd/man/latest/systemd-journald.service.html", "https://www.freedesktop.org/software/systemd/man/latest/journalctl.html"]
---

# systemd-journal

## Summary
systemd-journald collects structured logs from services, the kernel, and syslog, storing them in a binary journal that journalctl queries. Instead of parsing text, you filter on fields like _PID, _COMM, and priority with native operators.

## Details
- Journald receives stdout/stderr of services, kernel messages, and /dev/log; it adds metadata: pid, uid, unit, boot id, and timestamps.
- Storage: volatile under /run/log/journal or persistent under /var/log/journal (Storage=persistent); size caps via SystemMaxUse.
- journalctl -u service shows a unit's logs; -b filters the current boot, -f follows, -p err sets a priority floor.
- Time filtering: journalctl --since "1 hour ago" --until today; -k shows kernel messages only.
- Field queries: journalctl _PID=123, _COMM=sshd, or _SYSTEMD_UNIT=nginx.service; -o json-pretty exports structured records.
- Journald can forward to syslog (ForwardToSyslog), and journald Remote enables central log collection over TLS.
- Rotation is automatic; the journal survives crashes because records are appended with checksums (verify with journalctl --verify).

## Related
- [[wiki/os-shell/syslog-and-logging|Syslog & Logging]] — the classic protocol journald feeds
- [[wiki/os-shell/systemd-units|Systemd Units]] — services whose output lands in the journal
- [[wiki/os-shell/process-supervision|Process Supervision]] — log-based lifecycle visibility
- [[wiki/os-shell/head-tail-and-less|head, tail & less]] — journalctl -f replaces tail -f
- [[wiki/devops-infra/log-aggregation|Log Aggregation]] — shipping journal data to a collector
