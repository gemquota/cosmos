---
type: "concept"
title: "Open Redirects"
description: "Endpoints that redirect to attacker-chosen URLs, enabling phishing and token theft"
tags: ["open-redirects", "web-security", "phishing"]
timestamp: "2026-08-01T00:00:00Z"
status: "stub"
source: ["https://cheatsheetseries.owasp.org/cheatsheets/Unvalidated_Redirects_and_Forwards_Cheat_Sheet.html"]
---

# Open Redirects

- Open redirects occur when a redirect target comes from user input without validation, sending victims to phishing sites.
- They compound other attacks: OAuth redirect_uri confusion and token leakage rely on open redirects.
- Prevention: server-side allowlists of redirect destinations and avoiding redirect parameters for navigation.
- For mykb: OIDC/OAuth redirect URIs must be exact-match allowlisted, never user-supplied.

## Related

- [[wiki/identity/oidc-clients|OIDC Clients]] — redirect URI allowlisting
- [[wiki/identity/openid-connect|OpenID Connect]] — authorization redirects are the attack surface
- [[wiki/identity/phishing-resistance|Phishing Resistance]] — open redirects feed phishing
- [[wiki/security-auth/security-headers|Security Headers]] — browser protection stack
