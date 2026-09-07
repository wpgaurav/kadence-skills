#!/usr/bin/env python3
"""Extract ground-truth block attribute schemas from a Kadence Blocks install.

Reads every block.json shipped by the plugin and emits:
  reference/block-schema.json  - machine-readable, used by the validator
  reference/block-attributes.md - human/LLM-readable attribute tables
"""
import json
import pathlib
import sys

PLUGIN = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else "_reference/kadence-blocks")
OUT = pathlib.Path("reference")


def load_blocks():
    blocks = {}
    for path in sorted(PLUGIN.rglob("block.json")):
        try:
            data = json.loads(path.read_text())
        except json.JSONDecodeError:
            continue
        name = data.get("name")
        if not name:
            continue
        # dist/ wins over includes/ when both ship the same block
        if name in blocks and "dist" not in str(path):
            continue
        blocks[name] = {
            "name": name,
            "title": data.get("title", ""),
            "category": data.get("category", ""),
            "apiVersion": data.get("apiVersion"),
            "parent": data.get("parent"),
            "allowedBlocks": data.get("allowedBlocks"),
            "supports": data.get("supports", {}),
            "usesContext": data.get("usesContext"),
            "providesContext": data.get("providesContext"),
            "attributes": data.get("attributes", {}),
            "source": str(path.relative_to(PLUGIN)),
        }
    return blocks


def plugin_version():
    readme = PLUGIN / "readme.txt"
    for line in readme.read_text(errors="ignore").splitlines():
        if line.lower().startswith("stable tag:"):
            return line.split(":", 1)[1].strip()
    return "unknown"


def fmt_default(spec):
    if "default" not in spec:
        return ""
    return json.dumps(spec["default"])


def main():
    blocks = load_blocks()
    version = plugin_version()
    OUT.mkdir(exist_ok=True)

    (OUT / "block-schema.json").write_text(
        json.dumps({"version": version, "blocks": blocks}, indent=2, sort_keys=True) + "\n"
    )

    lines = [
        f"# Kadence Blocks Attribute Reference (v{version})",
        "",
        "Generated from the plugin's own `block.json` manifests by `tools/extract-schema.py`.",
        "Do not hand-edit. Attributes not listed here do not exist and are silently",
        "dropped by the editor on save.",
        "",
        f"**{len(blocks)} blocks.**",
        "",
        "## Index",
        "",
    ]
    for name in sorted(blocks):
        b = blocks[name]
        anchor = name.replace("/", "").replace("-", "")
        lines.append(f"- [`{name}`](#{anchor}) — {b['title']} ({len(b['attributes'])} attributes)")
    lines.append("")

    for name in sorted(blocks):
        b = blocks[name]
        lines += [f"## {name}", "", f"**{b['title']}** · category `{b['category']}` · apiVersion {b['apiVersion']}", ""]
        if b["parent"]:
            lines.append(f"- Parent-only: must be a direct child of {', '.join('`%s`' % p for p in b['parent'])}")
        if b["allowedBlocks"]:
            lines.append(f"- Allowed children: {', '.join('`%s`' % p for p in b['allowedBlocks'])}")
        if b["supports"]:
            lines.append(f"- Supports: `{json.dumps(b['supports'])}`")
        lines += ["", "| Attribute | Type | Default |", "|---|---|---|"]
        for attr in sorted(b["attributes"]):
            spec = b["attributes"][attr]
            t = spec.get("type", "")
            if isinstance(t, list):
                t = " \\| ".join(t)
            d = fmt_default(spec).replace("|", "\\|")
            lines.append(f"| `{attr}` | {t} | {'`%s`' % d if d else ''} |")
        lines.append("")

    (OUT / "block-attributes.md").write_text("\n".join(lines))
    print(f"{len(blocks)} blocks, plugin v{version}")
    print("wrote reference/block-schema.json, reference/block-attributes.md")


if __name__ == "__main__":
    main()
