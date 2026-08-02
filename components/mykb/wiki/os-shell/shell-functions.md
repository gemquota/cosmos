---
type: "concept"
title: "Shell Functions"
description: "Defining, scoping, return values, and exported functions"
tags: ["shell-functions", "bash", "zsh", "scripting"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://www.gnu.org/software/bash/manual/html_node/Shell-Functions.html"]
---

# Shell Functions

## Summary
Shell functions bundle commands under a name for reuse in interactive sessions and scripts. They behave like commands — positional parameters, redirection, and pipelines apply — but run in the current shell, so they can modify variables and change directories.

## Details
- Define with name() { ...; } or function name { ...; }; the body's $1..$9 and $@ are the caller's arguments, distinct from the script's.
- Return values are exit statuses (0-255), set with return N; capture output with "$(func)" and status with func || handle.
- Variables are global by default; local var scopes them to the function and its callees, which is essential for recursion and reuse.
- Functions can be exported to child shells via export -f (stored in BASH_FUNC_name%% env vars), letting subshells inherit them.
- Recursion works like any command; zsh supports autoloaded functions stored in files (fpath/autoload) for lazy loading.
- Redirection, pipelines, and job control apply: func | grep x runs func in a subshell context, so its local changes are lost.
- Use functions for prompt logic, wrappers around commands, and script decomposition; bash's local -r and zsh's typeset add discipline.

## Related
- [[wiki/os-shell/shell-scripting|Shell Scripting]] — functions are the composition unit
- [[wiki/os-shell/environment-variables|Environment Variables]] — how exported functions travel
- [[wiki/os-shell/errexit-and-shell-options|Errexit & Shell Options]] — return-status discipline
- [[wiki/os-shell/exit-codes|Exit Codes]] — the status channel functions return
- [[wiki/os-shell/zsh-configuration|Zsh Configuration]] — autoloadable function libraries
