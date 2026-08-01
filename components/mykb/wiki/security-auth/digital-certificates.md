---
type: "concept"
title: "Digital Certificates"
description: "Signed X.509 data structures binding a public key to an identity with validity constraints"
tags: ["certificates", "x509", "pki", "cryptography"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://www.rfc-editor.org/rfc/rfc5280"]
---

# Digital Certificates

## Summary

A digital certificate is a signed data structure that binds a public key to an identity. RFC 5280 defines the X.509 certificate format: version, serial number, issuer, subject, validity period, public key, extensions, and the issuing CA's signature. Certificates matter because they turn bare public keys into trustworthy identities: a verifier checks the signature chain and constraints rather than taking the key on faith. RSIS3 meets certificates everywhere — TLS server certs, code signing, and client certs for service identities — so reading them correctly is core competence.

## Details

- Structure: tbsCertificate carries subject, issuer, validity, public key, and extensions; the signatureAlgorithm and signature bind them together.
- Extensions: subject alternative names (SAN) carry hostnames; key usage and extended key usage constrain what the key may do; basic constraints mark CAs.
- Validation: build the chain to a trusted root, check validity times, verify signatures, confirm the SAN matches the hostname, and consult revocation (CRL/OCSP).
- Lifecycle: issuance by a CA, renewal before expiry (short-lived certs via ACME), and revocation for compromise or misuse.
- Common pitfalls: self-signed certs accepted silently, hostname mismatch, expired chains, and weak signature algorithms (SHA-1, RSA-1024).
- For mykb, certificate validation should live in one library so every service checks chains the same way.

## Related

- [[wiki/security-auth/public-key-infrastructure|Public Key Infrastructure]] — the system that issues and manages certificates
- [[wiki/security-auth/certificate-pinning|Certificate Pinning]] — pinning as defense against CA mis-issuance
- [[wiki/identity/client-certificates|Client Certificates]] — certificates used for authentication
- [[wiki/security/tls|TLS]] — certificates authenticate TLS servers
- [[wiki/security/lets-encrypt|Let's Encrypt]] — automated issuance of certificates
- [[wiki/security/certbot|Certbot]] — client tool for ACME issuance
- [[wiki/devops-infra/nginx|Nginx]] — serving certificates at the edge
