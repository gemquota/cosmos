---
type: "concept"
title: "Process Signals"
description: "Asynchronous notifications sent to processes to request actions or report conditions"
tags: ["signals", "processes", "unix", "interrupts"]
timestamp: "2026-08-01T00:00:00Z"
status: "stub"
---

# Process Signals

## Summary
Signals are asynchronous notifications: SIGINT (Ctrl-C), SIGTERM (polite termination), SIGKILL (unconditional), SIGHUP (hangup). Programs handle them to clean up, reload config, or die.

## Details
- Default actions vary — terminate, ignore, stop, core dump; `trap` in shell and handlers in code override defaults.
- SIGTERM is the polite stop; SIGKILL cannot be caught, so graceful systems handle TERM first.
- RSIS3 relevance: agent daemons must trap TERM to persist state before exiting.

## Related
- [[wiki/os-shell/process-management|Process Management]] — signals steer the process lifecycle
- [[wiki/os-shell/job-control|Job Control]] — Ctrl-Z/Ctrl-C are signal deliveries
- [[wiki/api-protocols/graceful-shutdown|Graceful Shutdown]] — service-layer TERM handling
- [[wiki/agent-systems/rollback-and-recovery|Rollback and Recovery]] — recovering state after a signal
