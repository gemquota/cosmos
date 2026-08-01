---
type: "concept"
title: "Identity Federation"
description: "Trust relationships that let identity assertions be accepted across organizational and technical boundaries"
tags: ["federation", "trust", "saml", "oidc", "identity"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://pages.nist.gov/800-63-3/sp800-63c.html"]
---

# Identity Federation

## Summary

Identity federation is the establishment of trust that lets one organization's identity provider authenticate users and have that authentication accepted by another organization's applications. The IdP asserts identity; the relying party validates the assertion against shared trust material. NIST SP 800-63C covers federation and assertion levels, including how federations should convey IAL, AAL, and attribute information without leaking private data. Federation matters to RSIS3 because agents and humans will cross many trust domains: mykb, SaaS APIs, dev environments, and partner systems.

## Details

- Trust mechanics: RPs trust IdPs through metadata exchange (SAML metadata, OIDC discovery documents), signing keys (JWKS), and explicit issuer allowlists.
- Protocols: SAML 2.0 and OIDC are the two dominant federation protocols; OAuth delegation of scopes is the authorization analogue.
- Roles: IdP/OP issues assertions; RP/SP consumes them; brokers and proxy IdPs translate between protocols or aggregate multiple IdPs.
- Attribute release: federation only works when attributes (email, groups, entitlements) flow with the assertion; consent and attribute minimization are privacy controls.
- Risks: identity spoofing via metadata tampering, scope/attribute creep, and single-IdP concentration; FAL levels rate the strength of the assertion delivery.
- For mykb, federation policy should map external identities to internal subjects with provenance: which IdP asserted what, at what assurance level.

## Related

- [[wiki/identity/identity-providers|Identity Providers]] — the issuer side of federation
- [[wiki/identity/saml-assertions|SAML Assertions]] — XML assertions as the federation payload
- [[wiki/identity/openid-connect|OpenID Connect]] — JSON federation over OAuth 2.0
- [[wiki/security/sso|Single Sign-On]] — SSO is the user-facing result of federation
- [[wiki/security/saml|SAML]] — existing article on the SAML protocol
- [[wiki/security/jwt|JWT]] — ID token format carrying federated claims
- [[wiki/identity/oidc-clients|OIDC Clients]] — the relying parties in a federation
- [[wiki/identity/jwks|JWKS]] — key material exchanged for federation trust
- [[wiki/memory/provenance|Provenance]] — recording the source of asserted identity
