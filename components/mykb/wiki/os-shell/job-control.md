---
type: "concept"
title: "Job Control"
description: "The shell's ability to run, suspend, resume, and background processes"
tags: ["jobs", "shell", "background", "processes"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
---

# Job Control

## Summary
Job control is the shell's user-facing management of running processes: `cmd &` starts a job in the background, Ctrl-Z suspends the foreground job, `jobs` lists the shell's jobs, and `fg`/`bg` move a job to the foreground or background. Behind these keystrokes is a kernel mechanism — process groups and terminal job control — that lets the shell signal an entire pipeline as one unit.

## Details
- Mechanism: when the shell runs a pipeline, it puts every process into one process group whose ID equals the leader's PID, and the terminal's foreground process group is the one allowed to read input and receive terminal-generated signals. Ctrl-Z sends SIGTSTP to the whole foreground group (suspending it), Ctrl-C sends SIGINT, and Ctrl-\ sends SIGQUIT; the shell's `wait` and `WUNTRACED`-style monitoring detect the stop and print `[1]+ Stopped`. `fg` resumes a job by sending SIGCONT and making it the foreground group; `bg` resumes it with SIGCONT but leaves it in the background. `jobs` shows state (Running, Stopped) and job numbers, `kill %1` signals a job by number, and `disown` removes a job from the shell's table so it survives shell exit.
- Concrete examples: `sleep 100 &` then `jobs` shows `[1]+ Running`; Ctrl-Z on a long `find` stops it and prints the job number; `bg %1` lets it keep running while you type; `rsync ... &` followed by `disown` keeps the transfer alive after logout; `trap 'kill %1' EXIT` cleans up background jobs when the script ends; a parallel build script starts several `make` jobs and `wait`s on them, checking their exit statuses.
- Failure modes: the classic failures are background jobs writing to the terminal (their output interleaves with your prompt, or they hang on terminal reads — redirect stdin/out/err with `</dev/null >log 2>&1`), jobs dying on shell exit because they were not disowned or run under `nohup`, and zombie/stopped jobs accumulating unnoticed. Process-group confusion bites in scripts: `kill $!` kills only the last background PID, not the group, so the rest of a pipeline keeps running; and signals sent to a job by number can target the wrong job after renumbering.
- Operational tradeoffs: job control is the shell's lightweight alternative to tmux and systemd for supervising parallel work — zero dependencies, works everywhere — at the cost of being terminal-bound and losing jobs when the shell exits unless disowned. For long-running or resumable work, tmux sessions or a process supervisor give persistence; for ad hoc parallel tasks, `&` plus `wait` is the pragmatic idiom. RSIS3 relevance: parallel agent subtasks run as shell jobs under supervision; the discipline of redirecting output, disowning long tasks, and checking each job's exit status is exactly the harness's contract with tool processes.

## Related
- [[wiki/os-shell/process-management|Process Management]] — job control is a user-level view of processes
- [[wiki/os-shell/process-signals|Process Signals]] — SIGTSTP, SIGCONT drive suspend and resume
- [[wiki/os-shell/tmux-sessions|Tmux Sessions]] — tmux extends job control to sessions
- [[wiki/os-shell/exit-codes|Exit Codes]] — jobs report status when they finish
- [[wiki/agent-systems/multi-agent-orchestration|Multi-Agent Orchestration]] — parallel agent jobs echo job control
