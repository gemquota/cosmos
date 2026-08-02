---
type: "concept"
title: "TLS Handshake"
description: "TLS basics, versions, and cipher suites"
tags: ["tls", "handshake", "encryption", "security", "protocols"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://www.rfc-editor.org/rfc/rfc8446", "https://developer.mozilla.org/en-US/docs/Web/Security/Transport_Layer_Security"]
---

# TLS Handshake

## Summary
TLS is the encryption layer under HTTPS, gRPC, and WebSockets. The handshake negotiates the protocol version, cipher suite, and keys — using certificates for authentication — before any application bytes flow. TLS 1.3 (RFC 8446) streamlined this to one round trip with forward secrecy by default.

## Details
- The job: authenticate the server (and optionally client), negotiate cryptographic parameters, and establish session keys for symmetric bulk encryption.
- TLS 1.3 handshake: ClientHello -> ServerHello + certificate + finished -> client finished; 1-RTT total, with 0-RTT resumption via session tickets.
- Cipher suites: TLS_AES_128_GCM_SHA256 and TLS_AES_256_GCM_SHA384 (ChaCha20 for mobile); TLS 1.3 removed weak algorithms (CBC, RSA key exchange, static DH).
- Forward secrecy: ephemeral key exchange (ECDHE) means compromising the server's long-term key cannot decrypt past sessions.
- Certificate authentication: the server presents an X.509 chain; the client validates signatures, expiry, and hostname against the CA trust store.
- TLS 1.2 still in service: ECDHE-RSA-AES128-GCM-SHA256 etc.; retire TLS 1.0/1.1 (formally deprecated) to pass compliance scans.
- Termination points: TLS often ends at a load balancer or CDN (edge termination), with optional re-encryption to origins.

## Related
- [[wiki/api-protocols/tls-certificates|TLS Certificates]] — the X.509 material the handshake validates
- [[wiki/api-protocols/mtls|mTLS]] — client certificates in the handshake
- [[wiki/security-auth/tls-encryption|TLS Encryption]] — the security-practice view
- [[wiki/api-protocols/quic|QUIC]] — TLS 1.3 integrated into the transport
- [[wiki/api-protocols/http3|HTTP/3]] — the web protocol built on QUIC+TLS
