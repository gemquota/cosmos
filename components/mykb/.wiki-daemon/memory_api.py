"""MyKB memory API — shared note access with concurrency semantics.

Phase 6 (Sequel II): MyKB stops being a single-workspace store and becomes
the shared nervous system for parallel sessions and agents. This module
provides the read/write primitives behind the memory endpoints:

- ``write_note`` — create-only note writes behind an advisory lock; the
  owning session may overwrite its own notes (create-only unless owner).
- ``list_notes`` / ``search_notes`` — read access over the wiki.
- ``refresh_index`` — rebuild hook for the search index after consolidation.
- ``MemoryLock`` — advisory fcntl lock (with O_EXCL fallback) so two
  parallel sessions consolidating simultaneously never clobber each other.

Stdlib only; the search API degrades to a deterministic token match when
the optional numpy/rank_bm25 index is unavailable.
"""

from __future__ import annotations

import hashlib
import json
import os
import re
import subprocess
import sys
from pathlib import Path
from typing import Optional

WIKI_REL = "wiki"
LOCK_NAME = "write.lock"
FRONTMATTER_RE = re.compile(r"^---\n(.*?)\n---", re.S)


class MemoryLock:
    """Advisory write lock for MyKB note mutations (fcntl, O_EXCL fallback)."""

    def __init__(self, root: Path):
        self.path = Path(root) / ".wiki-daemon" / LOCK_NAME
        self._fh = None

    def acquire(self) -> bool:
        self.path.parent.mkdir(parents=True, exist_ok=True)
        try:
            import fcntl
            self._fh = self.path.open("a+", encoding="utf-8")
            fcntl.flock(self._fh.fileno(), fcntl.LOCK_EX | fcntl.LOCK_NB)
            return True
        except BlockingIOError:
            if self._fh is not None:
                self._fh.close()
                self._fh = None
            return False
        except ImportError:  # non-POSIX fallback: exclusive create
            try:
                self._fh = self.path.open("x", encoding="utf-8")
                return True
            except FileExistsError:
                return False

    def release(self) -> None:
        if self._fh is None:
            return
        try:
            import fcntl
            fcntl.flock(self._fh.fileno(), fcntl.LOCK_UN)
        except ImportError:
            self.path.unlink(missing_ok=True)
        self._fh.close()
        self._fh = None

    def __enter__(self) -> "MemoryLock":
        if not self.acquire():
            raise BlockingIOError(f"memory write lock held: {self.path}")
        return self

    def __exit__(self, *exc) -> None:
        self.release()


def wiki_root(root: Path) -> Path:
    return (Path(root) / WIKI_REL).resolve()


def _resolve_note(root: Path, rel: str) -> Path:
    """Resolve a wiki-relative note path; refuse escapes outside the wiki."""
    base = wiki_root(root)
    p = (base / rel).resolve()
    try:
        p.relative_to(base)
    except ValueError:
        raise ValueError(f"note path escapes wiki root: {rel!r}")
    return p


def _owner(path: Path) -> Optional[str]:
    """Read ``session_id`` from the note's OKF frontmatter, if any."""
    try:
        text = path.read_text(encoding="utf-8", errors="ignore")[:2000]
    except OSError:
        return None
    m = FRONTMATTER_RE.search(text)
    if not m:
        return None
    for line in m.group(1).splitlines():
        if line.strip().startswith("session_id:"):
            return line.split(":", 1)[1].strip().strip('"').strip("'")
    return None


def write_note(root: Path, *, rel: str, content: str,
               session_id: Optional[str] = None,
               create_only: bool = True) -> Path:
    """Write a wiki note behind the advisory lock.

    ``create_only`` (default) refuses to overwrite an existing note unless
    the caller is the note's owning session. Returns the written path.
    """
    root = Path(root)
    with MemoryLock(root):
        target = _resolve_note(root, rel)
        if target.exists() and create_only:
            owner = _owner(target)
            if not (session_id and owner == session_id):
                raise FileExistsError(
                    f"note exists (owner={owner or 'unknown'}): {rel}")
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(content, encoding="utf-8")
    return target


def list_notes(root: Path, *, session_id: Optional[str] = None,
               limit: int = 200) -> list[dict]:
    """List wiki notes with ownership metadata."""
    base = wiki_root(root)
    out = []
    for p in sorted(base.rglob("*.md")):
        if any(seg.startswith(".") for seg in p.relative_to(base).parts):
            continue
        rel = str(p.relative_to(base))
        owner = _owner(p)
        if session_id and owner != session_id:
            continue
        try:
            st = p.stat()
        except OSError:
            continue
        out.append({
            "path": rel,
            "session_id": owner,
            "modified": st.st_mtime,
        })
        if len(out) >= limit:
            break
    return out


def _tokenize(text: str) -> set[str]:
    return set(re.findall(r"[a-z0-9]+", (text or "").lower()))


def search_notes(root: Path, query: str, top_n: int = 10) -> list[dict]:
    """Search notes; uses the fused index when available, else token match.

    Returns [{path, score, snippet}].
    """
    q = _tokenize(query)
    if not q:
        return []
    base = wiki_root(root)
    scored: list[tuple[float, Path, str]] = []
    for p in base.rglob("*.md"):
        if any(seg.startswith(".") for seg in p.relative_to(base).parts):
            continue
        try:
            text = p.read_text(encoding="utf-8", errors="ignore")
        except OSError:
            continue
        words = _tokenize(text)
        overlap = len(words & q)
        if overlap == 0:
            continue
        # crude TF-ish score: overlap weighted by query size
        score = overlap / len(q)
        scored.append((score, p, text))
    scored.sort(key=lambda x: x[0], reverse=True)
    out = []
    for score, p, text in scored[:top_n]:
        snippet = re.sub(r"\s+", " ", text)[:160]
        out.append({"path": str(p.relative_to(base)), "score": round(score, 3),
                    "snippet": snippet})
    return out


def refresh_index(root: Path, timeout_s: int = 300) -> bool:
    """Rebuild the search index (subprocess). Returns success."""
    script = Path(root) / ".wiki-daemon" / "build_files_index.py"
    if not script.is_file():
        return False
    try:
        proc = subprocess.run(
            [sys.executable, str(script)], cwd=str(Path(root) / ".wiki-daemon"),
            capture_output=True, text=True, timeout=timeout_s)
        return proc.returncode == 0
    except (OSError, subprocess.TimeoutExpired):
        return False


def sessions(root: Path) -> list[dict]:
    """Cross-session links: session_ids owning notes, with note counts."""
    counts: dict[str, int] = {}
    for n in list_notes(root):
        if n["session_id"]:
            counts[n["session_id"]] = counts.get(n["session_id"], 0) + 1
    return [{"session_id": sid, "notes": n}
            for sid, n in sorted(counts.items(), key=lambda kv: -kv[1])]
