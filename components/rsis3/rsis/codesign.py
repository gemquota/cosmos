"""Co-design workspaces — humans and the system design together.

Phase 40 (Sequel VIII): projects (11) gain co-design workspaces where
human drafts, system proposals and merged plans live with full
provenance. L2 goal formulation (28) becomes interactive — the system
proposes, the human edits, the merged goal enters the normal pipeline
with dual authorship recorded. Every artifact shows which parts are
human-authored, system-authored, or merged.
"""

from __future__ import annotations

import json
import logging
from pathlib import Path
from typing import Optional

from rsis.epoch1 import emit, load_json, now_ts, save_json, sha256_text

logger = logging.getLogger(__name__)


def codesign_dir(workspace: Path) -> Path:
    return Path(workspace) / "rack" / "codesign"


def canvas_path(workspace: Path, project: str) -> Path:
    return codesign_dir(workspace) / f"{project}.json"


def create_canvas(workspace: Path, project: str, title: str) -> dict:
    ws = Path(workspace)
    path = canvas_path(ws, project)
    canvas = {"project": project, "title": title, "created": now_ts(),
              "artifacts": []}
    save_json(path, canvas)
    emit(ws, "codesign_canvas", project=project)
    return canvas


def _load_canvas(workspace: Path, project: str) -> dict:
    return load_json(canvas_path(workspace, project),
                     {"project": project, "title": project, "artifacts": []})


def add_artifact(workspace: Path, project: str, text: str,
                 author: str, kind: str = "proposal") -> dict:
    """Add a human- or system-authored artifact (full provenance)."""
    ws = Path(workspace)
    canvas = _load_canvas(ws, project)
    artifact = {"id": f"a{len(canvas.get('artifacts', []))}", "kind": kind,
                "author": author, "text": text, "sha": sha256_text(text),
                "ts": now_ts()}
    canvas.setdefault("artifacts", []).append(artifact)
    save_json(canvas_path(ws, project), canvas)
    emit(ws, "codesign_proposed", project=project, author=author)
    return artifact


def merge(workspace: Path, project: str, artifact_ids: list[str],
          title: str, merged_by: str = "human") -> dict:
    """Merge artifacts into a joint plan with per-line authorship."""
    ws = Path(workspace)
    canvas = _load_canvas(ws, project)
    by_id = {a["id"]: a for a in canvas.get("artifacts", [])}
    parts = [by_id[i] for i in artifact_ids if i in by_id]
    if not parts:
        return {"merged": False, "reason": "no artifacts"}
    lines = []
    for part in parts:
        for line in part["text"].splitlines():
            lines.append({"line": line, "author": part["author"]})
    merged = {"id": f"m{len(canvas.get('merged', []))}", "title": title,
              "merged_by": merged_by, "lines": lines, "ts": now_ts()}
    canvas.setdefault("merged", []).append(merged)
    save_json(canvas_path(ws, project), canvas)
    split = {a: sum(1 for l in lines if l["author"] == a) for a in
             {l["author"] for l in lines}}
    emit(ws, "codesign_merged", project=project, authors=split)
    return {"merged": True, "id": merged["id"], "authorship": split,
            "lines": len(lines)}


def goal_from_merge(workspace: Path, project: str, merged_id: str) -> dict:
    """A merged plan enters the normal pipeline (28) with dual authorship."""
    from rsis.goals import propose
    canvas = _load_canvas(workspace, project)
    m = next((x for x in canvas.get("merged", []) if x["id"] == merged_id), None)
    if m is None:
        raise ValueError("merged plan not found")
    text = " ".join(l["line"] for l in m["lines"])
    return propose(workspace, m["title"], text[:400],
                   expected_value="co-designed", source=f"codesign:{project}",
                   proposer=m["merged_by"])


def status(workspace: Path, project: Optional[str] = None) -> dict:
    d = codesign_dir(workspace)
    if not d.is_dir():
        return {"canvases": 0}
    projects = [p.stem for p in sorted(d.glob("*.json"))]
    if project:
        c = _load_canvas(workspace, project)
        return {"project": project,
                "artifacts": len(c.get("artifacts", [])),
                "merged": len(c.get("merged", []))}
    return {"canvases": len(projects), "projects": projects}
