"""Cross-project generalization — one engine, many repositories (Phase 11).

A project profile (``rack/projects/<slug>.json``) tells the shared engine
how to run against an external repo: its goals, allowed paths, loop tuning,
SPACE series and MyKB synthesis namespace. Profiles are created with
``rsis init --project <repo>``; the daemon/bridge route by ``--project`` so
the Phases 4–5 ops investment amortizes across repositories.

Cross-project learning: syntheses tagged ``project:<name>`` in the shared
MyKB become goal seeds for that project (with provenance) via the memory
API — knowledge distilled in one project seeds another.
"""

from __future__ import annotations

import json
import logging
import re
import uuid
from datetime import datetime, timezone
from pathlib import Path
from typing import Optional

logger = logging.getLogger(__name__)

DEFAULT_SPACE_SERIES = list(range(1, 8))

DEFAULT_PROFILE = {
    "version": 1,
    "name": "",
    "repo": "",
    "goals": ["self-improve the codebase"],
    "allowed_paths": [],
    "loop_tuning": {},
    "space_series": DEFAULT_SPACE_SERIES,
    "synthesis_namespace": "",
    "created_at": "",
    "origin": "rsis-init",
}


def _now_ts() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def slugify(name: str) -> str:
    slug = re.sub(r"[^a-z0-9._-]+", "-", str(name).lower()).strip("-._")
    return slug or "project"


def projects_dir(workspace: Path) -> Path:
    return Path(workspace) / "rack" / "projects"


def profile_path(workspace: Path, name: str) -> Path:
    return projects_dir(workspace) / f"{slugify(name)}.json"


def init_project(workspace: Path, repo: str, name: Optional[str] = None,
                 goals: Optional[list[str]] = None,
                 allowed_paths: Optional[list[str]] = None,
                 space_series: Optional[list[int]] = None,
                 loop_tuning: Optional[dict] = None) -> dict:
    """Scaffold a project profile under ``rack/projects/`` (create-only)."""
    name = name or Path(str(repo)).name or slugify(repo)
    path = profile_path(workspace, name)
    if path.is_file():
        return load_project(workspace, name)
    profile = dict(DEFAULT_PROFILE)
    profile.update({
        "name": name,
        "repo": str(repo),
        "goals": [g for g in (goals or []) if g] or profile["goals"],
        "allowed_paths": [p for p in (allowed_paths or []) if p],
        "space_series": [int(s) for s in (space_series or DEFAULT_SPACE_SERIES)],
        "loop_tuning": loop_tuning or {},
        "synthesis_namespace": f"project:{name}",
        "created_at": _now_ts(),
    })
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(profile, indent=2) + "\n", encoding="utf-8")
    logger.info("project profile scaffolded: %s", path)
    return profile


def load_project(workspace: Path, name: str) -> Optional[dict]:
    path = profile_path(workspace, name)
    if not path.is_file():
        return None
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as e:
        logger.warning("project %s unreadable (%s)", name, e)
        return None


def list_projects(workspace: Path) -> list[dict]:
    d = projects_dir(workspace)
    out = []
    if d.is_dir():
        for f in sorted(d.glob("*.json")):
            try:
                out.append(json.loads(f.read_text(encoding="utf-8")))
            except (OSError, json.JSONDecodeError):
                continue
    return out


def default_profile(workspace: Path) -> dict:
    """The host workspace's own implicit profile (repo = workspace name)."""
    name = Path(workspace).resolve().name
    return {
        "version": 1, "name": name, "repo": str(Path(workspace).resolve()),
        "goals": [DEFAULT_PROFILE["goals"][0]], "allowed_paths": [],
        "loop_tuning": {}, "space_series": DEFAULT_SPACE_SERIES,
        "synthesis_namespace": "project:cosmos", "created_at": "",
        "origin": "implicit",
    }


def _parse_frontmatter(text: str) -> dict:
    m = re.match(r"^---\n(.*?)\n---", text, re.S)
    if not m:
        return {}
    front = {}
    for line in m.group(1).splitlines():
        if ":" not in line:
            continue
        k, v = line.split(":", 1)
        front[k.strip()] = v.strip().strip('"')
    return front


def project_goal_seeds(workspace: Path, mykb: Path,
                       name: str, limit: int = 5) -> list[dict]:
    """Syntheses tagged ``project:<name>`` in the shared MyKB → goal seeds.

    Each seed carries provenance: origin note path, project tag, and the
    synthesis timestamp, so cross-project knowledge is never anonymous.
    """
    syntheses = Path(mykb) / "wiki" / "syntheses"
    if not syntheses.is_dir():
        return []
    seeds = []
    for f in sorted(syntheses.glob("*.md")):
        try:
            text = f.read_text(encoding="utf-8")
        except OSError:
            continue
        front = _parse_frontmatter(text)
        tags = [t.strip() for t in str(front.get("tags", "")).split(",")]
        if f"project:{slugify(name)}" not in tags:
            continue
        seeds.append({
            "title": front.get("title") or f.stem,
            "rel": f"wiki/syntheses/{f.name}",
            "provenance": {
                "origin": str(f),
                "project": name,
                "source": "mykb-synthesis",
                "ts": front.get("timestamp", ""),
            },
        })
        if len(seeds) >= limit:
            break
    return seeds


def goal_sources(project: dict, workspace: Path, mykb: Path,
                 limit: int = 3) -> list[str]:
    """Profile goals + MyKB goal seeds for the project (with provenance)."""
    goals = list(project.get("goals") or [])
    for seed in project_goal_seeds(workspace, mykb, project["name"],
                                   limit=limit):
        prov = seed["provenance"]
        goals.append(
            f"{seed['title']} — follow the durable guidance in "
            f"{seed['rel']} (seed from {prov['project']}, {prov['source']})")
    return goals or ["self-improve the codebase"]


def main(workspace: Path, mykb: Path, repo: Optional[str] = None,
         name: Optional[str] = None, list_only: bool = False,
         json_out: bool = False) -> int:
    if list_only:
        projects = list_projects(workspace)
        if json_out:
            print(json.dumps({"projects": projects}))
            return 0
        if not projects:
            print("  projects: none scaffolded")
            return 0
        for p in projects:
            print(f"  • {p['name']} ({p['repo']}) — "
                  f"{len(p.get('goals') or [])} goal(s), "
                  f"{len(p.get('allowed_paths') or [])} allowed path(s)")
        return 0
    if not repo:
        print("  ✗ use: rsis init --project <repo> or rsis projects")
        return 2
    profile = init_project(workspace, repo, name=name)
    print(f"  ✓ project profile: rack/projects/{slugify(profile['name'])}.json")
    print(f"    repo: {profile['repo']}")
    print(f"    goals: {profile['goals']}")
    print(f"    allowed paths: {profile['allowed_paths'] or 'all'}")
    print(f"    space series: {profile['space_series']}")
    return 0


if __name__ == "__main__":
    import sys
    sys.exit(main(Path(".").resolve(), Path("../mykb").resolve()))
