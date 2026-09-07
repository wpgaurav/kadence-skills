# Kadence Page Compositions

How to assemble whole pages from the section patterns. This file is about
**order and rhythm** — the sections themselves live in the other pattern files,
and duplicating them here would just create a second copy to keep in sync.

## The assembly rule

A Kadence page is a flat list of `kadence/rowlayout` blocks. Rows do not nest
inside rows in normal use; each row is one section, edge to edge.

```
rowlayout   hero
rowlayout   logos or stats
rowlayout   features
rowlayout   proof
rowlayout   pricing
rowlayout   FAQ
rowlayout   final CTA
```

Because every row is independent, you can reorder a page by moving whole
`<!-- wp:kadence/rowlayout … -->` … `<!-- /wp:kadence/rowlayout -->` chunks with
no other edits. That is the main practical benefit of the row-per-section
discipline, and it is worth keeping even when a section is a single line.

## Recipe 1 — SaaS landing page

| # | Section | Pattern |
|---|---|---|
| 1 | Hero, centered or split | [hero](kadence-hero.md) 1 or 2 |
| 2 | Stat row | [stats](kadence-stats.md) count-up |
| 3 | Feature grid | [features](kadence-features.md) 1 |
| 4 | Alternating detail rows ×2 | [features](kadence-features.md) 4 |
| 5 | Testimonials | [testimonials](kadence-testimonials.md) 1 |
| 6 | Pricing cards | [pricing](kadence-pricing.md) 1 |
| 7 | FAQ | [faq](kadence-faq.md) 1 |
| 8 | Final CTA | [cta](kadence-cta.md) 1 or 4 |

Alternate the row backgrounds — `palette9`, none, `palette9`, none — so
sections separate without dividers. Three consecutive white sections read as
one very long section.

## Recipe 2 — Service page

| # | Section | Pattern |
|---|---|---|
| 1 | Hero with the outcome, not the service name | [hero](kadence-hero.md) 2 |
| 2 | The problem, in the reader's words | [snippets](kadence-snippets.md) heading pair |
| 3 | What you actually do, 3 steps | [features](kadence-features.md) 1 |
| 4 | Proof — one strong quote | [testimonials](kadence-testimonials.md) 2 |
| 5 | What it costs | [pricing](kadence-pricing.md) or a spec table |
| 6 | Objections | [faq](kadence-faq.md) 1 |
| 7 | Contact form | [forms](kadence-forms.md) |

Service pages convert on specificity, so section 3 should name the deliverable
and the timeline. "Discovery, build, handover" is not a process; "two-week
audit, four-week build, written handover and a recorded walkthrough" is.

## Recipe 3 — Comparison page

| # | Section | Pattern |
|---|---|---|
| 1 | Hero stating the comparison plainly | [hero](kadence-hero.md) 1 |
| 2 | The short answer, before the table | [snippets](kadence-snippets.md) heading pair |
| 3 | Full comparison table | [table](kadence-table.md) 1 |
| 4 | Where the other tool wins | [features](kadence-features.md) 3 |
| 5 | Who each is for | [tabs](kadence-tabs.md) 1 |
| 6 | CTA | [cta](kadence-cta.md) 2 |

Section 4 is not a concession, it is what makes the rest credible. A comparison
page with no row where the competitor wins gets read as marketing and
discounted entirely.

## Recipe 4 — About page

| # | Section | Pattern |
|---|---|---|
| 1 | Hero, one sentence on why you exist | [hero](kadence-hero.md) 3 |
| 2 | The origin, honestly | [snippets](kadence-snippets.md) heading pair |
| 3 | Team grid | [snippets](kadence-snippets.md) post grid against a team CPT |
| 4 | What you believe, 3–4 items | [features](kadence-features.md) 2 |
| 5 | Numbers with dates on them | [stats](kadence-stats.md) |
| 6 | Careers or contact CTA | [cta](kadence-cta.md) 2 |

## Vertical rhythm

Padding is what makes a page feel considered. A workable scale:

| Section type | `topPadding` / `bottomPadding` | Mobile (`…M`) |
|---|---|---|
| Hero | 100–140 | 60–80 |
| Standard section | 72–80 | 44–48 |
| Compact band (CTA bar) | 40–48 | 32 |

Keep it to two or three values across a page. Six different paddings read as
accidental even when each was chosen deliberately.

## Building a page programmatically

Assemble the sections into one file and create the page with WP-CLI:

```bash
wp post create --post_type=page --post_title="Pricing" --post_status=draft --post_content="$(cat page.html)"
```

Then open it once in the editor and watch for recovery prompts. That is the
only reliable check — a page can be structurally wrong in ways nothing catches
until the editor parses it.

For a repo full of section files, validate them all in one pass first:

```bash
python3 tools/lint-attributes.py sections/*.html
python3 tools/extract-examples.py /tmp/all.html
```

## uniqueID collisions across sections

This is the failure that survives everything else. Two sections copied from the
same pattern file share every `uniqueID`, so Kadence emits one CSS rule that
matches both, and editing one section changes the other.

Nothing warns you. The blocks validate, the page renders, and the bug shows up
weeks later as "why did the pricing section change when I edited the hero".

Give each section a prefix when you assemble a page — `hero_`, `feat_`,
`price_` — and never paste the same pattern twice without renaming. The
extraction harness in `tools/extract-examples.py` does exactly this rewrite
automatically, which is the only reason all the examples in this repo can be
validated in one document.

## What not to build

**Rows inside rows.** Kadence allows it and the editor lets you do it, but
nested rows break the one-section-per-row model that makes reordering safe, and
they compound padding in ways that are hard to reason about at mobile widths.
Use a column's own padding instead.

**A page with seven sections and no proof.** The most common structural failure
is not markup, it is five sections of claims and none of evidence. If recipes 1
through 4 have anything in common, it is that proof sits in the middle, before
the price.
