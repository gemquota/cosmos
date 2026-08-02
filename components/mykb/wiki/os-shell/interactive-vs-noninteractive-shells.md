---
type: "concept"
title: "Interactive vs Non-Interactive Shells"
description: "Startup files, prompts, and behavioral differences"
tags: ["shell", "interactive", "login", "startup-files"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://www.gnu.org/software/bash/manual/html_node/Bash-Startup-Files.html"]
---

# Interactive vs Non-Interactive Shells

## Summary
Shells change their behavior — which startup files they read, whether they show a prompt, and whether job control works — depending on whether they are interactive and whether they are login shells. Scripts and cron jobs get a very different environment than a terminal session.

## Details
- A login shell reads ~/.bash_profile (or ~/.profile); interactive non-login shells read ~/.bashrc; scripts read neither unless BASH_ENV points at a file.
- Interactive shells enable the prompt (PS1), history, job control, aliases, and completion; non-interactive shells skip all of that for speed and determinism.
- Non-interactive shells read commands from a file, -c string, or stdin and are used by scripts, cron, and ssh commands.
- Environment leakage is the classic trap: cron scripts fail because PATH lacks user additions — export what you need explicitly.
- sh vs bash: many systems link sh to a POSIX mode; shebang #!/bin/bash forces bash features while #!/bin/sh stays portable.
- Detecting mode: $- contains i for interactive, and [[ $- == *i* ]] gates interactive-only setup in a shared rc file.
- Login vs non-login matters for how ssh sessions and terminal emulators initialize: ssh gives a login shell, a new terminal tab often does not.

## Related
- [[wiki/os-shell/environment-variables|Environment Variables]] — what differs between modes
- [[wiki/os-shell/dotfiles|Dotfiles]] — the rc files each mode reads
- [[wiki/os-shell/shell-scripting|Shell Scripting]] — non-interactive behavior
- [[wiki/os-shell/readline-and-line-editing|Readline & Line Editing]] — interactive-only editing
- [[wiki/os-shell/cron-and-schedulers|Cron & Scheduling]] — the canonical non-interactive context
