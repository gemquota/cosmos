---
type: "concept"
title: "Secure Cookie Flag"
description: "Restricting cookie transmission to HTTPS connections"
tags: ["cookies", "http", "security", "https"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---
# Secure Cookie Flag

## Summary
The Secure attribute on a cookie instructs the browser to send it only over HTTPS connections, keeping the credential out of plaintext HTTP traffic where any on-path observer could read it. It is the single most important cookie flag, yet it is routinely defeated by mixed content, localhost development habits, and misconfigured load balancers.

## Details
- Mechanism: when a server sets `Set-Cookie: session=abc; Secure`, the browser attaches that cookie only to requests whose scheme is HTTPS (or to `localhost`, which browsers treat as a potentially trustworthy origin for development). The flag protects the cookie in transit: on an HTTP page, the browser simply does not send it, so session credentials never traverse a wire an attacker can sniff. It does not protect the cookie at rest or against XSS — that is the job of HttpOnly, encryption, and access controls.
- Concrete examples: a login service that always sets `Secure` prevents a user who accidentally hits the HTTP version of the site from leaking their session token to a network sniffer; an API that issues refresh tokens as Secure cookies keeps them out of third-party analytics and HTTP referrer leakage; a CDN that terminates TLS upstream must still preserve the `Secure` attribute on downstream `Set-Cookie` responses so the browser honors it end to end.
- Failure modes: the classic gap is mixed content — a page loaded over HTTPS that makes an HTTP subrequest, or an HTTP redirect chain before the cookie is set, which silently drops or strips the flag. Development setups on `http://localhost` often work without Secure, so teams ship code that never exercises the HTTPS path, then production mysteriously logs users out; conversely, setting Secure in dev on a non-localhost HTTP host makes cookies vanish entirely, which teams "fix" by removing the flag and forgetting to re-add it. Proxies that rewrite `Set-Cookie` headers, and cookie jars in non-browser clients that ignore the flag, are quieter variants.
- Operational tradeoffs: there is essentially no downside to setting Secure in production, so treat it as mandatory: enforce it with a `Strict-Transport-Security` header so browsers upgrade plaintext attempts before cookies are involved, and add a monitoring rule that flags any `Set-Cookie` without Secure emitted over HTTP. For local development, use `localhost` (where Secure cookies still work) or a self-signed HTTPS proxy rather than weakening the flag.
- RSIS3/mykb relevance: session and API credentials issued by the MyKB daemon or RSIS3 service boundaries should always carry Secure plus HttpOnly; the flag discipline mirrors the broader rule that credentials must never travel outside a trusted transport channel.

## Related
- [[wiki/api-protocols/secure-cookies|Secure Cookies]]
- [[wiki/api-protocols/httponly-flag|HttpOnly Cookie Flag]]
- [[wiki/api-protocols/samesite-lax-strict|SameSite Lax vs Strict]]
- [[wiki/api-protocols/cookie-prefixes|Cookie Prefixes]]
- [[wiki/api-protocols/http-cookies|HTTP Cookies]]
- [[wiki/api-protocols/csrf|CSRF]]
- [[wiki/security-auth/same-origin-policy|Same-Origin Policy]]
