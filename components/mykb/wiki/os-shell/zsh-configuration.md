---
type: "concept"
title: "Zsh Configuration"
description: "Customizing the Z shell: rc files, prompts, completions, and plugins"
tags: ["zsh", "shell", "config", "oh-my-zsh"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
---

# Zsh Configuration

## Summary
zsh is a modern interactive shell with powerful completion, globbing, history, and theming, and its behavior is defined by a set of configuration files: `.zshenv` (environment for every instance), `.zprofile` (login shell), `.zshrc` (interactive), and `.zlogout`. Most users' zsh configuration is really `.zshrc` plus a framework (oh-my-zsh or zinit) and a completion setup.

## Details
- Mechanism: zsh reads files in a strict order: `.zshenv` for all shells (put `PATH`/env here), `.zprofile` at login, then `.zshrc` for interactive shells, and `.zlogout` at exit. Options are set with `setopt` (e.g., `setopt autocd` to cd by typing a directory, `setopt extendedglob` for advanced globbing, `setopt histignorespace`), and the completion system is initialized with `autoload -Uz compinit && compinit`, which enables contextual tab completion with menus, descriptions, and configurable behavior (case-insensitive matching via `zstyle ':completion:*' matcher-list 'm:{a-z}={A-Z}'`). Prompt themes (powerlevel10k, starship) and plugins are layered on top; oh-my-zsh bundles thousands of plugins and themes but adds startup time unless lazy-loaded.
- Concrete examples: a `.zshrc` that sets `HISTSIZE=10000` and `setopt share_history` so history is shared across sessions; `zstyle` rules that make `git checkout <tab>` complete branch names and `cd <tab>` complete only directories; a `zle` widget that binds `Ctrl-r` to fuzzy history search; a `precmd` hook that runs `ls` or updates a title after every prompt; `PROMPT='%F{cyan}%n@%m%f %~ %# '` for a colored prompt; `alias -s md='nvim'` so typing `notes.md` opens it in nvim.
- Failure modes: the classic failures are startup-time bloat from eager framework loading (a 2-second prompt on every shell — fix by lazy-loading plugins or switching to a lean config), `export` statements in `.zshrc` leaking into scripts (environment belongs in `.zshenv`/`.zprofile`), and syntax incompatibility: a `.bashrc` snippet sourced into zsh breaks on bash-only syntax (``` ]]` works, `shopt` does not), which is why dotfiles need separate bash/zsh branches. Plugin updates that change keybindings and options silently, and a broken `.zshrc` that makes every interactive shell fail (fix with `zsh -f` to skip rc files) round out the footguns.
- Operational tradeoffs: a curated zsh config buys a dramatically better interactive experience — completion, history, and prompt — at the cost of maintenance and startup time; frameworks accelerate setup but add layers that obscure what your config actually does. The practice rules: keep `.zshenv` for environment and `.zshrc` for interactivity, initialize compinit once, measure startup (`zsh -i -c 'time (exit)'`), version-control the dotfiles, and prefer lazy-loaded plugins over eager frameworks.
- RSIS3/mykb relevance: agent shell sessions on this device run zsh; rc health affects every command — a broken or slow `.zshrc` degrades the harness's whole tool loop, which is why the agent environment pins a minimal, deterministic shell config rather than inheriting an unknown interactive state.

## Related
- [[wiki/os-shell/dotfiles|Dotfiles]] — zsh config is the flagship dotfile
- [[wiki/os-shell/shell-aliases|Shell Aliases]] — zsh extends aliases with global and suffix forms
- [[wiki/os-shell/command-line-interfaces|Command-Line Interfaces]] — zsh is a CLI itself
- [[wiki/software-engineering/developer-experience|Developer Experience]] — shell config shapes daily DX
- [[wiki/os-shell/entities/bash-patterns|Bash Scripting Patterns]] — shell idioms carry across zsh
