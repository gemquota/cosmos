---
type: "concept"
title: "Mutual TLS for Internal Services"
description: "mTLS identity verification between services using client certificates"
tags: ["mtls", "security", "service-mesh", "certificates"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---
# Mutual TLS for Internal Services

## Summary

Mutual TLS (mTLS) authenticates both ends of a connection: the client presents a certificate too, so the server knows exactly who is calling. It is the standard for internal service-to-service security, removing the password-in-config anti-pattern and enabling identity-based authorization.

## Details
- Mechanism: TLS with client-certificate request: the server sends a CertificateRequest, the client proves possession of its key, and both sides verify chains; identity comes from the certificate's subject (or SPIFFE ID in a mesh). Service meshes (Istio, Linkerd) automate issuance/rotation via mTLS between sidecars; raw mTLS means running your own CA and PKI.
- Concrete example: a payment service accepts connections only from clients presenting certificates signed by the internal CA, replacing a shared API token; a mesh rotates certificates automatically, so a compromised credential expires quickly; a database requires mTLS from app servers, blocking credential reuse elsewhere.
- Failure modes: CA/key management failures taking down all services (the CA is now the crown jewel — protect and rotate); certificate rotation without client updates breaking connections (use SPIFFE-style short-lived certs); SAN/subject mismatches causing validation failures; and mTLS giving a false sense of security when authorization still keys off insecure claims.
- Operational tradeoffs: mTLS buys strong identity and defense-in-depth at PKI operational cost; a mesh automates it but adds infrastructure; raw mTLS is fine for small, stable service counts. Keep the CA offline/HSM-backed, rotate signing keys, and test revocation paths.
- RSIS3/mykb relevance: the wiki's internal APIs enforce mTLS from a dedicated CA; this note records the CA layout and rotation runbook the loop's certificate automation follows.
- Revocation path: define what happens when a client certificate is compromised — CRL/OCSP or short-lived certs with fast expiry; without a revocation story, mTLS is a false promise. Exercise the revocation path in staging before relying on it during an incident.

## Related
- [[wiki/cloud-infra/https-and-tls|HTTPS & TLS]]
- [[wiki/cloud-infra/tls-1-3-session-resumption|TLS 1.3 Session Resumption]]
- [[wiki/cloud-infra/tls-performance|TLS Performance]]
- [[wiki/os-shell/tcp-ports-and-services|TCP Ports & Services]]
- [[wiki/cloud-infra/networking-fundamentals|Networking Fundamentals]]
