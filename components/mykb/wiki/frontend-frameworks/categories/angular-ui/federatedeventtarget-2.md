---
type: "entity"
title: "FederatedEventTarget"
status: "growing"
description: "Referenced in session 019ed74e"
tags: ["android", "angular", "api", "ast", "auth", "aws", "bootstrap", "bun", "entity"]
timestamp: "2026-07-19T22:41:39Z"
resource: ""
---


## Federatedeventtarget 2

FederatedEventTarget appears in 4 session(s) categorized as API, Cloud, Frontend, Mobile, Security. Related topics: android, angular, api, auth, aws, bootstrap, bun.

**Domain:** Mobile Platform › [[wiki/android-core/00-index|Android Core]] › [[wiki/web-platforms/00-index|Angular Ui]]

## Overview

FederatedEventTarget refers to a federated event-dispatch model, most familiar from rendering frameworks such as PixiJS, where a single scene-level event system dispatches interactions (pointer, touch, keyboard) to display objects. It generalizes the DOM EventTarget contract to non-DOM scene graphs. Categorized under API, Cloud, Frontend, Mobile, and Security, the entity captures a pattern that appears in cross-platform UI work: one target tree, one event pipeline, consistent hit-testing.

## How It Works

- A root target receives raw input and performs hit-testing to find the object under the pointer.
- Events then propagate along the display list, mirroring DOM capture and bubble phases.
- Handlers attach to individual objects without each object owning a native event listener, which scales to thousands of nodes.
- The same abstraction lets desktop and mobile input share one code path.

## Related Concepts

- [[wiki/web-platforms/dom-manipulation|DOM Manipulation]] — the event model this pattern mirrors
- [[wiki/web-platforms/component-architecture|Component Architecture]] — object trees that receive events
- [[wiki/web-platforms/web-components|Web Components]] — encapsulation and event boundaries


## Practical Notes

- Hit-testing cost grows with scene complexity; spatial indexes or render-order culling keep pointer events fast.
- The federated model preserves capture/bubble semantics, so libraries that expect DOM-like behavior integrate cleanly.
- Testing focuses on hit-test correctness, propagation order, and `stopPropagation` behavior across nested objects.


## Example

A scene with a button, a draggable sprite, and a background registers one federated listener on the stage; pointer events hit-test through the object tree and bubble like DOM events. This single-listener design keeps the entity count low and the behavior consistent across desktop and touch input.


## Related Entities

- [[wiki/frontend-frameworks/categories/angular-ui/aim-2|Aim 2]]
- [[wiki/frontend-frameworks/categories/angular-ui/autonomous-iterative-mode-2|Autonomous Iterative Mode 2]]
- [[wiki/frontend-frameworks/categories/angular-ui/avg-age-2|Avg Age 2]]
- [[wiki/frontend-frameworks/categories/angular-ui/avg-energy-2|Avg Energy 2]]
- [[wiki/frontend-frameworks/categories/angular-ui/batch-2|Batch 2]]
- `Dna 10`
- [[wiki/frontend-frameworks/categories/angular-ui/harmonica-explorer-2|Harmonica Explorer 2]]
- [[wiki/frontend-frameworks/categories/angular-ui/hidpi-2|Hidpi 2]]
