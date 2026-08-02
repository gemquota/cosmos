---
type: "concept"
title: "Process Groups & Sessions"
description: "Controlling terminals, process-group IDs, and how shells organize foreground/background jobs"
tags: ["process-groups", "sessions", "job-control", "terminal", "signals"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://man7.org/linux/man-pages/man7/credentials.7.html", "https://pubs.opengroup.org/onlinepubs/9699919799/basedefs/V1_chap11.html"]
---

# Process Groups & Sessions

## Summary
Every process belongs to a process group, and every process group belongs to a session. This hierarchy, together with the controlling terminal, is what lets shells run foreground and background jobs and deliver signals to the right set of processes.

## Details
- A process group is identified by a PGID, normally the PID of its leader; each member shares the group ID.
- A session is created by setsid(2): the calling process becomes session leader with no controlling terminal, and its process group becomes the session's only group.
- Only one process group at a time is the foreground group of the controlling terminal; the rest are background groups.
- Terminal-generated signals (SIGINT from Ctrl-C, SIGQUIT, SIGTSTP) are sent to every process in the foreground group.
- Background jobs that try to read from the terminal receive SIGTTIN and stop; writing may produce SIGTTOU unless tostop is off.
- When the session leader (usually the shell) exits, SIGHUP is sent to the foreground group, which is why background daemons detach with setsid.
- A process group whose parent is in a different session and has no session member is orphaned, and members are sent SIGHUP then SIGCONT.

## Related
- [[wiki/os-shell/job-control|Job Control]] — the shell feature built on process groups and sessions
- [[wiki/os-shell/process-signals|Process Signals]] — how signals target whole groups via kill(-pgid)
- [[wiki/os-shell/daemon-processes|Daemon Processes]] — setsid is the core of terminal detachment
- [[wiki/os-shell/pty-and-pseudo-terminals|PTYs & Pseudo-Terminals]] — the controlling terminal device
- [[wiki/os-shell/process-management|Process Management]] — the broader lifecycle this hierarchy organizes
