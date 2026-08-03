---
type: "concept"
title: "Path Resolution & Symlinks"
description: "How the kernel walks absolute and relative paths, symlinks, and mount points"
tags: ["path", "symlink", "filesystem", "unix"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# Path Resolution & Symlinks

## Summary
Path resolution is the kernel's walk from a path string to an inode: starting at the root (`/`) for absolute paths or the current directory for relative ones, traversing each component, following symlinks, and crossing mount points. Symlinks make the walk non-trivial — a link can point anywhere, even outside the tree you think you are in — which is why path canonicalization is a security-relevant operation.

## Details
- Mechanism: the kernel's `namei` walker processes path components one at a time against a dentry/inode cache: `.` stays put, `..` moves to the parent, mount points redirect traversal into another filesystem, and symlinks are followed (up to a limit of 40 chained links, beyond which `ELOOP`). The walk is performed relative to the process's root and current working directory, and `openat2` (with `RESOLVE_*` flags) added a way to constrain resolution — no symlinks, no magic links, no crossing mount points — which is what container runtimes and secure tools use. `realpath` and `readlink -f` perform canonicalization in userspace: they resolve every symlink and normalize `.`/`..` to produce the final absolute path.
- Concrete examples: `/usr/bin/python` being a symlink to `python3.12`, so the walk from `/` reaches the actual binary; `/proc/self/fd/N` magic links resolving to open files; a web app serving files via a user-supplied path where `realpath` plus a prefix check prevents `../../etc/passwd` traversal; `sudo` and `tar` refusing to follow symlinks out of a target directory for safety; a container's chrooted root making absolute paths resolve inside the container.
- Failure modes: the classic failures are symlink races (TOCTOU: a path checked with `realpath`, then the symlink swapped before `open`, so the check and the use see different targets — mitigated by `openat2`/`O_NOFOLLOW`), unbounded symlink chains (`ELOOP`), and broken links (the final target does not exist — `ENOENT` where the link exists but the file does not, a classic confusion), and permission boundary crossings where a symlink in a writable directory points into a protected one.
- Operational tradeoffs: canonicalization buys determinism and security at the cost of a syscall-heavy walk and the TOCTOU window between check and use; the modern answer is `openat2`'s `RESOLVE_*` flags, which make the constraints part of the open itself. For scripts, `readlink -f`/`realpath` are the reliable tools, and the practice rules are: resolve before comparing paths, never trust a string prefix check without canonicalizing, and treat symlinks in untrusted writable directories as a security boundary. RSIS3/mykb relevance: wiki scripts that resolve article paths should canonicalize before writing so a stray symlink cannot redirect a write outside the corpus — the same containment MyKB's slug-to-file mapping promises.

## Related
- [[wiki/cloud-infra/dns-resolution-process|DNS Resolution Process]] — related coverage in the same cluster
- [[wiki/devops-infra/observability-of-network-path|Observability of the Network Path]] — related coverage in the same cluster
- [[wiki/os-shell/path-resolution|Path Resolution]] — related coverage in the same cluster
- [[wiki/os-shell/dns-resolution|DNS Resolution]] — related coverage in the same cluster
- [[wiki/os-shell/kernel-architecture|Kernel Architecture]] — related coverage in the same cluster
- [[wiki/syntheses/knowledge-acquisition-workflow|Knowledge Acquisition Workflow]] — how stubs grow into full articles in mykb
- [[wiki/syntheses/mykb-acquisition-curation-and-practices|Acquisition, Curation & Practices]] — the curation loop this stub belongs to
