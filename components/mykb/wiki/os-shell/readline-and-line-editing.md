---
type: "concept"
title: "Readline & Line Editing"
description: "Emacs/vi modes, key bindings, and inputrc"
tags: ["readline", "line-editing", "bash", "inputrc", "emacs"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://tiswww.case.edu/php/chet/readline/rluserman.html", "https://www.gnu.org/software/bash/manual/html_node/Command-Line-Editing.html"]
---

# Readline & Line Editing

## Summary
GNU Readline is the line-editing library behind bash's interactive prompt, and zsh implements an equivalent (zle). It provides Emacs-style bindings by default, a vi mode, history navigation, incremental search, and programmable key bindings configured in ~/.inputrc.

## Details
- Emacs mode basics: Ctrl-A/E move to line ends, Ctrl-W kills a word, Ctrl-K kills to end, Ctrl-Y yanks; vi mode (set -o vi) reuses muscle memory from vim.
- History: Up/Down move through history, Ctrl-R starts reverse incremental search, Ctrl-G cancels it; history-search-backward with a prefix is a power binding.
- ~/.inputrc lines like set editing-mode vi or "C-u": "kill-whole-line" customize bindings; bind -P in bash lists active bindings.
- Readline variables control behavior: bell-style, completion-ignore-case, show-mode-in-prompt, and history-size.
- Key sequences support modifiers: "\e[A" is Up, "C-x C-r" rereads inputrc, and macros can chain keystrokes.
- History expansion (!!, !$) is a separate shell feature, often disabled with set +H because it misfires in scripts.
- zsh's zle has vi and emacs modes too, with widgets for history and completion that bash cannot match.

## Related
- [[wiki/os-shell/shell-completion|Shell Completion]] — Readline's completion machinery
- [[wiki/os-shell/interactive-vs-noninteractive-shells|Interactive vs Non-Interactive Shells]] — where editing matters
- [[wiki/os-shell/dotfiles|Dotfiles]] — inputrc and bashrc live there
- [[wiki/os-shell/shell-aliases|Shell Aliases]] — keyboard-level conveniences
- [[wiki/os-shell/zsh-configuration|Zsh Configuration]] — zle as the zsh equivalent
