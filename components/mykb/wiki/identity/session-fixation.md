---
type: "concept"
title: "Session Fixation"
description: "Attack that forces a victim to use an attacker-known session identifier"
tags: ["session-fixation", "attacks", "sessions", "web-security"]
timestamp: "2026-08-01T00:00:00Z"
status: "stub"
source: ["https://owasp.org/www-community/attacks/Session_fixation"]
---

# Session Fixation

- Session fixation works by setting a victim's session ID to a value the attacker knows, then waiting for the victim to authenticate with it.
- Attackers inject the ID via links, subdomains, or cookie injection; after login the attacker replays the same ID to take over the session.
- Defense: rotate the session ID on every privilege change (especially login), generate IDs server-side with high entropy, and reject client-supplied IDs.
- For mykb: session management must treat authentication as an ID-rotation event, never a continuation.

## Related

- [[wiki/identity/session-management|Session Management]] — the lifecycle rules that prevent fixation
- [[wiki/identity/session-hijacking|Session Hijacking]] — the sibling attack on live sessions
- [[wiki/security-auth/csrf-protection|CSRF Protection]] — related request-forgery family
- [[wiki/security/sso|Single Sign-On]] — SSO sessions are a fixation target
