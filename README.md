# Kadence Skills

[![Buy me a coffee](https://img.shields.io/badge/Buy%20me%20a%20coffee-FFDD00?style=flat&logo=buymeacoffee&logoColor=black)](https://buymeacoffee.com/gauravtiwari)

An [Agent Skill](https://code.claude.com/docs/en/skills) that teaches an AI to
generate WordPress Gutenberg markup with **Kadence Blocks 3.7.10** — heroes,
feature grids, CTAs, pricing, FAQs, tabs, tables, forms, stats and whole pages.

Every example is verified two ways: against the plugin's own attribute
manifests, and against a real WordPress block editor.

## Why this repo ships tooling, not just prose

Kadence markup fails in two ways that look like success:

1. **Invalid save HTML.** Static blocks must reproduce their `save()` output
   exactly. Miss a class and the editor offers to "recover" the block, which
   strips the user's styling.
2. **Valid markup that renders wrong.** Unknown attributes are dropped silently,
   and six blocks skip their modern render entirely without `"kbVersion":2` —
   `rowlayout` then emits no wrapper at all, so columns stack and backgrounds
   vanish. Nothing warns you; the block validates perfectly.

The second class of bug is invisible to validation, so the repo carries a
linter, a schema generator and live page fixtures to catch it.

## Requirements

| For | You need |
|---|---|
| Using the skill | An agent that reads `SKILL.md` — Claude Code, Claude Desktop, or any tool that loads Agent Skills |
| Running the linter | Python 3.8+ (no third-party packages) |
| Regenerating the schema | A copy of the Kadence Blocks plugin |
| Editor validation | A WordPress site with Kadence Blocks — [WordPress Studio](https://developer.wordpress.com/studio/) is the easiest |

Only the first is needed to use the skill. The committed
`reference/block-schema.json` means the linter works immediately, with no
plugin download.

## Installation

### As a Claude Code skill

The skill is named `kadence-blocks`, so the **directory must be named
`kadence-blocks`** even though the repo is `kadence-skills`.

Personal, available in every project:

```bash
git clone https://github.com/wpgaurav/kadence-skills.git ~/.claude/skills/kadence-blocks
```

Or project-scoped, so it ships with a repo and works for the whole team:

```bash
git clone https://github.com/wpgaurav/kadence-skills.git .claude/skills/kadence-blocks
```

Start a new Claude Code session so the skill is picked up. It then activates on
its own when you ask for Kadence work — "build a hero section with Kadence",
"make a pricing page", "why is this Kadence block broken" — or you can invoke it
directly by name with `/kadence-blocks`.

### Keeping it as a repo you can edit

If you plan to update the docs (recommended — that is what the tooling is for),
clone it somewhere you work and symlink instead, so `git pull` and edits are the
same tree the agent reads:

```bash
git clone https://github.com/wpgaurav/kadence-skills.git ~/Development/kadence-skills
ln -s ~/Development/kadence-skills ~/.claude/skills/kadence-blocks
```

### For other agents

The skill is plain Markdown with YAML frontmatter, so any tool that loads Agent
Skills can use it. Point it at the repo root; `SKILL.md` is the entry point and
links to everything else.

```bash
# Example: shared skills directory used by several agents
git clone https://github.com/wpgaurav/kadence-skills.git <skills-dir>/kadence-blocks
```

### Optional: plugin source, for regenerating the reference

Needed only when a new Kadence version ships. The extracted plugin is ~46 MB and
is **not** committed.

```bash
cd kadence-skills
curl -sL -o /tmp/kb.zip https://downloads.wordpress.org/plugin/kadence-blocks.3.7.10.zip
unzip -q /tmp/kb.zip -d _reference/
echo "_reference/" >> .git/info/exclude
```

### Optional: a site for editor validation

Validation needs a real block editor. With WordPress Studio, create a site and:

```bash
wp plugin install kadence-blocks --activate
wp theme install kadence --activate
```

### Verify the install

From the repo root:

```bash
./tools/check.sh
```

Expect `0 problem(s)` on both the docs and the fixtures. The linter reads
`reference/block-schema.json` relative to the repo root, so run it from there.

## Layout

```
SKILL.md                  Entry point: the rules, the block families, the router
kadence-*.md              Section patterns (hero, features, CTA, pricing, …)
reference/
  block-attributes.md     Every attribute, type and default — generated
  block-schema.json       The same data, machine-readable — used by the linter
  save-markup.md          Exact save HTML per block, verified by round-trip
tests/
  pages/                  Three full pages built from the docs, as regression fixtures
tools/
  extract-schema.py       Regenerate the reference from a plugin copy
  lint-attributes.py      Catch invented attributes, wrong types, missing kbVersion, bad tab anchors
  extract-examples.py     Pull every example into one file for editor validation
  add-kbversion.py        Bulk-add "kbVersion":2 where it is required
  make-probe.py           Emit minimal block instances to discover save markup
  check.sh                Run the static checks
```

## Pattern files

| File | Covers |
|---|---|
| [kadence-hero.md](kadence-hero.md) | Centered, split, background-image, video heroes |
| [kadence-features.md](kadence-features.md) | Feature grids, checklists, alternating rows |
| [kadence-cta.md](kadence-cta.md) | CTA bands, bars, dark banners |
| [kadence-pricing.md](kadence-pricing.md) | Pricing cards and comparison layouts |
| [kadence-testimonials.md](kadence-testimonials.md) | Grids, single quotes, carousels |
| [kadence-faq.md](kadence-faq.md) | Accordion FAQs |
| [kadence-tabs.md](kadence-tabs.md) | Tabbed panels |
| [kadence-table.md](kadence-table.md) | Data and comparison tables |
| [kadence-forms.md](kadence-forms.md) | Advanced Form and the legacy block |
| [kadence-media.md](kadence-media.md) | Images, galleries, video popups, maps |
| [kadence-stats.md](kadence-stats.md) | Count-ups, progress bars, countdowns |
| [kadence-pages.md](kadence-pages.md) | Whole-page recipes and section order |
| [kadence-snippets.md](kadence-snippets.md) | Small reusable fragments |

## Verifying changes

```bash
./tools/check.sh
```

runs the linter over every pattern file and fixture, then extracts all examples
into one document. Validate that document against a real editor — the WordPress
Studio MCP `validate_blocks` tool does it directly. Anything that comes back
with an auto-fix means a pattern file is wrong; correct the source `.md`, never
the extracted file.

Examples deliberately showing broken markup are excluded from both checks with
`<!-- skip-validate -->` on the line before the fence.

`tests/pages/` holds three complete pages built from the docs rather than copied
from them — see [tests/README.md](tests/README.md). Example-level checks prove
the snippets are valid; those pages prove the docs actually teach. Every
render-only bug found so far came from that second test, not the first.

## Updating for a new Kadence release

```bash
curl -sL -o /tmp/kb.zip https://downloads.wordpress.org/plugin/kadence-blocks.<version>.zip
unzip -q /tmp/kb.zip -d _reference/
python3 tools/extract-schema.py _reference/kadence-blocks
./tools/check.sh
```

`extract-schema.py` rewrites `reference/block-attributes.md` and
`reference/block-schema.json` from the new manifests, so the linter immediately
reflects added, removed and retyped attributes. Then re-validate every example
and every fixture against an editor running the new version.

Two things are version-coupled and worth re-checking by hand after an upgrade:
the six blocks that require `kbVersion:2`, and the tab-anchor rule. Both are
derived from plugin internals rather than from the manifests.

## Support This Project

Kadence Skills is free to use and teaches an AI agent to write Kadence Blocks 3.7.10 markup for WordPress, from heroes and pricing sections to whole pages. Whenever a new Kadence version ships, I regenerate the schema from its manifests and check every example again in a real block editor.

If the linter caught a missing kbVersion attribute before your Kadence columns stacked on a live page, you can buy me a coffee.

<a href="https://buymeacoffee.com/gauravtiwari"><img src="https://cdn.buymeacoffee.com/buttons/v2/default-yellow.png" alt="Buy me a coffee" height="50"></a>

I'd appreciate a star on the repo, and if the agent hands you Kadence markup that fails in the editor or renders wrong on the page, you can open an issue with your prompt and the markup it returned.

## A note on the plugin

Kadence Blocks itself is **not** redistributed here. `_reference/` is excluded
from version control and has to be downloaded separately from WordPress.org; the
plugin is GPLv2-or-later.

What is committed is derived from it: `reference/block-schema.json` and
`reference/block-attributes.md` are generated from the plugin's `block.json`
manifests, and `reference/save-markup.md` records save output observed by
round-tripping blocks through the editor.

This repo has no `LICENSE` file yet. Add one before sharing it widely.
