---
type: "concept"
title: "touch-action CSS"
description: "Declaring how browser touch gestures may manipulate an element"
tags: ["css", "touch", "gestures", "web"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---
# touch-action CSS

## Summary

touch-action declares which default touch behaviors (pan, pinch-zoom) the browser may perform on an element, letting JavaScript take over gestures like drag-and-drop and custom swipes without fighting the browser.

## Details
- Mechanism: touch-action: none disables all default touch handling on the element, so pointer events reach the app unimpeded; pan-x/pan-y and pinch-zoom allow subsets; manipulation is the recommended default for interactive UI (it disables double-tap zoom while keeping pan/zoom).
- Concrete example: a draggable map or slider sets touch-action: none so horizontal drags are not hijacked by vertical page scroll; a horizontally scrollable carousel uses pan-y (vertical page scroll still works); a button uses manipulation so double-tap zoom does not misfire.
- Failure modes: touch-action: none on a scrollable area breaks scrolling entirely (users cannot pan); forgetting pan-y on a horizontal gesture surface makes it impossible to scroll past it vertically; interactions with pointer events require also handling mouse/pen input consistently; and iframes/hybrid apps have their own touch gesture handling that can conflict.
- Operational tradeoffs: allowing default behaviors keeps accessibility and native feel (scroll, zoom); restricting them enables custom gestures at the cost of reimplementing what the browser provides. Use the narrowest restriction (pan-y, not none) and test with touch devices, trackpads, and mouse drag.
- RSIS3/mykb relevance: the OKF graph's drag-pan and zoom gestures use touch-action rules documented here so loop-generated interactive viewers inherit correct gesture behavior.
- Browser defaults: the UA applies its own touch-action defaults (pan/zoom) on the document; explicit declarations on interactive surfaces make intent visible and testable.
- Interaction with pointer capture: combining touch-action with setPointerCapture gives robust drag gestures; release capture on pointerup to keep subsequent taps behaving normally.
- Gesture synthesis: when touch-action: none is in play, implement equivalent mouse and keyboard paths; touch users are not the only ones who need the gesture to work.

## Related
- [[wiki/web-platforms/touch-gestures|Touch Gestures]]
- [[wiki/web-platforms/pointer-events-css|pointer-events CSS]]
- [[wiki/web-platforms/css-layout|CSS Layout]]
- [[wiki/web-platforms/web-accessibility|Web Accessibility]]
- [[wiki/android-core/gesture-input|Gesture Input]]
