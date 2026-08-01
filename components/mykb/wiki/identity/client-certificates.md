---
type: "concept"
title: "Client Certificates"
description: "X.509 certificates presented by clients for mutual TLS authentication"
tags: ["client-certificates", "mtls", "pki", "authentication"]
timestamp: "2026-08-01T00:00:00Z"
status: "stub"
source: ["https://cheatsheetseries.owasp.org/cheatsheets/Transport_Layer_Protection_Cheat_Sheet.html"]
---

# Client Certificates

- Client certificates authenticate the client to the server during the TLS handshake, creating mutual TLS (mTLS).
- They give machines and services cryptographically strong identities without shared secrets.
- Operational cost: certificate issuance, renewal, and revocation for every client require real PKI discipline.
- mTLS pairs naturally with service meshes and zero-trust architectures.
- For mykb: mTLS between internal triad services is stronger than long-lived bearer tokens and worth evaluating.

## Related

- [[wiki/security-auth/digital-certificates|Digital Certificates]] — the certificates clients present
- [[wiki/security-auth/public-key-infrastructure|Public Key Infrastructure]] — the PKI that issues client certs
- [[wiki/security-auth/tls-encryption|TLS Encryption]] — mTLS is TLS with client authn
- [[wiki/security/zero-trust|Zero Trust Architecture]] — mTLS as a zero-trust control
