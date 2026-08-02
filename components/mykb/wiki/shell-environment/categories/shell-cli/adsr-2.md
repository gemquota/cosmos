---
type: "entity"
status: "growing"
title: "ADSR"
description: "Acronym referenced in session 019ebd47"
tags: ["acronym", "android", "api", "ast", "auth", "aws", "bash", "cli", "entity"]
timestamp: "2026-07-19T22:41:39Z"
resource: ""
---

## Adsr 2

ADSR — Attack, Decay, Sustain, Release. An envelope model in sound synthesis.

**Related topics:** android, api, auth, aws, bash, cli

**Domain:** Mobile Platform › [[wiki/web-platforms/index|Android Core]] › [[wiki/web-platforms/supercategories/shell-environment/categories/shell-cli/index|Shell Cli

## Overview

ADSR is a four-stage amplitude envelope used in sound synthesis to shape how a note's volume changes over time. The acronym stands for Attack, Decay, Sustain, Release, and it defines the contour of every synthesized sound — from a plucked string to a drum hit. A synth without an envelope would click or drone; with one, each note has a perceivable beginning, body, and end.

## The Four Stages

- Attack: the time the signal takes to rise from silence to its peak level. Fast attacks sound percussive; slow attacks produce swelling, pad-like textures.
- Decay: the time to fall from the peak to the sustain level. Short decays give plucky sounds; long decays create resonant tails.
- Sustain: the level held while the note is pressed, not a time value — it only applies while the key or gate is held.
- Release: the time to fall from the sustain level to silence after the note ends. Long releases leave a lingering ring-out.

## In Practice

Envelopes are implemented as gain control signals: an `AudioParam` or a voltage that modulates the oscillator or noise source. In Web Audio, a scheduling pattern chains `linearRampToValueAtTime` (or exponential ramps) across the four stages against the audio clock. In MIDI and hardware synths, the envelope is triggered by note-on and note-off gates. ADSR parameters are among the most expressive knobs on an instrument: the same oscillator can sound like a kick, a marimba, or a string pad purely by changing its envelope.

## CLI and Scripting Context

The entity is tagged with shell and CLI terms, so ADSR also appears in command-line audio tools and generative scripts: parameters passed as `--attack`, `--decay`, `--sustain`, `--release`, or encoded in a synthesis config, letting shell pipelines render one-shots and loops deterministically. The acronym note originally referenced session 019ebd47 and is now resolved to the standard synthesis meaning, while remaining useful to any session that synthesizes or analyzes audio.

## Related Entities

- [[wiki/web-platforms/supercategories/shell-environment/categories/shell-cli/abbreviated-activity-history-2|Abbreviated Activity History 2
- [[wiki/web-platforms/supercategories/shell-environment/categories/shell-cli/beautifulsoup4-2|Beautifulsoup4 2
- [[wiki/web-platforms/supercategories/shell-environment/categories/shell-cli/bpm-10|Bpm 10
- [[wiki/web-platforms/supercategories/shell-environment/categories/shell-cli/cellsystem|Cellsystem
- [[wiki/web-platforms/supercategories/shell-environment/categories/shell-cli/cs-2|Cs 2
- [[wiki/web-platforms/supercategories/shell-environment/categories/shell-cli/cellstate|Cellstate
- [[wiki/web-platforms/supercategories/shell-environment/categories/shell-cli/deterministicrng|Deterministicrng
- [[wiki/web-platforms/supercategories/shell-environment/categories/shell-cli/genefunction|Genefunction
