---
type: "entity"
title: "PID"
description: "Process ID: the operating system identifier for a running process"
tags: ["entity", "acronym", "process", "os", "pid"]
timestamp: "2026-07-19T22:41:39Z"
resource: ""
---

# PID

## Summary

PID stands for process ID, the operating system's numeric identifier for a running process. PIDs matter because they are the handle for almost every process operation — signaling, waiting, tracing, and resource queries. They are also recycled, which is the classic source of bugs where a stale PID refers to an unrelated new process.

## Details

- **Definition** — Each process receives a unique identifier at creation; the kernel reuses numbers once the old process is fully reaped.
- **Uses** — Signals, /proc queries, job control, and monitoring all address processes by PID.
- **Lifecycle** — A PID becomes invalid at exit; waitpid reaps the zombie and frees the number for reuse, so checking liveness by PID alone is unsafe.
- **Worked example** — A script finds a server's PID, sends SIGTERM, waits for the port to close, then verifies the process is gone before restarting.
- **Common failure modes** — PID reuse killing the wrong process, pidfiles going stale after crashes, and races between lookup and signal delivery.
- **Practical relevance** — Supervisors and container runtimes manage this lifecycle so applications rarely touch raw PIDs, but scripts still do.
- **Variants** — Thread IDs, process group IDs, and session IDs extend the same namespace for coordinated control.
- **Telemetry note** — Recorded from session 019f2765 among shell and backend tags, matching process-management work.
- **pidfiles** — Writing the current PID to a file lets supervisors find the process, but stale pidfiles require validation — the file may outlive its process.
- **Namespaces** — Containers present PID namespaces, so a PID inside a container differs from the host's view; tooling must account for the mapping.
- **Worked example** — A deploy script reads a pidfile, checks /proc for the process, sends a graceful signal, and waits for exit before starting the replacement.
- **Instrumentation** — Monitoring tools report PIDs for process-level metrics; correlating a PID with a request requires thread and task identifiers at finer granularity.

## Related

- [[wiki/os-shell/fork-exec-and-process-creation|Fork Exec and Process Creation]] — where PIDs come from
- [[wiki/os-shell/process-groups-and-sessions|Process Groups and Sessions]] — PID namespaces above
- [[wiki/os-shell/daemon-processes|Daemon Processes]] — long-lived PID holders
- [[wiki/shell-environment/exit-codes-and-error-handling|Exit Codes and Error Handling]] — process outcomes
- [[wiki/api-services/categories/api-rest/subcategories/rest-http/calledprocesserror-2|CalledProcessError]] — child process failures
- [[wiki/os-shell/cgroups-and-namespaces|Cgroups and Namespaces]] — container process isolation
