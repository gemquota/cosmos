---
type: "concept"
title: "CSRF Tokens"
description: "Random per-session tokens that prove a request came from the real form"
tags: ["security", "csrf", "http", "web"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---
# CSRF Tokens

## Summary
A CSRF token is a random, unguessable value embedded in forms and validated on state-changing requests. Because an attacker's cross-site page cannot read or supply the token, it proves the request originated from the legitimate site.

## Details
CSRF protection works by adding a secret the attacker cannot know. The server generates a token per session (or per form), embeds it in the rendered page, and requires it on every state-changing request. A cross-site attack cannot read the token from the victim's page (same-origin policy) and cannot guess it (it is cryptographically random), so forged requests fail validation.

The mechanism: two main patterns exist. The synchronizer token pattern stores the token server-side and compares it with the submitted token. The double-submit cookie pattern sets the token in a cookie and also in a form field; the server compares the two, avoiding server-side state (with the caveat that a subdomain that can write cookies can defeat it, so the pattern should bind the token to the session). Validation must happen on the server for every method that changes state, and the token must be checked as a constant-time comparison against the session value.

Concrete example: a wiki's comment form includes <input type="hidden" name="_csrf" value="a3f9...">. On POST, the server compares it with the session's stored token. An attacker page auto-submitting a forged form cannot include the correct value (the token is not in any cookie the attacker can read), so the POST is rejected. The same protection applies to login forms to prevent login CSRF, where an attacker logs the victim into the attacker's account.

Failure modes: tokens stored in cookies readable by subdomains, tokens reused across sessions, tokens validated only for some methods (GET with side effects), and token comparison that is not constant-time (timing side channel) all weaken the control. Emitting the same token to every response without binding it to the session lets an attacker who can obtain one token reuse it. Removing the check on "simple" endpoints recreates the hole.

Operational tradeoffs: CSRF tokens are the reliable defense when cookies are the auth mechanism and SameSite can't be strict; they cost a little server state and form plumbing. Pairing tokens with SameSite=Lax covers the common cases, with tokens as the backstop for cross-site cookie contexts. Alternative or complementary controls: custom headers (an attacker can't set X-Requested-With cross-origin), Sec-Fetch-Site validation, and SameSite=None only where genuinely needed.

RSIS3/mykb relevance: any web form the wiki or dashboard exposes needs the token pattern; documenting the synchronizer-token contract here lets RSIS3 verify that every state-changing route validates the token.

## Related
- [[wiki/api-protocols/secure-cookies|Secure Cookies]]
- [[wiki/api-protocols/double-submit-cookie|Double-Submit Cookie]]
- [[wiki/api-protocols/synchronizer-token|Synchronizer Token Pattern]]
- [[wiki/api-protocols/sec-fetch-headers|Sec-Fetch Headers]]
- [[wiki/api-protocols/csrf|CSRF]]
- [[wiki/security-auth/csrf-protection|CSRF Protection]]
- [[wiki/api-protocols/http-headers|HTTP Headers]]
