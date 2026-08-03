---
type: "concept"
title: "Unicode Normalization"
description: "Canonical equivalence forms such as NFC and NFD"
tags: ["unicode", "encoding", "normalization", "i18n"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---
# Unicode Normalization

## Summary

Unicode normalization converts text to a canonical form (NFC/NFD/NFKC/NFKD) so visually identical strings compare equal. It is required for identifiers, search, dedup, and any security check that compares user strings.

## Details
- Mechanism: many characters can be written two ways — é as one codepoint (U+00E9) or e + combining accent (U+0065 U+0301); NFC composes to the single codepoint, NFD decomposes. NFKC/NFKD additionally fold compatibility characters (ﬁ → fi, ① → 1), changing meaning in some scripts, so they are for search/lenient matching, not identity.
- Concrete example: a username registry normalizing NFC treats "café" and "cafe\u0301" as the same identity; a search index normalizing NFKC lets users find "①" by typing "1"; a password or token check that skips normalization rejects valid logins or accepts lookalikes depending on direction.
- Failure modes: normalizing with NFC for storage but comparing with a raw string; using NFKC where meaning matters (it conflates distinct characters and can break identifiers); normalizing after hashing (order matters — hash the canonical form); and locale-dependent case folding interacting with normalization order.
- Operational tradeoffs: pick one form per field (NFC is the web default) and normalize at every boundary: ingestion, comparison, indexing, and rendering; document the form so libraries (URLs, file systems, databases) that normalize internally do not double-transform.
- RSIS3/mykb relevance: the wiki pipeline NFC-normalizes titles, tags, and search queries; this node is the reference for all string-comparison code in loop tooling.
- Filenames and URLs: filesystems and URL parsers normalize independently; compare against the normalized form used by the layer that stored the value to avoid misses.
- Testing: include composed/decomposed and compatibility-form fixtures in string tests so normalization regressions fail loudly rather than surfacing as lookup bugs.
- Security angle: normalization also defends against lookalike bypasses (homoglyph usernames, encoded payloads); normalize before allowlist checks so crafted variants cannot dodge the rules.

## Related
- [[wiki/api-protocols/web-security-owasp|Web Security (OWASP)]]
- [[wiki/web-platforms/url-normalization|URL Normalization]]
- [[wiki/web-platforms/path-normalization|Path Normalization]]
- [[wiki/web-platforms/symlink-following|Symlink Following]]
- [[wiki/security-auth/xss-prevention|XSS Prevention]]
- [[wiki/web-platforms/web-apis|Web APIs]]
- [[wiki/web-platforms/dom-manipulation|DOM Manipulation]]
