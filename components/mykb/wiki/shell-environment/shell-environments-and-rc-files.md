---
type: "concept"
title: "Shell Environments & RC Files"
description: "Startup files and environment configuration for shells"
tags: ["shell", "environment", "rc-files", "bash"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: [
  "https://www.gnu.org/software/bash/manual/bash.html",
  "https://zsh.sourceforge.io/Doc/Release/",
]
---

# Shell Environments & RC Files

## Summary
Shell environments are built from startup files, variables, and aliases that configure every interactive session. Bash and zsh each source different rc files in a defined order. Environment hygiene prevents confusing behavior in scripts and sessions, and it is the foundation of the shell-environment cluster.

## Details
- Bash sources /etc/profile, ~/.bash_profile, and ~/.bashrc depending on login and interactive mode.
- The GNU Bash manual documents startup file behavior precisely.
- zsh's manual covers its own rc files and option system.
- Environment variables (PATH, HOME, SHELL) shape tool behavior across processes.
- Portable scripts should not depend on interactive rc content.
- In mykb, shell environments connect to tmux, job control, and shell scripting.
- PATH ordering determines which tool version runs when names collide.
- Conditional startup blocks keep rc files fast and portable across machines.
- Shell configuration is personal; the rc-file and tmux articles show how these choices persist across sessions.
- Remote workflows depend on SSH, terminal multiplexers, and job control, all documented in this cluster.

## Related
- [[wiki/shell-environment/shell-scripting-robustness|Shell Scripting Robustness]]
- [[wiki/devops-infra/ephemeral-environments|Ephemeral Environments]]
- [[wiki/infrastructure/data-environments-dev-staging-prod|Data Environments Dev Staging Prod]]
- [[wiki/infrastructure/dbt-environments-and-jobs|Dbt Environments And Jobs]]
