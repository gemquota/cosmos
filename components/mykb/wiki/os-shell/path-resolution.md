---
type: "concept"
title: "Path Resolution"
description: "How the shell and kernel turn a path string into a file: relative, absolute, and symlink traversal"
tags: ["paths", "filesystem", "resolution", "symlinks"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
---

# Path Resolution

## Summary
Path resolution is the process of turning a path string into an actual file: absolute paths start at `/`, relative paths start at the current working directory, `..` moves up a level, and symlinks are followed as the kernel walks each component. Every shell command, every `open()`, and every script depends on getting this exactly right.

## Details
- Mechanism: the kernel's `namei` walker resolves a path by walking components from a starting directory (root for absolute, the process's cwd for relative) through the dentry cache, following symlinks up to the kernel's limit (40 chained links, beyond which `ELOOP`), and crossing mount points into other filesystems as it goes. The shell adds its own resolution layer on top: `PATH` determines which directory's executable runs for a bare command name (searched left to right, first match wins), aliases and functions intercept before PATH lookup, and `hash` caches lookups. Trailing slashes require a directory, `.` and `..` are normalized, and multiple slashes collapse — but symlinks are NOT collapsed by the kernel's walk: `/a/../b` and `/a/../b` through a symlink `a -> /x` differ, which is exactly why `realpath` exists.
- Concrete examples: typing `python` runs `/usr/bin/python` (or the first match in PATH); `cd ..` moves the shell's cwd up; `./script.sh` forces a relative lookup; `readlink -f file` prints the canonical path with every symlink and `..` resolved; a script computing `$(dirname $0)/../config.ini` breaks when `$0` is a symlink unless `readlink -f` is applied first; `find` with `-L` follows symlinks while `-P` does not, changing traversal results.
- Failure modes: the classic failures are symlink loops (`ELOOP`: `ln -s a a`), broken links (the link resolves but the target is missing — the error names the final component, confusing beginners), and the `..` through symlink trap (in some systems `..` after a symlink refers to the *link's* parent, not the target's — POSIX behavior differs across platforms). PATH pitfalls: a bare command resolving to the wrong executable because a writable directory appears earlier in PATH, empty PATH entries meaning the current directory, and `PATH` missing in cron environments. Case sensitivity and whitespace in names add further traps on Linux.
- Operational tradeoffs: deterministic resolution is a correctness and security property: canonicalize paths before comparing or authorizing (a string check against `/var/www` can be bypassed by `/var/www/../etc` or a symlink), and prefer `realpath`/`readlink -f` for any path that crosses symlinks. The tradeoff of full canonicalization is cost and TOCTOU windows, which `openat2`'s resolution flags close at the syscall level: `RESOLVE_NO_SYMLINKS`, `RESOLVE_NO_MAGICLINKS`, and `RESOLVE_BENEATH` make the constraints part of the open itself, which is why container runtimes and secure tools use them. Magic links such as `/proc/self/fd/N` resolve to open files and bypass normal path checks, and tools like `sudo` and `tar` refuse to follow symlinks out of a target directory for safety. RSIS3 relevance: scripts that touch wiki files need deterministic path resolution — resolve once, canonicalize, and use the canonical path everywhere, so a symlinked repo or renamed directory cannot silently redirect writes.

## Related
- [[wiki/os-shell/filesystem-hierarchy|Filesystem Hierarchy]] — resolution happens within the hierarchy
- [[wiki/os-shell/symlinks|Symlinks]] — links are resolved during path walking
- [[wiki/os-shell/environment-variables|Environment Variables]] — PATH controls command resolution
- [[wiki/os-shell/glob-patterns|Glob Patterns]] — globs produce paths for resolution
- [[wiki/devops-infra/backups|Backups]] — backup scope follows paths
