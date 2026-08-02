---
type: "concept"
title: "API Keys"
description: "Key issuance, usage, and limitations"
tags: ["api-keys", "authentication", "secrets", "api-security", "tokens"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://stripe.com/docs/keys", "https://cloud.google.com/docs/authentication/api-keys"]
---

# API Keys

## Summary
API keys are opaque strings that identify a caller: X-API-Key: <key> or a query parameter. They are the easiest credential to issue and embed, making them the default for developer platforms — but they are shared secrets with no user context, limited scoping, and a habit of leaking, so treat them as identification, not strong security.

## Details
- Issuance: servers generate high-entropy keys (32+ random bytes), store only a hash, and return the plaintext once; rotation invalidates the old key.
- Usage: sent in an X-API-Key header or query param; header beats query (query keys leak into logs and history).
- Limitations: keys are not user-bound, cannot express scopes or expiry cleanly, and are trivially shareable — one leaked key compromises the whole account.
- Mitigations: prefix keys by environment (sk_live_, pk_test_), support per-key rate limits and IP allowlists, and add secret scanning to catch leaks.
- OAuth comparison: API keys suit simple server-to-server and developer access; OAuth 2.0 adds delegation, scopes, and user consent.
- Logging: never log full keys — redact to the last 4 characters; ensure the key header is excluded from request logs.
- Storage: consumers must keep keys in environment variables or secret managers, not in client code or public repos.

## Related
- [[wiki/api-protocols/api-authentication-methods|API Authentication Methods]] — where keys fit in the taxonomy
- [[wiki/api-protocols/oauth2-client-credentials|Client Credentials]] — the OAuth machine-to-machine upgrade path
- [[wiki/api-protocols/rate-limit-algorithms|Rate Limit Algorithms]] — per-key quotas are the standard usage pattern
- [[wiki/api-services/secret-scanning|Secret Scanning]] — detecting leaked keys in code
- [[wiki/api-services/api-key-management|API Key Management]] — lifecycle, rotation, and storage
