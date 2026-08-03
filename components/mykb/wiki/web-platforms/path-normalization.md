---
type: "concept"
title: "Path Normalization"
description: "Resolving dot segments and traversal before filesystem access"
tags: ["paths", "security", "filesystem", "normalization"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---
# Path Normalization

## Summary

Path normalization canonicalizes file or URL paths — resolving ., .., duplicate slashes, and symlinks — before authorization or filesystem access. Skipping it lets crafted paths escape intended directories (directory traversal).

## Details
- Mechanism: normalize by removing dot segments, collapsing repeated separators, resolving symlinks/realpath, and rejecting absolute or drive-qualified forms where forbidden; then verify the resolved path stays under the allowed root. Web servers and frameworks do this internally, but custom file-serving code must do it explicitly.
- Concrete example: a request for /download/../../etc/passwd must resolve to an error, not the host file; URL-encoded variants (%2e%2e%2f, double encoding) must be decoded before normalization — decode once, normalize, then check the prefix.
- Failure modes: prefix checks on un-normalized paths (a/../b/secret passes a starts-with-a check); symlinks inside the allowed root pointing outside it; Unicode lookalikes (full-width dots) after normalization; and case-insensitive filesystems (Windows/macOS) where casing differences bypass exact-match checks.
- Operational tradeoffs: normalization must happen at one chokepoint after decoding and before any use; keep the canonical root as a realpath so comparisons are apples-to-apples. When serving user uploads, prefer random identifiers over user-controlled filenames entirely.
- RSIS3/mykb relevance: the wiki daemon serves note files by path; it normalizes and root-checks every request, a rule recorded here so future file-serving endpoints inherit the same guard.
- Windows specifics: backslash separators, drive letters, and UNC roots need their own normalization; a POSIX-only check is a traversal hole on Windows hosts.
- Logging: log the normalized path and the original on rejection so traversal attempts are visible in security monitoring.
- Framework use: prefer built-in file-serving middleware over custom path handling; a framework's battle-tested normalization beats a hand-rolled resolver on edge cases like backslashes and encoded dots.
- Decode-once rule: URL-decode exactly once before normalization; double-decoding turns encoded separators back into path syntax.

## Related
- [[wiki/api-protocols/web-security-owasp|Web Security (OWASP)]]
- [[wiki/web-platforms/symlink-following|Symlink Following]]
- [[wiki/web-platforms/sanitization-practice|Sanitization Practice]]
- [[wiki/web-platforms/output-encoding|Output Encoding]]
- [[wiki/security-auth/xss-prevention|XSS Prevention]]
- [[wiki/web-platforms/web-apis|Web APIs]]
- [[wiki/web-platforms/dom-manipulation|DOM Manipulation]]
