---
type: "concept"
title: "Session Hijacking"
description: "Stealing or replaying a live session to impersonate the authenticated user"
tags: ["session-hijacking", "attacks", "sessions", "web-security"]
timestamp: "2026-08-01T00:00:00Z"
status: "stub"
source: ["https://en.wikipedia.org/wiki/Session_hijacking"]
---

# Session Hijacking

- Session hijacking captures a valid session identifier — via network sniffing, XSS, malware, or logs — and replays it as the victim.
- Mitigations: TLS everywhere, HttpOnly and Secure cookies, binding sessions to device and IP signals, and short timeouts.
- Detection: concurrent sessions from new locations, abnormal request patterns, and session ID reuse alerts.
- For mykb: session binding plus anomaly detection keeps a stolen cookie from becoming a full account takeover.

## Related

- [[wiki/identity/session-management|Session Management]] — lifecycle controls that limit hijacking
- [[wiki/identity/account-takeover|Account Takeover]] — hijacking is a takeover path
- [[wiki/security-auth/xss-prevention|XSS Prevention]] — XSS is a common cookie stealer
- [[wiki/security-auth/security-headers|Security Headers]] — HttpOnly and Secure cookie flags
