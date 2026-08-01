---
type: "concept"
title: "SAML Assertions"
description: "XML statements issued by identity providers that carry authentication, attribute, and authorization data"
tags: ["saml", "assertions", "xml", "sso", "federation"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://docs.oasis-open.org/security/saml/v2.0/saml-core-2.0-os.pdf"]
---

# SAML Assertions

## Summary

SAML 2.0 is an XML-based framework for exchanging identity and attribute data between an identity provider (IdP) and service providers (SPs). Its core artifact is the assertion: a signed XML document stating that a subject was authenticated at a certain time, holds certain attributes, or is authorized for certain actions. SAML remains the enterprise workhorse for web browser SSO, especially in universities, governments, and legacy stacks, even as OIDC wins new deployments. Understanding assertions matters because nearly every legacy federation contract RSIS3 might integrate with speaks SAML.

## Details

- Assertion types: authentication statements (subject was authenticated by method X at time T), attribute statements (subject has attributes A, B), and authorization decision statements.
- Structure: assertions contain Issuer, Signature, Subject (NameID + confirmation), Conditions (audience, validity window), and Advice; they are transported by protocols (AuthnRequest/Response) and bindings (Redirect, POST, Artifact).
- Profiles: the Web Browser SSO Profile is the dominant flow; the ECP profile serves non-browser clients; metadata XML describes SPs and IdPs for trust configuration.
- Security: assertions are XML-signed (XMLDSIG); unsigned or weakly parsed assertions are a classic source of SSO bypass vulnerabilities, alongside XXE in metadata processing.
- SAML vs OIDC: SAML is XML + POST/Redirect bindings + enterprise metadata; OIDC is JSON + HTTPS + simpler clients; both achieve the same federation goal.
- For mykb, SAML support means parsing and validating signed assertions, checking conditions and audiences, and mapping NameID to RSIS3 identity records.

## Related

- [[wiki/identity/single-sign-on|Single Sign-On]] — SAML is a primary SSO protocol
- [[wiki/identity/identity-federation|Identity Federation]] — SAML assertions are the currency of federation
- [[wiki/security-auth/xml-external-entities|XML External Entities]] — SAML and metadata parsers are XXE surfaces
- [[wiki/security/saml|SAML]] — existing article on SAML 2.0
- [[wiki/security/oauth2|OAuth 2.0]] — the modern alternative to SAML
- [[wiki/security-auth/ldap-injection|LDAP Injection]] — legacy directory integration often pairs with SAML
- [[wiki/concepts/identity-system|RSIS3 Identity System]] — mapping federated NameIDs into local identities
