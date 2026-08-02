---
type: "concept"
title: "Speech Synthesis on the Web"
description: "The SpeechSynthesis API: text-to-speech voices, rates, and browser differences"
tags: ["speech", "tts", "web", "api", "accessibility"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://developer.mozilla.org/en-US/docs/Web/API/SpeechSynthesis", "https://developer.mozilla.org/en-US/docs/Web/API/Web_Speech_API"]
---
# Speech Synthesis on the Web

## Summary
The Web Speech API's SpeechSynthesis interface turns text into spoken audio using platform voices. It is useful for accessibility, notifications, and reading aids. Voice availability, quality, and behavior differ significantly across browsers and OSes.

## Details
- **Basics** — `speechSynthesis.speak(new SpeechSynthesisUtterance(text))`; options set voice, rate, pitch, and volume.
- **Voices** — `getVoices()` lists available voices; loading is async; pick voices defensively.
- **Quirks** — Chrome historically pauses long utterances and has a max-length bug; cancel before speaking new text.
- **Alternatives** — remote TTS (cloud APIs) offers better voices at network and cost trade-offs.
- **Worked example** — the mykb reader offers a "read aloud" toggle for articles using local synthesis with graceful degradation.
- **Relevance** — RSIS3's spoken-status features should degrade cleanly where local voices are absent.
- **Content pacing** — long texts benefit from sentence chunking and pause marks; SSML-like control is absent in the web API, so the app splits text into utterances with callbacks.

## Related
- [[wiki/web-platforms/i18n-web|Web Internationalization]] — adjacent concept in this wiki
- [[wiki/web-platforms/locale-data|Locale Data]] — adjacent concept in this wiki
- [[wiki/web-platforms/message-formatting|Message Formatting]] — adjacent concept in this wiki
- [[wiki/web-platforms/plural-rules|Plural Rules]] — adjacent concept in this wiki
- [[wiki/web-platforms/web-apis|Web APIs]] — existing coverage
- [[wiki/web-platforms/web-accessibility|Web Accessibility]] — existing coverage
- [[wiki/web-platforms/browser-engines|Browser Engines]] — existing coverage
