---
type: "concept"
title: "mTLS"
description: "Mutual TLS for service-to-service authentication"
tags: ["mtls", "tls", "authentication", "certificates", "service-to-service"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://www.cloudflare.com/learning/access-management/what-is-mutual-tls/", "https://linkerd.io/2.16/features/automatic-mtls/"]
---

# mTLS

## Summary
Mutual TLS (mTLS) extends the TLS handshake so both sides present and validate certificates: the client authenticates the server, and the server authenticates the client. It is the standard for service-to-service authentication inside clusters and meshes, replacing shared secrets and IP allowlists with cryptographic identity.

## Details
- Handshake difference: the server requests a client certificate (CertificateRequest); the client sends its cert chain, which the server validates before the handshake completes.
- Identity: the client's certificate subject or SAN becomes the caller identity (for example spiffe://cluster/ns/payments/svc/processor) that authorization checks use.
- Deployment: provision client certs per workload (SPIFFE/SPIRE, cert-manager, or mesh auto-injection) and rotate them on a schedule — never share one key across services.
- Where it shines: east-west traffic in Kubernetes, database connections, and anything where IP-based trust is spoofable.
- Costs and caveats: certificate lifecycle management, clock skew breaking validation, and performance overhead per connection (mitigated by session resumption).
- Not a silver bullet: mTLS authenticates the connection, not the user — pair it with application authorization for real access control.
- Meshes automate it: Istio and Linkerd issue and rotate per-workload certs transparently, making mTLS the default for mesh traffic.

## Related
- [[wiki/api-protocols/tls-handshake|TLS Handshake]] — mTLS is TLS with client authentication
- [[wiki/api-protocols/tls-certificates|TLS Certificates]] — the X.509 chains both sides validate
- [[wiki/api-protocols/service-mesh|Service Mesh]] — meshes automate mTLS at scale
- [[wiki/security-auth/certificate-pinning|Certificate Pinning]] — strict validation beyond CA trust
- [[wiki/security-auth/microsegmentation|Microsegmentation]] — mTLS underpins zero-trust segmentation
