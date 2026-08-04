---
type: "entity"
title: "Tmux Sessions"
description: "Terminal multiplexing: persistent, detachable terminal sessions with panes and windows"
tags: ["tmux", "terminal", "sessions", "multiplexer"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
---

# Tmux Sessions

## Summary
tmux runs a server process that owns terminal sessions: you create windows and panes, detach (`prefix` + `d`), and reattach later (`tmux attach`) — the session and its processes survive SSH drops, reboots of your local machine, and even closing the terminal entirely. Named sessions, windows, and panes turn one terminal into a persistent, resumable workspace.

## Details
- Mechanism: a tmux server daemon runs in the background and owns every session; each session has windows (tab-like), each window can be split into panes (tiled terminals), and each pane runs a real shell/process whose stdio is connected to tmux's pseudo-terminals. Detaching disconnects the client but leaves the server and processes running; reattaching restores the layout exactly. Keybindings use a prefix (default Ctrl-b): `%` splits vertically, `"` horizontally, `c` creates a window, `,` renames it, `d` detaches, `[` enters copy mode (scrollback). Config lives in `~/.tmux.conf`, and `tmux new -s name`, `tmux ls`, `tmux attach -t name`, and `tmux kill-session -t name` are the session-level commands.
- Concrete examples: an SSH session running a long build — detach, reconnect from anywhere, reattach and watch it finish; a development workspace with `code` in one window and a dev server in another, plus a vertical split for logs; `tmux new -s deploy` for a deploy run you can monitor without keeping a terminal open; resurrect/continuum plugins that restore sessions after a reboot; running a remote agent harness inside tmux so a dropped connection never kills the work.
- Failure modes: the classic failures are forgetting tmux exists on the remote host (an SSH drop kills your long job and you lose everything), `tmux attach` failing with "sessions should be nested with care" when attaching from inside a tmux session (fix with `tmux new -A -s name` or detach first), and zombie/accumulated sessions consuming memory (prune with `tmux ls` + `kill-server`). Panes that hold exited processes leave dead shells; scrollback limits can silently drop output; and a broken `~/.tmux.conf` can make every new session misbehave.
- Operational tradeoffs: tmux trades a small learning curve (prefix keybindings, nested-session awareness) for persistence and composability that a plain terminal cannot offer; the alternatives are screen (older, less featureful) and terminal-native tabs (no detach/reattach). The practice rules: always run long or unattended work inside tmux, use named sessions for distinct tasks, keep the config minimal and version-controlled, and treat tmux as the harness's default shell host for anything that must survive a disconnect.
- RSIS3/mykb relevance: long-running agent harnesses run inside tmux to survive session loss — the same durability principle as RSIS3 checkpoints: state must survive the death of its original owner, and tmux is the process-level half while checkpoints are the data-level half.

## Related
- [[wiki/os-shell/process-management|Process Management]] — tmux keeps processes alive without a terminal
- [[wiki/os-shell/job-control|Job Control]] — tmux is job control at session scale
- [[wiki/agent-systems/session-state-machine|Session State Machine]] — agent sessions map onto tmux sessions
- [[wiki/os-shell/zsh-configuration|Zsh Configuration]] — the shell inside tmux windows
- [[wiki/agent-systems/action-observation-loop|Action-Observation Loop]] — tmux keeps long-running loops alive
