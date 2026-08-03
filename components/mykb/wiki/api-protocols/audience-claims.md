---
type: "concept"
title: "Audience Claims"
description: "Verifying the aud claim so tokens minted elsewhere are rejected"
tags: ["jwt", "security", "claims", "api"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---
# Audience Claims

## Summary
The aud (audience) claim in a token names the intended recipient(s). Validating it stops token replay across services: a token minted for service A must be rejected by service B.

## Details
In OAuth2/OIDC and JWT terms, aud is a string or array naming the audience a token was issued for — typically the resource server's identifier (client_id or a service URL). When the resource server validates a token, it must check that its own identifier appears in aud; otherwise any service sharing the same issuer and signing key accepts tokens meant for another service.

The mechanism: the authorization server sets aud at mint time based on the client's requested scope or resource (RFC 8707 resource parameter, or OIDC's aud=client_id for ID tokens). The resource server compares its registered audience against the claim and rejects mismatches with 401 invalid_token. Without this check, an access token for the payments API works verbatim on the users API if both trust the same JWKS.

Concrete example: a single identity realm serves two APIs — wiki-api and graph-api — both validating with the same JWKS. A token issued with aud=wiki-api must 401 on graph-api. If graph-api skips the aud check, a leaked wiki token becomes a graph token. The fix is mandatory audience validation plus distinct audience identifiers per API.

Failure modes: treating aud as optional (libraries with lenient defaults) silently disables the protection; validating only the first element of an array when the server is the second breaks legitimate multi-audience tokens; and reusing the same audience string for multiple services recreates the cross-service replay hole. Also, clients should not be trusted to pick their audience — the server must pin it, or clients will mint tokens with aud=anything.

Operational tradeoffs: distinct audiences per service make validation precise but add registration overhead and complicate tokens that legitimately serve several services (arrays or wildcards, which are discouraged). The tradeoff is precision against operational complexity; the safe baseline is one audience per resource server, enforced, with a migration path when services merge.

RSIS3/mykb relevance: when RSIS3 adds a new API consumer, the checklist item "does the new service validate aud?" is the kind of durable rule that belongs in a synthesis note and check-practices.

## Related
- [[wiki/api-protocols/jwt-practice|JWT in Practice]] — related coverage in the same cluster
- [[wiki/api-protocols/issuer-validation|Issuer Validation]] — related coverage in the same cluster
- [[wiki/api-protocols/introspection-endpoint|Token Introspection]] — related coverage in the same cluster
- [[wiki/api-protocols/jwks-rotation|JWKS Rotation]] — related coverage in the same cluster
- [[wiki/api-protocols/json-web-tokens|JWT]] — related coverage in the same cluster
- [[wiki/api-protocols/oauth2-scopes|OAuth Scopes]] — related coverage in the same cluster
- [[wiki/identity/jwks|JWKS]] — related coverage in the same cluster
