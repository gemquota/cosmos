---
type: "concept"
title: "Symlinks"
description: "Filesystem pointers that make one path refer to another file or directory"
tags: ["symlinks", "filesystem", "links", "paths"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
---

# Symlinks

## Summary
A symbolic link (symlink) is a special file whose contents are a path to another target: accessing the link follows the path, so `/usr/bin/python3` can point at `python3.12` and `~/.zshrc` can point at a dotfiles repo. `ln -s target link` creates one; symlinks are how versions, dotfiles, and toolchain shims are juggled — and they dangle when the target moves.

## Details
- Mechanism: a symlink stores a string (the target path), which may be absolute or relative — relative links are resolved relative to the *link's* directory, not the current working directory, which is why `ln -s ../lib/foo.so link` works when `link` lives next to the target's parent. The kernel follows links during path resolution, up to 40 chained links (ELOOP beyond). Symlinks are filesystem-internal pointers: they work across filesystems (unlike hard links), can point to directories, and do not keep the target alive — delete the target and the link dangles, showing `ENOENT` on access. Hard links are the different mechanism: multiple directory entries for the *same inode*, same filesystem only, and the file lives until the last hard link is removed.
- Concrete examples: `ln -s ~/dotfiles/.zshrc ~/.zshrc` manages a dotfile; `ln -s python3.12 /usr/local/bin/python` shims a version; `ln -s /data /var/lib/app-data` relocates a data directory without breaking paths; `readlink -f`/`realpath` resolve a link chain to the canonical path; `ls -l` shows targets; `find -L` follows links while `-P` (default) does not; backup tools (`rsync -l`, `tar`) each have follow/no-follow modes.
- Failure modes: the classic failures are dangling links (target renamed or removed — the link itself still exists and `ls` shows it, but access fails), symlink loops (`ln -s a b && ln -s b a` — ELOOP), and the security class: symlink races and escapes where an attacker plants a link inside a writable directory so a privileged process writes through it to a protected location (the reason `tar` refuses to extract links that escape the target, and `openat2`/`O_NOFOLLOW` exist). Relative-link mistakes (a link created with the wrong relative target breaks when moved) and hard-link confusion (a hard link to a directory is impossible) round out the footguns.
- Operational tradeoffs: symlinks give cheap indirection — versioning, dotfile management, and path aliases without copying — at the cost of added complexity: tools must decide whether to follow, backups must handle link semantics (backing up a link is not backing up its target), and every canonicalization decision becomes a security boundary. The practice rules: prefer relative links for portability, canonicalize before authorizing path access, and use hard links only within a filesystem where the file itself must stay alive under multiple names. RSIS3 relevance: managed dotfile setups and toolchain shims rely on symlinks; the wiki toolchain uses the same indirection for versioned scripts — with the standing rule that writes always resolve to canonical paths first.

## Related
- [[wiki/os-shell/path-resolution|Path Resolution]] — resolution follows symlinks
- [[wiki/os-shell/filesystem-hierarchy|Filesystem Hierarchy]] — links connect hierarchy locations
- [[wiki/os-shell/dotfiles|Dotfiles]] — dotfile managers install via symlinks
- [[wiki/devops-infra/backups|Backups]] — backup tools must handle link semantics
- [[wiki/security/container-hardening|Container Hardening]] — hardened images avoid symlink escapes
