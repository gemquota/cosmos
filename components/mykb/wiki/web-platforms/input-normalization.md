---
type: "concept"
title: "Input Normalization"
description: "Canonicalizing input before validation and storage"
tags: ["validation", "input", "normalization", "practice"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---
# Input Normalization

## Summary

Input normalization brings user input to a canonical form before validation, storage, or comparison: trimming, case folding, and Unicode normalization. It prevents lookalike duplicates and encoding-based bypasses.

## Details
- Mechanism: canonicalize at the boundary — trim whitespace, apply case folding (which differs from lowercase for some scripts, e.g. ß→SS), and normalize Unicode via NFC/NFD so composed and decomposed forms compare equal. Then validate, then store.
- Concrete example: two registrations "café" (é as one codepoint) and "cafe\u0301" (e + combining accent) are the same string to a user but distinct bytes; NFC normalization makes lookups and uniqueness checks agree. A username allowlist after NFD normalization blocks homoglyph tricks that slip through a raw byte check.
- Failure modes: normalizing for display but not for identity (or vice versa); applying normalization that changes meaning (NFKC can conflate distinct characters like ① and 1); trimming only spaces, missing tabs/newlines/zero-width characters; and validating before normalizing, so encoded or composed variants dodge the rules.
- Operational tradeoffs: normalization is a policy decision — NFC is the web default for interchange, but identifiers may want stricter canonical forms; document which form each field uses. Normalize consistently at ingestion so downstream comparisons, dedup, and indexing share one shape.
- RSIS3/mykb relevance: the wiki ingestion pipeline NFC-normalizes titles and tags before dedup so the same note entered with composed vs decomposed accents is not duplicated.
- Order matters: normalize before validate, validate before sanitize, and store the canonical form; reversing the order lets encoding tricks bypass rules and creates duplicate identities downstream.
- Boundaries: apply the same normalization on write and on read for comparison; a search box that normalizes differently from the index misses matches, so centralize the transform in one module.
- Uniqueness: enforce uniqueness on the normalized form, not the raw input; two raw spellings that normalize identically are the same identity, and the database should know it.

## Related
- [[wiki/api-protocols/web-security-owasp|Web Security (OWASP)]]
- [[wiki/web-platforms/unicode-normalization|Unicode Normalization]]
- [[wiki/web-platforms/url-normalization|URL Normalization]]
- [[wiki/web-platforms/path-normalization|Path Normalization]]
- [[wiki/security-auth/xss-prevention|XSS Prevention]]
- [[wiki/web-platforms/web-apis|Web APIs]]
- [[wiki/web-platforms/dom-manipulation|DOM Manipulation]]
