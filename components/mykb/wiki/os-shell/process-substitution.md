---
type: "concept"
title: "Process Substitution"
description: "Feeding a command's output as if it were a file, via <(cmd)"
tags: ["process-substitution", "shell", "pipes", "bash"]
timestamp: "2026-08-01T00:00:00Z"
status: "stub"
---

# Process Substitution

## Summary
Process substitution (`<(cmd)`) runs a command and exposes its output as a named pipe or /dev/fd path, letting tools that expect files consume command output: `diff <(ls a) <(ls b)`.

## Details
- Bash and zsh support it; POSIX sh does not.
- Useful when a tool requires a file argument rather than stdin.
- RSIS3 relevance: comparing generated wiki indexes becomes a one-liner.

## Related
- [[wiki/os-shell/text-processing-pipelines|Text Processing Pipelines]] — process substitution is pipeline-adjacent
- [[wiki/os-shell/shell-scripting|Shell Scripting]] — a bash feature for scripts
- [[wiki/os-shell/stdin-stdout-stderr|Stdin Stdout Stderr]] — output becomes a stream-like file
- [[wiki/os-shell/sed-editing|Sed Editing]] — diff-style comparisons of transformed output
- [[wiki/data-storage/data-versioning|Data Versioning]] — comparing generated versions
