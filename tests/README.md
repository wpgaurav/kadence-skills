# Live page fixtures

Three complete pages built **from the pattern files**, not copied from them.
They exist to answer a question the example-level checks cannot: does following
these docs produce a page that works?

| Fixture | Exercises |
|---|---|
| `clinic-service-page.html` | 4-column row, `right-golden` / `left-golden`, progress bars, table with an icon cell and a caption, 4-pane accordion with `startCollapsed` and multiple-open, row `anchor` |
| `comparison-page.html` | 3 tabs with a nested table, `mobileLayout:"accordion"`, testimonial carousel, `show-more` with its required inner structure, dynamic post grid |
| `contact-page.html` | Advanced Form by post ID, Google Map, icon list, card column with mobile padding |

Each was validated in a real editor and rendered in a browser. All three are
deliberately in domains the pattern files do not cover, so they test whether the
docs teach rather than just supply copy-paste.

## Running them

```bash
python3 tools/lint-attributes.py tests/pages/*.html
```

Then validate the same files against a real editor. Two of them depend on site
state, so expect these to be inert rather than broken on a fresh install:

- `contact-page.html` references `kadence_form` post **9**. Create a form post
  and update the `id`.
- `comparison-page.html` uses `kadence/posts`, which needs published posts.

## What building these caught

Every one of these was a documentation bug, found only by rendering:

- `kbVersion:2` missing on six blocks — rows rendered with no wrapper at all.
- Tab anchors delete disallowed characters rather than hyphenating:
  `Cost per drop` → `tab-costperdrop`.
- `show-more` requires a `kb-show-more-content` column and a two-button
  `kb-show-more-buttons` group; without them it clamps nothing.
- `advanced-form-submit` needs `text`, which defaults to empty, giving a
  correctly styled button with no label.
- Google Maps falls back to a shared key bundled with the plugin, which is rate
  limited and fails intermittently.
