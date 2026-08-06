#!/usr/bin/env python3
"""COSMOS ecosystem data contracts — shared shapes + validators.

Enforces the contracts documented in contracts/README.md:

  - OKF frontmatter  (components/mykb/wiki/**/*.md)
  - files.json       (components/mykb/files.json)
  - ecosystem.json   (components/rsis3/dashboard/ecosystem.json)
  - loops.json       (components/rsis3/dashboard/loops.json)
  - telemetry JSONL  (components/rsis3/.rsis/telemetry/*.jsonl)
  - SPACE framework  (components/space/prompt-framework/framework.json)

Wired into `gen-static-data.py --check` and (telemetry section) the RSIS3
loop pipeline via `python -m rsis check-practices`.

Usage: python3 contracts/validate.py
Exits 1 on any FAIL (WARNs do not fail).
"""
from __future__ import annotations

import glob
import json
import os
import re
import sys
from datetime import datetime

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

OKF_TYPES = {
    "concept", "entity", "index", "synthesis", "decision", "question",
    "domain", "pulse", "episode", "log", "experiment", "plan", "project",
    "reflection", "source",
}
LOOP_IDS = {"L%d" % i for i in range(10)}
LOOP_STATUSES = {"n/a", "implemented", "active", "idle", "recent", "error"}
LOOP_REQUIRED = (
    "id", "name", "status", "target", "state_file", "runs", "last_run",
    "cycle", "history_len", "last_signal", "runtime", "params",
)
EVENT_TYPE = re.compile(r"^[a-z][a-z0-9_]*$")  # snake_case
LOOP_EVENT = re.compile(r"^l[1-9]_[a-z_]+$")
ISO_TS = re.compile(
    r"^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}(?:\.\d+)?(?:Z|[+-]\d{2}:\d{2})$"
)
FM_RE = re.compile(r"^---\s*\n(.*?)\n---", re.S)
KEY_RE = re.compile(r"^(\w+):\s*(.*)$", re.M)
LIST_RE = re.compile(r"^\[(.*)\]$", re.S)


def parse_frontmatter(text):
    fm = {}
    m = FM_RE.match(text or "")
    if not m:
        return fm
    for k, v in KEY_RE.findall(m.group(1)):
        v = v.strip().strip('"').strip("'")
        lm = LIST_RE.match(v)
        if lm:
            fm[k] = [x.strip().strip('"').strip("'")
                     for x in lm.group(1).split(",") if x.strip()]
        else:
            fm[k] = v
    return fm


def _issues(rows, sev, msg):
    rows.append((sev, msg))


def check_okf_frontmatter(wiki_dir, limit=8):
    """Section 1: every wiki page has frontmatter with type + title."""
    rows = []
    total = bad = warn = 0
    for p in sorted(glob.glob(os.path.join(wiki_dir, "**", "*.md"), recursive=True)):
        total += 1
        fm = parse_frontmatter(open(p, encoding="utf-8", errors="ignore").read())
        rel = os.path.relpath(p, ROOT).replace(os.sep, "/")
        if not fm:
            bad += 1
            if bad <= limit:
                _issues(rows, "FAIL", f"{rel}: missing frontmatter")
            continue
        if "type" not in fm or not fm.get("title"):
            bad += 1
            if bad <= limit:
                _issues(rows, "FAIL", f"{rel}: missing type/title")
            continue
        if fm.get("type") not in OKF_TYPES:
            _issues(rows, "WARN", f"{rel}: unknown type {fm.get('type')!r}")
            warn += 1
        for k in ("description", "tags", "timestamp", "status"):
            if k not in fm:
                warn += 1
                if warn <= limit:
                    _issues(rows, "WARN", f"{rel}: missing optional key {k}")
    rows.append(("INFO", f"okf_frontmatter: {total} pages, {bad} FAIL, {warn} WARN"))
    return rows, bad, warn


def check_files_json(path):
    """Section 2: files.json entries resolve, are unique, well-typed."""
    rows = []
    try:
        data = json.load(open(path))
    except (OSError, json.JSONDecodeError) as e:
        rows.append(("FAIL", f"files.json: unreadable ({e})"))
        return rows, 1, 0
    bad = 0
    if not isinstance(data, list):
        rows.append(("FAIL", "files.json: expected a list"))
        return rows, 1, 0
    seen = set()
    for i, e in enumerate(data):
        if not isinstance(e, dict):
            bad += 1
            rows.append(("FAIL", f"files.json[{i}]: entry not an object"))
            continue
        p = e.get("path", "")
        if (not p.endswith(".md") or p.startswith("components/")
                or p in seen or not os.path.exists(
                    os.path.join(os.path.dirname(path), p))):
            bad += 1
            rows.append(("FAIL", f"files.json: bad path {p!r}"))
        seen.add(p)
        if not isinstance(e.get("type"), str) or not isinstance(e.get("title"), str):
            bad += 1
            rows.append(("FAIL", f"files.json: type/title not string at {p}"))
        if not isinstance(e.get("tags"), list):
            bad += 1
            rows.append(("FAIL", f"files.json: tags not array at {p}"))
    rows.append(("INFO", f"files.json: {len(data)} entries, {bad} FAIL"))
    return rows, bad, 0


def check_ecosystem_json(path):
    """Section 3: ecosystem.json shape + telemetry arithmetic."""
    rows = []
    try:
        d = json.load(open(path))
    except (OSError, json.JSONDecodeError) as e:
        rows.append(("FAIL", f"ecosystem.json: unreadable ({e})"))
        return rows, 1, 0
    bad = 0
    if not isinstance(d.get("generated"), str):
        bad += 1
        rows.append(("FAIL", "ecosystem.json: missing generated"))
    comps = d.get("components", {})
    for key, want in (("mykb", {"files", "md"}), ("space", {"files"}),
                      ("rsis3", {"files"})):
        c = comps.get(key)
        if not isinstance(c, dict) or not want.issubset(c.keys()):
            bad += 1
            rows.append(("FAIL", f"ecosystem.json: components.{key} missing {want - set((c or {}).keys())}"))
        else:
            for f in want:
                if not isinstance(c[f], int) or c[f] < 0:
                    bad += 1
                    rows.append(("FAIL", f"ecosystem.json: components.{key}.{f} not int>=0"))
    tel = d.get("telemetry", {})
    for k in ("pulses", "goals", "passed", "failed", "held", "total", "improvements"):
        if not isinstance(tel.get(k), int) or tel[k] < 0:
            bad += 1
            rows.append(("FAIL", f"ecosystem.json: telemetry.{k} not int>=0"))
    if isinstance(tel.get("total"), int) and tel["total"] > 0:
        if tel.get("passed", 0) + tel.get("failed", 0) + tel.get("held", 0) != tel["total"]:
            bad += 1
            rows.append(("FAIL", "ecosystem.json: passed+failed+held != total"))
    rows.append(("INFO", f"ecosystem.json: {bad} FAIL"))
    return rows, bad, 0


def check_loops_json(path):
    """Section 4: loops.json has all ten ids with required per-loop keys."""
    rows = []
    try:
        d = json.load(open(path))
    except (OSError, json.JSONDecodeError) as e:
        rows.append(("FAIL", f"loops.json: unreadable ({e})"))
        return rows, 1, 0
    bad = 0
    if not isinstance(d.get("generated"), str):
        bad += 1
    loops = d.get("loops")
    if not isinstance(loops, list):
        rows.append(("FAIL", "loops.json: loops not a list"))
        return rows, bad + 1, 0
    ids = {e.get("id") for e in loops if isinstance(e, dict)}
    if ids != LOOP_IDS:
        bad += 1
        rows.append(("FAIL", f"loops.json: ids {ids ^ LOOP_IDS}"))
    for e in loops:
        if not isinstance(e, dict):
            bad += 1
            rows.append(("FAIL", "loops.json: entry not an object"))
            continue
        missing = [k for k in LOOP_REQUIRED if k not in e]
        if missing:
            bad += 1
            rows.append(("FAIL", f"loops.json: {e.get('id')} missing {missing}"))
        if not isinstance(e.get("runs"), int) or e["runs"] < 0:
            bad += 1
            rows.append(("FAIL", f"loops.json: {e.get('id')} runs not int>=0"))
        if e.get("status") not in LOOP_STATUSES:
            bad += 1
            rows.append(("FAIL", f"loops.json: {e.get('id')} bad status {e.get('status')!r}"))
    rows.append(("INFO", f"loops.json: {len(loops)} loops, {bad} FAIL"))
    return rows, bad, 0


def check_telemetry_dir(telemetry_dir):
    """Section 5: every jsonl line is a well-formed telemetry event."""
    rows = []
    bad = files = events = 0
    for p in sorted(glob.glob(os.path.join(telemetry_dir, "*.jsonl"))):
        files += 1
        for ln, line in enumerate(open(p, encoding="utf-8", errors="ignore")):
            if not line.strip():
                continue
            events += 1
            try:
                ev = json.loads(line)
            except json.JSONDecodeError:
                bad += 1
                if bad <= 8:
                    rows.append(("FAIL", f"{os.path.basename(p)}:{ln+1} invalid JSON"))
                continue
            if not isinstance(ev, dict):
                bad += 1
                continue
            et = ev.get("type", "")
            if not isinstance(et, str) or not EVENT_TYPE.match(et):
                bad += 1
                if bad <= 8:
                    rows.append(("FAIL", f"{os.path.basename(p)}:{ln+1} bad type {et!r}"))
            elif et.startswith("l") and not LOOP_EVENT.match(et):
                bad += 1
                if bad <= 8:
                    rows.append(("FAIL", f"{os.path.basename(p)}:{ln+1} malformed loop event {et!r}"))
            ts = ev.get("timestamp", "")
            if not isinstance(ts, str) or not ISO_TS.match(ts):
                bad += 1
                if bad <= 8:
                    rows.append(("FAIL", f"{os.path.basename(p)}:{ln+1} bad timestamp {ts!r}"))
    rows.append(("INFO", f"telemetry: {files} files, {events} events, {bad} FAIL"))
    return rows, bad, 0


def check_space_framework(path):
    """Section 6: SPACE framework definition shape + 326-probe total."""
    rows = []
    try:
        d = json.load(open(path))
    except (OSError, json.JSONDecodeError) as e:
        rows.append(("FAIL", f"framework.json: unreadable ({e})"))
        return rows, 1, 0
    bad = 0
    meta = d.get("meta")
    if not isinstance(meta, dict) or not all(
            k in meta for k in ("name", "description", "total_series",
                                "total_rounds", "total_open_ended_questions",
                                "total_multi_choice_followups")):
        bad += 1
        rows.append(("FAIL", "framework.json: meta missing required keys"))
    if not isinstance(d.get("dependency_chain"), dict) or not isinstance(
            d.get("series"), list) or not d["series"]:
        bad += 1
        rows.append(("FAIL", "framework.json: dependency_chain/series malformed"))
    else:
        oe = mc = 0
        for s in d["series"]:
            if not isinstance(s.get("id"), int) or not isinstance(
                    s.get("name"), str) or not isinstance(s.get("path"), str):
                bad += 1
                rows.append(("FAIL", f"framework.json: series {s.get('id')} malformed"))
            oe += s.get("total_open_ended", 0) or 0
            mc += s.get("total_multi_choice", 0) or 0
        if meta and isinstance(meta.get("total_open_ended_questions"), int) \
                and oe != meta["total_open_ended_questions"]:
            bad += 1
            rows.append(("FAIL", f"framework.json: open-ended total {oe} != meta {meta['total_open_ended_questions']}"))
        rows.append(("INFO", f"framework: {len(d['series'])} series, {oe} open-ended + {mc} multi-choice probes"))
    rows.append(("INFO", f"framework.json: {bad} FAIL"))
    return rows, bad, 0


def run_checks():
    """Run every section; return (rows, total_fail, total_warn)."""
    rows = []
    total_fail = total_warn = 0
    checks = [
        ("OKF frontmatter", lambda: check_okf_frontmatter(
            os.path.join(ROOT, "components", "mykb", "wiki"))),
        ("files.json", lambda: check_files_json(
            os.path.join(ROOT, "components", "mykb", "files.json"))),
        ("ecosystem.json", lambda: check_ecosystem_json(
            os.path.join(ROOT, "components", "rsis3", "dashboard", "ecosystem.json"))),
        ("loops.json", lambda: check_loops_json(
            os.path.join(ROOT, "components", "rsis3", "dashboard", "loops.json"))),
        ("telemetry", lambda: check_telemetry_dir(
            os.path.join(ROOT, "components", "rsis3", ".rsis", "telemetry"))),
        ("SPACE framework", lambda: check_space_framework(
            os.path.join(ROOT, "components", "space", "prompt-framework", "framework.json"))),
    ]
    for name, fn in checks:
        section, bad, warn = fn()
        total_fail += bad
        total_warn += warn
        rows.append((name, section, bad, warn))
    return rows, total_fail, total_warn


def main():
    rows, total_fail, total_warn = run_checks()
    for name, section, _, _ in rows:
        print(f"[{name}]")
        for sev, msg in section:
            print(f"  {msg}" if sev == "INFO" else f"  {sev}: {msg}")
    print(f"\ncontracts: {'OK' if total_fail == 0 else 'FAIL'} "
          f"({total_fail} FAIL, {total_warn} WARN)")
    return 0 if total_fail == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
