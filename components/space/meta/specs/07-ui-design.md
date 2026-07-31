# 7: UI Design Specification

**Status:** Draft
**Version:** 1.0.0
**Created:** 2026-07-25
**Depends On:** `02-architecture.md`, `04-api-design.md`

---

## 1. Purpose

Defines the web UI and terminal UI for SPACE, replacing the original React app with a feature-complete, accessible interface that leverages the full engine capabilities.

## 2. Scope

- Web UI (React/Next.js) component architecture and views
- Terminal UI (TUI) for headless environments
- Real-time progress dashboard
- Session management interface
- Inline LLM chat for question answering
- Responsive design and accessibility

---

## 3. Design

### 3.1 Web UI Views

```
┌────────────────────────────────────────────────────┐
│  App Shell                                         │
│  ┌──────────┬─────────────────────────────────┐    │
│  │          │                                 │    │
│  │ Sidebar  │         Main Content Area       │    │
│  │          │                                 │    │
│  │ Projects │  ┌───────────────────────────┐  │    │
│  │ Sessions │  │                           │  │    │
│  │ Progress │  │    Active View            │  │    │
│  │          │  │                           │  │    │
│  │ Config   │  │    (one of:)              │  │    │
│  │          │  │    - Dashboard            │  │    │
│  │          │  │    - Question Card        │  │    │
│  │          │  │    - Series Overview      │  │    │
│  │          │  │    - Summary / Export     │  │    │
│  │          │  │    - Settings             │  │    │
│  │          │  │    - LLM Chat             │  │    │
│  │          │  │                           │  │    │
│  │          │  └───────────────────────────┘  │    │
│  └──────────┴─────────────────────────────────┘    │
└────────────────────────────────────────────────────┘
```

### 3.2 View Definitions

**Dashboard View**
- Project list with completion bars
- Recent sessions with timestamps
- Quick-start button
- Framework stats (7 series, 326 probes, etc.)

**Question Card View**
- Series/round header with breadcrumb navigation
- Question text (optionally LLM-refined)
- Context template resolved with artifacts
- Open-ended textarea with character count
- Multi-choice selection with keyboard shortcuts (a/b/c/d/e)
- Auto-save indicator
- Previous/Next question buttons
- Progress bar per series

**Series Overview View**
- All rounds in grid layout
- Round completion status
- Artifact preview for completed rounds
- Jump-to-round navigation

**Summary / Export View**
- Overall completion percentage
- Per-series collapsible sections
- Answer review with edit capability
- Export format selector (JSON, MD, YAML, Prompt, HTML)
- Download button
- Diff view for comparing sessions

**Settings View**
- LLM provider configuration
- Auto-save interval
- Adaptive questions toggle
- Theme selection (dark/light)
- Keyboard shortcut reference

**LLM Chat View**
- Inline chat panel (toggleable)
- Ask SPACE questions about the specification
- "Explain this question" button
- "Suggest answer" button (LLM drafts based on context)

### 3.3 Component Tree

```
App
├── AppShell
│   ├── Sidebar
│   │   ├── ProjectList
│   │   ├── SessionList
│   │   ├── ProgressTracker
│   │   └── SettingsLink
│   └── MainContent
│       ├── Dashboard
│       │   ├── ProjectCard
│       │   ├── QuickStart
│       │   └── FrameworkStats
│       ├── QuestionView
│       │   ├── QuestionBreadcrumb
│       │   ├── SeriesProgress
│       │   ├── QuestionCard
│       │   │   ├── QuestionText (with LLM refinement)
│       │   │   ├── OpenEndedInput
│       │   │   ├── MultiChoiceSelector
│       │   │   └── AutoSaveIndicator
│       │   └── QuestionNavigation
│       ├── SeriesOverview
│       │   ├── RoundGrid
│       │   └── ArtifactPreview
│       ├── SummaryView
│       │   ├── CompletionStats
│       │   ├── SeriesAccordion
│       │   │   └── AnswerCard
│       │   ├── ExportPanel
│       │   └── DiffView
│       ├── SettingsView
│       │   ├── LLMConfig
│       │   ├── EngineConfig
│       │   └── ThemeConfig
│       └── LLMChat
│           ├── ChatMessageList
│           ├── ChatInput
│           └── ContextPanel
```

### 3.4 Terminal UI (TUI)

For environments without a browser, SPACE provides a TUI using Ink (React for CLI) or Blessed:

```
┌── SPACE — My Project ───────────────────────────────┐
│ Series 1/7: Conceptual Depth  │  Round 1/3           │
│ Progress: ████░░░░░░ 12%       │  Time: 3m 42s        │
├─────────────────────────────────────────────────────┤
│                                                     │
│ Q 1.1.1 — Domain and Audience                      │
│                                                     │
│ What is the primary domain or field this project    │
│ addresses?                                          │
│                                                     │
│ ┌─────────────────────────────────────────────────┐ │
│ │ > Machine learning recommendation systems       │ │
│ │   with focus on collaborative filtering and     │ │
│ │   content-based approaches                      │ │
│ └─────────────────────────────────────────────────┘ │
│                                                     │
│ After answering, select one:                        │
│   [a] A single well-established domain              │
│   [b] An interdisciplinary space spanning 2-3 domai │
│   [c] An emerging or niche area with evolving termi │
│                                                     │
│ Selection: _                                        │
│                                                     │
│ [Tab] Next Q  [Shift+Tab] Prev  [Ctrl+S] Save      │
│ [Ctrl+E] Export  [Ctrl+Q] Quit                      │
└─────────────────────────────────────────────────────┘
```

### 3.5 Keyboard Shortcuts

| Key | Action |
|-----|--------|
| `Tab` | Next question |
| `Shift+Tab` | Previous question |
| `a/b/c/d/e` | Select multi-choice option |
| `Ctrl+Enter` | Submit answer and advance |
| `Ctrl+S` | Force save |
| `Ctrl+E` | Open export dialog |
| `Ctrl+/` | Toggle LLM chat |
| `Escape` | Cancel / go back |
| `?` | Show help overlay |

### 3.6 Responsive Breakpoints

| Breakpoint | Layout |
|:----------:|--------|
| >1200px | Full sidebar + content |
| 768-1200px | Collapsible sidebar + content |
| <768px | Bottom nav + full-width content |
| TUI | Single column, keyboard-driven |

---

## 5. Accessibility

- WCAG 2.1 AA compliance target
- All interactive elements keyboard-focusable
- ARIA labels on all non-text controls
- Color contrast ratio ≥4.5:1 for text
- Screen reader announcements for state changes
- Reduced motion option (disable animations)

---

## 6. Data Model

UI consumes the same types from `01-data-schema.md`. Additional UI-specific types:

```typescript
interface UIState {
  current_view: ViewName;
  sidebar_collapsed: boolean;
  llm_chat_open: boolean;
  theme: 'dark' | 'light';
  keyboard_shortcuts_enabled: boolean;
}

type ViewName = 'dashboard' | 'question' | 'series' | 'summary' | 'settings' | 'chat';
```

---

## 7. Edge Cases

- **No projects exist:** Show empty state with "Create your first project" CTA
- **LLM unavailable:** Hide LLM features; show offline indicator
- **Very long answers (>5000 chars):** Auto-expand textarea, show char count
- **Browser tab closed without save:** Auto-save already persisted state; show recovery banner on reopen
- **Multiple browser tabs:** BroadcastChannel syncs state across tabs

---

## 8. Testing Strategy

- Visual regression tests (screenshot comparison)
- Accessibility audit (axe-core)
- Keyboard navigation test suite
- Responsive layout tests at each breakpoint
- TUI tests using snapshot assertions

---

## 9. Open Questions

- Should the web UI support PWA (offline capability)?
- TUI: Ink vs Blessed vs custom?
- Should the LLM chat be a sidebar panel or a modal?
- Dark/light theme: CSS variables or Tailwind?

---

## 10. Changelog

| Version | Date | Change |
|---------|------|--------|
| 1.0.0 | 2026-07-25 | Initial draft |
