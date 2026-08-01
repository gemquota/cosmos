---
type: "concept"
title: "Web Components"
description: "The standard-based way to create reusable UI components with custom elements and shadow DOM"
tags: ["web-components", "custom-elements", "shadow-dom", "standards"]
timestamp: "2026-08-01T00:00:00Z"
status: "stub"
---

# Web Components

## Summary
Web Components are the browser-native component system: custom elements define new tags, shadow DOM encapsulates styles and structure, and templates/HTML imports provide reusable markup. No framework required.

## Details
- Custom elements give lifecycle hooks (connectedCallback, attributeChangedCallback).
- Shadow DOM isolates styles, which is both power and a pitfall for global theming.
- RSIS3 relevance: framework-independent widgets can be shared across any dashboard.

## Related
- [[wiki/web-platforms/component-architecture|Component Architecture]] — Web Components are the standards implementation
- [[wiki/web-platforms/web-standards|Web Standards]] — custom elements are standardized
- [[wiki/web-platforms/web-accessibility|Web Accessibility]] — custom elements need explicit a11y semantics
- [[wiki/web-platforms/web-frameworks|Web Frameworks]] — frameworks can consume Web Components
- [[wiki/testing/golden-tests|Golden Tests]] — custom elements are golden-testable
