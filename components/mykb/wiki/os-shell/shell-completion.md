---
type: "concept"
title: "Shell Completion"
description: "Tab completion, programmable completion, and compgen"
tags: ["completion", "bash", "zsh", "compgen", "tab"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://www.gnu.org/software/bash/manual/html_node/Programmable-Completion.html"]
---

# Shell Completion

## Summary
Tab completion lets shells finish commands, filenames, variables, and options without typing them. Bash's programmable completion system routes completion to per-command functions; zsh's compinit/compdef system is even more powerful.

## Details
- Basic completion covers filenames, commands on PATH, variables ($ + Tab), and user names (~ + Tab); double-Tab shows all matches.
- Programmable completion: complete -F _func cmd registers a function, and the bash-completion project ships thousands of them (git, systemctl, ssh).
- compgen -c, -f, -v, -A produce candidate lists for scripts; complete -W "a b c" gives a fixed word list for a command.
- Completion respects context: bash-completion completes host names after ssh, package names for apt, and options for docker.
- Case-insensitive matching and menu completion (set show-all-if-ambiguous, completion-ignore-case) speed up daily use.
- zsh uses compinit + compdef, offers menu selection with arrow keys, and completes inside words; Zsh's completion is context-rich and scriptable.
- Completion runs in the current shell, so functions must not print stray output; they write candidates to COMPREPLY instead.

## Related
- [[wiki/os-shell/readline-and-line-editing|Readline & Line Editing]] — the key layer under completion
- [[wiki/os-shell/interactive-vs-noninteractive-shells|Interactive vs Non-Interactive Shells]] — completion is interactive-only
- [[wiki/os-shell/zsh-configuration|Zsh Configuration]] — compinit setup lives here
- [[wiki/os-shell/command-line-interfaces|Command-Line Interfaces]] — what completion makes usable
- [[wiki/os-shell/dotfiles|Dotfiles]] — where completion scripts are installed
