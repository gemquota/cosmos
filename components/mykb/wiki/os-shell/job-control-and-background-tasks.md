---
type: "concept"
title: "Job Control & Background Tasks"
description: "Foreground/background switching and job management in shells"
tags: ["job-control", "background", "shell", "process"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: [
  "https://www.gnu.org/software/bash/manual/html_node/Job-Control.html",
  "https://en.wikipedia.org/wiki/Job_control_(Unix)",
]
---

# Job Control & Background Tasks

## Summary
Job control lets interactive shells run processes in the background and switch between them. It is built on process groups and terminal signals. Understanding it prevents orphaned processes, lost output, and surprise shutdowns of long-running work.

## Details
- Foreground jobs own the terminal; background jobs run without it and can be recalled with jobs.
- Ctrl-Z suspends a job; fg and bg resume it in foreground or background.
- The Bash manual's job-control section defines the semantics precisely.
- Disown and nohup detach jobs from the session so they survive logout.
- Process groups tie related jobs together for terminal signal delivery.
- In mykb, job control connects to process lifecycle, tmux, and SSH sessions.
- Process group IDs tie a pipeline together for signal delivery.
- nohup, disown, and setsid each change how background work survives logout.
- Kernel and userspace behavior meet here; the related process, memory, and filesystem articles provide the implementation detail.
- Tuning this behavior in production relies on the system monitoring and resource utilization articles of this cluster.

## Related
- [[wiki/os-shell/cron-and-scheduled-tasks|Cron & Scheduled Tasks]]
- [[wiki/cloud-infra/congestion-control-algorithms|Congestion Control Algorithms]]
- [[wiki/os-shell/job-control|Job Control]]
- [[wiki/os-shell/access-control-lists|Access Control Lists]]
