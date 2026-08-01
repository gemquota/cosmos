---
type: "concept"
title: "Tmux Sessions"
description: "Terminal multiplexing: persistent, detachable terminal sessions with panes and windows"
tags: ["tmux", "terminal", "sessions", "multiplexer"]
timestamp: "2026-08-01T00:00:00Z"
status: "stub"
---

# Tmux Sessions

## Summary
tmux runs a server holding terminal sessions you can detach and reattach, surviving disconnects. Windows, panes, and named sessions turn one terminal into a persistent workspace.

## Details
- Detach with prefix-b, reattach with `tmux attach`; sessions survive SSH drops and reboots.
- Paned layouts and session names support multiple parallel workflows.
- RSIS3 relevance: long-running agent harnesses run inside tmux to survive session loss.

## Related
- [[wiki/os-shell/process-management|Process Management]] — tmux keeps processes alive without a terminal
- [[wiki/os-shell/job-control|Job Control]] — tmux is job control at session scale
- [[wiki/agent-systems/session-state-machine|Session State Machine]] — agent sessions map onto tmux sessions
- [[wiki/os-shell/zsh-configuration|Zsh Configuration]] — the shell inside tmux windows
- [[wiki/agent-systems/action-observation-loop|Action-Observation Loop]] — tmux keeps long-running loops alive
