#!/usr/bin/env python3
"""Invariant checker for a slice of promoted mykb files.

Usage: python3 ops/reports/adversarial-reviews/check_slice.py <slice.txt>
Prints per-file violations + summary. Paths in slice.txt are relative to
components/mykb/wiki/ (e.g. devops-infra/foo.md).
"""
import re, sys, os, glob

WIKI = os.path.abspath("components/mykb/wiki")
FM_RE = re.compile(r"^---\s*\n(.*?)\n(?:---|\.\.\.)", re.DOTALL)
KEY_RE = re.compile(r"^(\w+):\s*(.*)$", re.M)
LIST_RE = re.compile(r"^\[(.*)\]$", re.S)
WIKILINK_RE = re.compile(r"\[\[([^\]|#]+)(?:#[^\]|]*)?(?:\|[^\]]+)?\]\]")
MDLINK_RE = re.compile(r"\[[^\]]*\]\(([^)\s]+\.md)(?:[^)]*)\)")
REQUIRED = ["type", "title", "description", "tags", "timestamp", "status"]
PLACEHOLDER_RE = re.compile(
    r"\b(TODO|TBD|FIXME|XXX|lorem ipsum|placeholder|coming soon|to be written|"
    r"insert [a-z ]+|your [a-z ]+ here|example\.com)\b", re.I)
# literal doc-example targets that are intentional, not broken links
DOC_EXAMPLES = {"wikilink", "wikilinks", "alpha", "file", "target", "path",
                "backlinks", "alpha:", "wiki/{area}/{page}", "wiki/concepts/...",
                "raw/archive/…", "wiki/…/overview", "-f \"$input\"", "space"}

def parse_fm(text):
    fm = {}
    m = FM_RE.match(text)
    if not m:
        return fm
    for k, v in KEY_RE.findall(m.group(1)):
        v = v.strip().strip('"').strip("'")
        lm = LIST_RE.match(v)
        fm[k] = [x.strip().strip('"').strip("'") for x in lm.group(1).split(",") if x.strip()] if lm else v
    return fm

def body_words(text):
    return len(re.sub(r"^---\s*\n.*?\n(?:---|\.\.\.)", "", text, count=1, flags=re.DOTALL).split())

def load_targets():
    existing = set()
    for p in glob.glob(f"{WIKI}/**/*.md", recursive=True):
        rel = os.path.relpath(p, WIKI)[:-3]
        existing.add(rel)
        existing.add(rel.split("/")[-1])
    return existing

def resolve(raw, existing):
    t = raw.strip()
    if t.endswith(".md"):
        t = t[:-3]
    t = t.lstrip("./").split("#")[0].strip()
    if not t or t.lower() in DOC_EXAMPLES:
        return True  # skip doc examples
    cands = [t, "wiki/" + t] if not t.startswith("wiki/") else [t]
    base = t.split("/")[-1]
    if base != t:
        cands.append(base)
    return any(c in existing for c in cands)

def main():
    slice_path = sys.argv[1]
    rels = [l.strip() for l in open(slice_path) if l.strip()]
    existing = load_targets()
    summary = {"missing": 0, "status": 0, "words": 0, "fm_keys": 0,
               "wikilinks": 0, "mdlinks": 0, "placeholders": 0, "selflinks": 0}
    rows = []
    for rel in rels:
        path = os.path.join(WIKI, rel)
        if not os.path.exists(path):
            summary["missing"] += 1
            rows.append((rel, ["MISSING FILE"]))
            continue
        try:
            text = open(path, encoding="utf-8").read()
        except UnicodeDecodeError:
            rows.append((rel, ["NON-UTF8"]))
            continue
        v = []
        fm = parse_fm(text)
        w = body_words(text)
        # status
        if fm.get("status") != "growing":
            v.append(f"status={fm.get('status')!r} (want growing)"); summary["status"] += 1
        # words
        if w < 320:
            v.append(f"words={w} (<320)"); summary["words"] += 1
        # fm keys
        missing = [k for k in REQUIRED if k not in fm]
        if missing:
            v.append(f"fm missing: {','.join(missing)}"); summary["fm_keys"] += 1
        # Summary sentence duplicated verbatim as first Details bullet
        sm = re.search(r"## Summary\s*\n(.*?)\n", text, re.DOTALL)
        dt = re.search(r"## Details\s*\n(.*?)\n", text, re.DOTALL)
        if sm and dt:
            s1 = sm.group(1).strip()
            d1 = dt.group(1).strip().splitlines()[0] if dt.group(1).strip() else ""
            if s1 and d1 and s1 in d1:
                v.append("Summary sentence duplicated in Details"); summary["fm_keys"] += 1
        # placeholders
        ph = sorted(set(PLACEHOLDER_RE.findall(text)))
        if ph:
            v.append(f"placeholders: {ph[:5]}"); summary["placeholders"] += 1
        # unclosed wikilinks ([[ without ]])
        if "[[" in text and "]]" not in text:
            v.append("unclosed [[ without ]]"); summary["wikilinks"] += 1
        # namespace-vs-type mismatch
        ns = rel.split("/")[0]
        typ = fm.get("type")
        if ns == "syntheses" and typ not in (None, "synthesis"):
            v.append(f"type={typ!r} in syntheses/ namespace"); summary["fm_keys"] += 1
        # links
        node = "wiki/" + rel[:-3]
        bad_w = []
        for m in WIKILINK_RE.finditer(text):
            tgt = m.group(1).strip()
            if tgt == node or tgt == rel[:-3]:
                summary["selflinks"] += 1
                v.append(f"self-link: [[{tgt}]]")
            elif not resolve(tgt, existing):
                bad_w.append(m.group(1).strip())
        if bad_w:
            v.append(f"broken wikilinks: {bad_w[:6]}"); summary["wikilinks"] += 1
        bad_m = []
        for m in MDLINK_RE.finditer(text):
            tgt = m.group(1).strip()
            if not resolve(tgt, existing):
                bad_m.append(m.group(1))
        if bad_m:
            v.append(f"broken md links: {bad_m[:6]}"); summary["mdlinks"] += 1
        if v:
            rows.append((rel, v))
    # print
    ok = len(rels) - len(rows)
    print(f"slice: {len(rels)} files, {ok} clean, {len(rows)} with violations")
    print(f"summary: {summary}")
    for rel, v in rows:
        print(f"  {rel}")
        for x in v:
            print(f"    - {x}")

if __name__ == "__main__":
    main()
