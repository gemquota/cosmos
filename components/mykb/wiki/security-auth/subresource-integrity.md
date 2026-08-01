---
type: "concept"
title: "Subresource Integrity"
description: "Hash-based verification that fetched scripts and styles have not been altered"
tags: ["sri", "integrity", "cdns", "browsers"]
timestamp: "2026-08-01T00:00:00Z"
status: "stub"
source: ["https://developer.mozilla.org/en-US/docs/Web/Security/Subresource_Integrity"]
---

# Subresource Integrity

- Subresource integrity (SRI) pins the cryptographic hash of a script or style so the browser refuses content that does not match.
- It protects against CDN compromise and supply-chain tampering of third-party assets.
- SRI requires hashes that change on every asset update, so it works best with versioned builds.
- For mykb: any third-party browser assets (fonts, analytics, libraries) should ship with SRI hashes.

## Related

- [[wiki/security-auth/content-security-policy|Content Security Policy]] — complementary browser control
- [[wiki/security/supply-chain-security|Software Supply Chain Security]] — defense against tampered dependencies
- [[wiki/security/sbom|SBOM]] — inventorying third-party assets
- [[wiki/security-auth/security-headers|Security Headers]] — header hardening stack
- [[wiki/security-auth/digital-certificates|Digital Certificates]] — integrity verification family
