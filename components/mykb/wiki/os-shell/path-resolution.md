---
type: "concept"
title: "Path Resolution"
description: "How the shell and kernel turn a path string into a file: relative, absolute, and symlink traversal"
tags: ["paths", "filesystem", "resolution", "symlinks"]
timestamp: "2026-08-01T00:00:00Z"
status: "stub"
---

# Path Resolution

## Summary
Path resolution walks a filesystem from a root: absolute paths start at /, relative paths at the current directory, and `..` moves up. Symlinks are followed along the way; `realpath` resolves the final canonical path.

## Details
- The PATH variable drives command resolution: which directory's executable runs.
- Trailing slashes, `.` components, and symlink loops are the classic pitfalls.
- RSIS3 relevance: scripts that touch wiki files need deterministic path resolution.

## Related
- [[wiki/os-shell/filesystem-hierarchy|Filesystem Hierarchy]] — resolution happens within the hierarchy
- [[wiki/os-shell/symlinks|Symlinks]] — links are resolved during path walking
- [[wiki/os-shell/environment-variables|Environment Variables]] — PATH controls command resolution
- [[wiki/os-shell/glob-patterns|Glob Patterns]] — globs produce paths for resolution
- [[wiki/devops-infra/backups|Backups]] — backup scope follows paths
