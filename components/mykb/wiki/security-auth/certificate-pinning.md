---
type: "concept"
title: "Certificate Pinning"
description: "Hard-coding expected certificates or public keys to defeat CA mis-issuance"
tags: ["pinning", "certificates", "tls", "defense"]
timestamp: "2026-08-01T00:00:00Z"
status: "stub"
source: ["https://owasp.org/www-community/controls/Certificate_and_Public_Key_Pinning"]
---

# Certificate Pinning

- Pinning binds a client to a specific certificate or public key, rejecting anything else even if a CA mis-issues.
- The OWASP guidance warns pinning is brittle: expired pins break production, and rigid pins hurt rotation.
- Modern practice prefers short-lived certificates and strict chain validation over long-term pinning, except in high-risk native clients.
- For mykb: pinning belongs in mobile/native clients for privileged operations, with remote updateable pin sets.

## Related

- [[wiki/security-auth/digital-certificates|Digital Certificates]] — the certificates being pinned
- [[wiki/security-auth/public-key-infrastructure|Public Key Infrastructure]] — the trust system pinning supplements
- [[wiki/identity/key-rotation|Key Rotation]] — pins complicate rotation
- [[wiki/security/tls|TLS]] — the protocol pins apply to
