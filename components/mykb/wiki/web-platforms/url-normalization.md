---
type: "concept"
title: "URL Normalization"
description: "Canonicalizing URLs to defeat parser and matching inconsistencies"
tags: ["url", "security", "normalization", "practice"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---
# URL Normalization

## Summary

URL normalization canonicalizes URLs — case, dot segments, default ports, percent-encoding, hostname forms — so equivalent addresses compare equal and security checks see one canonical form. Skipping it breaks caches, dedup, and allowlists.

## Details
- Mechanism: a URL parser (WHATWG URL in JS) normalizes scheme/host case, strips default ports, resolves dot segments, and percent-encodes as needed; further canonicalization may add trailing-slash policy, punycode conversion, and scheme-relative handling. Normalize before storing, comparing, or authorizing.
- Concrete example: https://EXAMPLE.com:443/a/../b and https://example.com/b are the same resource; an allowlist comparing raw strings misses the match. Redirect or SSRF guards must parse and normalize — checking startsWith('https://') on a crafted URL like https://trusted.com@evil.net leaks the check.
- Failure modes: comparing unparsed strings (case, default ports, dot segments, IDN lookalikes); URL parsers disagreeing across languages (the server and the filter must use the same spec); userinfo (@) and scheme confusion; and normalization that changes semantics — percent-encoded vs decoded paths matter for filesystem mapping.
- Operational tradeoffs: normalization at one chokepoint (a URL helper module) prevents scattered inconsistencies; the cost is choosing policy (trailing slash, default port, punycode) and keeping the parser version pinned. Test with a corpus of edge-case URLs in CI.
- RSIS3/mykb relevance: the wiki links would be normalized through a shared URL helper before storage; this node records the policy so the loop's link handling matches.
- Punycode and IDN: normalize internationalized hostnames to punycode before comparisons, and be aware that homograph domains look identical in UI — display the punycode or a verified label.
- Scheme policy: parse first, then allowlist schemes (http, https, mailto where intended); raw prefix checks on the original string are the classic SSRF and open-redirect bug.
- Cache keys: normalize URLs before using them as cache keys or dedup identifiers; two spellings of one URL otherwise create duplicate cache entries and duplicate content.

## Related
- [[wiki/api-protocols/web-security-owasp|Web Security (OWASP)]]
- [[wiki/web-platforms/path-normalization|Path Normalization]]
- [[wiki/web-platforms/symlink-following|Symlink Following]]
- [[wiki/web-platforms/sanitization-practice|Sanitization Practice]]
- [[wiki/security-auth/xss-prevention|XSS Prevention]]
- [[wiki/web-platforms/web-apis|Web APIs]]
- [[wiki/web-platforms/dom-manipulation|DOM Manipulation]]
