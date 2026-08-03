---
type: "concept"
title: "Popup Security"
description: "window.opener, popup abuse, and how noopener breaks the link"
tags: ["security", "web", "popups", "attacks"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---
# Popup Security

## Summary
Popup security covers two directions: pages that open popups controlling or being controlled by the opener, and popups used to abuse user trust (fake dialogs, phishing chrome). The core mechanism is window.opener, which rel="noopener" and the COOP header sever.

## Details
When a page opens another via window.open or a target=_blank link, the new page gets a reference to the opener via window.opener. If the opened page is cross-origin, it cannot read the opener's DOM or storage, but it can navigate the opener — window.opener.location = 'https://evil.example/phish' — turning a link-click into a silent redirect of the original tab. That reverse-tabnabbing attack is the canonical popup security bug.

The mechanism: rel="noopener noreferrer" on links and {noopener: true} in window.open strip the opener reference, so the new page cannot navigate the old one. Browsers now default target=_blank links to noopener. The Cross-Origin-Opener-Policy (COOP) header generalizes this at the document level: same-origin isolates the browsing context group so cross-origin windows lose the opener relationship entirely.

Concrete example: a wiki page links to a third-party site with target=_blank but no rel. The third-party site's script runs window.opener.location = 'https://evil.example/fake-login'. The victim returns to what looks like the wiki, sees a login form, and enters credentials on the attacker's page. With rel="noopener", the opener reference doesn't exist and the attack fails.

Failure modes: relying on popup blockers to protect users (they only stop unwanted popups, not tabnabbing); window.open from cross-origin contexts creating opener chains that COOP: same-origin can break; and phishing-style popups (fake dialogs using window.alert or styled overlays) that no header prevents — user education and careful UI are the mitigations. Also, popups that must communicate with the opener (OAuth flows) use postMessage with origin validation, never direct references.

Operational tradeoffs: adding rel="noopener" to every external link and defaulting to noopener in window.open is zero-cost and should be a lint rule; COOP: same-origin is stricter but can break popup-based OAuth flows that rely on opener access, so those flows must switch to postMessage. The baseline: noopener on all external navigations, COOP where popup flows allow, and postMessage with origin checks for any real cross-window communication.

RSIS3/mykb relevance: the dashboard's external links and any popup-based auth must follow the noopener rule; documenting it lets RSIS3's checks scan link attributes.

## Related
- [[wiki/api-protocols/web-security-owasp|Web Security (OWASP)]]
- [[wiki/api-protocols/clickjacking-defense|Clickjacking Defense]]
- [[wiki/api-protocols/iframe-sandboxing|iframe Sandboxing]]
- [[wiki/api-protocols/cors|CORS]]
- [[wiki/security-auth/security-headers|Security Headers]]
- [[wiki/security-auth/content-security-policy|Content Security Policy]]
