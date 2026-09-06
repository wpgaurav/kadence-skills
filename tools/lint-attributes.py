#!/usr/bin/env python3
"""Check that every attribute used in block markup actually exists.

The editor silently drops unknown attributes, so markup can validate 100% and
still do nothing. This catches invented attribute names before they ship.

Usage:  python3 tools/lint-attributes.py FILE [FILE ...]
"""
import json
import pathlib
import re
import sys

SCHEMA = json.load(open("reference/block-schema.json"))["blocks"]

# Blocks registered in JS without a block.json, verified by inspecting the
# plugin bundle. Kept here so the linter does not report false positives.
EXTRA = {
    "kadence/pane": {"id", "uniqueID", "title", "icon", "iconSide", "hideLabel",
                     "titleTag", "ariaLabel", "anchor", "className"},
}
# Attributes WordPress adds to every block.
UNIVERSAL = {"className", "anchor", "lock", "metadata", "align", "style"}

BLOCK = re.compile(r"<!--\s*wp:([a-z0-9-]+/[a-z0-9-]+)\s*(\{.*?\})?\s*/?-->", re.S)

# These six blocks gate their modern PHP render on `kbVersion > 1`. Without it
# the block still validates in the editor but falls back to a legacy path —
# rowlayout emits no wrapper at all. Silent, and only visible on the front end.
KB_VERSION_REQUIRED = {
    "kadence/rowlayout",
    "kadence/column",
    "kadence/infobox",
    "kadence/googlemaps",
    "kadence/advancedgallery",
    "kadence/testimonials",
}


PY_TYPE = {
    "string": str,
    "number": (int, float),
    "integer": int,
    "boolean": bool,
    "array": list,
    "object": dict,
    "null": type(None),
}


def type_ok(value, declared):
    """Booleans are ints in Python, so check bool before number."""
    if declared is None:
        return True
    wanted = declared if isinstance(declared, list) else [declared]
    for w in wanted:
        py = PY_TYPE.get(w)
        if py is None:
            return True
        if w in ("number", "integer") and isinstance(value, bool):
            continue
        if isinstance(value, py):
            return True
    return False


def known(block):
    if block in SCHEMA:
        return set(SCHEMA[block]["attributes"]) | UNIVERSAL
    if block in EXTRA:
        return EXTRA[block] | UNIVERSAL
    return None


SKIP_FENCE = re.compile(
    r"<!--\s*skip-validate\s*-->\s*\n```html\n.*?\n```", re.S)


def strip_skipped(text):
    """Blank out fenced examples marked <!-- skip-validate -->.

    Those are the deliberate "don't do this" snippets. Newlines are preserved so
    reported line numbers still point at the right place in the file.
    """
    return SKIP_FENCE.sub(lambda m: "\n" * m.group(0).count("\n"), text)


TAB_LI = re.compile(r'<li id="([^"]*)"[^>]*>\s*<a href="#([^"]*)"', re.S)


def tab_anchor(text):
    """Kadence builds a tab's anchor by deleting disallowed characters.

    Not a hyphenating slugify: "Cost per drop" -> "tab-costperdrop".
    """
    return "tab-" + re.sub(r"[^a-z0-9-]", "", text.lower())


def check_tab_anchors(arg, text, block, attrs, start, line):
    """Compare a tabs block's rendered anchors against its `titles`."""
    if block != "kadence/tabs":
        return 0
    titles = attrs.get("titles")
    if not isinstance(titles, list):
        return 0
    # The <ul> belongs to this block's own save HTML, before the next comment.
    nxt = text.find("<!-- wp:", start + 1)
    chunk = text[start: nxt if nxt != -1 else len(text)]
    found = TAB_LI.findall(chunk)
    problems = 0
    for i, title in enumerate(titles):
        if not isinstance(title, dict):
            continue
        want = title.get("anchor") or tab_anchor(title.get("text", ""))
        if i >= len(found):
            print(f"{arg}:{line}: kadence/tabs title {i + 1} "
                  f"({title.get('text','')!r}) has no matching <li>")
            problems += 1
            continue
        got_id, got_href = found[i]
        if got_id != want or got_href != want:
            print(f"{arg}:{line}: kadence/tabs title {i + 1} "
                  f"({title.get('text','')!r}) should use anchor {want!r}, "
                  f"HTML has id={got_id!r} href={got_href!r}")
            problems += 1
    return problems


def main():
    problems = 0
    seen = 0
    for arg in sys.argv[1:]:
        text = strip_skipped(pathlib.Path(arg).read_text())
        for m in BLOCK.finditer(text):
            block, raw = m.group(1), m.group(2)
            if not raw:
                continue
            if not block.startswith("kadence/"):
                continue
            try:
                attrs = json.loads(raw)
            except json.JSONDecodeError as e:
                print(f"{arg}: {block}: malformed JSON — {e}")
                problems += 1
                continue
            seen += 1
            valid = known(block)
            if valid is None:
                print(f"{arg}: unknown block {block}")
                problems += 1
                continue
            line = text[: m.start()].count("\n") + 1
            spec = SCHEMA.get(block, {}).get("attributes", {})
            if block in KB_VERSION_REQUIRED and attrs.get("kbVersion", 0) <= 1:
                print(f"{arg}:{line}: {block} needs \"kbVersion\":2 — without it "
                      f"the front end falls back to the legacy render")
                problems += 1
            for a, v in attrs.items():
                if a not in valid:
                    print(f"{arg}:{line}: {block} has no attribute `{a}`")
                    problems += 1
                elif a in spec and not type_ok(v, spec[a].get("type")):
                    want = spec[a].get("type")
                    print(f"{arg}:{line}: {block}.{a} should be {want}, "
                          f"got {json.dumps(v)[:60]}")
                    problems += 1
            problems += check_tab_anchors(arg, text, block, attrs, m.start(), line)
    print(f"\n{seen} block instances checked, {problems} problem(s)")
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
