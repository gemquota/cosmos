---
type: "concept"
title: "Accessibility Testing"
description: "Automated and manual a11y checks"
tags: [accessibility", "testing", "a11y", "wcag", "qa"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://developer.mozilla.org/en-US/docs/Learn/Tools_and_testing/Cross_browser_testing/Accessibility", "https://www.w3.org/WAI/test-evaluate/"]
---

# Accessibility Testing

## Summary
Accessibility testing verifies that interfaces work for people with disabilities. Automated tools like axe and Lighthouse catch a large subset of issues — missing labels, contrast failures, invalid ARIA — while manual checks cover keyboard flows, screen readers, and zoom. The two complement each other: automation finds rules, humans find experience.

## Details
- Automated scans: axe rules run in browsers, CI, and test runners; Lighthouse audits score common WCAG criteria.
- Keyboard testing: tab through every flow, verify visible focus, and check skip links and focus traps.
- Screen reader testing: NVDA, VoiceOver, or TalkBack with real flows — automation cannot judge announced experience.
- Content checks: zoom to 200-400%, forced colors, reduced motion, and text-only rendering expose layout fragility.
- WCAG audits: map findings to success criteria with severity and retest after fixes.
- In CI: axe in unit/E2E suites plus scheduled full audits catch regressions before merge.

## Related
- [[wiki/frontend/wcag|WCAG]] — the criteria being tested
- [[wiki/frontend/aria|ARIA]] — semantics under test
- [[wiki/frontend/keyboard-navigation|Keyboard Navigation]] — a core manual check
- [[wiki/frontend/screen-readers|Screen Readers]] — assistive-tech verification
- [[wiki/frontend/frontend-testing|Frontend Testing]] — automated a11y in the stack
- [[wiki/web-platforms/web-accessibility|Web Accessibility]] — the discipline
