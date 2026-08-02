---
type: "concept"
title: "find"
description: "Expression syntax, -exec, -print0, and pruning"
tags: ["find", "files", "search", "command-line"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://man7.org/linux/man-pages/man1/find.1.html"]
---

# find

## Summary
find walks directory trees and evaluates an expression of tests and actions against each entry, printing matches by default. It is the standard way to locate files by name, type, size, or age, and to act on them with -exec or -delete.

## Details
- Expression grammar: tests such as -name '*.log', -type f, -size +10M, -mtime -7, -user alice; actions -print, -ls, -delete, -exec, -execdir.
- Operators: -and (default), -or, -not/!, and parentheses for grouping: find . -type f \( -name '*.c' -o -name '*.h' \).
- -exec cmd {} \; runs once per match; -exec cmd {} + batches matches into one invocation, which is far faster for cp and rm.
- -print0 and -execdir pair with xargs -0 and avoid whitespace and permission pitfalls; find ... -print0 | xargs -0 is the robust idiom.
- -prune stops descent into matched directories (e.g., skipping .git and node_modules); -maxdepth/-mindepth bound the walk.
- -delete implies -depth and refuses to delete non-empty directories; GNU find also has -printf for custom output.
- Performance: pruning early and using -type f before -name order tests for cheap pruning; find reads directory entries, not file contents.

## Related
- [[wiki/os-shell/xargs|xargs]] — the batching partner for find output
- [[wiki/os-shell/glob-patterns|Glob Patterns]] — shell-native recursive alternatives (**)
- [[wiki/os-shell/path-resolution|Path Resolution]] — how find's starting paths resolve
- [[wiki/os-shell/grep-patterns|Grep Patterns]] — searching inside the files find locates
- [[wiki/os-shell/filesystem-hierarchy|Filesystem Hierarchy]] — knowing where to look
