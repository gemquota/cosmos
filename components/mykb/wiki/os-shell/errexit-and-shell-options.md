---
type: "concept"
title: "Errexit & Shell Options"
description: "set -e/-u/-o pipefail and strict-mode tradeoffs"
tags: ["errexit", "shell-options", "bash", "strict-mode", "pipefail"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://www.gnu.org/software/bash/manual/html_node/The-Set-Builtin.html"]
---

# Errexit & Shell Options

## Summary
Shell "strict mode" combines set -e (exit on error), set -u (error on unset variables), and set -o pipefail (propagate failures through pipelines). Each flag fixes a silent-failure mode, and each has sharp edges that change how scripts must be written.

## Details
- set -e exits the shell when a simple command fails, but not in condition contexts: if, while, until, !, &&, ||, or a command whose status is tested.
- Commands in a pipeline are exempt unless pipefail is on; functions called from conditional contexts inherit the exemption.
- set -u turns unset-variable references into errors — great for typos, painful for ${1:-} idioms that intentionally probe optional args.
- set -o pipefail makes a pipeline's status the last non-zero command, so grep | head no longer hides grep failures.
- set -x traces commands as executed, the debugging companion; set -C (noclobber) protects files from accidental redirection overwrites.
- Strict mode is a contract, not magic: signal handlers, command substitution, and stray ! usage still surprise newcomers.
- zsh has analogous options (ERR_EXIT, NO_UNSET, PIPE_FAIL) with slightly different semantics.

## Related
- [[wiki/os-shell/exit-codes|Exit Codes]] — the statuses set -e reacts to
- [[wiki/os-shell/shell-functions|Shell Functions]] — how functions interact with errexit
- [[wiki/os-shell/command-substitution|Command Substitution]] — status propagation into expansions
- [[wiki/os-shell/shell-trap-handlers|Trap Handlers]] — ERR traps pair with errexit
- [[wiki/os-shell/shell-scripting|Shell Scripting]] — where strict mode is adopted
