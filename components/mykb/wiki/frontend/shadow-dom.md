---
type: "concept"
title: "Shadow DOM"
description: "Encapsulated DOM subtrees isolating styles and structure"
tags: [shadow-dom", "web-components", "encapsulation", "css", "browser"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://developer.mozilla.org/en-US/docs/Web/API/Web_components/Using_shadow_DOM", "https://dom.spec.whatwg.org/#shadow-trees"]
---

# Shadow DOM

## Summary
Shadow DOM attaches a private subtree to a host element. Styles declared inside the shadow tree do not leak out, and page styles do not leak in, which gives components true encapsulation. It is one of the three pillars of web components, alongside custom elements and HTML templates.

## Details
- Attachment: element.attachShadow({mode: "open"}) creates the tree; closed mode hides internals from script but limits testing.
- Scoping: selectors and CSS rules inside a shadow root cannot match outside elements, eliminating class collisions.
- Inheritance still applies: inheritable properties such as color and font cascade into shadow content, which keeps theming possible.
- Composition: slots project light-DOM children into the shadow tree, letting consumers pass in their own markup.
- Styling hooks: ::part() exposes chosen internals to page CSS, and custom properties pierce encapsulation deliberately.
- Use cases: design-system components, widgets embedded in hostile CSS environments, and framework-agnostic UI elements.

## Related
- [[wiki/frontend/web-components|Web Components]] — the standard Shadow DOM is part of
- [[wiki/frontend/dom-api|DOM API]] — node model shadow trees extend
- [[wiki/frontend/css-custom-properties|CSS Custom Properties]] — theming that works through encapsulation
- [[wiki/frontend/theming|Theming]] — styling shadow roots from outside
- [[wiki/web-platforms/web-components|Web Components]] — platform notes on the full spec
- [[wiki/frontend/css-cascade-specificity|CSS Cascade and Specificity]] — what encapsulation bypasses
