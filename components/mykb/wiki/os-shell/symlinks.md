---
type: "concept"
title: "Symlinks"
description: "Filesystem pointers that make one path refer to another file or directory"
tags: ["symlinks", "filesystem", "links", "paths"]
timestamp: "2026-08-01T00:00:00Z"
status: "stub"
---

# Symlinks

## Summary
A symbolic link (symlink) is a special file containing a path to another target; accessing the link follows the target. `ln -s target link` creates one; symlinks are how dotfiles and system versions are juggled.

## Details
- Symlinks can dangle when the target moves; hard links are a different mechanism (same inode, same filesystem).
- Tooling must decide whether to follow links — tar, find, and rsync all have follow/no-follow modes.
- RSIS3 relevance: managed dotfile setups and toolchain shims rely on symlinks.

## Related
- [[wiki/os-shell/path-resolution|Path Resolution]] — resolution follows symlinks
- [[wiki/os-shell/filesystem-hierarchy|Filesystem Hierarchy]] — links connect hierarchy locations
- [[wiki/os-shell/dotfiles|Dotfiles]] — dotfile managers install via symlinks
- [[wiki/devops-infra/backups|Backups]] — backup tools must handle link semantics
- [[wiki/security/container-hardening|Container Hardening]] — hardened images avoid symlink escapes
