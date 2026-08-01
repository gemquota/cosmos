---
type: "concept"
title: "Identity Providers"
description: "Systems that enroll subjects, manage their credentials, and assert identity to relying parties"
tags: ["idp", "identity", "authentication", "federation", "nist"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://pages.nist.gov/800-63-3/sp800-63-3.html"]
---

# Identity Providers

## Summary

An identity provider (IdP) is the system that performs the identity functions of the digital-identity lifecycle: enrolling a subject, issuing and managing credentials, authenticating the subject, and producing assertions (SAML assertions or OIDC tokens) that relying parties consume. NIST SP 800-63-3 defines the IdP role inside a broader digital identity model and ties it to assurance levels (IAL for identity proofing, AAL for authentication, FAL for federation). IdPs matter to mykb because every federation and SSO design — and every external login RSIS3 consumes — resolves to an IdP boundary.

## Details

- Core functions: identity proofing at enrollment, credential issuance and storage, authentication ceremonies, and assertion issuance to RPs.
- Deployment shapes: enterprise IdPs (Microsoft Entra ID, Okta, Keycloak), social IdPs (Google, GitHub, Apple), and self-hosted identity servers inside the network.
- Assurance: IAL says how strongly the claimed identity was proven; AAL says how strongly authentication was performed; FAL says how strongly assertions are conveyed — RSIS3 should record these levels per identity.
- IdP proxy vs origin: proxies aggregate multiple upstream IdPs behind one interface; the origin IdP actually performs authentication.
- Operational duties: key management for signing assertions, session management, MFA enforcement, and monitoring of abuse like credential stuffing.
- For mykb, an IdP boundary means the trust decision is local: accept assertions only from configured issuers with verified signing keys.

## Related

- [[wiki/identity/identity-federation|Identity Federation]] — trust between IdPs and RPs
- [[wiki/identity/single-sign-on|Single Sign-On]] — SSO routes through the IdP
- [[wiki/identity/mfa-patterns|MFA Patterns]] — IdPs enforce factor requirements
- [[wiki/identity/openid-connect|OpenID Connect]] — modern IdP-to-RP protocol
- [[wiki/security/ldap|LDAP]] — directory backend many IdPs use
- [[wiki/identity/hardware-security-keys|Hardware Security Keys]] — authenticators IdPs support
- [[wiki/identity/smartcards|Smartcards]] — enterprise credential form for IdP login
- [[wiki/security/mfa|Multi-Factor Authentication]] — factor enforcement at the IdP
- [[wiki/concepts/identity-system|RSIS3 Identity System]] — RSIS3's own identity provider role
