---
type: "concept"
title: "Session Fixation"
description: "Attack that forces a victim to use an attacker-known session identifier"
tags: ["session-fixation", "attacks", "sessions", "web-security"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://owasp.org/www-community/attacks/Session_fixation"]
---

# Session Fixation

## Summary
Session fixation is an attack that forces a victim to use an attacker-known session identifier, then waits for the victim to authenticate with it — after which the attacker replays the same ID to take over the session. It succeeds when a web application accepts a session ID supplied by the client before authentication, rather than generating a fresh server-side ID at login.

## Details
- Session fixation works by setting a victim's session ID to a value the attacker knows, then waiting for the victim to authenticate with it. The attacker needs no credentials and no code execution — only the ability to plant a cookie or URL parameter, then reap the authenticated session after the victim logs in.
- Attackers inject the ID via links, subdomains, or cookie injection; after login the attacker replays the same ID to take over the session. Injection vectors include phishing links with a session parameter, subdomain cookies that the application accepts from a sibling domain the attacker controls, and cross-site scripting that sets a cookie.
- Defense: rotate the session ID on every privilege change (especially login), generate IDs server-side with high entropy, and reject client-supplied IDs. The decisive control is rotation: whether or not the attacker planted an ID, a fresh server-generated ID issued at login invalidates the planted one — the attack has nothing to replay.
- Concrete example: an attacker sends a victim `https://bank.example/login?session=attacker123`; the application honors the parameter as the session ID. The victim logs in; the application marks session `attacker123` as authenticated without changing it; the attacker, who already knows the ID, loads the same session and is logged in as the victim.
- Failure modes: session IDs accepted from URL parameters (which leak via referrer and logs) or from the client at all; IDs that are not rotated on login or privilege escalation; and session IDs that are guessable or sequential, which lets an attacker skip planting and simply find valid sessions.
- The sibling attack family is session hijacking, which steals an existing session rather than planting one; the defenses overlap (secure cookies, binding, monitoring), but fixation is defeated specifically by generation and rotation rules, not by watching for theft.
- For mykb: session management must treat authentication as an ID-rotation event, never a continuation — a rule that applies to agent sessions as much as human ones, since a fixed agent session would let an attacker operate as the agent.

## Related
- [[wiki/identity/session-management|Session Management]] — the lifecycle rules that prevent fixation
- [[wiki/identity/session-hijacking|Session Hijacking]] — the sibling attack on live sessions
- [[wiki/security-auth/csrf-protection|CSRF Protection]] — related request-forgery family
- [[wiki/security/sso|Single Sign-On]] — SSO sessions are a fixation target
