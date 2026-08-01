---
type: "concept"
title: "TLS Encryption"
description: "Transport Layer Security: encrypted, authenticated channels between clients and servers"
tags: ["tls", "encryption", "https", "cryptography", "rfc"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://www.rfc-editor.org/rfc/rfc8446"]
---

# TLS Encryption

## Summary

Transport Layer Security (TLS) provides confidential and authenticated communication over TCP. TLS 1.3 (RFC 8446) is the current standard: a handshake negotiates cipher suites and keys, the server proves its identity with a certificate, and all application data flows encrypted with forward-secret keys. TLS matters because it is the security floor for everything else: tokens, passwords, API calls, and federation assertions are only as safe as the channel they travel on. Every mykb service boundary — web UI, API, sync, federation — should be TLS 1.2+ with strong cipher suites.

## Details

- Handshake: ClientHello/ServerHello negotiate protocol version and cipher suite; key exchange (ECDHE in TLS 1.3) produces ephemeral keys, giving forward secrecy; certificates authenticate the server.
- TLS 1.3 changes: removed legacy ciphers and RSA key exchange, added 0-RTT resumption, reduced round trips to one, and hardened the handshake.
- Cipher suites: AEAD encryption (AES-GCM, ChaCha20-Poly1305) with ECDHE key exchange are the modern minimum.
- Certificate validation: clients verify the chain to a trusted root, check hostname (SAN), and respect revocation.
- Mutual TLS: both sides present certificates, enabling service-to-service authentication without shared secrets.
- Operational concerns: certificate lifecycle (renewal via ACME/Lets Encrypt), protocol downgrade attacks, and cipher suite configuration drift.
- For RSIS3, TLS plus mTLS between internal services is the transport half of zero trust; tokens and policies are the other half.

## Related

- [[wiki/security-auth/digital-certificates|Digital Certificates]] — the identity layer inside TLS
- [[wiki/security-auth/certificate-pinning|Certificate Pinning]] — extra validation for high-risk clients
- [[wiki/security/tls|TLS]] — existing article on TLS
- [[wiki/security/https|HTTPS]] — HTTP over TLS
- [[wiki/security/cipher-suites|Cipher Suites]] — the algorithms TLS negotiates
- [[wiki/security/lets-encrypt|Let's Encrypt]] — automated certificate issuance
- [[wiki/identity/client-certificates|Client Certificates]] — mTLS uses client-side certificates
- [[wiki/concepts/triad-architecture|Triad Architecture]] — encrypted channels between triad components
