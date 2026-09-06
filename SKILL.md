---
name: kadence-blocks
description: Generate production-ready WordPress Gutenberg markup with Kadence Blocks 3.7.10 — heroes, feature grids, CTAs, pricing, FAQs, tabs, testimonials, tables, forms, stats and full page layouts. Use when asked to build a WordPress section, landing page, or template with Kadence.
---

# Kadence Blocks Template Creation

Produce block markup that pastes into the WordPress editor and validates on the
first try. Everything here is verified against **Kadence Blocks 3.7.10** on
WordPress 7.1.

## Read this before generating anything

Kadence markup is unforgiving in one specific way: a static block's saved HTML
must match what its `save()` function would produce, exactly. Get a class name
or a wrapper `<div>` wrong and the editor throws "This block contains
unexpected or invalid content" and offers to recover it — which strips the
user's styling.

Three rules cover most of the failure surface.

**Rule 1 — Know which blocks save HTML and which don't.** Dynamic blocks are
comment-only; writing HTML inside them makes them invalid. Static blocks
require their exact HTML. `kadence/rowlayout` is dynamic, which surprises
people: it has no `<div class="wp-block-kadence-rowlayout">` wrapper and no
`kt-row-column-wrap`. Those exist only on the rendered front end.

**Rule 2 — Class names are built from `uniqueID` with no separator, usually.**
`uniqueID` `abc123` gives `kadence-columnabc123`. A minority of blocks use a
hyphen. Both lists are in [reference/save-markup.md](reference/save-markup.md).
Never put a generated class in `className`.

**Rule 3 — Only use attributes that exist.** The editor silently discards
unknown attribute names and wrong types, so invented attributes produce markup
that validates perfectly and does nothing. Check
[reference/block-attributes.md](reference/block-attributes.md) — all 62 blocks
and 2,705 attributes, generated from the plugin's own manifests.

**Rule 4 — Six blocks need `"kbVersion":2` or they do not render properly.**
`rowlayout`, `column`, `infobox`, `googlemaps`, `advancedgallery` and
`testimonials` gate their modern PHP render on `kbVersion > 1`. Omit it and the
block still validates in the editor — but on the front end `rowlayout` emits
**no wrapper at all**, so columns stack, backgrounds vanish and padding is
ignored, while `testimonials` degrades to a bulleted list.

This is the one failure the editor cannot warn you about, because the markup is
genuinely valid. The editor sets `kbVersion` for you when you insert a block
through the UI; hand-written markup has to include it.

**Do not add `kbVersion` to any other block.** It exists only on those six. On
`image`, `advancedbtn`, `icon`, `iconlist` and everything else it is an unknown
attribute, and the editor drops it silently. The linter flags both mistakes —
missing where required, present where it is not — so run it rather than trying
to remember the list.

## Reference files

| File | What it holds |
|---|---|
| [reference/save-markup.md](reference/save-markup.md) | Exact save HTML per block, class formulas, sourced-attribute rules |
| [reference/block-attributes.md](reference/block-attributes.md) | Every attribute, type and default, generated from `block.json` |
| [reference/block-schema.json](reference/block-schema.json) | The same data, machine-readable, used by the linter |

## Pattern files

| File | Covers |
|---|---|
| [kadence-hero.md](kadence-hero.md) | Centered, split, background-image and video heroes |
| [kadence-features.md](kadence-features.md) | Feature grids, icon lists, alternating rows |
| [kadence-cta.md](kadence-cta.md) | Call-to-action bands, newsletter strips, banners |
| [kadence-pricing.md](kadence-pricing.md) | Pricing tables and comparison columns |
| [kadence-testimonials.md](kadence-testimonials.md) | Testimonial grids, carousels, logo walls |
| [kadence-faq.md](kadence-faq.md) | Accordion FAQs with schema-friendly structure |
| [kadence-tabs.md](kadence-tabs.md) | Tabbed content, the trickiest markup in the plugin |
| [kadence-table.md](kadence-table.md) | Data and comparison tables |
| [kadence-forms.md](kadence-forms.md) | Advanced Form and the legacy inline form |
| [kadence-media.md](kadence-media.md) | Images, galleries, video popups, maps |
| [kadence-stats.md](kadence-stats.md) | Count-up numbers, progress bars, countdowns |
| [kadence-pages.md](kadence-pages.md) | Whole-page compositions built from the above |
| [kadence-snippets.md](kadence-snippets.md) | Small reusable fragments and utility patterns |

## The block set

### Layout
| Block | Family | Purpose |
|---|---|---|
| `kadence/rowlayout` | dynamic | Section container, 1–6 columns |
| `kadence/column` | static | A column inside a row |

### Content
| Block | Family | Purpose |
|---|---|---|
| `kadence/advancedheading` | static | Headings *and* paragraphs |
| `kadence/advancedbtn` | static | Button group wrapper |
| `kadence/singlebtn` | dynamic | One button |
| `kadence/infobox` | static | Icon + title + text card |
| `kadence/iconlist` + `kadence/listitem` | static | Checklists |
| `kadence/icon` + `kadence/single-icon` | static | Standalone icons |
| `kadence/image` | static | Image with advanced controls |
| `kadence/spacer` | static | Spacing and dividers |
| `kadence/show-more` | static | Collapsible overflow content |

### Composite
| Block | Family | Purpose |
|---|---|---|
| `kadence/accordion` + `kadence/pane` | static | FAQs |
| `kadence/tabs` + `kadence/tab` | static | Tabbed panels |
| `kadence/testimonials` + `kadence/testimonial` | dynamic | Social proof |
| `kadence/table` + `table-row` + `table-data` | dynamic | Tables |
| `kadence/posts` | dynamic | Post grid |
| `kadence/advanced-form` | dynamic | Form by post ID |
| `kadence/countup`, `countdown`, `progress-bar` | mixed | Stats |
| `kadence/advancedgallery` | static | Galleries |
| `kadence/videopopup`, `googlemaps`, `lottie` | mixed | Embeds |

## Attributes you will use constantly

### Colors
Kadence themes expose a palette. Use `palette1` … `palette9` rather than hex
so the section follows the site's theme. `palette1`–`palette3` are usually the
brand accents, `palette4`–`palette6` neutrals/text, `palette7`–`palette9`
backgrounds from dark to light.

```
"bgColor":"palette9"     row background
"color":"palette4"       text color
"background":"palette1"  button fill
```

Hex values work too. Mixing them is fine; palette slots just survive a theme
change.

### Responsive values
Kadence has three conventions and does not use them consistently. Check the
attribute table when unsure.

- **Three-value arrays** `[desktop, tablet, mobile]` — `fontHeight`, `maxWidth`
  on `advancedheading`, `width` on `singlebtn`.
- **Four-value arrays** `[top, right, bottom, left]` — `padding`, `margin`,
  `borderRadius`.
- **Separate attributes per breakpoint** — `size` / `tabSize` / `mobileSize` on
  `advancedheading`; `topPadding` / `topPaddingM` on `rowlayout`.

There is no `tabletSize`. It is `tabSize`. This is the single most common
invented attribute.

### Row sizing
```
"align":"full"            edge-to-edge section
"inheritMaxWidth":true    constrain inner content to theme width
"maxWidth":1200           explicit inner width (number, not array)
"topPadding":100          desktop padding, number
"topPaddingM":60          mobile padding
"verticalAlignment":"middle"
```

## uniqueID discipline

Kadence emits one CSS rule per `uniqueID`. Two blocks sharing an ID share
styling, which shows up as "why did changing this section change that one".

- Give every block on the page a distinct `uniqueID`.
- Real Kadence IDs look like `123_a4b5c6`. Readable IDs (`hero_h1`) work fine
  and are easier to hand-edit.
- When you paste two examples from these files onto one page, rename the IDs in
  the second one. The examples deliberately use per-file prefixes to reduce the
  chance of collision, but they are not globally unique.

## Verifying your output

The repo ships the checks used to build it:

```bash
python3 tools/lint-attributes.py path/to/markup.html
```

catches invented attribute names and wrong types — the failures that pass
validation but silently do nothing.

```bash
python3 tools/extract-examples.py /tmp/all.html
```

pulls every example in the repo into one file for a single editor round-trip.
Validate that file against a real site (the WordPress Studio MCP
`validate_blocks` tool, or paste into an editor and watch for recovery
prompts).

```bash
python3 tools/extract-schema.py _reference/kadence-blocks
```

regenerates the attribute reference from a plugin copy. Re-run it after a
Kadence update and re-lint; that is how these docs stay honest across versions.

## When you are unsure

Prefer the pattern file over improvising. If you need a variant that is not
covered:

1. Start from the closest verified pattern.
2. Change only attributes you have confirmed in the attribute table.
3. Leave the save HTML structurally identical unless the attribute you changed
   is one the table flags as structural (`mediaType` on infobox, `columns` on
   iconlist, `paneCount` on accordion, `tabCount` on tabs).
4. Lint, then validate.

Guessing a class name is never safe. Guessing an attribute name is worse,
because nothing will tell you it was wrong.
