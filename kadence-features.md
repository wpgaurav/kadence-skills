# Kadence Feature Sections

Feature grids, checklists and alternating rows. Every example validates 100%
against Kadence Blocks 3.7.10.

The workhorse here is `kadence/infobox` — a static block whose **saved HTML
changes shape depending on its attributes**. That makes it the easiest Kadence
block to get subtly wrong, so read the shape rules below before editing one.

## The infobox shape rules

The wrapper element and two of its classes are computed:

| Attribute | Effect on saved HTML |
|---|---|
| `link` set | Wrapper becomes `<a class="… info-box-link" href="…">` |
| `link` empty | Wrapper stays `<span class="… info-box-link">` |
| `hAlign` | Sets `kt-info-halign-{value}` — `center`, `left`, `right` |
| `mediaAlign` | Sets `kt-blocks-info-box-media-align-{value}` — `top`, `left`, `right` |
| `mediaIcon[0].icon` | Sets the inner `<span data-name="…">` |
| `mediaIcon[0].width` | Sets `data-stroke` |

Change any of those in the JSON and you must change the HTML to match. Change
colors, padding, sizes or radii and the HTML stays put.

`mediaIcon` is an **array holding one object**, not a string:

```
"mediaIcon":[{"icon":"fe_zap","color":"palette1","size":40,"width":2,"unit":"px","hoverAnimation":"none","hoverColor":"","flipIcon":"","title":"","mobileSize":"","tabletSize":""}]
```

## Pattern 1 — Three-column icon feature grid

The default feature section. Three cards, icon on top, centered.

```html
<!-- wp:kadence/rowlayout {"uniqueID":"feat1_row","columns":3,"colLayout":"equal","align":"full","inheritMaxWidth":true,"topPadding":80,"bottomPadding":80,"topPaddingM":48,"bottomPaddingM":48,"bgColor":"palette9","columnGutter":"default","kbVersion":2} -->
<!-- wp:kadence/column {"uniqueID":"feat1_c1","kbVersion":2} -->
<div class="wp-block-kadence-column kadence-columnfeat1_c1"><div class="kt-inside-inner-col"><!-- wp:kadence/infobox {"uniqueID":"feat1_b1","mediaType":"icon","mediaIcon":[{"icon":"fe_zap","color":"palette1","size":40,"width":2,"unit":"px","hoverAnimation":"none","hoverColor":"","flipIcon":"","title":"","mobileSize":"","tabletSize":""}],"title":"Instant setup","contentText":"Connect your data source once. Everything after that is automatic.","containerBackground":"#ffffff","containerBorderRadius":10,"containerPadding":[28,24,28,24],"kbVersion":2} -->
<div class="wp-block-kadence-infobox kt-info-boxfeat1_b1"><span class="kt-blocks-info-box-link-wrap info-box-link kt-blocks-info-box-media-align-top kt-info-halign-center"><div class="kt-blocks-info-box-media-container"><div class="kt-blocks-info-box-media kt-info-media-animate-none"><div class="kadence-info-box-icon-container kt-info-icon-animate-none"><div class="kadence-info-box-icon-inner-container"><span data-name="fe_zap" data-stroke="2" data-class="kt-info-svg-icon" class="kadence-dynamic-icon"></span></div></div></div></div><div class="kt-infobox-textcontent"><h2 class="kt-blocks-info-box-title">Instant setup</h2><p class="kt-blocks-info-box-text">Connect your data source once. Everything after that is automatic.</p></div></span></div>
<!-- /wp:kadence/infobox --></div></div>
<!-- /wp:kadence/column -->

<!-- wp:kadence/column {"uniqueID":"feat1_c2","kbVersion":2} -->
<div class="wp-block-kadence-column kadence-columnfeat1_c2"><div class="kt-inside-inner-col"><!-- wp:kadence/infobox {"uniqueID":"feat1_b2","mediaType":"icon","mediaIcon":[{"icon":"fe_shield","color":"palette1","size":40,"width":2,"unit":"px","hoverAnimation":"none","hoverColor":"","flipIcon":"","title":"","mobileSize":"","tabletSize":""}],"title":"Audited access","contentText":"Every read and write is logged, with per-field permissions you can actually explain.","containerBackground":"#ffffff","containerBorderRadius":10,"containerPadding":[28,24,28,24],"kbVersion":2} -->
<div class="wp-block-kadence-infobox kt-info-boxfeat1_b2"><span class="kt-blocks-info-box-link-wrap info-box-link kt-blocks-info-box-media-align-top kt-info-halign-center"><div class="kt-blocks-info-box-media-container"><div class="kt-blocks-info-box-media kt-info-media-animate-none"><div class="kadence-info-box-icon-container kt-info-icon-animate-none"><div class="kadence-info-box-icon-inner-container"><span data-name="fe_shield" data-stroke="2" data-class="kt-info-svg-icon" class="kadence-dynamic-icon"></span></div></div></div></div><div class="kt-infobox-textcontent"><h2 class="kt-blocks-info-box-title">Audited access</h2><p class="kt-blocks-info-box-text">Every read and write is logged, with per-field permissions you can actually explain.</p></div></span></div>
<!-- /wp:kadence/infobox --></div></div>
<!-- /wp:kadence/column -->

<!-- wp:kadence/column {"uniqueID":"feat1_c3","kbVersion":2} -->
<div class="wp-block-kadence-column kadence-columnfeat1_c3"><div class="kt-inside-inner-col"><!-- wp:kadence/infobox {"uniqueID":"feat1_b3","mediaType":"icon","mediaIcon":[{"icon":"fe_trendingUp","color":"palette1","size":40,"width":2,"unit":"px","hoverAnimation":"none","hoverColor":"","flipIcon":"","title":"","mobileSize":"","tabletSize":""}],"title":"Reports that load","contentText":"Sub-second queries on ten million rows, because the aggregates are precomputed.","containerBackground":"#ffffff","containerBorderRadius":10,"containerPadding":[28,24,28,24],"kbVersion":2} -->
<div class="wp-block-kadence-infobox kt-info-boxfeat1_b3"><span class="kt-blocks-info-box-link-wrap info-box-link kt-blocks-info-box-media-align-top kt-info-halign-center"><div class="kt-blocks-info-box-media-container"><div class="kt-blocks-info-box-media kt-info-media-animate-none"><div class="kadence-info-box-icon-container kt-info-icon-animate-none"><div class="kadence-info-box-icon-inner-container"><span data-name="fe_trendingUp" data-stroke="2" data-class="kt-info-svg-icon" class="kadence-dynamic-icon"></span></div></div></div></div><div class="kt-infobox-textcontent"><h2 class="kt-blocks-info-box-title">Reports that load</h2><p class="kt-blocks-info-box-text">Sub-second queries on ten million rows, because the aggregates are precomputed.</p></div></span></div>
<!-- /wp:kadence/infobox --></div></div>
<!-- /wp:kadence/column -->
<!-- /wp:kadence/rowlayout -->
```

**Payoff:** `columns:3` on the row is the only thing you change to make it a
four-up grid — add a fourth column, bump the number, done.

Note `containerBorderRadius` is a **single number**, not a four-value array,
even though `containerPadding` next to it is a four-value array. This is the
kind of inconsistency the linter exists to catch.

## Pattern 2 — Clickable feature cards

Same grid, but each card links somewhere. The wrapper element changes from
`<span>` to `<a>`, and `hAlign` moves the text left.

```html
<!-- wp:kadence/rowlayout {"uniqueID":"feat2_row","columns":2,"colLayout":"equal","align":"full","inheritMaxWidth":true,"topPadding":70,"bottomPadding":70,"topPaddingM":40,"bottomPaddingM":40,"kbVersion":2} -->
<!-- wp:kadence/column {"uniqueID":"feat2_c1","kbVersion":2} -->
<div class="wp-block-kadence-column kadence-columnfeat2_c1"><div class="kt-inside-inner-col"><!-- wp:kadence/infobox {"uniqueID":"feat2_b1","mediaType":"icon","hAlign":"left","link":"/features/imports/","title":"Imports","contentText":"CSV, Postgres, and the six APIs you actually use.","containerBackground":"palette9","containerBorderRadius":8,"containerPadding":[24,24,24,24],"kbVersion":2} -->
<div class="wp-block-kadence-infobox kt-info-boxfeat2_b1"><a class="kt-blocks-info-box-link-wrap info-box-link kt-blocks-info-box-media-align-top kt-info-halign-left" href="/features/imports/"><div class="kt-blocks-info-box-media-container"><div class="kt-blocks-info-box-media kt-info-media-animate-none"><div class="kadence-info-box-icon-container kt-info-icon-animate-none"><div class="kadence-info-box-icon-inner-container"><span data-name="fe_aperture" data-stroke="2" data-class="kt-info-svg-icon" class="kadence-dynamic-icon"></span></div></div></div></div><div class="kt-infobox-textcontent"><h2 class="kt-blocks-info-box-title">Imports</h2><p class="kt-blocks-info-box-text">CSV, Postgres, and the six APIs you actually use.</p></div></a></div>
<!-- /wp:kadence/infobox --></div></div>
<!-- /wp:kadence/column -->

<!-- wp:kadence/column {"uniqueID":"feat2_c2","kbVersion":2} -->
<div class="wp-block-kadence-column kadence-columnfeat2_c2"><div class="kt-inside-inner-col"><!-- wp:kadence/infobox {"uniqueID":"feat2_b2","mediaType":"icon","hAlign":"left","link":"/features/exports/","title":"Exports","contentText":"Scheduled, versioned, and reproducible six months later.","containerBackground":"palette9","containerBorderRadius":8,"containerPadding":[24,24,24,24],"kbVersion":2} -->
<div class="wp-block-kadence-infobox kt-info-boxfeat2_b2"><a class="kt-blocks-info-box-link-wrap info-box-link kt-blocks-info-box-media-align-top kt-info-halign-left" href="/features/exports/"><div class="kt-blocks-info-box-media-container"><div class="kt-blocks-info-box-media kt-info-media-animate-none"><div class="kadence-info-box-icon-container kt-info-icon-animate-none"><div class="kadence-info-box-icon-inner-container"><span data-name="fe_aperture" data-stroke="2" data-class="kt-info-svg-icon" class="kadence-dynamic-icon"></span></div></div></div></div><div class="kt-infobox-textcontent"><h2 class="kt-blocks-info-box-title">Exports</h2><p class="kt-blocks-info-box-text">Scheduled, versioned, and reproducible six months later.</p></div></a></div>
<!-- /wp:kadence/infobox --></div></div>
<!-- /wp:kadence/column -->
<!-- /wp:kadence/rowlayout -->
```

**Payoff:** the whole card becomes one link target, which is better for both
click area and screen readers than a "learn more" link buried in the text.

## Pattern 3 — Checklist

`kadence/iconlist` for benefit lists. Cheaper than infoboxes when each item is
one line.

```html
<!-- wp:kadence/rowlayout {"uniqueID":"feat3_row","columns":1,"colLayout":"equal","inheritMaxWidth":true,"topPadding":60,"bottomPadding":60,"kbVersion":2} -->
<!-- wp:kadence/column {"uniqueID":"feat3_col","kbVersion":2} -->
<div class="wp-block-kadence-column kadence-columnfeat3_col"><div class="kt-inside-inner-col"><!-- wp:kadence/advancedheading {"uniqueID":"feat3_h","htmlTag":"h2","size":34,"mobileSize":26,"fontWeight":"700","margin":[0,0,20,0]} -->
<h2 class="kt-adv-headingfeat3_h wp-block-kadence-advancedheading" data-kb-block="kb-adv-headingfeat3_h">What you get on every plan</h2>
<!-- /wp:kadence/advancedheading -->

<!-- wp:kadence/iconlist {"uniqueID":"feat3_list","columns":2,"mobileColumns":1,"icon":"fe_check","listGap":12} -->
<div class="wp-block-kadence-iconlist kt-svg-icon-list-items kt-svg-icon-list-itemsfeat3_list kt-svg-icon-list-columns-2 alignnone kt-mobile-svg-icon-list-columns-1"><ul class="kt-svg-icon-list"><!-- wp:kadence/listitem {"uniqueID":"feat3_i1","text":"Unlimited projects"} -->
<li class="wp-block-kadence-listitem kt-svg-icon-list-item-wrap kt-svg-icon-list-item-feat3_i1"><span data-name="USE_PARENT_DEFAULT_ICON" data-stroke="USE_PARENT_DEFAULT_WIDTH" data-class="kt-svg-icon-list-single" class="kadence-dynamic-icon"></span><span class="kt-svg-icon-list-text">Unlimited projects</span></li>
<!-- /wp:kadence/listitem -->

<!-- wp:kadence/listitem {"uniqueID":"feat3_i2","text":"Daily backups kept 30 days"} -->
<li class="wp-block-kadence-listitem kt-svg-icon-list-item-wrap kt-svg-icon-list-item-feat3_i2"><span data-name="USE_PARENT_DEFAULT_ICON" data-stroke="USE_PARENT_DEFAULT_WIDTH" data-class="kt-svg-icon-list-single" class="kadence-dynamic-icon"></span><span class="kt-svg-icon-list-text">Daily backups kept 30 days</span></li>
<!-- /wp:kadence/listitem -->

<!-- wp:kadence/listitem {"uniqueID":"feat3_i3","text":"SSO on every tier"} -->
<li class="wp-block-kadence-listitem kt-svg-icon-list-item-wrap kt-svg-icon-list-item-feat3_i3"><span data-name="USE_PARENT_DEFAULT_ICON" data-stroke="USE_PARENT_DEFAULT_WIDTH" data-class="kt-svg-icon-list-single" class="kadence-dynamic-icon"></span><span class="kt-svg-icon-list-text">SSO on every tier</span></li>
<!-- /wp:kadence/listitem -->

<!-- wp:kadence/listitem {"uniqueID":"feat3_i4","text":"No per-seat pricing"} -->
<li class="wp-block-kadence-listitem kt-svg-icon-list-item-wrap kt-svg-icon-list-item-feat3_i4"><span data-name="USE_PARENT_DEFAULT_ICON" data-stroke="USE_PARENT_DEFAULT_WIDTH" data-class="kt-svg-icon-list-single" class="kadence-dynamic-icon"></span><span class="kt-svg-icon-list-text">No per-seat pricing</span></li>
<!-- /wp:kadence/listitem --></ul></div>
<!-- /wp:kadence/iconlist --></div></div>
<!-- /wp:kadence/column -->
<!-- /wp:kadence/rowlayout -->
```

**Payoff:** `columns:2` on the list makes a two-up checklist without a second
row or column — the `<ul>` handles it.

Three rules for icon lists:

- `kt-svg-icon-list-columns-N` in the class **must** match the `columns`
  attribute. Nothing warns you when they drift.
- Setting `tabletColumns` or `mobileColumns` **adds another class** —
  `kt-tablet-svg-icon-list-columns-N` and `kt-mobile-svg-icon-list-columns-N`,
  appended after `alignnone`. Omit the attribute and omit the class; set one and
  you must add its class too.
- `listGap` is a plain number (pixels). Not an array.
- Each item's `text` lives in **both** the JSON and the
  `<span class="kt-svg-icon-list-text">`. The HTML wins; the editor drops the
  JSON copy on its next save, which is expected and harmless.

The literal `USE_PARENT_DEFAULT_ICON` and `USE_PARENT_DEFAULT_WIDTH` strings are
correct. They tell Kadence to inherit the list's `icon` and stroke width. Only
replace them when an individual item overrides the icon.

## Pattern 4 — Alternating image and text rows

For explaining three or four capabilities in sequence. Flip `collapseOrder` per
row so mobile always reads text-then-image.

```html
<!-- wp:kadence/rowlayout {"uniqueID":"feat4_row","columns":2,"colLayout":"equal","align":"full","inheritMaxWidth":true,"topPadding":70,"bottomPadding":70,"verticalAlignment":"middle","collapseOrder":"right-to-left","kbVersion":2} -->
<!-- wp:kadence/column {"uniqueID":"feat4_c1","verticalAlignment":"middle","kbVersion":2} -->
<div class="wp-block-kadence-column kadence-columnfeat4_c1"><div class="kt-inside-inner-col"><!-- wp:kadence/image {"uniqueID":"feat4_img","id":0,"borderRadius":[8,8,8,8]} -->
<figure class="wp-block-kadence-image kb-imagefeat4_img"><img src="https://example.com/wp-content/uploads/schedule.png" alt="Schedule editor with three recurring exports configured" class="kb-img"/></figure>
<!-- /wp:kadence/image --></div></div>
<!-- /wp:kadence/column -->

<!-- wp:kadence/column {"uniqueID":"feat4_c2","verticalAlignment":"middle","kbVersion":2} -->
<div class="wp-block-kadence-column kadence-columnfeat4_c2"><div class="kt-inside-inner-col"><!-- wp:kadence/advancedheading {"uniqueID":"feat4_h","htmlTag":"h3","size":30,"mobileSize":24,"fontWeight":"700","margin":[0,0,14,0]} -->
<h3 class="kt-adv-headingfeat4_h wp-block-kadence-advancedheading" data-kb-block="kb-adv-headingfeat4_h">Schedules that survive a rename</h3>
<!-- /wp:kadence/advancedheading -->

<!-- wp:kadence/advancedheading {"uniqueID":"feat4_p","htmlTag":"p","color":"palette4","size":17,"margin":[0,0,0,0]} -->
<p class="kt-adv-headingfeat4_p wp-block-kadence-advancedheading" data-kb-block="kb-adv-headingfeat4_p">Exports bind to column IDs, not column names. Rename a field upstream and nothing downstream breaks.</p>
<!-- /wp:kadence/advancedheading --></div></div>
<!-- /wp:kadence/column -->
<!-- /wp:kadence/rowlayout -->
```

**Payoff:** `collapseOrder:"right-to-left"` puts the text column first on
mobile even though the image is first in source order — no duplicate blocks.

For the next row down, swap the column contents and set
`"collapseOrder":"left-to-right"`.

## Picking a pattern

| Feature count | Each needs | Use |
|---|---|---|
| 3–6, one line each | An icon | Pattern 1 |
| 3–6, each links to a page | An icon and a target | Pattern 2 |
| 6–12, terse | Nothing but a tick | Pattern 3 |
| 2–4, each needs explaining | A screenshot | Pattern 4 |

## Limits worth knowing

Infobox does not do equal-height cards on its own. In a three-column row with
uneven copy, the cards will differ in height unless the theme stretches them.
Either keep the copy lengths close, or set the column's `verticalAlignment` and
accept the gap.

There is no built-in hover-lift. `containerHoverBackground` and the hover color
attributes exist, but transform effects need custom CSS.

`mediaType:"image"` works but changes the media container markup substantially.
Probe it against a real editor before shipping a batch of image-media infoboxes
rather than adapting the icon markup by hand.
