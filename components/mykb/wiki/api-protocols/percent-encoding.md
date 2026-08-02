---
type: "concept"
title: "Percent-Encoding"
description: "Encoding reserved and non-ASCII bytes in URLs as %XX escape sequences"
tags: ["url", "encoding", "http", "security"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---
# Percent-Encoding

## Summary
Encoding reserved and non-ASCII bytes in URLs as %XX escape sequences. A stub in the mykb wiki that frames the concept and the questions to expand into a full article.

## Details
- Reserved characters and non-ASCII bytes are escaped as %XX triplets
- Encoding mistakes cause double-decoding vulnerabilities in proxies and backends
- Open question — which charset does percent-encoding actually operate on?

## Related
- [[wiki/api-protocols/http-fundamentals|HTTP Fundamentals]] — related coverage in the same cluster
- [[wiki/api-protocols/punycode-domains|Punycode Domains]] — related coverage in the same cluster
- [[wiki/api-protocols/url-structure|URL Structure]] — related coverage in the same cluster
- [[wiki/api-protocols/uri-vs-url|URI vs URL]] — related coverage in the same cluster
- [[wiki/api-protocols/http-methods|HTTP Methods]] — related coverage in the same cluster
- [[wiki/api-protocols/http-headers|HTTP Headers]] — related coverage in the same cluster
- [[wiki/security-auth/same-origin-policy|Same-Origin Policy]] — related coverage in the same cluster
