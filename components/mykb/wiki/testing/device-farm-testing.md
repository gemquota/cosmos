---
type: "concept"
title: "Device Farm Testing"
description: "Running mobile tests on real-device clouds and emulators"
tags: ["device-farm", "testing", "mobile", "cloud"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://www.browserstack.com/docs", "https://saucelabs.com/platform"]
---

# Device Farm Testing

## Summary
Device farm testing runs mobile and web tests on real-device and emulator clouds, thousands of device, OS, and browser combinations in parallel. It covers platform fragmentation without owning a hardware lab.

## Details
- Providers: BrowserStack, Sauce Labs, AWS Device Farm, and Firebase Test Lab.
- Use cases: OS version matrices, manufacturer quirks, network profiles, and parallel E2E.
- Combine with CI on release candidates; debug via videos, logs, and screenshots.
- Real devices catch issues emulators miss: sensors, memory, GPU, and carrier behavior.
- Control cost: run a targeted device matrix, not everything, on every commit.
- Integrate Appium, XCUITest, and Espresso suites with farm APIs.
- Sanitize secrets and test data on third-party infrastructure.

## Related
- [[wiki/testing/mobile-testing|Mobile Testing]] — the suites farms execute
- [[wiki/testing/compatibility-testing|Compatibility Testing]] — coverage goals for farms
- [[wiki/testing/ui-testing|UI Testing]] — browser tests on farm grids
- [[wiki/testing/test-parallelism|Test Parallelism]] — parallel execution across devices
- [[wiki/testing/test-environments|Test Environments]] — managed device environments
- [[wiki/testing/ci-quality-gates|CI Quality Gates]] — farm runs gating releases
