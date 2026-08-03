---
type: "concept"
title: "Symlink Following"
description: "Attacks that traverse symbolic links during file operations"
tags: ["security", "filesystem", "paths", "attacks"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---
# Symlink Following

## Summary

Symlink following is a filesystem security decision: whether file-serving code resolves symbolic links, and whether the resolved target stays inside the allowed directory. Unchecked following enables path traversal and writes outside sandboxes.

## Details
- Mechanism: symlinks transparently redirect opens, so a directory containing links can expose files elsewhere; the risk appears when user input chooses paths (download endpoints, uploads, archives) or when archives create links during extraction. The check must resolve realpath of the final target, not the lexical path.
- Concrete example: a note server root contains symlink "notes/course -> /etc"; requesting notes/course/passwd serves the host file if the server only checks the lexical prefix. Zip extraction is the classic vector — a crafted archive with a symlink plus files written through it escapes the extraction dir.
- Failure modes: checking the prefix before resolving symlinks (the link itself matches the prefix); TOCTOU — the link swaps between check and open (use openat/O_NOFOLLOW or open with resolved handle); symlink loops causing hangs; and Windows junctions/links needing their own handling.
- Operational tradeoffs: some products legitimately need symlinks (user-managed dirs); the safe pattern is resolve realpath, verify containment, and open with no-follow semantics at the syscall level. For archives, extract to a fresh directory with link creation disabled or validated.
- RSIS3/mykb relevance: the wiki daemon resolves and root-checks symlinks before serving notes, and archive imports refuse links — a rule recorded here for loop tooling.
- Directory symlinks in user content: even when serving is safe, editors resolving relative paths through links can surprise users; expose resolved realpaths in listings so tooling agrees on identities.
- Audit: periodically scan content roots for unexpected symlinks (automated find -type l) so drift from archives or manual edits is caught before it becomes a serving hole.

## Related
- [[wiki/api-protocols/web-security-owasp|Web Security (OWASP)]]
- [[wiki/web-platforms/sanitization-practice|Sanitization Practice]]
- [[wiki/web-platforms/output-encoding|Output Encoding]]
- [[wiki/web-platforms/safe-html-rendering|Safe HTML Rendering]]
- [[wiki/security-auth/xss-prevention|XSS Prevention]]
- [[wiki/web-platforms/web-apis|Web APIs]]
- [[wiki/web-platforms/dom-manipulation|DOM Manipulation]]
