---
type: "concept"
title: "API Basic Auth"
description: "Base64 username:password credentials sent in the Authorization header"
tags: ["http", "auth", "api", "security"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---
# API Basic Auth

## Summary
HTTP Basic authentication sends base64(user:password) in the Authorization header. It is simple and universally supported, but it is only safe over TLS and has no native logout or credential scoping.

## Details
Basic auth (RFC 7617) puts base64-encoded "username:password" in the Authorization header: Authorization: Basic dXNlcjpwYXNz. Base64 is not encryption — anyone who sees the header can decode it instantly — so TLS is mandatory on every hop. The server responds 401 with WWW-Authenticate: Basic realm="..." to prompt clients that have not sent credentials.

The mechanism: every request carries the full credential pair, which means no session state server-side, trivially replayable traffic if TLS fails, and credentials embedded in logs, proxies, and browser history when people paste URLs like https://user:pass@host/. Most server frameworks auto-decode and compare against a user store, and many support constant-time comparison to blunt timing side channels.

Concrete example: a CI script calling a private wiki export endpoint uses a dedicated service account with a long random password: curl -u "svc-export:$(cat ~/.secrets/export)" https://wiki.internal/export. That is a reasonable use — machine-to-machine, low value, TLS-only. A customer-facing SaaS login is not: there is no standard way to revoke a leaked credential short of changing the password, no scope limiting, and no MFA hook.

Failure modes: sending basic auth over plain HTTP leaks credentials to any observer and any transparent proxy; embedding credentials in URLs leaks them into access logs and referrer headers; and reusing a human password as the API secret makes a database breach cascade. Brute force is also cheap, so rate limiting and lockout are mandatory if basic auth is exposed to the internet.

Operational tradeoffs: basic auth is the lowest-friction option for scripts, cron jobs, and legacy integrations because every HTTP client supports it; but it lacks refresh tokens, scopes, and revocation, so its total cost of ownership rises with user count. The upgrade path is API keys for scripts and OAuth2/OIDC for humans, often via a compatibility shim that maps basic credentials onto the same token backend.

RSIS3/mykb relevance: when RSIS3 automations call mykb's .wiki-daemon API, the credential pattern — dedicated token, TLS, no URL embedding — is the standing practice to encode in synthesis notes.

## Related
- [[wiki/api-protocols/auth-flows-web|Auth Flows on the Web]] — related coverage in the same cluster
- [[wiki/api-protocols/api-digest-auth|API Digest Auth]] — related coverage in the same cluster
- [[wiki/api-protocols/bearer-tokens|Bearer Tokens]] — related coverage in the same cluster
- [[wiki/api-protocols/m2m-tokens|Machine-to-Machine Tokens]] — related coverage in the same cluster
- [[wiki/api-protocols/api-authentication-methods|API Authentication Methods]] — related coverage in the same cluster
- [[wiki/api-protocols/api-keys|API Keys]] — related coverage in the same cluster
- [[wiki/api-protocols/basic-authentication|Basic Authentication]] — related coverage in the same cluster
