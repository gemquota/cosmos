---
type: "entity"
title: "WCAG"
description: "Principles, guidelines, and conformance levels for accessibility"
tags: [accessibility", "wcag", "standards", "a11y", "compliance"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://www.w3.org/WAI/WCAG22/", "https://www.w3.org/WAI/standards-guidelines/wcag/"]
---

# WCAG

## Summary
The Web Content Accessibility Guidelines are the W3C's standard for making web content usable by people with disabilities. WCAG 2.2 organizes requirements into four principles — perceivable, operable, understandable, robust — and assigns each success criterion a conformance level from A to AAA. Most regulations and procurement policies reference AA conformance.

## Details
- Principles: perceivable (alternatives, adaptability, distinguishable), operable (keyboard, timing, seizures, navigation), understandable (readable, predictable, input assistance), robust (compatible, parsable).
- Levels: A is the essential baseline, AA is the legal and procurement norm, AAA is an enhanced target for specific content.
- WCAG 2.2 additions: focus not obscured, focus appearance, dragging alternatives, and target size minimums reflect modern interfaces.
- Conformance: pages claim conformance per level and technology; WCAG 2.1/2.2 remain stable while WCAG 3.0 is drafted around outcome-based testing.
- Relationship to law: EN 301 549, ADA, and Section 508 incorporate WCAG by reference.
- Practice: audit against criteria, fix highest-impact failures first, and verify with automated plus manual testing.

## Related
- [[wiki/frontend/aria|ARIA]] — the semantics layer complementing WCAG
- [[wiki/frontend/color-contrast|Color Contrast]] — a core AA criterion
- [[wiki/frontend/keyboard-navigation|Keyboard Navigation]] — the operable principle in practice
- [[wiki/frontend/accessibility-testing|Accessibility Testing]] — verifying conformance
- [[wiki/frontend/screen-readers|Screen Readers]] — assistive tech WCAG addresses
- [[wiki/web-platforms/web-accessibility|Web Accessibility]] — platform context for the guidelines
