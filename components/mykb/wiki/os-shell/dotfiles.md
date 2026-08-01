---
type: "concept"
title: "Dotfiles"
description: "The hidden configuration files in a home directory that personalize the shell and tools"
tags: ["dotfiles", "config", "shell", "home"]
timestamp: "2026-08-01T00:00:00Z"
status: "stub"
---

# Dotfiles

## Summary
Dotfiles are the `.name` files (`.bashrc`, `.zshrc`, `.gitconfig`, `.vimrc`) that configure user environments. Versioning them turns a personal setup into a reproducible, portable system.

## Details
- Store them in git, symlink into place, and use dotfile managers (chezmoi, GNU stow) to manage hosts.
- Keep secrets out; keep PATH, aliases, and editor settings in.
- RSIS3 relevance: agent sessions inherit the environment dotfiles define.

## Related
- [[wiki/os-shell/zsh-configuration|Zsh Configuration]] — the shell config most teams customize
- [[wiki/os-shell/shell-aliases|Shell Aliases]] — shortcuts defined in dotfiles
- [[wiki/os-shell/symlinks|Symlinks]] — how dotfiles are usually installed
- [[wiki/software-engineering/developer-experience|Developer Experience]] — dotfiles are personal DX
- [[wiki/memory/provenance|Provenance]] — dotfiles capture environment provenance
