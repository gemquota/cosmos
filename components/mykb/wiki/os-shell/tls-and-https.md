---
type: "concept"
title: "TLS & HTTPS"
description: "Handshake, certificates, and encryption basics"
tags: ["tls", "https", "certificates", "crypto", "handshake"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://www.rfc-editor.org/rfc/rfc8446", "https://man7.org/linux/man-pages/man1/openssl.1.html"]
---

# TLS & HTTPS

## Summary
Transport Layer Security encrypts and authenticates traffic between clients and servers. HTTPS is HTTP running inside TLS on port 443, and the protocol's handshake negotiates keys, verifies certificates, and establishes forward-secret session keys.

## Details
- TLS 1.3 handshake: ClientHello with key shares, ServerHello, server certificate and signature, then finished messages — one round trip for the key exchange.
- Cipher suites name the algorithms: key exchange (ECDHE), authentication (RSA/ECDSA), bulk cipher (AES-GCM, ChaCha20), and hash (SHA-256).
- Certificates: a chain from the server's leaf up to a trusted CA; clients verify signatures, validity dates, and hostname via SAN.
- Perfect forward secrecy with ECDHE means compromising a server's long-term key does not decrypt past sessions.
- Session resumption uses PSKs/tickets so repeat connections skip the full handshake.
- SNI (Server Name Indication) carries the hostname in plaintext, letting one IP serve many certificates; ECH encrypts it.
- Tooling: openssl s_client -connect shows the chain and cipher; certbot automates Let's Encrypt issuance and renewal.

## Related
- [[wiki/os-shell/http-basics|HTTP Basics]] — the protocol TLS wraps
- [[wiki/security/tls|TLS]] — the security perspective
- [[wiki/security-auth/digital-certificates|Digital Certificates]] — the PKI underneath
- [[wiki/identity/client-certificates|Client Certificates]] — mutual TLS in the other direction
- [[wiki/security/certbot|Certbot]] — automated certificate lifecycle
