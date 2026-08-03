---
type: "concept"
title: "Shell Scripting Robustness"
description: "Writing scripts that survive quoting, globbing, unset variables, and failure"
tags: ["shell", "scripting", "bash", "robustness"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# Shell Scripting Robustness

## Summary
Writing scripts that survive quoting, globbing, unset variables, and failure. Robust scripts assume the worst about their inputs and environment, and they fail loudly and early instead of corrupting data silently.

## Details
- **Quote everything** — unquoted variables undergo word splitting and glob expansion, so `rm $files` with a filename containing a space deletes two files, and `cp $src $dst` with a `*` in a name expands to every matching file; the rule is to double-quote every expansion (`"$var"`, `"$@"`) and reserve quotes with intent: single quotes for literal strings, double quotes for strings that must expand variables, and no quotes only when splitting is deliberately wanted.
- **set -u for unset variables** — `set -u` (nounset) makes references to unset variables a fatal error instead of silently expanding to empty; empty expansion is one of the most common sources of destructive commands (`rm -rf "$prefix/"` with `prefix` unset becomes `rm -rf /`); use `${var:-default}` for optional values and `${var:?message}` to fail with a clear error when a required variable is missing.
- **Glob safety** — globs that match nothing stay literal by default (`echo *.md` prints `*.md` when no markdown exists), and a glob can match an unexpected file; `nullglob` makes non-matching globs expand to nothing, and `failglob` turns them into errors; when passing glob results as arguments, arrays (`files=(*.md)`) preserve each match as one word even with spaces in filenames.
- **set -e and traps** — `set -e` stops the script on the first failing command, but it has exceptions (conditions, `&&`/`||` lists, pipelines); `set -o pipefail` extends failure to the whole pipeline; `trap ... EXIT` and `trap ... ERR` guarantee cleanup (removing temp files, killing children) and logging even when the script dies, which is how scripts avoid leaving half-finished state.
- **Failure modes** — the classic killers are: unquoted variables with spaces or glob characters in filenames; `set -e` silently disabled inside functions called from conditions; pipelines whose middle command fails but whose status is masked; temporary files left behind after failure; and running destructive commands on the wrong working directory because the script assumed `cd` succeeded (check the `cd` status or use subshells).
- **Validation patterns** — check argument count and file existence before acting (`[[ -f "$input" ]]`), use `--` to end option parsing (`rm -- "$file"` protects files starting with `-`), validate downloaded or generated files (non-empty, expected format) before overwriting anything, and make destructive operations conditional on explicit confirmation in interactive contexts.
- **Operational practice** — run scripts with `bash -n` to syntax-check, `shellcheck` to lint, and a dry-run mode (`--dry-run`) for anything destructive; log each stage to stderr so a failed run shows exactly where it stopped; and treat the script's own exit status as part of its contract, matching the exit-code discipline documented in the shell environment notes.
- **RSIS3 relevance** — the repo's build and snapshot scripts (gen-static-data.py, build_graph.py) run under these rules: quoting and pipefail protection matter because they process wiki filenames that contain spaces and special characters, and a robust wrapper around each generator is what keeps a single malformed note from silently breaking the whole snapshot.

## Related
- [[wiki/shell-environment/shell-environments-and-rc-files|Shell Environments & RC Files]]
- [[wiki/os-shell/shell-scripting|Shell Scripting]]
- [[wiki/os-shell/arrays-in-shell|Arrays in Bash/Zsh]]
- [[wiki/os-shell/errexit-and-shell-options|Errexit & Shell Options]]
- [[wiki/shell-environment/terminal-multiplexers-tmux|Terminal Multiplexers: tmux]]
