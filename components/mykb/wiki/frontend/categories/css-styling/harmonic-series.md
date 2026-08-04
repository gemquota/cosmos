---
type: "entity"
title: "Harmonic Series"
description: "Harmonic Series"
tags: ["entity", "api", "ast", "bug", "cli", "css"]
timestamp: "2026-07-19T22:41:43Z"
resource: ""
status: "growing"
---

## Harmonic Series

A music/audio theory concept related to harmonic sequences and sound generation. Connected to a touchscreen musical instrument development project.

The harmonic series is the sequence of frequencies that are integer multiples of a fundamental tone: f, 2f, 3f, 4f, and so on. The first few members dominate how we hear pitch and timbre. The second harmonic is an octave above the fundamental, the third is an octave and a fifth, and the fourth is two octaves; together these ratios explain why the octave, fifth, and fourth sound consonant across musical traditions.

Almost every pitched instrument produces a fundamental together with a spectrum of these overtones, and the relative loudness of each partial is what distinguishes a flute from a violin playing the same note. Synthesis exploits this directly: additive synthesis builds tones by summing sine waves at harmonic frequencies, and filtering, ring modulation, and FM techniques all shape the harmonic content of a generated sound. Understanding the series therefore matters for both analysis — reading a spectrum — and construction — choosing partials deliberately.

In the touchscreen musical instrument project, the harmonic series informs sound generation and tuning. Sliding between notes implies continuous frequency control, and chromatic sequencing places notes one semitone apart while the harmonic content gives each generated tone its character. A player expects octaves and fifths to feel related, which is exactly the structure the series provides.

Implementation on mobile uses the Web Audio API or native engines to create oscillators and shape their partials with filters and envelopes. Related project pages cover [[wiki/frontend/categories/css-styling/gesture-harmonics|Gesture Harmonics]] and the [[wiki/frontend/categories/css-styling/harmonica-harmonic-explorer|Harmonica Harmonic Explorer]], which carry the interaction details.

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
