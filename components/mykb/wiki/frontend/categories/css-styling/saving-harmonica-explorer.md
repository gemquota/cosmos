---
type: "entity"
title: "Saving Harmonica Explorer"
description: "Harmonica Explorer"
tags: ["entity", "api", "ast", "bug", "cli", "css"]
timestamp: "2026-07-19T22:41:43Z"
resource: ""
status: "growing"
---

## Saving Harmonica Explorer

Harmonica Explorer is a music exploration project for touchscreen devices. Its defining interaction lets a user slide between notes with chromatic sequencing: instead of tapping discrete keys, the user glides across a continuous surface and the app selects notes along the chromatic scale, producing smooth runs and bends that resemble playing a real harmonica.

The chromatic scale is the core musical idea. Twelve semitones span each octave, and sequencing through them in order gives the full chromatic run, while skipping steps produces the diatonic scales and melodies familiar from most music. A touchscreen maps naturally to this: horizontal position selects the pitch, vertical position can control breath or bend, and the continuous surface makes glissando — the slide between notes — effortless to perform.

Exploration is the point of the project. Because there are no wrong notes in the same sense as a fixed-key instrument, users can wander through scales and discover melodies, and the app can highlight the current scale, show note names, or record what was played. Saving is part of that loop: the explorer lets users save snippets, sessions, or settings so that a good discovery is not lost when the app closes.

Such a project exercises the whole frontend stack: pointer handling for the slide gesture, Web Audio or the platform audio API for sound, state management for notes and saves, and CSS styling for the visual layout. The related entities below record the neighboring frontend pages observed in the same sessions, giving the project a place in the wider vocabulary of the knowledge base.



Saving also raises the state questions every interactive app faces: what to persist, where to store it, and how to restore it on launch. Session history, recorded snippets, and user preferences each have different storage needs, from in-memory lists to local storage to backend sync. The explorer's saving feature turns it from a toy into a tool, because users can revisit and build on what they discovered.
**Related topics:** api, bug, cli, css

**Domain:** Web Platforms › [[wiki/web-platforms/index|Frontend]] › [[wiki/web-platforms/index|Css Styling]]

## Related Entities

- [[wiki/frontend/categories/css-styling/importerror-10|Importerror 10]]
- [[wiki/frontend/categories/css-styling/css-10|Css 10]]
- [[wiki/frontend/categories/css-styling/complete-reference-2|Complete Reference 2]]
- [[wiki/frontend/categories/css-styling/database-2|Database 2]]
- [[wiki/frontend/categories/css-styling/display-2|Display 2]]
- [[wiki/frontend/categories/css-styling/html-10|Html 10]]
- [[wiki/frontend/categories/css-styling/reference-2|Reference 2]]
- [[wiki/frontend/categories/css-styling/dob-2|Dob 2]]
