---
type: "concept"
title: "Clickjacking Defense"
description: "Frame-busting headers that prevent invisible overlay attacks"
tags: ["security", "web", "headers", "attacks"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---
# Clickjacking Defense

## Summary
Clickjacking tricks users into clicking invisible framed UI by overlaying a victim page inside an attacker's page. Defense is frame-busting at the protocol level with X-Frame-Options or the CSP frame-ancestors directive.

## Details
Clickjacking (UI redressing) embeds a victim site in a transparent or disguised iframe and positions a decoy button over it. The user believes they are clicking the decoy but actually clicks the victim's button — approving a payment, granting OAuth consent, toggling admin settings. The attack needs no vulnerability in the victim beyond being framable.

The mechanism: the browser renders the iframe only if the victim allows framing. Two mechanisms control this: X-Frame-Options: DENY / SAMEORIGIN / ALLOW-FROM (legacy) and the CSP directive frame-ancestors 'none' | 'self' | <origins>, which supersedes X-Frame-Options in modern browsers. The browser compares the ancestor origins against the policy and refuses to render the frame when they don't match. frame-ancestors does not affect top-level navigation, only embedding.

Concrete example: an OAuth authorization page without framing protection can be embedded under an attacker page with a transparent overlay; the user clicks "Play" and unknowingly approves token access. Setting frame-ancestors 'none' (or SAMEORIGIN if same-origin embedding is needed) blocks it. The same protection must apply to admin panels, payment confirmations, and password change forms — anything with a high-value button.

Failure modes: JavaScript frame-busting (if top != self) is unreliable — sandboxed iframes, sandbox without allow-top-navigation, and X-Frame-Options support gaps all defeat it; ALLOW-FROM was never widely supported, so it must not be relied on; and forgetting the CSP header on non-HTML responses or only setting X-Frame-Options on some routes leaves pockets of exposure. Double-click or confirm dialogs are mitigation, not defense.

Operational tradeoffs: frame-ancestors is stricter and more expressive than X-Frame-Options and should be the primary control, with X-Frame-Options retained for legacy browsers (both can be set; frame-ancestors wins where supported). Sites that legitimately embed widgets need an explicit allowlist — and that allowlist is itself attack surface if any listed origin is attacker-controllable.

RSIS3/mykb relevance: the unified dashboard embeds mykb and SPACE views same-origin; its framing policy is a concrete case of the SAMEORIGIN choice and a reusable example for security reviews.

## Related
- [[wiki/api-protocols/web-security-owasp|Web Security (OWASP)]]
- [[wiki/api-protocols/iframe-sandboxing|iframe Sandboxing]]
- [[wiki/api-protocols/popup-security|Popup Security]]
- [[wiki/api-protocols/cors|CORS]]
- [[wiki/security-auth/security-headers|Security Headers]]
- [[wiki/security-auth/content-security-policy|Content Security Policy]]
