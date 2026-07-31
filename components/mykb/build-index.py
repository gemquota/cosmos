#!/usr/bin/env python3
"""Build enriched index.json from wiki/*.md frontmatter."""
import os, re, json

WIKI = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'wiki')
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'wiki', 'index.json')

entries = []

for root, dirs, files in os.walk(WIKI):
    for fn in sorted(files):
        if not fn.endswith('.md'):
            continue
        path = os.path.join(root, fn)
        rel = os.path.relpath(path, WIKI)
        try:
            text = open(path, encoding='utf-8').read()
        except:
            continue

        entry = {"path": rel}
        m = re.match(r'^---\s*\n(.*?)\n(?:---|\.\.\.)', text, re.DOTALL)
        if m:
            fm = m.group(1)
            t = re.search(r'^type:\s*"([^"]+)"', fm, re.MULTILINE)
            if t:
                entry["type"] = t.group(1)
            title = re.search(r'^title:\s*"([^"]+)"', fm, re.MULTILINE)
            if title:
                entry["title"] = title.group(1)
            tags = re.search(r'^tags:\s*\[(.*?)\]', fm, re.DOTALL)
            if tags:
                parsed = re.findall(r'"([^"]+)"', tags.group(1))
                if parsed:
                    entry["tags"] = parsed

        entries.append(entry)

with open(OUT, 'w', encoding='utf-8') as f:
    json.dump(entries, f, indent=1, ensure_ascii=False)

types = {}
for e in entries:
    t = e.get("type", "unknown")
    types[t] = types.get(t, 0) + 1

print(f"Wrote {len(entries)} entries to {OUT}")
print("Types:")
for t, c in sorted(types.items(), key=lambda x: -x[1]):
    print(f"  {t}: {c}")
