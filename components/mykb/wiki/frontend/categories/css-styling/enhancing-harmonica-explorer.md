---
type: "entity"
title: "Enhancing Harmonica Explorer"
description: "Harmonica Explorer"
tags: ["entity", "api", "ast", "bug", "cli", "css"]
timestamp: "2026-07-19T22:41:44Z"
resource: ""
status: "growing"
---

## Enhancing Harmonica Explorer

Harmonica Explorer — a music exploration project for touchscreen devices. Allows sliding between notes with chromatic sequencing.

Enhancing the Harmonica Explorer means improving an interactive musical instrument that runs on touchscreen devices. The core interaction is sliding between notes: instead of discrete buttons, the player drags a finger across a playing surface and the instrument responds with continuous or stepped pitch changes. Chromatic sequencing arranges the notes so that adjacent positions are one semitone apart, giving the player access to the full twelve-note scale and making the slide gesture musically predictable.

Enhancement work in the sessions spanned several layers. On the interaction side, touch handling must distinguish slide gestures from taps, apply smoothing to avoid jitter, and map screen coordinates to frequencies or note indices consistently. On the audio side, the Web Audio API generates tones, and the harmonic content, envelope, and volume of each note determine how the instrument feels. Latency is the critical constraint: any delay between finger movement and sound breaks the sense of playing an instrument.

On the styling side, CSS and canvas rendering create the playing surface, note indicators, and visual feedback such as glow or highlight while a note is held. Accessibility matters too: larger hit areas, visual contrast, and an alternative input path make the instrument usable beyond ideal conditions. The project family is documented across related pages including [[wiki/frontend/categories/css-styling/gesture-harmonics|Gesture Harmonics]], [[wiki/frontend/categories/css-styling/hold-mode|Hold Mode]], and [[wiki/frontend/categories/css-styling/saving-harmonica-explorer|Saving Harmonica Explorer]].

Future sessions should extend this page with the specific enhancements implemented and the measurements taken before and after. That measurement-first approach keeps enhancements grounded in observed behavior rather than assumptions.

**Related topics:** api, bug, cli, css

**Domain:** Web Platforms › [[wiki/web-platforms/00-index|Frontend]] › [[wiki/web-platforms/00-index|Css Styling]]

## Related Entities

- [[wiki/frontend/categories/css-styling/importerro|Importerror 10]]
- [[wiki/frontend/categories/css-styling/cs|Css 10]]
- [[wiki/frontend/categories/css-styling/complete-reference-2|Complete Reference 2]]
- [[wiki/frontend/categories/css-styling/database-2|Database 2]]
- [[wiki/frontend/categories/css-styling/display-2|Display 2]]
- [[wiki/frontend/categories/css-styling/htm|Html 10]]
- [[wiki/frontend/categories/css-styling/reference-2|Reference 2]]
- [[wiki/frontend/categories/css-styling/dob-2|Dob 2]]
