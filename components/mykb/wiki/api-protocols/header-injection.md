---
type: "concept"
title: "Header Injection"
description: "Injecting CRLF or separator bytes into HTTP headers to alter responses"
tags: ["security", "http", "injection", "attacks"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---
# Header Injection

## Summary
Header injection occurs when user input reaches an HTTP response header without sanitization, letting an attacker add arbitrary headers, split the response, or set cookies for the victim's browser. It is a downstream consequence of unsafe header construction.

## Details
HTTP header values are terminated by CRLF sequences and delimited by colons. When an application interpolates user input into a header value — a redirect Location, a Content-Disposition filename, a Set-Cookie value, a custom header — and the input contains CR (0x0D), LF (0x0A), or in some stacks NUL, the attacker can end the current header and begin new ones. CRLF injection is the specific case; header injection is the general class.

The mechanism: the vulnerable code builds something like Location: https://example.com/next=<input> and hands it to the HTTP layer, which serializes it verbatim. Input containing %0d%0a decodes to CRLF; the serializer emits the attacker's header lines. Impact scales with what the injected headers control: Set-Cookie enables session fixation, Location enables open-redirect-style attacks, and a double CRLF can terminate the header block entirely — response splitting — where the leftover bytes become a second response body that caches can associate with other users.

Concrete example: a login flow echoes a next parameter into the Location header after authentication. An attacker sends next=/ok%0d%0aSet-Cookie:session%3dhijacked%3b%20Path%3d/ and the victim's browser stores the forged cookie for the trusted domain after a legitimate login — a session-fixation primitive. The same parameter, reflected into a log line, forges audit entries.

Failure modes: the injection is silent when the added header is well-formed; proxies that pass CRLF through rather than rejecting it keep legacy stacks vulnerable; and frameworks that validate header names but not values leave the value path open. Every place input touches a header — including custom request-id echoes — needs the same boundary check.

Operational tradeoffs: the durable fix is to validate and encode at the boundary: reject or percent-encode CR, LF, and NUL in any input that will be serialized into a header, use framework header APIs that enforce valid values, and set headers from allowlisted sources rather than raw input. Logging should escape newlines so injected log entries are visible in audit. Fuzz tests with %0d, %0a, and double-encoded variants should cover every reflected parameter.

RSIS3/mykb relevance: the rule "never echo input into headers without boundary validation" belongs in the wiki's security synthesis notes; RSIS3's checks can grep for raw input in header construction.

## Related
- [[wiki/api-protocols/web-security-owasp|Web Security (OWASP)]] — related coverage in the same cluster
- [[wiki/api-protocols/crlf-injection|CRLF Injection]] — related coverage in the same cluster
- [[wiki/api-protocols/response-splitting|Response Splitting]] — related coverage in the same cluster
- [[wiki/api-protocols/content-sniffing|Content Sniffing Attacks]] — related coverage in the same cluster
- [[wiki/security-auth/sql-injection-prevention|SQL Injection Prevention]] — related coverage in the same cluster
- [[wiki/security-auth/command-injection|Command Injection]] — related coverage in the same cluster
- [[wiki/security-auth/ldap-injection|LDAP Injection]] — related coverage in the same cluster
