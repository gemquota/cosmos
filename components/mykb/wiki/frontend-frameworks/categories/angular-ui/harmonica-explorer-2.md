---
type: "entity"
title: "Harmonica Explorer"
status: "growing"
description: "Harmonica Explorer"
tags: ["android", "angular", "api", "ast", "aws", "bug", "cli", "css", "entity"]
timestamp: "2026-07-19T22:41:40Z"
resource: ""
---

## Harmonica Explorer 2

Harmonica Explorer — a music exploration project for touchscreen devices. Allows sliding between notes with chromatic sequencing.

**Related topics:** android, angular, api, aws, bug, cli, css

**Domain:** Mobile Platform › [[wiki/mobile-platform/supercategories/android-core/index|Android Core]] › [[wiki/web-platforms/supercategories/frontend-frameworks/categories/angular-ui/index|Angular Ui

## Overview

Harmonica Explorer is a music exploration project designed for touchscreen devices, letting users slide between notes with chromatic sequencing. Such an instrument UI maps a physical layout — harmonica holes and reeds — onto a touch grid, where horizontal movement advances through the chromatic scale and vertical position selects draw vs blow or octave. The project combines audio synthesis, gesture handling, and responsive layout.

## Design Notes

- Chromatic sequencing means adjacent slots differ by one semitone, so the layout must prevent accidental double-triggers between neighbors.
- Touch gestures need debouncing and slide tracking: press, drag, and release each map to note onset, bend, and offset.
- Latency is critical: the audio engine must respond within a few milliseconds of the touch event for a playable feel.
- The UI adapts across phone and tablet sizes, which ties into the mobile tags on the entity.

## Related Concepts

- [[wiki/web-platforms/web-apis|Web APIs]] — audio and touch capabilities in the browser
- [[wiki/mobile-platform/adaptive-layouts|Adaptive Layouts]] — responsive instrument surfaces
- [[wiki/web-platforms/component-architecture|Component Architecture]] — separating the note grid from the audio engine


## Example

Dragging a finger across the screen moves the active note one semitone per grid column; lifting the finger ends the note, and sliding vertically switches between blow and draw rows. A subtle haptic or visual tick confirms each step, making the chromatic sequence learnable without sheet music.


## Related Concepts

- [[wiki/web-platforms/web-performance-optimization|Web Performance Optimization]] — keeping audio under the latency budget
- [[wiki/security/secrets-management|Secrets Management]] — no secrets involved, but asset licensing and attribution belong in the project metadata


## Related Entities

- [[wiki/web-platforms/supercategories/frontend-frameworks/categories/angular-ui/aim-2|Aim 2
- [[wiki/web-platforms/supercategories/frontend-frameworks/categories/angular-ui/autonomous-iterative-mode-2|Autonomous Iterative Mode 2
- [[wiki/web-platforms/supercategories/frontend-frameworks/categories/angular-ui/avg-age-2|Avg Age 2
- [[wiki/web-platforms/supercategories/frontend-frameworks/categories/angular-ui/avg-energy-2|Avg Energy 2
- [[wiki/web-platforms/supercategories/frontend-frameworks/categories/angular-ui/batch-2|Batch 2
- [[wiki/web-platforms/supercategories/frontend-frameworks/categories/angular-ui/dna-10|Dna 10
- [[wiki/web-platforms/supercategories/frontend-frameworks/categories/angular-ui/hidpi-2|Hidpi 2
- [[wiki/web-platforms/supercategories/frontend-frameworks/categories/angular-ui/hud-2|Hud 2
