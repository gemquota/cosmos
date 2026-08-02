---
type: "concept"
title: "diff & patch"
description: "Unified diffs and applying patches"
tags: ["diff", "patch", "version-control", "text"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://man7.org/linux/man-pages/man1/diff.1.html", "https://man7.org/linux/man-pages/man1/patch.1.html"]
---

# diff & patch

## Summary
diff compares files or directory trees and reports differences; patch applies those differences to other copies. Unified diffs with context are the standard exchange format, and git's diff output follows the same shape.

## Details
- diff -u a b produces a unified diff with headers, hunks, and context lines; -r recurses directories, -N treats missing files as empty.
- A hunk header like @@ -1,5 +1,6 @@ shows the old and new line ranges; lines prefixed - are removed, + added, space means context.
- patch -p1 < changes.patch applies from a parent directory, stripping one path component; -p0 applies from the original location.
- patch --dry-run or --forward tests applicability; fuzz (patch -F) tolerates drifted context at some risk of misapplication.
- Reverse-apply with -R undoes a patch; git diff | git apply and git format-patch produce and consume the same format.
- diff options: -w ignores whitespace, -B ignores blank lines, --color highlights; diff -u <(cmd1) <(cmd2) compares command output.
- Beyond text: diff --binary and git's binary patch handling; for configs, diff -u config.old config.new is the review idiom.

## Related
- [[wiki/os-shell/grep-patterns|Grep Patterns]] — reviewing what changed
- [[wiki/dev-tools/merge-conflicts|Merge Conflicts]] — when patches collide
- [[wiki/dev-tools/git-rebase|Git Rebase]] — patch application at scale
- [[wiki/dev-tools/conventional-commits|Conventional Commits]] — the change log patches carry
- [[wiki/os-shell/sed-editing|sed Editing]] — programmatic text edits vs diffs
