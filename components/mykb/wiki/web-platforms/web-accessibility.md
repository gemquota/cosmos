---
type: "concept"
title: "Web Accessibility"
description: "Designing and building websites so people with disabilities can perceive, operate, and understand them"
tags: ["accessibility", "a11y", "wcag", "inclusion"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://www.w3.org/WAI/fundamentals/accessibility-intro/"]
---

# Web Accessibility

## Summary
Web accessibility means designing sites so that people with disabilities — visual, auditory, motor, cognitive — can use them. The W3C's Web Accessibility Initiative defines the standards: WCAG, WAI-ARIA, and the authoring/ATAG guidelines.

## Details
- WCAG organizes requirements under four principles: Perceivable, Operable, Understandable, Robust (POUR), with A/AA/AAA conformance levels.
- Core practices: semantic HTML, alt text, keyboard operability, sufficient color contrast, and focus management.
- WAI-ARIA supplements HTML with roles and properties for complex widgets, but native elements come first: 'no ARIA is better than bad ARIA'.
- Accessibility benefits everyone: captions help noisy environments, keyboard support helps power users, clear contrast helps daylight reading.
- Testing mixes automation (axe) with manual checks: keyboard-only navigation and screen-reader passes.
- RSIS3 relevance: any dashboard the agent or human uses should pass basic a11y checks to be reliably operable.
- Worked example: a button implemented as <button> inherits focus and Enter/Space handling for free.

## Related
- [[wiki/web-platforms/web-standards|Web Standards]] — a11y requirements are standards-track
- [[wiki/web-platforms/web-components|Web Components]] — custom elements must expose accessible semantics
- [[wiki/web-platforms/dom-manipulation|DOM Manipulation]] — ARIA roles live on DOM nodes
- [[wiki/security/rbac|RBAC]] — permission clarity is an accessibility concern too
- [[wiki/testing/entities/test-patterns|Testing Patterns]] — a11y checks belong in the test suite
- [[wiki/concepts/cognitive-load|Cognitive Load]] — accessible design reduces cognitive load
- [[wiki/memory/information-architecture|Information Architecture]] — clear structure is an a11y win
