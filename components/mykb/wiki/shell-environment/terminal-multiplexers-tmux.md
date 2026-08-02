---
type: "concept"
title: "Terminal Multiplexers: tmux"
description: "Sessions, windows, and panes for persistent terminals"
tags: ["tmux", "terminal", "multiplexer", "shell"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: [
  "https://github.com/tmux/tmux/wiki",
  "https://man7.org/linux/man-pages/man1/tmux.1.html",
]
---

# Terminal Multiplexers: tmux

## Summary
tmux multiplexes a terminal into persistent sessions with windows and panes, surviving disconnects. It is the standard tool for long-running work on remote servers. Sessions detach and reattach, making SSH-based workflows resilient to network drops.

## Details
- Sessions persist after disconnection; reattach with tmux attach.
- Config files, key-binding tweaks, and plugins make tmux behavior consistent across machines.
- The tmux project wiki documents commands and configuration.
- Sockets and attach-session commands let multiple users share a session for pair debugging.
- tmux pairs with SSH to keep deploys and tail sessions alive across network drops.
- In mykb, tmux connects to shell environments, SSH, and remote development.
- Copy mode and search make tmux usable for reviewing long output without a mouse.
- Config files and plugins make tmux behavior consistent across machines.
- Shell configuration is personal; the rc-file and tmux articles show how these choices persist across sessions.
- Remote workflows depend on SSH, terminal multiplexers, and job control, all documented in this cluster.

## Related
- [[wiki/shell-environment/unix-text-processing-tools|Unix Text Processing Tools]]
- [[wiki/shell-environment/shell-scripting-robustness|Shell Scripting Robustness]]
- [[wiki/os-shell/terminal-emulators|Terminal Emulators]]
- [[wiki/os-shell/tmux-sessions|Tmux Sessions]]
