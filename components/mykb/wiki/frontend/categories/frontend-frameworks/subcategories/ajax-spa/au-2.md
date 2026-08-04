---
type: "entity"
title: "AU"
description: "Authentication"
tags: ["acronym", "ajax", "android", "api", "ast", "auth", "entity"]
timestamp: "2026-07-19T22:41:39Z"
resource: ""
status: "growing"
---

## Au 2

Authentication — the process of verifying the identity of users or systems. Sessions show OAuth 2.0, JWT, API keys, session-based auth, and multi-factor authentication.

Authentication answers the question of who is making a request. The three common factors are something you know, such as a password, something you have, such as a phone or security key, and something you are, such as a fingerprint. Multi-factor authentication combines factors so that compromising a single credential is not enough.

Passwords should be stored as salted, slow hashes such as bcrypt or Argon2, never in plain text, and logins should be protected against brute force with rate limiting and lockout policies. Sessions are established after successful authentication: a server-side session store paired with a signed cookie, or a stateless token such as a JWT carrying claims that the server can verify.

OAuth 2.0 lets a user authorize a client application to access resources on their behalf. The authorization code flow with PKCE is the recommended pattern for public clients, exchanging a temporary code for tokens without exposing the client secret. Tokens are scoped, expire, and can be refreshed, which limits the damage if one is leaked.

API keys identify machine clients and should be stored, transmitted, and rotated with the same care as passwords. Every authentication scheme has failure modes: leaked tokens, weak secrets, and confused-deputy problems where a legitimate service is tricked into acting on behalf of an attacker. Logging and monitoring, including attempts that result in [[wiki/security-auth/categories/auth-security/subcategories/authentication/access-denied|Access Denied]], are part of the discipline documented across the [[wiki/web-platforms/00-index|Frontend Frameworks]] and [[wiki/web-platforms/00-index|Security Auth]] domains.

**Domain:** Web Platforms › [[wiki/web-platforms/00-index|Frontend]] › [[wiki/web-platforms/00-index|Frontend Frameworks]] › Au 2

## Related Entities

- [[wiki/frontend/categories/frontend-frameworks/subcategories/ajax-spa/ac|Ace 10]]
- [[wiki/frontend/categories/frontend-frameworks/subcategories/ajax-spa/aa|Aa]]
- [[wiki/frontend/categories/frontend-frameworks/subcategories/ajax-spa/insecurerequestwarning-2|Insecurerequestwarning 2]]
- [[wiki/frontend/categories/frontend-frameworks/subcategories/ajax-spa/jetbrain|Jetbrains 10]]
- [[wiki/frontend/categories/frontend-frameworks/subcategories/ajax-spa/cs|Csv 10]]
- [[wiki/frontend/categories/frontend-frameworks/subcategories/ajax-spa/dataframe-2|Dataframe 2]]
- [[wiki/frontend/categories/frontend-frameworks/subcategories/ajax-spa/invalid-login-2|Invalid Login 2]]
- [[wiki/frontend/categories/frontend-frameworks/subcategories/ajax-spa/langchain-2|Langchain 2]]
