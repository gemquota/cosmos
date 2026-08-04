---
type: "entity"
title: "SwiftUI Fundamentals"
description: "Apple's declarative UI framework: views, state, modifiers, and the SwiftUI data flow"
tags: ["swiftui", "apple", "ios", "declarative", "ui"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://developer.apple.com/documentation/swiftui", "https://developer.apple.com/tutorials/swiftui"]
---
# SwiftUI Fundamentals

## Summary
SwiftUI builds Apple interfaces declaratively: views describe UI, modifiers customize it, and property wrappers (`@State`, `@Binding`, `@Observable`) manage state. The framework derives rendering from state changes and integrates with iOS, macOS, watchOS, and visionOS.

## Details
- **View model** — views are value types describing their appearance; body recomputes when state changes; identity drives updates.
- **State wrappers** — @State owns view state; @Binding shares it; @Observable/@ObservedObject model app state; @Environment propagates injected values.
- **Layout** — stacks (HStack/VStack/ZStack), grids (LazyVGrid), and safe-area and container-relative sizing.
- **Interop** — UIKit/AppKit bridges (UIViewRepresentable) wrap legacy components.
- **Worked example** — a mykb iOS reader uses @Observable for the article store and NavigationStack for browsing.
- **Relevance** — SwiftUI's state-driven rendering mirrors the declarative patterns RSIS3 documents for web UIs.
- **Previews and modifiers** — `#Preview` macros render live views in Xcode; modifier order matters because each modifier wraps the view, so background, padding, and font changes compose top-down.

## Related
- [[wiki/web-platforms/prefers-color-scheme|prefers-color-scheme]] — adjacent concept in this wiki
- [[wiki/web-platforms/dark-mode-practice|Dark Mode Practice]] — adjacent concept in this wiki
- [[wiki/web-platforms/clamp-practice|clamp() in Practice]] — adjacent concept in this wiki
- [[wiki/web-platforms/aspect-ratio-css|aspect-ratio in CSS]] — adjacent concept in this wiki
- [[wiki/mobile-platform/swiftui|SwiftUI]] — existing coverage
- [[wiki/mobile-platform/ios-platform|iOS Platform]] — existing coverage
- [[wiki/mobile-platform/swift-language|Swift Language]] — existing coverage
