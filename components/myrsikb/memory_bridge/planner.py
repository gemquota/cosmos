#!/usr/bin/env python3
"""Executive Planner — Hierarchical planning with long time horizons.

The Executive Planner takes high-level goals from L3 Self-Direction and
decomposes them into multi-step plans with dependencies, contingencies,
and utility estimation.

A plan is a tree of::

    goal → subgoals → steps → actions

Each step has:

  - ``id`` — unique within the plan (``{plan_id}-step-{nn}``)
  - ``description`` — what this step accomplishes
  - ``priority`` — estimated utility (0–1)
  - ``dependencies`` — step IDs that must complete first
  - ``status`` — pending | in_progress | completed | failed | skipped
  - ``expected_duration`` — human-readable time estimate
  - ``contingency`` — fallback plan if this step fails
  - ``subtasks`` — finer-grained breakdown

Usage::

    from memory_bridge import ExecutivePlanner

    planner = ExecutivePlanner()
    plan = planner.create_plan(
        title="Improve L3 self-direction capability",
        goal_id="goal-0012",
        horizon="medium",
    )
    # Planner auto-decomposes into steps based on goal type

    next_step = planner.next_step(plan.id)
    planner.complete_step(plan.id, next_step.id)
    planner.fail_step(plan.id, next_step.id)

    status = planner.plan_status(plan.id)
"""

import json
import re
import uuid
from datetime import datetime
from pathlib import Path
from typing import Optional
from dataclasses import dataclass, field

from memory_bridge.config import resolve_wiki_path
try:
    from memory_bridge.experience_memory import ExperienceMemory
except ImportError:
    ExperienceMemory = None


#  ── Data classes ──────────────────────────────────────────────

@dataclass
class PlanStep:
    """A single step within an executive plan."""
    id: str
    description: str
    priority: float = 0.5
    status: str = "pending"  # pending | in_progress | completed | failed | skipped
    dependencies: list[str] = field(default_factory=list)
    subtasks: list[str] = field(default_factory=list)
    expected_duration: str = "1 cycle"
    contingency: str = ""
    notes: str = ""

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "description": self.description,
            "priority": self.priority,
            "status": self.status,
            "dependencies": self.dependencies,
            "subtasks": self.subtasks,
            "expected_duration": self.expected_duration,
            "contingency": self.contingency,
            "notes": self.notes,
        }


@dataclass
class ExecutivePlan:
    """A hierarchical plan with steps, metadata, and progress tracking."""
    id: str
    title: str
    goal_id: str
    horizon: str  # short | medium | long
    steps: list[PlanStep] = field(default_factory=list)
    status: str = "draft"  # draft | active | completed | abandoned
    created_at: float = 0.0

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "title": self.title,
            "goal_id": self.goal_id,
            "horizon": self.horizon,
            "steps": [s.to_dict() for s in self.steps],
            "status": self.status,
            "created_at": self.created_at,
        }


#  ── Helpers ─────────────────────────────────────────────────────

def _frontmatter(**fields) -> str:
    lines = ["---"]
    for k, v in fields.items():
        if k == "tags" and isinstance(v, (list, tuple)):
            quoted = ", ".join(f'"{t}"' for t in v)
            lines.append(f"tags: [{quoted}]")
        elif isinstance(v, str):
            lines.append(f'{k}: "{v.replace(chr(34), chr(39))}"')
        elif isinstance(v, bool):
            lines.append(f"{k}: {'true' if v else 'false'}")
        elif isinstance(v, (int, float)):
            lines.append(f"{k}: {v}")
        else:
            lines.append(f"{k}: {json.dumps(v)}")
    lines.append("---")
    return "\n".join(lines)


def _iso_now() -> str:
    return datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")


#  ── ExecutivePlanner ──────────────────────────────────────────

class ExecutivePlanner:
    """Decomposes high-level goals into dependency-aware, multi-step plans.

    The planner understands goal patterns and generates appropriate step
    decompositions.  It tracks progress across step lifecycles and
    produces execution recommendations (which step to tackle next).

    Plans are persisted as wiki pages in ``wiki/plans/``.
    Active plans are also held in memory for fast status queries.
    """

    def __init__(self, wiki_root: Optional[str | Path] = None):
        self._wiki = Path(wiki_root) if wiki_root else resolve_wiki_path()
        self._plan_dir = self._wiki / "plans"
        self._plan_dir.mkdir(parents=True, exist_ok=True)
        self._active_plans: dict[str, ExecutivePlan] = {}
        self._load_active_plans()

    # ── plan creation ───────────────────────────────────────

    def create_plan(self, title: str, goal_id: str,
                     horizon: str = "medium",
                     steps: Optional[list[dict]] = None) -> ExecutivePlan:
        """Create a new executive plan.

        If ``steps`` is not provided, the planner auto-decomposes the
        goal title into appropriate steps based on recognized patterns
        (layer score improvement, documentation, knowledge gaps, etc.).

        Args:
            title:     Human-readable plan title (same as or derived from goal).
            goal_id:   ID of the L3 goal this plan addresses.
            horizon:   ``"short"`` (1–3 cycles), ``"medium"`` (4–10), or
                       ``"long"`` (11+).
            steps:     Optional pre-defined steps.  If ``None``, the
                       planner auto-generates them from the title.

        Returns:
            The created ``ExecutivePlan``.
        """
        plan_id = f"plan-{uuid.uuid4().hex[:8]}"

        if steps is None:
            steps = self._decompose_goal(title, horizon, plan_id)

        # Inject past experience context from similar pulses
        past_context = self._retrieve_past_context(title)
        if past_context:
            # Append a context step derived from past lessons
            context_step = {
                "description": f"Review {len(past_context)} relevant past experiences",
                "priority": 0.9,
                "subtasks": [
                    p.get("lesson", "")[:120] for p in past_context[:3]
                    if p.get("lesson")
                ],
                "notes": "Retrieved from ExperienceMemory for episodic context",
            }
            steps.insert(0, context_step)

        plan_steps = []
        for i, s in enumerate(steps):
            step_id = f"{plan_id}-step-{i:02d}"
            plan_steps.append(PlanStep(
                id=step_id,
                description=s.get("description", f"Step {i+1}"),
                priority=s.get("priority", 0.5),
                dependencies=self._resolve_dep_ids(s.get("dependencies", []), plan_id, i),
                subtasks=s.get("subtasks", []),
                expected_duration=s.get("expected_duration", "1 cycle"),
                contingency=s.get("contingency", ""),
                notes=s.get("notes", ""),
            ))

        plan = ExecutivePlan(
            id=plan_id,
            title=title,
            goal_id=goal_id,
            horizon=horizon,
            steps=plan_steps,
            created_at=datetime.utcnow().timestamp(),
        )

        self._active_plans[plan_id] = plan
        self._persist_plan(plan)
        return plan

    # ── step lifecycle ──────────────────────────────────────

    def next_step(self, plan_id: str) -> Optional[PlanStep]:
        """Get the next actionable step (dependencies met, highest priority).

        Returns ``None`` if all steps are complete or the plan doesn't exist.
        """
        plan = self._active_plans.get(plan_id)
        if not plan:
            return None

        # Gather completed step IDs
        completed = {s.id for s in plan.steps if s.status == "completed"}

        # Find pending steps whose dependencies are satisfied
        available = []
        for step in plan.steps:
            if step.status != "pending":
                continue
            deps_met = all(d in completed for d in step.dependencies)
            if deps_met:
                available.append(step)

        if not available:
            return None

        # Return highest priority
        available.sort(key=lambda s: -s.priority)
        return available[0]

    def start_step(self, plan_id: str, step_id: str) -> bool:
        """Mark a step as in_progress. Returns True if successful."""
        plan = self._active_plans.get(plan_id)
        if not plan:
            return False
        for step in plan.steps:
            if step.id == step_id and step.status == "pending":
                step.status = "in_progress"
                plan.status = "active"
                self._persist_plan(plan)
                return True
        return False

    def complete_step(self, plan_id: str, step_id: str,
                       notes: str = "") -> bool:
        """Mark a step as completed. Returns True if successful."""
        plan = self._active_plans.get(plan_id)
        if not plan:
            return False
        for step in plan.steps:
            if step.id == step_id and step.status == "in_progress":
                step.status = "completed"
                if notes:
                    step.notes = notes
                self._persist_plan(plan)
                return True
        return False

    def fail_step(self, plan_id: str, step_id: str,
                   notes: str = "") -> bool:
        """Mark a step as failed and attempt contingency if defined."""
        plan = self._active_plans.get(plan_id)
        if not plan:
            return False
        for step in plan.steps:
            if step.id == step_id and step.status in ("pending", "in_progress"):
                # If contingency exists, create a new step for it
                if step.contingency and step.contingency not in ("", "none"):
                    self._apply_contingency(plan, step)
                step.status = "failed"
                if notes:
                    step.notes = notes
                self._persist_plan(plan)
                return True
        return False

    def skip_step(self, plan_id: str, step_id: str,
                   reason: str = "") -> bool:
        """Mark a step as skipped."""
        plan = self._active_plans.get(plan_id)
        if not plan:
            return False
        for step in plan.steps:
            if step.id == step_id:
                step.status = "skipped"
                if reason:
                    step.notes = reason
                self._persist_plan(plan)
                return True
        return False

    # ── plan status ─────────────────────────────────────────

    def plan_status(self, plan_id: str) -> Optional[dict]:
        """Get detailed status of a plan."""
        plan = self._active_plans.get(plan_id)
        if not plan:
            return None

        total = len(plan.steps)
        completed = sum(1 for s in plan.steps if s.status == "completed")
        in_progress = sum(1 for s in plan.steps if s.status == "in_progress")
        failed = sum(1 for s in plan.steps if s.status == "failed")
        skipped = sum(1 for s in plan.steps if s.status == "skipped")
        pending = sum(1 for s in plan.steps if s.status == "pending")

        # Get next step
        nxt = self.next_step(plan_id)

        return {
            "plan_id": plan_id,
            "title": plan.title,
            "goal_id": plan.goal_id,
            "horizon": plan.horizon,
            "status": plan.status,
            "progress": {
                "total": total,
                "completed": completed,
                "in_progress": in_progress,
                "failed": failed,
                "skipped": skipped,
                "pending": pending,
                "percent": round((completed / total) * 100, 1) if total > 0 else 0,
            },
            "next_step": nxt.to_dict() if nxt else None,
            "steps": [s.to_dict() for s in plan.steps],
        }

    def list_active_plans(self) -> list[dict]:
        """Return all plans with active or draft status."""
        active = []
        for plan in self._active_plans.values():
            if plan.status in ("draft", "active"):
                active.append({
                    "id": plan.id,
                    "title": plan.title,
                    "goal_id": plan.goal_id,
                    "horizon": plan.horizon,
                    "status": plan.status,
                    "step_count": len(plan.steps),
                    "completed": sum(1 for s in plan.steps if s.status == "completed"),
                })
        return active

    def abandon_plan(self, plan_id: str) -> bool:
        """Mark a plan as abandoned."""
        plan = self._active_plans.get(plan_id)
        if not plan:
            return False
        plan.status = "abandoned"
        self._persist_plan(plan)
        return True

    # ── goal / pattern decomposition ───────────────────────

    def _retrieve_past_context(self, title: str) -> list[dict]:
        """Query ExperienceMemory for past pulses similar to this goal.

        Returns a list of past pulse summaries with lessons and outcomes.
        Returns empty list if ExperienceMemory is unavailable or empty.
        """
        if ExperienceMemory is None:
            return []
        try:
            mem = ExperienceMemory(self._wiki)
            similar = mem.retrieve_similar_pulses(title, top_k=3)
            results = []
            for p in similar:
                if isinstance(p, dict) and "error" not in p:
                    results.append({
                        "id": p.get("id", ""),
                        "description": p.get("description", ""),
                        "score": p.get("score", 0),
                        "lesson": p.get("snippet", ""),
                    })
            return results
        except Exception:
            return []

    def _decompose_goal(self, title: str, horizon: str,
                        plan_id: str) -> list[dict]:
        """Auto-decompose a goal title into structured steps.

        Recognised patterns (in priority order):

          1. ``"Improve/Boost/Raise <layer> [score/capability]"``
          2. ``"Document/Define/Write <entity>"``
          3. ``"Resolve/Fix <crisis/issue>"``
          4. ``"Adopt/Implement <experiment result>"``
          5. ``"Learn/Research <topic>"``
          6. Default generic decomposition
        """
        t = title.lower()

        # Pattern 1: Layer score improvement
        layer_match = re.search(
            r"(improve|boost|raise|increase)\s+(l[1-6])\b", t
        )
        if layer_match:
            action = layer_match.group(1)
            layer = layer_match.group(2).upper()
            return self._layer_improvement_steps(layer, action, horizon, plan_id)

        # Pattern 2: Documentation
        if any(w in t for w in ["document", "define", "write", "wiki"]):
            return self._documentation_steps(title, horizon, plan_id)

        # Pattern 3: Crisis resolution
        if any(w in t for w in ["resolve", "crisis", "recover", "fix", "repair"]):
            return self._crisis_steps(title, horizon, plan_id)

        # Pattern 4: Adoption (from experiment results)
        if any(w in t for w in ["adopt", "implement", "deploy"]):
            return self._adoption_steps(title, horizon, plan_id)

        # Pattern 5: Research / learning
        if any(w in t for w in ["learn", "research", "study", "understand"]):
            return self._research_steps(title, horizon, plan_id)

        # Pattern 6: Address (generic performance/knowledge gap)
        if "address" in t or "declining" in t or "performance" in t:
            return self._performance_steps(title, horizon, plan_id)

        # Default: Generic decomposition
        return self._generic_steps(title, horizon, plan_id)

    def _layer_improvement_steps(self, layer: str, action: str,
                                  horizon: str, plan_id: str) -> list[dict]:
        """Steps for improving a specific capability layer."""
        depth = {"short": 2, "medium": 4, "long": 6}.get(horizon, 4)
        prefix = plan_id or "plan"
        return [
            {
                "description": f"Analyze {layer} current metrics and identify weak sub-metrics",
                "priority": 0.90,
                "expected_duration": "1 cycle",
                "contingency": "Use default metrics breakdown if telemetry unavailable",
            },
            {
                "description": f"Research known improvement strategies for {layer}",
                "priority": 0.70,
                "dependencies": [f"{prefix}-step-00"],
                "expected_duration": "1 cycle",
                "contingency": "Apply strategy from most similar past pulse",
            },
            {
                "description": f"Implement {layer} improvement via targeted pulse cycle",
                "priority": 0.85,
                "dependencies": [f"{prefix}-step-00", f"{prefix}-step-01"],
                "expected_duration": "1-2 cycles" if horizon != "short" else "1 cycle",
                "contingency": "Rollback to last verified commit if tests fail",
            },
            {
                "description": f"Benchmark {layer} against baseline and record delta",
                "priority": 0.65,
                "dependencies": [f"{prefix}-step-02"],
                "expected_duration": "1 cycle",
                "contingency": "Compare against historical average if no baseline exists",
            },
        ][:depth]

    def _documentation_steps(self, title: str, horizon: str,
                              plan_id: str) -> list[dict]:
        """Steps for documenting an entity or concept."""
        prefix = plan_id or "plan"
        return [
            {
                "description": f"Research and gather information about: {title[:60]}",
                "priority": 0.80,
                "expected_duration": "1 cycle",
                "contingency": "Use mykb search to find existing related notes",
            },
            {
                "description": "Write structured wiki page with YAML frontmatter",
                "priority": 0.90,
                "dependencies": [f"{prefix}-step-00"],
                "expected_duration": "1 cycle",
                "contingency": "Write stub first, expand in subsequent cycles",
            },
            {
                "description": "Cross-link with existing entities and add backlinks",
                "priority": 0.60,
                "dependencies": [f"{prefix}-step-01"],
                "expected_duration": "1 cycle",
                "contingency": "Auto-generate links from related sessions",
            },
            {
                "description": "Verify documentation completeness via gap analysis",
                "priority": 0.50,
                "dependencies": [f"{prefix}-step-02"],
                "expected_duration": "1 cycle",
                "contingency": "Re-run gap detector to check coverage",
            },
        ]

    def _crisis_steps(self, title: str, horizon: str,
                       plan_id: str) -> list[dict]:
        """Steps for resolving an active crisis."""
        prefix = plan_id or "plan"
        return [
            {
                "description": f"Diagnose root cause of: {title[:60]}",
                "priority": 0.95,
                "expected_duration": "1 cycle",
                "contingency": "Check crisis_monitor history for triggered violations",
            },
            {
                "description": "Generate and prioritize mitigation options",
                "priority": 0.90,
                "dependencies": [f"{prefix}-step-00"],
                "expected_duration": "1 cycle",
                "contingency": "Apply most conservative fix first",
            },
            {
                "description": "Execute mitigation and verify resolution",
                "priority": 0.95,
                "dependencies": [f"{prefix}-step-01"],
                "expected_duration": "1-2 cycles",
                "contingency": "Rollback and try alternative if tests fail",
            },
            {
                "description": "Record post-mortem and add preventive measures",
                "priority": 0.70,
                "dependencies": [f"{prefix}-step-02"],
                "expected_duration": "1 cycle",
                "contingency": "Write at minimum a brief lessons-learned note",
            },
        ]

    def _adoption_steps(self, title: str, horizon: str,
                         plan_id: str) -> list[dict]:
        """Steps for adopting a winning experiment treatment."""
        prefix = plan_id or "plan"
        return [
            {
                "description": f"Review winning treatment details for: {title[:60]}",
                "priority": 0.85,
                "expected_duration": "1 cycle",
                "contingency": "Consult experiment wiki page for full conclusion",
            },
            {
                "description": "Implement treatment as new default behavior",
                "priority": 0.90,
                "dependencies": [f"{prefix}-step-00"],
                "expected_duration": "1-2 cycles",
                "contingency": "Apply as optional config flag first for safety",
            },
            {
                "description": "Monitor for regression over a validation period",
                "priority": 0.75,
                "dependencies": [f"{prefix}-step-01"],
                "expected_duration": "2-3 cycles",
                "contingency": "Rollback if pass rate drops below prior baseline",
            },
        ]

    def _research_steps(self, title: str, horizon: str,
                         plan_id: str) -> list[dict]:
        """Steps for learning/research goals."""
        prefix = plan_id or "plan"
        steps = [
            {
                "description": f"Define scope and key questions for: {title[:60]}",
                "priority": 0.80,
                "expected_duration": "1 cycle",
                "contingency": "Start with broad overview, narrow down",
            },
            {
                "description": "Gather information from existing knowledge base",
                "priority": 0.75,
                "dependencies": [f"{prefix}-step-00"],
                "expected_duration": "1 cycle",
                "contingency": "Search mykb for related entities and sessions",
            },
            {
                "description": "Synthesize findings into structured wiki content",
                "priority": 0.85,
                "dependencies": [f"{prefix}-step-01"],
                "expected_duration": "1-2 cycles",
                "contingency": "Create outline first, fill in details iteratively",
            },
            {
                "description": "Verify understanding via self-questioning",
                "priority": 0.60,
                "dependencies": [f"{prefix}-step-02"],
                "expected_duration": "1 cycle",
                "contingency": "Use gap detector to check for remaining unknowns",
            },
        ]
        return steps

    def _performance_steps(self, title: str, horizon: str,
                            plan_id: str) -> list[dict]:
        """Steps for addressing performance concerns."""
        prefix = plan_id or "plan"
        return [
            {
                "description": f"Analyze performance data for: {title[:60]}",
                "priority": 0.90,
                "expected_duration": "1 cycle",
                "contingency": "Review recent pulses for patterns",
            },
            {
                "description": "Identify root causes and contributing factors",
                "priority": 0.85,
                "dependencies": [f"{prefix}-step-00"],
                "expected_duration": "1 cycle",
                "contingency": "Check reflection engine findings for clues",
            },
            {
                "description": "Design and implement corrective actions",
                "priority": 0.85,
                "dependencies": [f"{prefix}-step-01"],
                "expected_duration": "1-2 cycles",
                "contingency": "Apply most impactful fix first",
            },
        ]

    def _generic_steps(self, title: str, horizon: str,
                        plan_id: str) -> list[dict]:
        """Default generic goal decomposition."""
        depth = {"short": 2, "medium": 3, "long": 5}.get(horizon, 3)
        prefix = plan_id or "plan"
        steps = []
        for i in range(depth):
            steps.append({
                "description": f"Step {i+1}: {title[:60]} (phase {i+1}/{depth})",
                "priority": round(0.90 - i * 0.10, 2),
                "dependencies": [f"{prefix}-step-{j:02d}" for j in range(i)] if i > 0 else [],
                "expected_duration": "1 cycle",
                "contingency": f"Re-evaluate and adapt plan if this step fails",
                "notes": "",
            })
        return steps

    # ── internal helpers ────────────────────────────────────

    def _resolve_dep_ids(self, deps: list, plan_id: str, idx: int) -> list[str]:
        """Resolve dependency references.  Supports both full IDs and
        relative ``"prev"`` / ``"all-prior"`` patterns."""
        resolved = []
        for d in deps:
            if d == "prev" and idx > 0:
                resolved.append(f"{plan_id}-step-{idx - 1:02d}")
            elif d == "all-prior":
                for j in range(idx):
                    resolved.append(f"{plan_id}-step-{j:02d}")
            elif d.startswith(f"{plan_id}-step-"):
                resolved.append(d)
            else:
                # Assume it's a relative index
                resolved.append(d)
        return resolved

    def _apply_contingency(self, plan: ExecutivePlan, failed_step: PlanStep):
        """When a step fails, add a contingency step after it if one is defined."""
        if not failed_step.contingency or failed_step.contingency in ("", "none"):
            return

        # Find the index of the failed step
        indices = [i for i, s in enumerate(plan.steps) if s.id == failed_step.id]
        if not indices:
            return
        idx = indices[0]

        contingency_step = PlanStep(
            id=f"{failed_step.id}-contingency",
            description=f"Contingency: {failed_step.contingency[:80]}",
            priority=failed_step.priority * 0.8,  # Slightly lower priority
            dependencies=[failed_step.id] + failed_step.dependencies,
            expected_duration="1 cycle",
            contingency="",
            notes=f"Auto-generated contingency for failed step '{failed_step.id}'",
        )

        # Insert after the failed step
        plan.steps.insert(idx + 1, contingency_step)

    def _persist_plan(self, plan: ExecutivePlan):
        """Save plan as a wiki page."""
        timestamp = _iso_now()
        date_key = timestamp[:10] if "T" in timestamp else datetime.utcnow().strftime("%Y-%m-%d")

        completed = sum(1 for s in plan.steps if s.status == "completed")
        total = len(plan.steps)

        body = [
            f"# Plan: {plan.title}",
            f"**Goal:** {plan.goal_id}",
            f"**Horizon:** {plan.horizon}",
            f"**Status:** {plan.status}",
            f"**Progress:** {completed}/{total} steps completed",
            f"**Created:** {datetime.utcfromtimestamp(plan.created_at).strftime('%Y-%m-%d %H:%M UTC') if plan.created_at else 'unknown'}",
            "",
            "## Steps",
            "",
        ]

        for step in plan.steps:
            status_icon = {
                "pending": "○", "in_progress": "◉",
                "completed": "●", "failed": "✕", "skipped": "—",
            }.get(step.status, "○")
            deps_str = f"  _depends on: {', '.join(step.dependencies)}_" if step.dependencies else ""
            body.append(f"### {status_icon} {step.id}: {step.description}")
            body.append(f"  Priority: {step.priority} | Duration: {step.expected_duration}")
            if deps_str:
                body.append(deps_str)
            if step.contingency:
                body.append(f"  Contingency: {step.contingency}")
            if step.notes:
                body.append(f"  Notes: {step.notes}")
            body.append("")

        if plan.steps:
            body.append("## Dependencies\n")
            body.append("```")
            for step in plan.steps:
                if step.dependencies:
                    for dep in step.dependencies:
                        body.append(f"{step.id} → {dep}")
            body.append("```\n")

        front = {
            "type": "plan",
            "title": f"Plan: {plan.title[:80]}",
            "description": f"{plan.horizon}-term — {completed}/{total} steps ({plan.status})",
            "tags": ["plan", plan.horizon, plan.status, date_key[:7]],
            "timestamp": timestamp,
        }

        path = self._plan_dir / f"{plan.id}.md"
        content = _frontmatter(**front) + "\n\n" + "\n".join(body) + "\n"
        path.write_text(content, encoding="utf-8")

    def _load_active_plans(self):
        """Load any existing draft/active plans from the wiki."""
        for path in self._plan_dir.glob("plan-*.md"):
            text = path.read_text(encoding="utf-8")
            m = re.match(r"^---\s*\n(.*?)\n---\n?(.*)", text, re.DOTALL)
            if not m:
                continue
            fm = {}
            for line in m.group(1).split("\n"):
                if ":" not in line:
                    continue
                k, v = line.strip().split(":", 1)
                fm[k.strip()] = v.strip().strip('"')

            # Only load non-completed plans
            tags = fm.get("tags", "")
            if isinstance(tags, str):
                status_from_tags = "completed" if "completed" in tags else (
                    "abandoned" if "abandoned" in tags else "active"
                )
            else:
                status_from_tags = "active"

            if status_from_tags in ("completed", "abandoned"):
                continue

            # Reconstruct plan from the body (simplified — enough for status queries)
            plan_id = path.stem
            plan = ExecutivePlan(
                id=plan_id,
                title=fm.get("title", "").replace("Plan: ", "", 1) if "Plan: " in fm.get("title", "") else fm.get("title", ""),
                goal_id=fm.get("description", ""),
                horizon="medium",
                status="active",
            )
            self._active_plans[plan_id] = plan
