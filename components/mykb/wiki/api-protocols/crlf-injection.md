---
type: "concept"
title: "CRLF Injection"
description: "Injecting carriage-return line-feed sequences to smuggle headers or split responses"
tags: ["security", "http", "injection", "attacks"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---
# CRLF Injection

## Summary
CRLF injection happens when user input containing carriage-return and line-feed bytes (0x0D 0x0A) reaches an HTTP header or log line. The attacker terminates the current header and starts new ones, enabling response splitting, header injection, and log forgery.

## Details
HTTP separates headers with CRLF sequences. If an application echoes user input into a header value without stripping CR and LF, an attacker can inject %0d%0a (decoded) followed by arbitrary header lines — or, in older stacks, a whole fake response body. The classic result is response splitting: the server sends one response, then the attacker's injected headers and body as a second response, which caches and proxies can mis-associate with other requests.

The mechanism: the vulnerable code builds a header like Location: https://site/redirect?next=<input> and passes it to the HTTP layer, which naively writes it. Input of next=/ok%0d%0aSet-Cookie:%20session=attacker%0d%0a%0d%0a<html>evil</html> turns one response into two. Modern frameworks sanitize header values or reject CR/LF outright, but logging paths and legacy gateways often remain vulnerable — CRLF in log lines forges log entries that mislead incident responders.

Concrete example: a redirect endpoint reflects the next parameter into the Location header. An attacker sends next=%0d%0aX-Injected:%20yes and the response carries an extra header — if a proxy trusts that header, the impact escalates. More seriously, injecting a Set-Cookie header lets an attacker plant a session cookie on a victim's browser for the trusted domain, a primitive for session fixation.

Failure modes: the attack is often invisible because the injected header is well-formed; header injection compounds into cache poisoning (if the injected header affects caching), XSS (if a script can be smuggled into a later header), and session fixation; and permissive proxies that pass CRLF through instead of rejecting it keep old stacks vulnerable even after the app framework fixes itself.

Operational tradeoffs: the durable fix is rejecting or encoding CR, LF, and NUL in any input that can reach a header, log line, or cookie value — validation at the boundary, not ad hoc escaping per call site. Headers should be built with framework APIs that validate names and values, and logs should encode newlines (for example as \\n) so forgery is visible. Testing should fuzz every reflected parameter with %0d, %0a, %00, and their double-encoded variants.

RSIS3/mykb relevance: this is a canonical "validate at the boundary" rule for the wiki's redirect and logging code; encoding it here gives RSIS3's security reviews a concrete input list to test.

## Related
- [[wiki/api-protocols/web-security-owasp|Web Security (OWASP)]]
- [[wiki/api-protocols/response-splitting|Response Splitting]]
- [[wiki/api-protocols/content-sniffing|Content Sniffing Attacks]]
- [[wiki/api-protocols/template-injection|Template Injection]]
- [[wiki/security-auth/sql-injection-prevention|SQL Injection Prevention]]
- [[wiki/security-auth/command-injection|Command Injection]]
- [[wiki/security-auth/ldap-injection|LDAP Injection]]
