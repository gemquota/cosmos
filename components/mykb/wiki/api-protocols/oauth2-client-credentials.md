---
type: "concept"
title: "Client Credentials"
description: "Machine-to-machine OAuth grant"
tags: ["oauth2", "client-credentials", "m2m", "service-accounts", "tokens"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://www.rfc-editor.org/rfc/rfc6749#section-4.4", "https://auth0.com/docs/get-started/apis/grant-client-credentials"]
---

# Client Credentials

## Summary
The client credentials grant lets a service authenticate as itself — no user involved. The client POSTs its client_id and client_secret (or mTLS) to the token endpoint and receives an access token representing the application, used for machine-to-machine API calls with scopes scoped to the service's own permissions.

## Details
- Flow: token endpoint request with grant_type=client_credentials plus client_id/client_secret (or private_key_jwt / mTLS); response is an access token with a scope claim.
- Identity: the token represents the client application (a service account), not a user; resource servers authorize by client identity and scopes.
- Use cases: backend-to-backend calls, cron jobs, service accounts, and API integrations where no user consent applies.
- Scopes: consent is administrator-granted rather than user-granted; scopes like api:read, jobs:write limit what the machine identity may do.
- Security: protect client secrets like passwords (secret managers), rotate them, and prefer mTLS or signed JWTs over shared secrets for high-assurance systems.
- Token lifetime: access tokens are short-lived; renew by requesting again — no refresh token in this grant.
- Audience: request an audience/resource parameter so the token is bound to the target API.

## Related
- [[wiki/api-protocols/oauth2|OAuth 2.0]] — the framework this grant belongs to
- [[wiki/api-protocols/api-keys|API Keys]] — the simpler predecessor for machine calls
- [[wiki/api-protocols/oauth2-scopes|OAuth Scopes]] — permission granularity for service accounts
- [[wiki/api-protocols/mtls|mTLS]] — stronger client authentication for the grant
- [[wiki/api-protocols/json-web-tokens|JWT]] — the access token format often used
