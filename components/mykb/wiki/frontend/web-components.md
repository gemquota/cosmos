---
type: "concept"
title: "Web Components"
description: "Custom elements, templates, and slots"
tags: [web-components", "custom-elements", "shadow-dom", "javascript", "standard"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://developer.mozilla.org/en-US/docs/Web/API/Web_components", "https://html.spec.whatwg.org/multipage/custom-elements.html"]
---

# Web Components

## Summary
Web Components are a set of browser standards for building reusable UI elements: custom elements define new tags, shadow DOM encapsulates internals, and templates plus slots define structure. They are framework-agnostic by design, which makes them ideal for design systems that must work across React, Vue, and plain HTML.

## Details
- Custom elements: class extends HTMLElement; customElements.define registers the tag; lifecycle callbacks fire on create and connect.
- Shadow DOM: scopes styles and markup; open mode is testable, closed mode maximizes isolation.
- Templates and slots: template holds inert markup; slots project light-DOM children into the component.
- Observable attributes: observedAttributes and attributeChangedCallback react to attribute changes without re-rendering.
- Interop: properties, attributes, and events form the public API; framework wrappers adapt them to JSX or templates.
- State: lit and other libraries add reactive properties; plain components manage state with callbacks and events.

## Related
- [[wiki/frontend/shadow-dom|Shadow DOM]] — the encapsulation pillar
- [[wiki/frontend/semantic-html|Semantic HTML]] — custom elements extend the vocabulary
- [[wiki/frontend/islands-architecture|Islands Architecture]] — components as islands
- [[wiki/web-platforms/web-components|Web Components]] — the platform-level article
- [[wiki/frontend/design-systems|Design Systems]] — cross-framework component distribution
- [[wiki/frontend/component-composition|Component Composition]] — composing from custom elements
