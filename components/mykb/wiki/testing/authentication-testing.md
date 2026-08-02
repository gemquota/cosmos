---
type: "concept"
title: "Authentication Testing"
description: "Testing login, sessions, tokens, and authorization flows"
tags: ["authentication", "testing", "security", "authz"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://owasp.org/www-project-web-security-testing-guide/latest/4-Web_Application_Security_Testing/04-Authentication_Testing/", "https://owasp.org/API-Security/editions/2023/en/0xa1-broken-object-level-authorization/"]
---

# Authentication Testing

## Summary
Authentication testing verifies login, sessions, tokens, and authorization flows for weaknesses: bypasses, session fixation, token misuse, and privilege escalation. Identity is the front door of most applications, so its failures are severe.

## Details
- Test areas: login with credentials, SSO, and MFA; session management; password reset; token lifecycle.
- OWASP WSTG dedicates an authentication testing chapter with concrete cases.
- Attack patterns: credential stuffing, brute force, session fixation, and JWT tampering.
- Verify lockout policies, secure cookie flags, and token expiration and revocation.
- Authorization: test IDOR, role escalation, and missing access checks.
- Automate authentication flows in API tests and keep a negative-test matrix.
- Include social-login and OAuth callback paths in scope.

## Related
- [[wiki/testing/security-testing|Security Testing]] — the discipline auth testing serves
- [[wiki/security-auth/token-authentication|Token Authentication]] — token lifecycle under test
- [[wiki/security-auth/least-privilege|Least Privilege]] — authorization policy to verify
- [[wiki/security-auth/privilege-escalation|Privilege Escalation]] — a key auth failure mode
- [[wiki/testing/api-testing|API Testing]] — auth flows automated in API suites
- [[wiki/testing/negative-testing|Negative Testing]] — rejected credentials and expired tokens
