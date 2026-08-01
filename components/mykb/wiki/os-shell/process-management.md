---
type: "concept"
title: "Process Management"
description: "The lifecycle of operating-system processes: creation, scheduling, signalling, and termination"
tags: ["processes", "os", "lifecycle", "signals"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://www.gnu.org/software/libc/manual/html_node/Processes.html"]
---

# Process Management

## Summary
Process management covers how operating systems create, schedule, and terminate processes. The GNU C Library manual documents the primitives — fork, exec, exit, and the signals that coordinate them — which every shell and daemon builds upon.

## Details
- Creation: fork() clones the current process; exec() replaces its image with a new program; the two-step gives the parent control over the child's setup.
- Lifecycle: running, sleeping, stopped, zombie (exited but unreaped); a parent must wait() to reap children or zombies accumulate.
- Signals are asynchronous notifications: SIGTERM requests shutdown, SIGKILL forces it, SIGINT interrupts, SIGHUP notifies terminal hangup.
- Process groups and sessions (from setsid) organize terminal job control; foreground and background jobs live in these groups.
- Daemons detach from the terminal, redirect stdio, and run under init/systemd supervision.
- RSIS3 relevance: the mykb daemon and agent subprocesses are managed processes — signals, exit codes, and reaping matter for reliability.
- Worked example: a shell runs `sleep 100 &`, then `kill %1` delivers SIGTERM to the job's process group.

## Related
- [[wiki/os-shell/process-signals|Process Signals]] — the async control channel between processes
- [[wiki/os-shell/job-control|Job Control]] — shell management of foreground and background jobs
- [[wiki/os-shell/exit-codes|Exit Codes]] — the status channel processes return on exit
- [[wiki/os-shell/systemd-units|Systemd Units]] — supervision of long-lived services
- [[wiki/api-protocols/graceful-shutdown|Graceful Shutdown]] — clean SIGTERM handling at the service layer
- [[wiki/concepts/deadband-control|Deadband Control]] — avoiding thrash in process restarts
- [[wiki/agent-systems/session-state-machine|Session State Machine]] — agent sessions mirror process lifecycles
