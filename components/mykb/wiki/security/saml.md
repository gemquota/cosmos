---
type: "concept"
title: "SAML"
description: "XML-based enterprise federation protocol for browser-based single sign-on"
tags: ["saml", "sso", "federation", "xml", "enterprise"]
timestamp: "2026-07-31T00:00:00Z"
status: "growing"
---

# SAML

## Summary
SAML (Security Assertion Markup Language) is the XML-based standard for enterprise SSO: an identity provider issues signed assertions that service providers trust.

## Details
- Flows: SP-initiated and IdP-initiated redirects carry `<saml:Assertion>` documents.
- Strong in legacy enterprise stacks (ADFS, Okta, Shibboleth); heavier than OIDC.
- New apps usually choose OIDC; SAML remains for enterprise interop.

## Flows

SAML has two primary flows. In SP-initiated SSO, the user first contacts the service provider, which redirects to the identity provider with an authentication request; after login, the IdP posts a signed assertion back. In IdP-initiated SSO, the user starts at the identity provider's portal and is redirected to the service provider carrying an assertion, with no request in the other direction. Both flows rely on browser redirects and form posts — SAML 2.0 has no native mobile or API binding — which is why native apps typically layer OAuth on top of or instead of SAML.

## Assertions

The `<saml:Assertion>` document carries the core claims: who the subject is, when the assertion was issued and expires, which conditions apply (audience, destination), and the attribute statements a service provider requested. Assertions are signed with the IdP's certificate, and the SP validates the signature, the audience restriction, and the validity window before trusting them. Attribute statements carry roles and profile data, which downstream systems map to authorization decisions — the bridge between identity and [[wiki/security/rbac|RBAC]].

## Integration Notes

SAML integration is dominated by metadata exchange: IdP and SP publish XML metadata describing endpoints, certificates, and bindings, and mismatched metadata is the most common integration failure. Certificate rotation must be coordinated or users are locked out at the next renewal. For environments that also use modern protocols, [[wiki/security/mfa|MFA]] can be layered onto the IdP, and [[wiki/security/webauthn|WebAuthn]] and [[wiki/security/passkeys|passkeys]] increasingly serve as the second factor behind a SAML login. TLS protects the redirects, and [[wiki/security/zero-trust|zero trust]] architectures treat SAML as one trust signal among several rather than the whole story. Teams choosing protocols today often prefer OIDC for new apps while keeping SAML for enterprise interop.

## Related
- [[wiki/security/sso|Single Sign-On]] — the goal SAML serves
- [[wiki/security/oauth2|OAuth 2.0]] — modern alternative
- [[wiki/security/ldap|LDAP]] — directory underneath
- [[wiki/security/jwt|JWT]] — assertion format contrast
- [[wiki/security/rbac|RBAC]] — assertions carry roles
