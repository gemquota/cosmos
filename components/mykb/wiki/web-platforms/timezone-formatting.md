---
type: "concept"
title: "Timezone Handling"
description: "Converting, naming, and formatting instants across time zones"
tags: ["i18n", "timezones", "dates", "localization"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---
# Timezone Handling

## Summary

Timezone formatting is the display-timezone half of date handling: the same instant renders differently per viewer, per offset, and per daylight-saving rule. Getting it right means storing instants, choosing a display zone explicitly, and using Intl.

## Details
- Mechanism: instants are absolute (epoch ms); a timezone (IANA name like Europe/Berlin) converts an instant to a wall-clock with DST rules; Intl.DateTimeFormat with timeZone renders it. Offsets alone (+02:00) are not zones — they cannot express DST transitions, so historical or future times computed with fixed offsets go wrong.
- Concrete example: a meeting at 2026-08-03T15:00:00Z renders as 17:00 in Europe/Berlin (CEST) and 08:00 in America/Los_Angeles (PDT); formatting with the server's zone shows every user the server's time — the classic "why is this event at 3am" bug. Relative and absolute renderings ("in 2h" vs "at 17:00") have different zone needs.
- Failure modes: storing local wall-clock without an offset; applying DST rules to fixed offsets; using new Date(string) where ISO-with-Z and date-only strings parse differently; forgetting that the same IANA zone's offset changes across history (political shifts); and formatting in UTC when users expect local.
- Operational tradeoffs: render in the user's zone by default, offer UTC/absolute views for distributed teams, and always keep the instant canonical in storage; test with zones that have unusual DST (Australia, Iran) and with future-dated entries.
- RSIS3/mykb relevance: the wiki stores ISO-8601 UTC instants and would render via Intl per reader; this node documents the zone policy so log entries compare cleanly across contributors.
- DST correctness: IANA zones encode transition history; use the zone database (Intl) rather than fixed offsets, and test dates near transitions (spring forward/fall back) where the off-by-one bugs live.
- Server policy: store instants in UTC ISO-8601 and format only at the display boundary; a stored local time without an offset is a data model bug, not a formatting bug.

## Related
- [[wiki/web-platforms/responsive-design-systems|Responsive Design Systems]]
- [[wiki/web-platforms/i18n-web|Web Internationalization]]
- [[wiki/web-platforms/l10n-practice|Localization Practice]]
- [[wiki/web-platforms/locale-data|Locale Data]]
- [[wiki/mobile-platform/internationalization|Internationalization]]
- [[wiki/mobile-platform/localization|Localization]]
- [[wiki/web-platforms/web-standards|Web Standards]]
