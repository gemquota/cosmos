---
type: "concept"
title: "Zsh Configuration"
description: "Customizing the Z shell: rc files, prompts, completions, and plugins"
tags: ["zsh", "shell", "config", "oh-my-zsh"]
timestamp: "2026-08-01T00:00:00Z"
status: "stub"
---

# Zsh Configuration

## Summary
zsh is a modern interactive shell with powerful completion, globbing, and theming. Configuration lives in `.zshrc` (interactive) and `.zprofile`/`.zshenv` (login/environment), often managed with frameworks like oh-my-zsh.

## Details
- Completion system: contextual tab completion with `compinit`; menu selection and case-insensitivity are config toggles.
- Prompt themes (starship, powerlevel10k) make the shell scannable.
- RSIS3 relevance: agent shell sessions on this device run zsh; rc health affects every command.

## Related
- [[wiki/os-shell/dotfiles|Dotfiles]] — zsh config is the flagship dotfile
- [[wiki/os-shell/shell-aliases|Shell Aliases]] — zsh extends aliases with global and suffix forms
- [[wiki/os-shell/command-line-interfaces|Command-Line Interfaces]] — zsh is a CLI itself
- [[wiki/software-engineering/developer-experience|Developer Experience]] — shell config shapes daily DX
- [[wiki/os-shell/entities/bash-patterns|Bash Scripting Patterns]] — shell idioms carry across zsh
