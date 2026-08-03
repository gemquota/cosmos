---
type: "concept"
title: "X-Frame-Options"
description: "Legacy header that prevents a page from being embedded in frames"
tags: ["security", "http", "headers", "clickjacking"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---
# X-Frame-Options

## Summary
X-Frame-Options is the legacy HTTP response header that tells browsers whether a page may be embedded in a frame or iframe. It was the original defense against clickjacking — the attack where a transparent, malicious page sits on top of a framed target and tricks users into clicking buttons they cannot see — and it remains widely sent even though Content Security Policy's `frame-ancestors` is the modern replacement.

## Details
- Mechanism: the header takes two values: `DENY`, which forbids any framing, and `SAMEORIGIN`, which allows framing only by the same origin. The browser enforces it when the page is loaded inside a frame, refusing to render the framed document if the embedding context violates the policy. `frame-ancestors` in CSP does the same job with more expressiveness — it can list multiple allowed origins, including specific hosts and schemes — and the two interact in a quirky way: browsers that support both apply the stricter of the two, and `frame-ancestors` wins when they conflict.
- Concrete examples: a login page sends `X-Frame-Options: DENY` so a phishing site cannot frame it inside a fake banking shell; an admin console sends `SAMEORIGIN` so the app's own iframe-based layouts still work while external sites cannot embed it; a widget provider deliberately omits the header and instead uses CSP `frame-ancestors https://allowed.example` so only its partner sites can embed the widget. CSP `frame-ancestors` can also be set to `'none'` for the same effect as DENY.
- Failure modes: sending only X-Frame-Options means modern browsers get coarse protection, but the header has known quirks: it is ignored inside `<iframe>` for top-level documents in some legacy flows, it cannot express multi-origin allowlists, and it is a no-op when the browser only checks CSP. Clickjacking also has non-frame vectors (like `window.open` and pop-under overlays) that neither header covers. The compatibility trap is the reverse: some older browsers ignore `frame-ancestors`, which is why many sites still send both headers.
- Operational tradeoffs: sending `X-Frame-Options: SAMEORIGIN` plus a matching CSP `frame-ancestors 'self'` covers legacy and modern browsers simultaneously and is essentially free; the cost only appears when a product legitimately needs embedding, which then requires a carefully scoped `frame-ancestors` allowlist and testing of every embedding partner. For internal tools and auth pages, deny-all framing is the safe default, and security scanners should flag pages that embed sensitive surfaces without either control.
- RSIS3/mykb relevance: the MyKB and RSIS3 dashboards are embedded in the unified dashboard; defining which origins may frame them (self-only, plus the deployment origin) is a standing security posture, and the header choice is a small, durable part of the platform's hardening checklist.

## Related
- [[wiki/api-protocols/web-security-owasp|Web Security (OWASP)]] — related coverage in the same cluster
- [[wiki/api-protocols/mime-sniffing|MIME Sniffing]] — related coverage in the same cluster
- [[wiki/api-protocols/nosniff-header|X-Content-Type-Options nosniff]] — related coverage in the same cluster
- [[wiki/api-protocols/hsts-practice|HSTS in Practice]] — related coverage in the same cluster
- [[wiki/security-auth/security-headers|Security Headers]] — related coverage in the same cluster
- [[wiki/security-auth/content-security-policy|Content Security Policy]] — related coverage in the same cluster
- [[wiki/security-auth/same-origin-policy|Same-Origin Policy]] — related coverage in the same cluster
