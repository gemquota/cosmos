---
type: "concept"
title: "iframe Sandboxing"
description: "The sandbox attribute that strips embedded frames of privileges"
tags: ["security", "web", "iframe", "headers"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---
# iframe Sandboxing

## Summary
The iframe sandbox attribute runs embedded content with restricted privileges: no scripts, no forms, no popups, no same-origin access — unless explicitly re-enabled. It is the browser's containment primitive for untrusted embeds.

## Details
<iframe sandbox="..."></iframe> applies a restrictive default policy to the framed document: scripts are blocked, forms cannot submit, popups are blocked, plugins and pointer-lock are disabled, and the frame is treated as a unique opaque origin so it cannot access the parent or its own cookies. Each capability is re-granted individually with tokens: allow-scripts, allow-forms, allow-popups, allow-same-origin, allow-top-navigation, and others.

The mechanism: the sandbox is enforced by the browser's navigation and capability checks. The unique-origin default is the critical part: without allow-same-origin, the framed page cannot read cookies or storage for its real origin, so even a compromised embed can't exfiltrate parent-domain state. The combination allow-scripts plus allow-same-origin is the dangerous one — it recreates a normal same-origin iframe, so the two should never be used together for untrusted content.

Concrete example: a dashboard embeds a third-party chart widget in <iframe sandbox="allow-scripts allow-popups"></iframe>. The widget's scripts run (needed for rendering), but it cannot submit forms, open the parent, or reach the dashboard's cookies (opaque origin). If the widget is compromised, the blast radius is the widget's own frame. Hosting untrusted HTML without any sandbox would give the embed the parent's origin if same-origin, or at least full browsing capability.

Failure modes: adding allow-same-origin to untrusted embeds re-opens cookie theft; allow-top-navigation lets the embed redirect the whole page (phishing); a missing allow-scripts can silently break legitimate embeds (confusing debugging); and sandboxed frames that need their own storage (localStorage) fail unless allow-same-origin is granted — the exact tradeoff that tempts developers into the unsafe combination.

Operational tradeoffs: sandboxing is cheap and layered: sandbox the frame, add CSP frame-ancestors to control who embeds you, and treat allowlist decisions as security review items. The baseline for untrusted embeds: no allow-same-origin, scripts only when required, and a documented list of every token granted. For your own widgets, sandbox plus an explicit origin contract is still safer than none.

RSIS3/mykb relevance: the dashboard embeds mykb and SPACE views; if those embeds ever load third-party content, the sandbox token list is the standing contract to document and enforce.

## Related
- [[wiki/api-protocols/web-security-owasp|Web Security (OWASP)]]
- [[wiki/api-protocols/popup-security|Popup Security]]
- [[wiki/api-protocols/clickjacking-defense|Clickjacking Defense]]
- [[wiki/api-protocols/cors|CORS]]
- [[wiki/security-auth/security-headers|Security Headers]]
- [[wiki/security-auth/content-security-policy|Content Security Policy]]
