# Phase 4: Interactive UI — Development Guide

**Spec References:** `specs/07-ui-design.md`
**Prerequisites:** Phase 1 complete
**Estimated Effort:** 3–4 weeks
**Sprint Count:** 2

**Status:** Implemented | **Tests:** ✅ | **Last Cycle:** 004 | **Coverage:** 80%+

---

## Overview

Replace the original React frontend with a modern, feature-complete web UI and optionally a terminal UI. Both consume the `CoreAPI` from Phase 1 and support the full 326-probe elicitation flow with LLM features from Phase 2.

---

## Task Table

| ID | Title | Spec | Effort | Deps | Acceptance Criteria |
|----|-------|------|:------:|------|---------------------|
| 4.T1 | App shell with routing and sidebar | 07 §3.1 | M | — | Layout matches spec; navigation works |
| 4.T2 | Dashboard view (project list, quick start) | 07 §3.2 | M | 4.T1 | Projects listed; can create/start sessions |
| 4.T3 | Question card view (OE + MC input) | 07 §3.2 | L | 4.T1 | All 326 question types render correctly |
| 4.T4 | Series overview view (round grid) | 07 §3.2 | M | 4.T3 | Round status displayed; jump-to-round works |
| 4.T5 | Summary/export view | 07 §3.2 | M | 4.T3, 3.T1 | Answers reviewable; export triggers download |
| 4.T6 | Auto-save with indicator | 07 §3.2 | M | 4.T3 | State saved on every change; indicator shown |
| 4.T7 | Keyboard shortcuts | 07 §3.5 | S | 4.T3 | Tab, Shift+Tab, a-e, Ctrl+Enter all work |
| 4.T8 | Responsive layout (768px, <768px) | 07 §3.6 | M | 4.T1 | Looks good at all breakpoints |
| 4.T9 | Accessibility (ARIA, focus management) | 07 §5 | M | 4.T3 | axe-core audit passes |
| 4.T10 | LLM chat panel (toggleable sidebar) | 07 §3.2 | L | 4.T1, 2.T1 | Ask questions, get suggestions |
| 4.T11 | Settings view | 07 §3.2 | S | 4.T1 | LLM config, theme, shortcuts display |
| 4.T12 | Session management (list, resume, delete) | 07 §3.2 | M | 4.T2 | Sessions listed; resume loads correct state |
| 4.T13 | Theme (dark + light) | 07 §3.2 | M | 4.T1 | Toggle works; all components themed |
| 4.T14 | Terminal UI (TUI) with Ink | 07 §3.4 | XL | 4.T3 | Full question flow in terminal |

---

## Task Details

#### 4.T3: Question Card View

**What:**
The core interaction surface — renders a question with its open-ended textarea, multi-choice selection, and navigation controls.

**Files:**
- `src/components/QuestionCard.tsx`
- `src/components/OpenEndedInput.tsx`
- `src/components/MultiChoiceSelector.tsx`
- `src/components/QuestionNavigation.tsx`

**Implementation Notes:**
- Question text may be LLM-refined (show original as tooltip)
- Context template resolved and shown as subtle context block
- Textarea auto-saves on blur and on Ctrl+S
- Multi-choice: radio buttons with keyboard shortcuts (a/b/c/d/e shown in labels)
- Navigation: Previous / Complete & Next / Skip buttons
- Skip requires a reason (modal prompt)

**Done When:**
- [ ] Renders all question types from the 7 series correctly
- [ ] Textarea accepts free-form text
- [ ] Multi-choice selection dispatches correct action
- [ ] Auto-save triggers on answer change
- [ ] Keyboard shortcuts work for choice selection

---

#### 4.T10: LLM Chat Panel

**What:**
A toggleable side panel where users can chat with SPACE's LLM to ask about the specification, get answer suggestions, or explain questions.

**Files:**
- `src/components/LLMChat/ChatPanel.tsx`
- `src/components/LLMChat/ChatMessage.tsx`
- `src/components/LLMChat/ChatInput.tsx`
- `src/components/LLMChat/context-panel.tsx`

**Implementation Notes:**
- Messages: user text + LLM response
- Context: current question + accumulated artifacts sent with each message
- "Explain this question" button sends the current question to LLM
- "Suggest answer" button generates a draft based on context
- Chat history preserved per session
- Toggle with Ctrl+/ or button

**Done When:**
- [ ] Chat panel opens/closes with keyboard shortcut
- [ ] Messages sent to LLM with correct context
- [ ] Responses rendered with Markdown support
- [ ] "Explain" and "Suggest" buttons work
- [ ] Chat history persists across page refreshes

---

## Testing

- Visual regression: screenshot comparison for each view
- Accessibility: axe-core automated audit
- Keyboard: full navigation without mouse
- Responsive: automated tests at 1200px, 768px, 375px widths
- Integration: end-to-end flow from dashboard → question → export

## Risks

- TUI complexity with Ink — may need to defer to Phase 4.5 if web UI takes longer
- LLM chat latency — show typing indicator and streaming responses
