---
type: "concept"
title: "PTYs & Pseudo-Terminals"
description: "How terminals multiplex I/O via /dev/pts"
tags: ["pty", "terminal", "tty", "io", "kernel"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://man7.org/linux/man-pages/man4/ptmx.4.html", "https://man7.org/linux/man-pages/man7/pty.7.html"]
---

# PTYs & Pseudo-Terminals

## Summary
A pseudo-terminal (pty) is a kernel pair of devices that emulates a hardware terminal: the master side is used by programs like ssh and tmux, the slave side (a /dev/pts/N node) is attached to a shell or process. Everything typed and printed flows through this pair.

## Details
- Opening /dev/ptmx allocates a new pair; the slave appears as /dev/pts/N and behaves like a real tty to applications.
- The line discipline in the middle provides canonical input processing: line buffering, echo, erase keys, and signal generation (Ctrl-C -> SIGINT).
- Modes: raw mode (no echo, no buffering) is used by editors, pagers, and ssh; canonical mode suits interactive shells.
- Terminal size travels via TIOCGWINSZ ioctls and SIGWINCH, keeping full-screen apps correct when the window resizes.
- sshd, tmux, screen, and terminal emulators all allocate ptys; the master can even pass input while the slave thinks it has a real keyboard.
- /dev/pts files are visible in ps TTY columns and lsof; each pty has a name and usually a permissions check on the slave.
- Security: pty access controls (ptmx) and TIOCSTI restrictions prevent untrusted programs from injecting keystrokes.

## Related
- [[wiki/os-shell/terminal-emulators|Terminal Emulators]] — the master-side consumer
- [[wiki/os-shell/process-groups-and-sessions|Process Groups & Sessions]] — controlling terminals come from ptys
- [[wiki/os-shell/ssh-and-remote-access|SSH & Remote Access]] — sshd allocates a pty per session
- [[wiki/os-shell/ansi-escape-sequences|ANSI Escape Sequences]] — what flows through the pty
- [[wiki/os-shell/job-control|Job Control]] — stop signals from the line discipline
