# Kadence Blocks Save Markup — Ground Truth (v3.7.10)

Verified by round-tripping every block through the real WordPress block editor
on WP 7.1 + Kadence Blocks 3.7.10. Each entry is the exact HTML the block's
`save()` emits. Getting this wrong is what triggers "This block contains
unexpected or invalid content" in the editor.

## The two block families

WordPress blocks come in two shapes, and Kadence uses both. Which family a
block belongs to decides how you write it — there is no middle ground.

**Dynamic blocks save nothing.** The block comment *is* the whole block. Write
them self-closing (`<!-- wp:name {...} /-->`) when they have no inner blocks,
or as an open/close pair wrapping only other block comments. Adding any HTML
of your own makes them invalid. The front end renders these in PHP at request
time, so nothing you write in the file affects the output.

**Static blocks save HTML.** The saved HTML must match what `save()` would
produce, character for character, or the editor flags the block as invalid.
You cannot invent class names, reorder attributes, or omit wrapper divs.

> **Dynamic (comment-only)** — `rowlayout`, `singlebtn`, `testimonials`,
> `testimonial`, `table`, `table-row`, `table-data`, `posts`, `progress-bar`,
> `tableofcontents`, `lottie`, `identity`, `vector`, `search`, `navigation`,
> `advanced-form`, and every `advanced-form-*` field block.
>
> **Static (HTML required)** — `column`, `advancedheading`, `advancedbtn`,
> `infobox`, `icon`, `single-icon`, `iconlist`, `listitem`, `image`, `spacer`,
> `accordion`, `pane`, `tabs`, `tab`, `countup`, `show-more`, `videopopup`,
> `googlemaps`, `advancedgallery`, `countdown`, `countdown-inner`, `form`.

The single most common failure in hand-written Kadence markup is wrapping
`rowlayout` in `<div class="wp-block-kadence-rowlayout">…<div class="kt-row-column-wrap">`.
That row wrapper does not exist in the saved output. Kadence builds it in PHP.

## The uniqueID rule

Every Kadence block takes a `uniqueID`. Kadence generates the per-block CSS by
matching a class built from that ID, so the class in your HTML has to match the
`uniqueID` in your JSON exactly.

**Most class formulas concatenate with no separator.** `uniqueID` `123_a4b5c6`
produces `kadence-column123_a4b5c6`, not `kadence-column-123_a4b5c6`. A few
blocks *do* use a hyphen. There is no rule to infer it from — copy the formula
from the table below.

| Block | Class formula | Separator |
|---|---|---|
| `column` | `kadence-column{ID}` | none |
| `advancedheading` | `kt-adv-heading{ID}` | none |
| `advancedbtn` | `kb-btns{ID}` | none |
| `infobox` | `kt-info-box{ID}` | none |
| `icon` | `kt-svg-icons{ID}` | none |
| `iconlist` | `kt-svg-icon-list-items{ID}` | none |
| `image` | `kb-image{ID}` | none |
| `accordion` | `kt-accordion-id{ID}` | none |
| `pane` | `kt-pane{ID}` | none |
| `tabs` | `kt-tabs-id{ID}` | none |
| `tab` | `kt-inner-tab{ID}` | none |
| `show-more` | `kb-block-show-more-container{ID}` | none |
| `videopopup` | `kadence-video-popup{ID}` | none |
| `googlemaps` | `kb-google-maps-container{ID}` | none |
| `form` | `kadence-form-{ID}` | **hyphen** |
| `single-icon` | `kt-svg-item-{ID}` | **hyphen** |
| `listitem` | `kt-svg-icon-list-item-{ID}` | **hyphen** |
| `spacer` | `kt-block-spacer-{ID}` | **hyphen** |
| `countup` | `kb-count-up-{ID}` | **hyphen** |
| `countdown` | `kb-countdown-container-{ID}` | **hyphen** |
| `countdown-inner` | `kb-countdown-inner-{ID}` | **hyphen** |
| `advancedgallery` | `kb-gallery-wrap-id-{ID}` | **hyphen** |

Never put these classes in a `className` attribute. `className` is a separate
user-facing attribute; writing the generated class there produces the doubled
output you see when a bad paste gets auto-recovered
(`kadence-columnABC kadence-column-ABC`).

## kbVersion: valid markup that still renders wrong

Six blocks branch their PHP render on `kbVersion`:

```php
if ( ! empty( $attributes['kbVersion'] ) && $attributes['kbVersion'] > 1 ) {
```

`rowlayout`, `column`, `infobox`, `googlemaps`, `advancedgallery` and
`testimonials`. **Always write `"kbVersion":2` on these.**

The failure mode is unusually nasty because nothing catches it:

| | With `kbVersion:2` | Without |
|---|---|---|
| Editor validation | Passes | Passes |
| `rowlayout` front end | `<div class="kb-row-layout-wrap kb-row-layout-id{ID} …">` + `.kt-row-column-wrap` | **Nothing** — the wrapper is dropped and children render bare |
| Columns | Grid, per `columns` | Stacked |
| Row background / padding | Applied | Ignored |
| `testimonials` | Grid or carousel | Plain `<ul>` bullets |

The generated CSS is emitted either way — Kadence writes
`#kt-layout-id{ID} > .kt-row-column-wrap { … }` regardless — so the styles are
in the page, targeting elements that were never rendered. That is why the
symptom reads as "my CSS is not applying" rather than "my block is broken".

The editor stamps `kbVersion:2` automatically on insert. Only hand-written and
generated markup is exposed to this.

## Sourced attributes live in the HTML

Some attributes are read back out of the saved HTML rather than the block
comment. For these, the HTML is authoritative — a value in the JSON that
disagrees with the HTML is discarded on parse.

| Block | Attribute | Source | Selector |
|---|---|---|---|
| `advancedheading` | `content` | html | the heading tag itself |
| `infobox` | `title` | rich-text | `.kt-blocks-info-box-title` |
| `infobox` | `contentText` | rich-text | `.kt-blocks-info-box-text` |
| `infobox` | `learnMore` | rich-text | `.kt-blocks-info-box-learnmore` |
| `infobox` | `number` | rich-text | `div.kt-blocks-info-box-number` |
| `infobox` | `link` / `target` | attribute | `a.info-box-link` |
| `listitem` | `text` | html | `.kt-svg-icon-list-text` |
| `image` | `url` / `alt` / `title` | attribute | `img` |
| `image` | `caption` | html | `figcaption` |
| `pane` | `title` | children | `.kt-blocks-accordion-title` |
| `advancedgallery` | `images` | query | `.kadence-blocks-gallery-item` |

Writing the value in both places is safe, and it is what the editor itself does
on first save. Note that the editor then *strips* the sourced key back out of
the block comment on its next round-trip, because the HTML already carries it —
so seeing `text` disappear from a `listitem`'s JSON is normal, not data loss.

Writing the value only in the JSON is the failure mode: the block validates, and
the text renders as empty.

## Per-block save markup

`{ID}` below is the block's own `uniqueID`. `⟨children⟩` is where inner block
comments go.

### kadence/rowlayout — dynamic
```html
<!-- wp:kadence/rowlayout {"uniqueID":"{ID}","columns":2,"colLayout":"equal","kbVersion":2} -->
⟨kadence/column blocks only⟩
<!-- /wp:kadence/rowlayout -->
```
No HTML. The number of `kadence/column` children must equal `columns`.

### kadence/column — static
```html
<!-- wp:kadence/column {"uniqueID":"{ID}","kbVersion":2} -->
<div class="wp-block-kadence-column kadence-column{ID}"><div class="kt-inside-inner-col">⟨children⟩</div></div>
<!-- /wp:kadence/column -->
```

### kadence/advancedheading — static
```html
<!-- wp:kadence/advancedheading {"uniqueID":"{ID}","htmlTag":"h2"} -->
<h2 class="kt-adv-heading{ID} wp-block-kadence-advancedheading" data-kb-block="kb-adv-heading{ID}">Text</h2>
<!-- /wp:kadence/advancedheading -->
```
The tag must match `htmlTag`. `p`, `span` and `div` are valid tags too.

### kadence/advancedbtn + kadence/singlebtn — static wrapper, dynamic children
```html
<!-- wp:kadence/advancedbtn {"uniqueID":"{ID}"} -->
<div class="wp-block-kadence-advancedbtn kb-buttons-wrap kb-btns{ID}"><!-- wp:kadence/singlebtn {"uniqueID":"{BTN}","text":"Get started","link":"/pricing/"} /--></div>
<!-- /wp:kadence/advancedbtn -->
```
`singlebtn` is self-closing and carries its label in the `text` attribute — it
has no anchor markup of its own.

### kadence/infobox — static
```html
<!-- wp:kadence/infobox {"uniqueID":"{ID}","title":"Heading","contentText":"Body copy.","kbVersion":2} -->
<div class="wp-block-kadence-infobox kt-info-box{ID}"><span class="kt-blocks-info-box-link-wrap info-box-link kt-blocks-info-box-media-align-top kt-info-halign-center"><div class="kt-blocks-info-box-media-container"><div class="kt-blocks-info-box-media kt-info-media-animate-none"><div class="kadence-info-box-icon-container kt-info-icon-animate-none"><div class="kadence-info-box-icon-inner-container"><span data-name="fe_aperture" data-stroke="2" data-class="kt-info-svg-icon" class="kadence-dynamic-icon"></span></div></div></div></div><div class="kt-infobox-textcontent"><h2 class="kt-blocks-info-box-title">Heading</h2><p class="kt-blocks-info-box-text">Body copy.</p></div></span></div>
<!-- /wp:kadence/infobox -->
```
The inner structure is conditional on `mediaType`, `mediaAlign`, `hAlign` and
whether a link is set. The form above is the icon/top/center default. Change
those attributes and the wrapper classes change with them — verify before
shipping a variant.

### kadence/icon + kadence/single-icon — static
```html
<!-- wp:kadence/icon {"uniqueID":"{ID}"} -->
<div class="wp-block-kadence-icon kt-svg-icons kt-svg-icons{ID} alignnone"><!-- wp:kadence/single-icon {"uniqueID":"{I}","icon":"fe_check"} -->
<div class="wp-block-kadence-single-icon kt-svg-style-default kt-svg-icon-wrap kt-svg-item-{I}"><span data-name="fe_check" data-stroke="2" class="kadence-dynamic-icon"></span></div>
<!-- /wp:kadence/single-icon --></div>
<!-- /wp:kadence/icon -->
```
`data-name` must equal the `icon` attribute.

### kadence/iconlist + kadence/listitem — static
```html
<!-- wp:kadence/iconlist {"uniqueID":"{ID}"} -->
<div class="wp-block-kadence-iconlist kt-svg-icon-list-items kt-svg-icon-list-items{ID} kt-svg-icon-list-columns-1 alignnone"><ul class="kt-svg-icon-list"><!-- wp:kadence/listitem {"uniqueID":"{LI}","text":"Item one"} -->
<li class="wp-block-kadence-listitem kt-svg-icon-list-item-wrap kt-svg-icon-list-item-{LI}"><span data-name="USE_PARENT_DEFAULT_ICON" data-stroke="USE_PARENT_DEFAULT_WIDTH" data-class="kt-svg-icon-list-single" class="kadence-dynamic-icon"></span><span class="kt-svg-icon-list-text">Item one</span></li>
<!-- /wp:kadence/listitem --></ul></div>
<!-- /wp:kadence/iconlist -->
```
`kt-svg-icon-list-columns-N` must match the `columns` attribute. The literal
strings `USE_PARENT_DEFAULT_ICON` and `USE_PARENT_DEFAULT_WIDTH` are correct —
they are placeholders Kadence resolves at render time when the item does not
override the list's icon.

### kadence/image — static
```html
<!-- wp:kadence/image {"uniqueID":"{ID}","id":42,"url":"https://example.com/a.jpg","alt":"Alt text"} -->
<figure class="wp-block-kadence-image kb-image{ID}"><img alt="Alt text" class="kb-img wp-image-42" src="https://example.com/a.jpg"/></figure>
<!-- /wp:kadence/image -->
```
`url` and `alt` are read from the `img` tag, so they must appear there.

### kadence/spacer — static
```html
<!-- wp:kadence/spacer {"uniqueID":"{ID}","spacerHeight":40} -->
<div class="wp-block-kadence-spacer aligncenter kt-block-spacer-{ID}"><div class="kt-block-spacer kt-block-spacer-halign-center"><hr class="kt-divider"/></div></div>
<!-- /wp:kadence/spacer -->
```
`dividerEnable` defaults to **true**, so the `<hr class="kt-divider"/>` above is
the default output. Drop the `<hr>` only when you also set
`"dividerEnable":false`. `aligncenter` tracks the `hAlign` attribute.

### kadence/accordion + kadence/pane — static
```html
<!-- wp:kadence/accordion {"uniqueID":"{ID}","paneCount":1} -->
<div class="wp-block-kadence-accordion alignnone"><div class="kt-accordion-wrap kt-accordion-id{ID} kt-accordion-has-1-panes kt-active-pane-0 kt-accordion-block kt-pane-header-alignment-left kt-accodion-icon-style-basic kt-accodion-icon-side-right" style="max-width:none"><div class="kt-accordion-inner-wrap" data-allow-multiple-open="false" data-start-open="0"><!-- wp:kadence/pane {"id":1,"uniqueID":"{P}"} -->
<div class="wp-block-kadence-pane kt-accordion-pane kt-accordion-pane-1 kt-pane{P}"><div class="kt-accordion-header-wrap"><button class="kt-blocks-accordion-header kt-acccordion-button-label-show" type="button"><span class="kt-blocks-accordion-title-wrap"><span class="kt-blocks-accordion-title">Question</span></span><span class="kt-blocks-accordion-icon-trigger"></span></button></div><div class="kt-accordion-panel"><div class="kt-accordion-panel-inner">⟨children⟩</div></div></div>
<!-- /wp:kadence/pane --></div></div></div>
<!-- /wp:kadence/accordion -->
```
`kt-accordion-has-N-panes` must equal `paneCount` (default 2) and the number of
`kadence/pane` children.

`kt-accordion-pane-N` comes from the pane's own **`id` attribute**, not from its
position in the list. `id` defaults to 1, so every pane after the first needs an
explicit `"id":2`, `"id":3`, … — omit it and all your panes collide on
`kt-accordion-pane-1`, which is a silent styling bug rather than a validation
error.

`kt-accodion-icon-style-basic` and `kt-accodion-icon-side-right` are misspelled
in the plugin. Reproduce the typo exactly.

### kadence/tabs + kadence/tab — static
```html
<!-- wp:kadence/tabs {"uniqueID":"{ID}","tabCount":2,"titles":[{"text":"Monthly","icon":"","iconSide":"right","onlyIcon":false,"subText":"","anchor":""},{"text":"Yearly","icon":"","iconSide":"right","onlyIcon":false,"subText":"","anchor":""}]} -->
<div class="wp-block-kadence-tabs alignnone"><div class="kt-tabs-wrap kt-tabs-id{ID} kt-tabs-has-2-tabs kt-active-tab-1 kt-tabs-layout-tabs kt-tabs-tablet-layout-inherit kt-tabs-mobile-layout-inherit kt-tab-alignment-left "><ul class="kt-tabs-title-list"><li id="tab-monthly" class="kt-title-item kt-title-item-1 kt-tabs-svg-show-always kt-tabs-icon-side-right kt-tab-title-active"><a href="#tab-monthly" data-tab="1" class="kt-tab-title kt-tab-title-1 "><span class="kt-title-text">Monthly</span></a></li><li id="tab-yearly" class="kt-title-item kt-title-item-2 kt-tabs-svg-show-always kt-tabs-icon-side-right kt-tab-title-inactive"><a href="#tab-yearly" data-tab="2" class="kt-tab-title kt-tab-title-2 "><span class="kt-title-text">Yearly</span></a></li></ul><div class="kt-tabs-content-wrap"><!-- wp:kadence/tab {"id":1,"uniqueID":"{T1}"} -->
<div class="wp-block-kadence-tab kt-tab-inner-content kt-inner-tab-1 kt-inner-tab{T1}"><div class="kt-tab-inner-content-inner">⟨children⟩</div></div>
<!-- /wp:kadence/tab -->

<!-- wp:kadence/tab {"id":2,"uniqueID":"{T2}"} -->
<div class="wp-block-kadence-tab kt-tab-inner-content kt-inner-tab-2 kt-inner-tab{T2}"><div class="kt-tab-inner-content-inner">⟨children⟩</div></div>
<!-- /wp:kadence/tab --></div></div></div>
<!-- /wp:kadence/tabs -->
```
Four things have to stay in sync, and three of them are easy to get wrong:

- `tabCount`, the length of `titles`, `kt-tabs-has-N-tabs`, and the number of
  `kadence/tab` children must all agree.
- **The `<li id>` and `<a href>` are slugified from the title text**, not from
  the tab number. `"text":"Monthly"` gives `id="tab-monthly"` and
  `href="#tab-monthly"`. You only get `tab-tab1` when the title is literally
  the default `"Tab 1"`. Set a title object's `anchor` to override the slug.
- Exactly one `<li>` carries `kt-tab-title-active`; the rest carry
  `kt-tab-title-inactive`. The active one matches `kt-active-tab-N`.
- Like accordion panes, `kt-inner-tab-N` comes from the tab's **`id` attribute**
  (default 1), so tabs after the first need an explicit `"id":2`, `"id":3`, ….

Note the trailing space inside `class="kt-tab-title kt-tab-title-1 "` and after
`kt-tab-alignment-left `. Both are real and must be reproduced.

### kadence/testimonials + kadence/testimonial — dynamic
```html
<!-- wp:kadence/testimonials {"uniqueID":"{ID}","layout":"basic","columns":[3,3,2,2,1,1],"kbVersion":2} -->
<!-- wp:kadence/testimonial {"uniqueID":"{T}","content":"Quote text.","name":"Jane Doe","occupation":"CTO"} /-->
<!-- /wp:kadence/testimonials -->
```

### kadence/table / table-row / table-data — dynamic
```html
<!-- wp:kadence/table {"uniqueID":"{ID}","columns":2} -->
<!-- wp:kadence/table-row {"uniqueID":"{R}","row":0} -->
<!-- wp:kadence/table-data {"uniqueID":"{C}","column":0} -->
<!-- wp:paragraph --><p>Cell text</p><!-- /wp:paragraph -->
<!-- /wp:kadence/table-data -->
<!-- /wp:kadence/table-row -->
<!-- /wp:kadence/table -->
```
Cells hold **inner blocks**, not a `content` attribute. `kadence/table` has no
`rows` attribute — row count comes from the number of `table-row` children.

### kadence/advanced-form — dynamic
```html
<!-- wp:kadence/advanced-form {"uniqueID":"{ID}","id":123} /-->
```
`id` is the post ID of a `kadence_form` custom post. The form's fields live in
that post, not in the page. The `advanced-form-*` field blocks are all dynamic
and belong inside the form post's content.

### kadence/form — static, legacy
The legacy inline form saves a complete `<form>` with every field rendered.
It is deprecated in favour of `advanced-form`; prefer `advanced-form` for new
work and only hand-write `kadence/form` when editing existing content.
