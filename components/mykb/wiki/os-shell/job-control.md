---
type: "concept"
title: "Job Control"
description: "The shell's ability to run, suspend, resume, and background processes"
tags: ["jobs", "shell", "background", "processes"]
timestamp: "2026-08-01T00:00:00Z"
status: "stub"
---

# Job Control

## Summary
Job control lets the shell manage running processes: `&` backgrounds a job, Ctrl-Z suspends it, `jobs` lists them, and `fg`/`bg` resume in the foreground or background.

## Details
- Each job belongs to a process group, letting the shell signal the whole tree at once.
- Background jobs still write to the terminal unless redirected; `nohup` and `disown` detach them further.
- RSIS3 relevance: parallel agent subtasks run as shell jobs under supervision.

## Related
- [[wiki/os-shell/process-management|Process Management]] — job control is a user-level view of processes
- [[wiki/os-shell/process-signals|Process Signals]] — SIGTSTP, SIGCONT drive suspend and resume
- [[wiki/os-shell/tmux-sessions|Tmux Sessions]] — tmux extends job control to sessions
- [[wiki/os-shell/exit-codes|Exit Codes]] — jobs report status when they finish
- [[wiki/agent-systems/multi-agent-orchestration|Multi-Agent Orchestration]] — parallel agent jobs echo job control
