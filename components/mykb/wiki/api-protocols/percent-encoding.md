---
type: "concept"
title: "Percent-Encoding"
description: "The %XX encoding scheme that makes URLs transport-safe"
tags: ["http", "url", "encoding", "standards"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---
# Percent-Encoding

## Summary
Percent-encoding (URL encoding) represents bytes that are unsafe in URLs as %XX — %20 for space, %2F for slash. It is how query strings and paths carry arbitrary data, and its edge cases (which characters are encoded, double-encoding, normalization) are a classic source of security bugs.

## Details
RFC 3986 defines which characters are allowed raw in URIs: unreserved (A-Z, a-z, 0-9, -._~), reserved delimiters (:/?#[]@!$&'()*+,;=) allowed only in their structural roles, and everything else percent-encoded as UTF-8 bytes (%XX). The query component has looser rules than the path; spaces become %20 (or + in form encoding, a frequent source of confusion).

The mechanism: the browser and servers decode percent-encoded bytes at parse time. The security-relevant edge cases: double-encoding (a %25 decodes to %, and %252F decodes once to %2F, which a second decode turns into /); decoding timing (a WAF that matches encoded input but the app decodes after the check); and normalization differences (should %2F in a path be a slash or data? some servers decode, some don't, and proxies disagree). Each disagreement is a potential bypass.

Concrete example: a wiki API filters paths to block /admin but the server decodes %61dmin before routing. The attacker requests /%61dmin and the filter (matching raw input) misses it while the router sees /admin. The fix is single, consistent decoding at one layer, with filters applied after decoding — and no double-decoding anywhere in the chain.

Failure modes: decode-twice vulnerabilities where an extra decode turns harmless input into a separator or control character; encoding spaces as + in the path (legal only in query strings, and even there only for form data); rejecting valid UTF-8 percent sequences, which breaks internationalized input; and inconsistent charset assumptions (percent bytes are decoded as UTF-8, but legacy stacks assume latin-1).

Operational tradeoffs: the robust pattern is decode once at the framework boundary and treat the decoded value as authoritative everywhere downstream; validate after decoding, never before. Canonicalize early (resolve %2E%2E before access checks) to avoid traversal via encoding. Tests should cover %00, %2F, %5C, double-encoded forms, and mixed case hex (%2f vs %2F).

RSIS3/mykb relevance: the wiki's link parser and API routing must decode consistently; documenting the decode-once rule gives RSIS3's security checks a concrete bypass test list.

## Related
- [[wiki/api-protocols/http-fundamentals|HTTP Fundamentals]] — related coverage in the same cluster
- [[wiki/api-protocols/punycode-domains|Punycode Domains]] — related coverage in the same cluster
- [[wiki/api-protocols/url-structure|URL Structure]] — related coverage in the same cluster
- [[wiki/api-protocols/uri-vs-url|URI vs URL]] — related coverage in the same cluster
- [[wiki/api-protocols/http-methods|HTTP Methods]] — related coverage in the same cluster
- [[wiki/api-protocols/http-headers|HTTP Headers]] — related coverage in the same cluster
- [[wiki/security-auth/same-origin-policy|Same-Origin Policy]] — related coverage in the same cluster
