---
type: "concept"
title: "Response Splitting"
description: "CRLF injection that splits one HTTP response into two"
tags: ["security", "http", "injection", "attacks"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---
# Response Splitting

## Summary
Response splitting is the endgame of CRLF injection: an attacker injects CRLF sequences into a response so the server emits the attacker's headers and body as a second response. Caches and proxies can then serve the attacker's content to other users.

## Details
HTTP responses are separated by a blank line (CRLF CRLF). If user input with CRLF reaches a header value, the attacker can terminate the header block and write arbitrary bytes — headers, then a body — that the server serializes as a continuation. In vulnerable stacks, one request produces two responses on the same connection; the first belongs to the requester, the second is left for the next request on that connection — which may be another user's, served through a shared cache or proxy.

The mechanism: the vulnerable code interpolates input into a header (Location, Set-Cookie, custom headers) without stripping 0x0D/0x0A. Input like %0d%0aContent-Length:%200%0d%0a%0d%0a<html>... decodes to a full second response. Impact: cache poisoning (the poisoned second response is cached and served to everyone), XSS via injected HTML, and session fixation via injected Set-Cookie. Modern frameworks reject CRLF in header values, which mostly retired the bug — but legacy gateways, logging paths, and hand-rolled header code remain.

Concrete example: a redirect endpoint reflects a next parameter into Location. An attacker sends next=/ok%0d%0aSet-Cookie:%20session=hijacked%0d%0a%0d%0a<html>pwned</html>. The server emits the legitimate redirect, then the attacker's Set-Cookie and HTML body as a second response; a caching proxy that doesn't reject the split caches the HTML, and subsequent visitors to the URL get the attacker's page.

Failure modes: stacks that validate header names but not values; proxies that pass CRLF through unchanged; and double-decoding anywhere in the chain that turns %250d%250a into CRLF after validation. The attack is also a log-forgery vector: CRLF in log lines fabricates audit entries.

Operational tradeoffs: the durable fix is boundary validation — reject CR, LF, and NUL in any input destined for headers or logs — plus framework header APIs that enforce valid values. Response splitting is best understood as a consequence of header injection: fix the injection, and the splitting disappears. Tests should fuzz every reflected parameter with CRLF and encoded variants and verify a single response on the wire.

RSIS3/mykb relevance: the wiki's redirect and logging code should sanitize at the boundary; documenting the reject-CRLF rule gives RSIS3's security checks a concrete fuzz list.

## Related
- [[wiki/api-protocols/web-security-owasp|Web Security (OWASP)]]
- [[wiki/api-protocols/content-sniffing|Content Sniffing Attacks]]
- [[wiki/api-protocols/template-injection|Template Injection]]
- [[wiki/api-protocols/sql-injection-practice|SQL Injection]]
- [[wiki/security-auth/sql-injection-prevention|SQL Injection Prevention]]
- [[wiki/security-auth/command-injection|Command Injection]]
- [[wiki/security-auth/ldap-injection|LDAP Injection]]
