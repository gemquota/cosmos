---
type: "concept"
title: "TLS"
description: "Transport Layer Security: the cryptographic protocol encrypting and authenticating internet traffic"
tags: ["tls", "cryptography", "https", "security", "networking"]
timestamp: "2026-07-31T00:00:00Z"
status: "stub"
---

# TLS

## Summary
TLS (Transport Layer Security) encrypts and authenticates traffic between clients and servers. It is the foundation of HTTPS, mTLS service meshes, and secure API calls.

## Details
- Handshake negotiates cipher suite, exchanges keys (ECDHE), and verifies certificates via the PKI chain.
- TLS 1.3 removed legacy ciphers and shortened handshakes; TLS 1.2 remains widely supported.
- mTLS extends it to mutual authentication — central to zero-trust and service meshes.

## Related
- [[wiki/security/https|HTTPS]] — TLS in the browser
- [[wiki/security/cipher-suites|Cipher Suites]] — algorithm negotiation
- [[wiki/security/certbot|Certbot]] — certificate automation
- [[wiki/security/lets-encrypt|Let's Encrypt]] — free CA
- [[wiki/devops-infra/istio|Istio]] — mTLS at the mesh
- [[wiki/security/zero-trust|Zero Trust Architecture]] — encrypt everything
