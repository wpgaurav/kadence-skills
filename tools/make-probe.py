#!/usr/bin/env python3
"""Emit a minimal instance of each block so the live editor can tell us its
canonical save markup. Written comment-only on purpose: whatever the editor
adds back is the ground-truth save output."""
import json, sys, pathlib

schema = json.load(open("reference/block-schema.json"))["blocks"]

# Blocks whose children are structurally required for a meaningful probe.
CHILDREN = {
    "kadence/rowlayout":    ['kadence/column'],
    "kadence/advancedbtn":  ['kadence/singlebtn'],
    "kadence/icon":         ['kadence/single-icon'],
    "kadence/iconlist":     ['kadence/listitem'],
    "kadence/testimonials": ['kadence/testimonial'],
    "kadence/tabs":         ['kadence/tab'],
    "kadence/table":        ['kadence/table-row'],
    "kadence/table-row":    ['kadence/table-data'],
    "kadence/countdown":    ['kadence/countdown-inner'],
}
# Minimal non-uniqueID attributes some blocks need to render at all.
SEED = {
    "kadence/rowlayout":      {"columns": 1, "colLayout": "equal"},
    "kadence/advancedheading": {"htmlTag": "h2"},
    "kadence/singlebtn":      {"text": "Button"},
    "kadence/table":          {"rows": 1, "columns": 1},
}

def emit(name, n, depth=0):
    pad = "  " * depth
    attrs = {"uniqueID": f"probe{n}"}
    attrs.update(SEED.get(name, {}))
    kids = CHILDREN.get(name)
    a = json.dumps(attrs, separators=(",", ":"))
    if not kids:
        return f"{pad}<!-- wp:{name.split('/')[1] if False else name} {a} --><!-- /wp:{name} -->"
    inner = "\n".join(emit(k, f"{n}{i}", depth + 1) for i, k in enumerate(kids))
    return f"{pad}<!-- wp:{name} {a} -->\n{inner}\n{pad}<!-- /wp:{name} -->"

names = sys.argv[2:]
out = []
for i, name in enumerate(names):
    if name not in schema:
        sys.exit(f"unknown block: {name}")
    out.append(emit(name, i))
pathlib.Path(sys.argv[1]).write_text("\n\n".join(out) + "\n")
print(f"wrote {sys.argv[1]}: {len(names)} blocks")
