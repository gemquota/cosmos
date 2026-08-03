---
type: "concept"
title: "Issuer Validation"
description: "Checking the iss claim so tokens from the wrong issuer are rejected"
tags: ["jwt", "security", "claims", "api"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---
# Issuer Validation

## Summary
The iss (issuer) claim names which authorization server minted a token. Validating it against a trusted allowlist stops tokens minted by an attacker's server — or a different tenant's server — from being accepted.

## Details
In JWT and OIDC terms, iss is a URL or identifier identifying the issuer — the authorization server that created and signed the token. The resource server must compare iss against its configured trusted issuers and reject anything else. Without this check, a token minted by any server whose signing key the verifier trusts (or that can be made to look trusted) passes validation.

The mechanism: the check is part of the standard claim-validation suite alongside aud, exp, nbf, and iat. The verifier pins a list of accepted issuers per environment (https://auth.example.com for prod, a different URL for staging) and rejects tokens whose iss is not in the list. This matters most in multi-tenant and federated setups, where one signing infrastructure serves many issuers, and in testing environments where a dev IdP's keys can accidentally be trusted in production.

Concrete example: a service validates JWTs with a JWKS fetched from https://auth.example.com/jwks. An attacker sets up their own IdP at https://evil.example.com, gets it to sign a token with a role=admin claim, and presents it. If the verifier checks signature against the configured JWKS but never checks iss, the attacker's token is rejected only if the signature check uses the right key — but in a confused configuration (shared keys, or a jku header pointing at the attacker's key), iss validation is the last line that stops it. Pinning iss plus pinned JWKS URL plus allowed algorithms is the complete fix.

Failure modes: treating iss as optional (lenient libraries); accepting any https URL as an issuer without an allowlist; and trusting iss without verifying that the signing key actually belongs to that issuer — the claim and the key must be bound together, which is what OIDC discovery and JWKS kid validation provide. Regex-based issuer matching can be bypassed with lookalike URLs.

Operational tradeoffs: strict issuer allowlists complicate multi-issuer migrations (both issuers must be listed during cutover) and test setups, but the cost is small compared with the risk of cross-issuer token acceptance. The baseline: per-environment issuer allowlist, mandatory iss check, and the same strictness applied to audience and algorithm.

RSIS3/mykb relevance: RSIS3's token validation checklist should include "iss pinned per environment"; documenting the allowlist here gives the loop a concrete configuration to verify.

## Related
- [[wiki/api-protocols/jwt-practice|JWT in Practice]] — related coverage in the same cluster
- [[wiki/api-protocols/introspection-endpoint|Token Introspection]] — related coverage in the same cluster
- [[wiki/api-protocols/jwks-rotation|JWKS Rotation]] — related coverage in the same cluster
- [[wiki/api-protocols/jti-claims|JWT ID Claims]] — related coverage in the same cluster
- [[wiki/api-protocols/json-web-tokens|JWT]] — related coverage in the same cluster
- [[wiki/api-protocols/oauth2-scopes|OAuth Scopes]] — related coverage in the same cluster
- [[wiki/identity/jwks|JWKS]] — related coverage in the same cluster
