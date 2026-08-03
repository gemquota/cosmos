---
type: "concept"
title: "Denylist Validation"
description: "Blocking known-bad patterns instead of allowing known-good ones"
tags: ["validation", "input", "security", "practice"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---
# Denylist Validation

## Summary

Denylist validation rejects a known set of bad inputs while accepting everything else. It is convenient and fast to start but structurally incomplete: unknown attacks and typos pass through, so it must be paired with allowlist checks.

## Details
- Mechanism: maintain a list of prohibited patterns (SQL keywords, script tags, dangerous filenames, reserved words) and reject or transform matches. It is the default instinct for input hardening because it matches how attacks are discovered — add the pattern you just saw.
- Concrete example: blocking inputs containing "<script" or "DROP TABLE" stops naive payloads but misses obfuscations like <scr\0ipt>, case variation, or encoding tricks; a filter applied before normalization misses double-encoded input entirely.
- Failure modes: evasion via encoding, case, whitespace, and Unicode lookalikes; incomplete lists that create a false sense of security; legitimate input rejected because it contains a blocked substring (a username with "select"); and maintenance burden as the list grows with every incident.
- Operational tradeoffs: denylists are appropriate for low-risk, high-volume checks (blocking obvious spam terms, reserved words in identifiers) but never as the sole defense for injection — use allowlists for structured fields, parameterized queries, and context-aware output encoding. Order matters: normalize, then validate.
- RSIS3/mykb relevance: the wiki ingestion pipeline uses denylists only for spam-style signals (duplicate title patterns) while frontmatter types and tags remain allowlisted, matching the security posture documented in this cluster.
- WAF-style denylisting (signature matching) suffers the same completeness problem at the proxy layer; treat signatures as detection, not as a validation boundary.
- Logging denylist hits is mandatory: a healthy denylist mostly blocks noise; a spike in hits is usually the first signal of an attack campaign.
- Normalize first: apply Unicode normalization, case folding, and decoding before denylist matching; a pattern checked against raw input misses the encoded variant that arrives at the parser.

## Related
- [[wiki/api-protocols/web-security-owasp|Web Security (OWASP)]]
- [[wiki/web-platforms/input-normalization|Input Normalization]]
- [[wiki/web-platforms/unicode-normalization|Unicode Normalization]]
- [[wiki/web-platforms/url-normalization|URL Normalization]]
- [[wiki/security-auth/xss-prevention|XSS Prevention]]
- [[wiki/web-platforms/web-apis|Web APIs]]
- [[wiki/web-platforms/dom-manipulation|DOM Manipulation]]
