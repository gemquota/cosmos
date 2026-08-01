---
type: "concept"
title: "SAML"
description: "XML-based enterprise federation protocol for browser-based single sign-on"
tags: ["saml", "sso", "federation", "xml", "enterprise"]
timestamp: "2026-07-31T00:00:00Z"
status: "stub"
---

# SAML

## Summary
SAML (Security Assertion Markup Language) is the XML-based standard for enterprise SSO: an identity provider issues signed assertions that service providers trust.

## Details
- Flows: SP-initiated and IdP-initiated redirects carry `<saml:Assertion>` documents.
- Strong in legacy enterprise stacks (ADFS, Okta, Shibboleth); heavier than OIDC.
- New apps usually choose OIDC; SAML remains for enterprise interop.

## Related
- [[wiki/security/sso|Single Sign-On]] — the goal SAML serves
- [[wiki/security/oauth2|OAuth 2.0]] — modern alternative
- [[wiki/security/ldap|LDAP]] — directory underneath
- [[wiki/security/jwt|JWT]] — assertion format contrast
- [[wiki/security/rbac|RBAC]] — assertions carry roles
