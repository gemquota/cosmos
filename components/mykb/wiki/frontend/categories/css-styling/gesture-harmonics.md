---
status: "growing"
type: "entity"
title: "Gesture Harmonics"
description: "Gesture Harmonics"
tags: ["entity", "api", "ast", "bug", "cli", "css"]
timestamp: "2026-07-19T22:41:43Z"
resource: ""
---

## Gesture Harmonics

A touchscreen musical instrument project allowing sliding between notes with chromatic sequencing. Appears in agent sessions involving interactive music visualization and sound generation.

**Domain:** Web Platforms › [[wiki/web-platforms/00-index|Frontend]] › [[wiki/web-platforms/00-index|Css Styling]]

## Overview

Gesture Harmonics is an interactive instrument where touch position controls pitch. Rather than discrete keys, it maps continuous finger movement onto a chromatic scale, letting the player slide between notes with glissando-like transitions while retaining quantized, musical steps. Sessions involving the project pair it with visualization of the sound and real-time synthesis.

## Interaction Design

- Touch position on a two-dimensional surface maps to pitch and intensity.
- Sliding gestures traverse chromatic steps, giving both precision and expressive portamento.
- Visual feedback — glow, waveform, or note trails — reinforces the mapping between gesture and sound.

## Audio and Rendering

- Synthesis typically uses oscillators, gain envelopes, and effects chains in the browser Web Audio API.
- Low-latency handling of touch events keeps the instrument responsive; samples are scheduled ahead of time.
- The visualization layer renders waveforms or note grids in sync with the audio clock.

## Session Context

- The project appears in agent sessions that combine interactive music and visualization, so the instrument is exercised as both a sound engine and a drawing surface.
- Sessions iterate on responsiveness: touch latency, scheduling ahead of the audio clock, and frame pacing all affect how playable the instrument feels.
- Refinements typically alternate between the audio graph and the visual layer, keeping the two in sync rather than treating them independently.

## Related Concepts

- [[wiki/frontend/categories/frontend-frameworks/subcategories/ajax-spa/retroaudio|RetroAudio]] — companion audio experiments
- [[wiki/frontend/categories/frontend-frameworks/subcategories/ajax-spa/drumsynth|DrumSynth]] — related sound synthesis work
- [[wiki/web-platforms/web-apis|Web APIs]] — browser interfaces behind synthesis and input
- [[wiki/frontend/animation-performance|Animation Performance]] — keeping the visual layer smooth

## Related Entities

- [[wiki/frontend/categories/css-styling/importerror|Importerror 10]]
- [[wiki/frontend/categories/css-styling/css|Css 10]]
- [[wiki/frontend/categories/css-styling/complete-reference-2|Complete Reference 2]]
- [[wiki/frontend/categories/css-styling/database-2|Database 2]]
- [[wiki/frontend/categories/css-styling/display-2|Display 2]]
- [[wiki/frontend/categories/css-styling/html|Html 10]]
- [[wiki/frontend/categories/css-styling/reference-2|Reference 2]]
- [[wiki/frontend/categories/css-styling/dob-2|Dob 2]]
