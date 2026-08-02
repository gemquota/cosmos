---
type: "concept"
title: "Accessibility Testing"
description: "Verifying WCAG compliance and assistive-technology usability"
tags: ["accessibility", "testing", "wcag", "inclusive-design"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://www.w3.org/WAI/test-evaluate/", "https://developer.chrome.com/docs/lighthouse/accessibility"]
---

# Accessibility Testing

## Summary
Accessibility testing verifies that products work for people with disabilities, covering WCAG success criteria across perceivable, operable, understandable, and robust principles. It combines automated checks, manual testing, and assistive-technology validation.

## Details
- Standards: WCAG 2.x levels A and AA, with WAI-ARIA for rich components.
- Automated tools: axe-core, Lighthouse accessibility audits, and WAVE catch a fraction of issues.
- Manual testing: keyboard-only operation, contrast review, focus order, and screen reader passes.
- Include disabled users in testing; automated tools cannot judge usability.
- Test early: accessibility is a design constraint, not a QA afterthought.
- Common issues: missing labels, low contrast, keyboard traps, and non-semantic markup.
- Enforce via CI gates and design-system component tests.

## Related
- [[wiki/testing/screen-reader-testing|Screen Reader Testing]] — assistive-technology validation
- [[wiki/web-platforms/web-accessibility|Web Accessibility]] — platform view of WCAG
- [[wiki/testing/ui-testing|UI Testing]] — behavioral UI checks with accessibility
- [[wiki/testing/ci-quality-gates|CI Quality Gates]] — automated accessibility gates
- [[wiki/testing/compatibility-testing|Compatibility Testing]] — assistive tech across browsers
- [[wiki/testing/component-testing|Component Testing]] — role assertions in component tests
