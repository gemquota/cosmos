#!/usr/bin/env python3
"""
RRP Conversational Protocol — Configurable XYZ Pattern.

X = open-ended questions per round
Y = multi-choice follow-ups per open-ended answer  
Z = rounds of questioning

Structure:
  R1:          X open-ended Qs
  R2..RZ:      X×Y multi-choice (Y per previous open-ended) + X new open-ended
  Final RZ+1:  X×Y open-ended probing questions → decision

Example (333): 3 + 2×(9+3) + 9 = 36 questions
Example (242): 2 + 1×(8+2) + 8 = 20 questions

Usage:
  --auto     System auto-answers (best guess from goal analysis)
  --interactive  User answers each question interactively
  --x X --y Y --z Z  Configure pattern (default: 3 3 3)
"""

import json, sys, random
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))
from rsis.rrp_bridge import RRPBridge


# ── Question Banks ──────────────────────────────────────────────────────

OPEN_ENDED_BANK = {
    "error_handling": [
        "What error types or edge cases should this code handle?",
        "Should failures be silent (log only), loud (raise exception), or retry with backoff?",
        "What's the recovery strategy if this operation fails partway through?",
        "How should we propagate errors — exception chaining or custom error types?",
        "Are there resource cleanup concerns (file handles, connections) on failure?",
        "Should we differentiate between transient vs permanent failures?",
    ],
    "type_safety": [
        "What input types should this function accept and what constraints apply?",
        "What return type best represents this operation's possible outcomes?",
        "How should we represent optional/missing values — None, Optional, or sentinel?",
        "Should we enforce types at runtime, at static-analysis time, or both?",
        "How do we handle variant types without losing type information?",
        "What type contracts should exist between this function and its callers?",
    ],
    "test_coverage": [
        "What are the key scenarios (happy, error, edge) that need test coverage?",
        "How do we verify this change doesn't break existing behavior?",
        "Should we prioritize unit tests, integration, or property-based tests?",
        "What mocking strategy isolates this code from its dependencies?",
        "How do we measure whether test coverage is adequate?",
        "What regression tests should we add to prevent repeat issues?",
    ],
    "logging": [
        "What operations and state changes should be visible in logs?",
        "What log levels (DEBUG, INFO, WARNING, ERROR) suit different events?",
        "What contextual data (timing, params, request IDs) should logs include?",
        "How should we handle PII or sensitive data in log messages?",
        "Should we use structured logging (JSON) or plain text?",
        "What log retention and rotation strategy applies here?",
    ],
    "documentation": [
        "What aspects of this code need documentation — API, internals, both?",
        "What docstring format (Google, NumPy, Sphinx) fits this codebase?",
        "Should docs include usage examples, edge-case notes, or design rationale?",
        "How do we keep documentation in sync with code changes?",
        "What README or architecture docs should reference this module?",
        "Who is the audience for this documentation — users or maintainers?",
    ],
    "code_quality": [
        "What complexity issues exist — long functions, deep nesting, duplication?",
        "Which patterns or abstractions would improve readability most?",
        "Are there duplicated code blocks across files that could be unified?",
        "How should we balance conciseness against explicitness?",
        "What naming conventions should guide variable, function, and class names?",
        "Should we extract this into smaller modules or keep it cohesive?",
    ],
    "input_validation": [
        "What external inputs (user, file, network) reach this code path?",
        "What are the valid ranges, formats, and types for each input?",
        "Should we reject invalid inputs loudly or coerce/cleanse them?",
        "At what boundary should validation happen — public API or internal?",
        "How do we validate without duplicating checks across layers?",
        "What error message format helps callers fix invalid inputs?",
    ],
    "maintainability": [
        "What makes this code hard to maintain or reason about currently?",
        "How should we decompose this into smaller, focused units?",
        "What dependencies exist and how tightly coupled are they?",
        "What testability improvements would make this easier to change?",
        "How do we reduce cognitive load for future maintainers?",
        "What configuration should be externalized vs hardcoded?",
    ],
    "performance": [
        "What performance characteristics matter — latency, throughput, memory?",
        "Are there obvious bottlenecks, N^2 operations, or unnecessary allocations?",
        "Should we cache results, precompute, or lazy-evaluate?",
        "What profiling approach would confirm where time is spent?",
        "How do we measure performance regression risk of this change?",
        "What's the acceptable performance tradeoff for clarity/correctness?",
    ],
    "security": [
        "What data flows through this code that needs protection?",
        "Could user input reach sensitive operations (filesystem, network, eval)?",
        "Are there injection risks (SQL, command, path traversal) to address?",
        "What privilege boundaries exist and how do we enforce them?",
        "Should we audit/log security-relevant operations?",
        "What threat model applies to this component?",
    ],
}

MULTI_CHOICE_BANK = {
    "error_handling": [
        {"q": "Default behavior on error?", "opts": ["Raise descriptive exception", "Retry N times then raise", "Log and continue", "Return error object"]},
        {"q": "Exception hierarchy?", "opts": ["Custom exception subclassing Exception", "Use built-in exceptions only", "Custom base + built-in subtypes", "No exceptions — error returns"]},
        {"q": "Failure granularity?", "opts": ["Fail atomically — all or nothing", "Partial success with error report", "Best-effort with warnings", "Silent degradation"]},
    ],
    "type_safety": [
        {"q": "Type enforcement strictness?", "opts": ["Full mypy strict mode", "Public API only", "Runtime isinstance checks", "Documentation only"]},
        {"q": "Optional value handling?", "opts": ["Optional[T] with early None check", "Default values + sentinels", "Union[T, None] with guards", "Raise if missing"]},
        {"q": "Type complexity limit?", "opts": ["Simple types only (str, int, bool)", "Generic containers OK", "Protocols and generics OK", "No limit — full expressiveness"]},
    ],
    "test_coverage": [
        {"q": "Testing strategy?", "opts": ["Unit tests + happy path", "Units + edge cases + errors", "Integration tests full pipeline", "Property-based + invariants"]},
        {"q": "Mocking approach?", "opts": ["Minimal mocking — real objects", "Full mock external deps", "Test doubles with verification", "Integration with real deps"]},
        {"q": "Coverage target?", "opts": ["Line coverage > 80%", "Branch coverage > 70%", "Critical paths only", "No target — pragmatic coverage"]},
    ],
    "logging": [
        {"q": "Log verbosity?", "opts": ["DEBUG for flow, INFO for state", "WARNING only for anomalies", "ERROR only for failures", "No logging — keep it clean"]},
        {"q": "Log format?", "opts": ["Structured JSON logs", "Plain text with timestamps", "Key-value pairs", "Minimal — just message"]},
        {"q": "Context in logs?", "opts": ["Function + params + timing", "Correlation IDs only", "Full context including traces", "No context — message only"]},
    ],
    "documentation": [
        {"q": "Documentation scope?", "opts": ["Docstrings for all public", "Public + internal notes", "Only complex logic", "No docs — self-documenting code"]},
        {"q": "Docstring style?", "opts": ["Google style (Args/Returns/Raises)", "NumPy style", "Sphinx/RST", "Minimal one-liner"]},
        {"q": "Examples in docs?", "opts": ["Usage examples for all public", "Examples for complex functions", "No examples — tests serve as docs", "REPL/screenshot for UI"]},
    ],
    "code_quality": [
        {"q": "Function size limit?", "opts": ["< 20 lines", "< 50 lines", "< 100 lines", "No limit — clarity matters"]},
        {"q": "Nesting depth limit?", "opts": ["Max 2 levels", "Max 3 levels", "Max 4 levels", "No limit — guard with early returns"]},
        {"q": "Duplication tolerance?", "opts": ["Zero tolerance — DRY everywhere", "Tolerate 2-3 line repeats", "Tolerate if extraction hurts readability", "No DRY — clarity over abstraction"]},
    ],
    "input_validation": [
        {"q": "Validation boundary?", "opts": ["All public API inputs", "External/user inputs only", "Trust internal, validate external", "Defensive everywhere"]},
        {"q": "Invalid input handling?", "opts": ["Raise ValueError with message", "Coerce/cleanse to valid", "Return default/fallback", "Log warning + skip"]},
        {"q": "Validation rigor?", "opts": ["Type + range + format checks", "Type checks only", "Schema validation", "Minimal — document assumptions"]},
    ],
    "maintainability": [
        {"q": "Module size preference?", "opts": ["< 200 lines per module", "< 500 lines", "< 1000 lines", "Cohesion over size limit"]},
        {"q": "Coupling tolerance?", "opts": ["Loose coupling — interfaces", "Moderate coupling within modules", "Tight coupling OK for related code", "Decouple everything via events"]},
        {"q": "Configuration approach?", "opts": ["Constants at module top", "Config classes/dataclasses", "Environment variables + defaults", "Config files (YAML/TOML/JSON)"]},
    ],
    "performance": [
        {"q": "Optimization priority?", "opts": ["Correctness first, perf second", "Hot-path optimization", "Memory efficiency", "Latency minimization"]},
        {"q": "Caching strategy?", "opts": ["LRU cache with TTL", "Precompute at startup", "Memoize pure functions", "No caching — keep stateless"]},
        {"q": "Data structure choice?", "opts": ["Default Python types first", "Specialized (deque, Counter)", "NumPy/Pandas for numerical", "Custom data structures"]},
    ],
    "security": [
        {"q": "Input sanitization?", "opts": ["Sanitize all external input", "Sanitize only at trust boundaries", "Escape on output not input", "Trust framework's handling"]},
        {"q": "Auth/perimeter?", "opts": ["Auth check on every entry point", "Auth at service boundary", "Internal: no auth needed", "Role-based access control"]},
        {"q": "Audit trail?", "opts": ["Log all security-relevant ops", "Log access to sensitive data", "Log only failures", "No audit logging"]},
    ],
}

DEFAULT_MULTI_CHOICE = [
    {"q": "Implementation priority?", "opts": ["Correctness first", "Readability first", "Performance first", "Safety first"]},
    {"q": "Validation approach?", "opts": ["Run existing tests", "New tests + full suite", "Manual review + tests", "Progressive: unit to integration to manual"]},
    {"q": "Rollback strategy?", "opts": ["Git revert", "Feature flag toggle", "Progressive rollout", "No rollback — additive change"]},
]

PROBE_QUESTIONS = [
    "What edge cases remain unhandled after this analysis?",
    "What assumptions does this implementation make that could break?",
    "How would you verify this change works correctly in production?",
    "What monitoring or observability should accompany this change?",
    "What would a reviewer most likely criticize about this approach?",
    "If this causes a regression, what's most likely to break?",
    "What technical debt does this introduce or pay down?",
    "How does this change interact with other system parts?",
    "What documentation would a new team member need?",
    "What performance characteristics would indicate a problem?",
    "How would you test this without the specific implementation?",
    "What rollback scenarios should we prepare for?",
    "What metrics would tell us this was successful?",
    "What failure modes exist that we haven't discussed?",
    "How does this scale under increased load or data volume?",
    "What dependencies does this introduce and are they justified?",
    "Could this change be safely reverted after deployment?",
    "What's the blast radius if this fails in production?",
]


# ── Auto-Answer Engine ─────────────────────────────────────────────────

def auto_answer_open(question: str, goal: str) -> str:
    q = question.lower()
    g = goal.lower()
    if any(w in q for w in ["error","exception","failure","recovery","fall"]):
        return "Use specific exception types for each failure mode. Recovery caller-driven. Retry for transient failures."
    if any(w in q for w in ["type","annotation","optional","union","generic"]):
        return "Full type annotations mypy strict. Optional[T] where None valid. Protocols for structural typing."
    if any(w in q for w in ["test","coverage","mock","regression"]):
        return "Unit tests core+edge+error. Full suite regressions. Minimal mocking, test real objects."
    if any(w in q for w in ["log","audit","monitor","observe"]):
        return "Structured logging key decision points. DEBUG flow, INFO state, WARNING anomalies. Include correlation IDs."
    if any(w in q for w in ["doc","document","readme","example"]):
        return "Google-style docstrings public APIs: Args/Returns/Raises. Usage examples. Keep README synced."
    if any(w in q for w in ["complex","readability","duplicate","nest","refactor"]):
        return "Single-responsibility units. Max 2 nesting. Extract repeated patterns. Early returns flatten control flow."
    if any(w in q for w in ["valid","input","boundary","sanitize"]):
        return "Validate at public API boundary. Clear error messages. Type hints + runtime guards critical paths."
    if any(w in q for w in ["perf","bottleneck","cache","optimize","slow"]):
        return "Profile first. LRU cache repeated computations. Optimize hot paths after measuring."
    if any(w in q for w in ["security","injection","privilege","threat","exploit"]):
        return "Sanitize external input at trust boundaries. Parameterized queries. Least privilege. Audit security ops."
    if any(w in q for w in ["scale","load","throughput","concurrent"]):
        return "Stateless horizontal scaling. Connection pooling. Rate limiting. Monitor key metrics."
    if any(w in q for w in ["rollback","revert","deploy","blast"]):
        return "Feature flags gradual rollout. Git revert. 15min post-deploy monitoring. Document rollback."
    if any(w in q for w in ["assumption","break","risk"]):
        return "Document key assumptions. Regression tests critical paths. Canary deployments limit blast radius."
    if any(w in q for w in ["metric","success","measure","indicator"]):
        return "Define success metrics pre-deploy. Track error rates, latency p50/p99. Alert on deviation."
    if "error" in g or "except" in g or "timeout" in g:
        return "Specific exception types. Caller-driven recovery. Descriptive error messages."
    if "type" in g or "annotation" in g:
        return "Full type annotations public functions. mypy strict. Optional[T] where semantically valid."
    if "test" in g or "coverage" in g:
        return "Unit tests modified functions + edge cases. Full regression. >80% coverage new code."
    if "refactor" in g or "complex" in g:
        return "Smaller functions. Reduced nesting. Extracted patterns. Clear naming."
    return "Standard best practices: correctness, readability, testability."


def auto_answer_multi(question: str, options: list, goal: str) -> str:
    d = goal.lower()
    best, best_score = options[0], -1
    for opt in options:
        o = opt.lower()
        s = 0
        for kw in d.split():
            kw = kw.strip(",.!?;:")
            if kw in o:
                s += 1
        pairs = [("error", "exception"), ("error", "raise"), ("type", "annotation"),
                 ("type", "mypy"), ("test", "test"), ("log", "log"), ("doc", "doc"),
                 ("valid", "valid"), ("implement", "custom"), ("refactor", "readability")]
        for kw, opt_kw in pairs:
            if kw in d and opt_kw in o:
                s += 3
        if s > best_score:
            best_score, best = s, opt
    if best_score <= 0:
        pref = ["Raise descriptive exception", "Full mypy strict mode",
                "Optional[T] with early None check", "Unit tests + happy path",
                "Correctness first", "Run existing tests", "Git revert",
                "Structured JSON logs", "Docstrings for all public"]
        for p in pref:
            if p in options:
                best = p
                break
    return best


# ── Conversation Engine ─────────────────────────────────────────────────

class RRPConversation333:
    """XYZ-Pattern RRP Conversation: X open-ended × Y follow-ups × Z rounds."""

    def __init__(self, goal: str, target_files: list[str], interactive: bool = False,
                 x: int = 3, y: int = 3, z: int = 3):
        self.goal = goal
        self.target_files = target_files
        self.interactive = interactive
        self.x = x
        self.y = y
        self.z = z
        self.bridge = RRPBridge()
        self.round = 0
        self.answered_questions = []
        self.conversation_log = []

        d = goal.lower()
        all_types = list(OPEN_ENDED_BANK.keys())
        self.relevant = [t for t in all_types if t.replace("_", " ") in d or t in d]
        if not self.relevant:
            self.relevant = ["code_quality"]

    def ask(self, prompt: str, is_multi: bool = False, options: list = None) -> str:
        tag = "MC" if options else "OE"
        if self.interactive:
            print(f"  [{tag}] {prompt}")
            if options:
                for i, opt in enumerate(options, 1):
                    print(f"         [{i}] {opt}")
                choice = input("  Answer (number or text): ").strip()
                ans = options[int(choice) - 1] if choice.isdigit() and 1 <= int(choice) <= len(options) else choice
            else:
                ans = input("  Answer: ").strip()
        else:
            ans = auto_answer_multi(prompt, options, self.goal) if options else auto_answer_open(prompt, self.goal)
            a_short = ans[:80] + "..." if len(ans) > 80 else ans
            print(f"  [{tag}] {prompt[:80]}")
            print(f"        \u2192 {a_short}")

        self.answered_questions.append({"q": prompt, "a": ans, "type": "multi" if options else "open"})
        return ans

    def pick_questions(self, bank: dict, count: int, used: set = None) -> list:
        if used is None:
            used = set()
        candidates = []
        for t, qs in bank.items():
            for q in qs:
                if q not in used:
                    score = 2 if t in self.relevant else 1
                    candidates.append((t, q, score))
        candidates.sort(key=lambda x: -x[2])
        # Shuffle the lower-score ones
        high_count = len([c for c in candidates if c[2] > 1])
        pool = list(candidates)
        random.shuffle(pool)
        # Pick with type diversity
        picked, seen_types = [], set()
        for t, q, _ in pool:
            if len(picked) >= count:
                break
            limit = max(2, count // max(len(self.relevant), 1)) if t in self.relevant else 1
            if t not in seen_types or len([p for p in picked if p[0] == t]) < limit:
                picked.append((t, q))
                seen_types.add(t)
                used.add(q)
        # If still not enough, grab any
        if len(picked) < count:
            for t, q, _ in pool:
                if (t, q) not in picked and q not in used and len(picked) < count:
                    picked.append((t, q))
                    used.add(q)
        return picked

    def pick_multi(self, answer: str, count: int = 3) -> list:
        d = (answer + " " + self.goal).lower()
        candidates, used_set = [], set()
        for t, mc_list in MULTI_CHOICE_BANK.items():
            if t in d or any(w in d for w in t.split("_")):
                for mc in mc_list:
                    if mc["q"] not in used_set:
                        candidates.append(mc)
                        used_set.add(mc["q"])
        while len(candidates) < count:
            for mc in DEFAULT_MULTI_CHOICE:
                if mc["q"] not in used_set:
                    candidates.append(mc)
                    used_set.add(mc["q"])
            break
        if len(candidates) < count:
            for t, mc_list in MULTI_CHOICE_BANK.items():
                for mc in mc_list:
                    if mc["q"] not in used_set and len(candidates) < count:
                        candidates.append(mc)
                        used_set.add(mc["q"])
        random.shuffle(candidates)
        return candidates[:count]

    def run(self) -> dict:
        total_q = self.x + (self.z - 1) * (self.x * self.y + self.x) + self.x * self.y

        print(f"\n  {'='*52}")
        print(f"  XYZ RRP Conversation  —  X={self.x}  Y={self.y}  Z={self.z}")
        print(f"  Goal: {self.goal[:60]}...")
        print(f"  Mode: {'Interactive' if self.interactive else 'Auto'}")
        print(f"  Questions: {total_q} (R1: {self.x} OE + R2-R{self.z}: {self.x}x{self.y} MC+{self.x} OE + Final: {self.x}x{self.y} OE)")
        print(f"  {'='*52}\n")

        used = set()
        open_answers = []  # Track open-ended answers across rounds for follow-ups

        # ── ROUND 1: X open-ended ──
        self.round = 1
        label = f" ROUND 1: {self.x} Open-Ended Questions "
        print(f"  \u250c\u2500{label:-^48}\u2510")
        r1_qs = self.pick_questions(OPEN_ENDED_BANK, self.x, used)
        r1_qa = []
        for t, q in r1_qs:
            a = self.ask(q)
            r1_qa.append({"q": q, "a": a, "type": t})
            open_answers.append(a)
        self.conversation_log.append({"round": 1, "phase": "open_ended", "qa": r1_qa})
        print(f"  \u2514{'-'*52}\u2518")

        # ── ROUNDS 2..Z: X*Y multi-choice + X open-ended each ──
        round_oe_log = [r1_qa]
        for ri in range(2, self.z + 1):
            self.round = ri
            prev_oe = round_oe_log[-1]
            label = f" ROUND {ri}: {self.x}\u00d7{self.y} MC + {self.x} OE "
            print(f"\n  \u250c\u2500{label:-^48}\u2510")

            # X*Y multi-choice (Y per previous open-ended answer)
            mc_all = []
            for i, ans in enumerate(prev_oe):
                mcs = self.pick_multi(ans["a"], self.y)
                for mc in mcs:
                    a = self.ask(mc["q"], is_multi=True, options=mc["opts"])
                    mc_all.append({"q": mc["q"], "a": a, "follow_up_to": i})

            self.conversation_log.append({"round": ri, "phase": "multi_choice", "qa": mc_all})

            # X new open-ended
            r_open_qs = self.pick_questions(OPEN_ENDED_BANK, self.x, used)
            open_qa = []
            for t, q in r_open_qs:
                a = self.ask(q)
                open_qa.append({"q": q, "a": a, "type": t})
                open_answers.append(a)

            self.conversation_log.append({"round": ri, "phase": "open_ended", "qa": open_qa})
            round_oe_log.append(open_qa)
            print(f"  \u2514{'-'*52}\u2518")

        # ── FINAL ROUND: X×Y open-ended probing ──
        self.round = self.z + 1
        label = f" ROUND {self.z+1}: {self.x}\u00d7{self.y} Final Probing "
        print(f"\n  \u250c\u2500{label:-^48}\u2510")
        random.shuffle(PROBE_QUESTIONS)
        final_qa = []
        for q in PROBE_QUESTIONS[:self.x * self.y]:
            a = self.ask(q)
            final_qa.append({"q": q, "a": a, "type": "probe"})
        self.conversation_log.append({"round": self.z + 1, "phase": "probing", "qa": final_qa})
        print(f"  \u2514{'-'*52}\u2518")

        # ── DECISION ──
        rrp_result = self.bridge.refine_goal(self.goal)
        constraints = dict(rrp_result.constraints)
        locked = [k for k, v in constraints.items() if v == "LOCKED"]

        if hasattr(rrp_result, 'contradiction_detected') and rrp_result.contradiction_detected:
            decision, confidence = "HOLD", 0.35
        elif len(locked) >= 3:
            decision, confidence = "PASS", 0.80
        elif len(locked) >= 1:
            decision, confidence = "PASS", 0.75
        else:
            decision, confidence = "PASS", 0.70

        final = {
            "decision": decision, "confidence": confidence,
            "reasoning": f"XYZ conversation complete: {len(self.answered_questions)} questions across {self.z+1} rounds. Locked: {locked}.",
            "constraints": constraints, "total_questions": len(self.answered_questions),
            "rounds": self.z + 1, "pattern": f"{self.x}{self.y}{self.z}",
        }
        self.conversation_log.append({"round": self.z + 1, "phase": "decision", "decision": final})

        print(f"\n  {'='*52}")
        print(f"  XYZ COMPLETE  —  {len(self.answered_questions)}/{total_q} questions")
        print(f"  Decision: {decision}  (conf: {confidence:.2f})")
        print(f"  Constraints: {dict(constraints)}")
        print(f"  {'='*52}\n")

        return {
            "goal": self.goal, "target_files": self.target_files,
            "mode": "interactive" if self.interactive else "auto",
            "pattern": f"{self.x}{self.y}{self.z}",
            "rounds": self.z + 1, "config": {"x": self.x, "y": self.y, "z": self.z},
            "total_questions": len(self.answered_questions),
            "expected_questions": total_q,
            "answered_questions": self.answered_questions,
            "conversation_log": self.conversation_log,
            "final_decision": final,
        }


# ── CLI ──
if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="XYZ-pattern RRP conversation")
    parser.add_argument("--goal", default="Implement TimeoutError in rsis/timeout.py")
    parser.add_argument("--files", nargs="+", default=["rsis/timeout.py"])
    parser.add_argument("--interactive", "-i", action="store_true")
    parser.add_argument("--x", type=int, default=3)
    parser.add_argument("--y", type=int, default=3)
    parser.add_argument("--z", type=int, default=3)
    parser.add_argument("--output", "-o")
    args = parser.parse_args()

    conv = RRPConversation333(args.goal, args.files, interactive=args.interactive,
                              x=args.x, y=args.y, z=args.z)
    result = conv.run()

    if args.output:
        Path(args.output).write_text(json.dumps(result, indent=2, default=str))
        print(f"Saved: {args.output}")
