# Kadence Snippets

Small fragments to paste inside a column. Each one is complete and validated —
copy, change the `uniqueID`s, done.

For full sections see the pattern files; for whole pages see
[kadence-pages.md](kadence-pages.md).

## Heading and paragraph pair

The two blocks you will use more than all the others combined. Both are
`kadence/advancedheading` — Kadence uses one block for headings *and* body
copy, with `htmlTag` deciding which.

```html
<!-- wp:kadence/advancedheading {"uniqueID":"sn1_h","htmlTag":"h2","size":32,"mobileSize":25,"fontWeight":"700","margin":[0,0,12,0]} -->
<h2 class="kt-adv-headingsn1_h wp-block-kadence-advancedheading" data-kb-block="kb-adv-headingsn1_h">Section heading</h2>
<!-- /wp:kadence/advancedheading -->

<!-- wp:kadence/advancedheading {"uniqueID":"sn1_p","htmlTag":"p","size":17,"color":"palette4","margin":[0,0,0,0]} -->
<p class="kt-adv-headingsn1_p wp-block-kadence-advancedheading" data-kb-block="kb-adv-headingsn1_p">Supporting paragraph.</p>
<!-- /wp:kadence/advancedheading -->
```

The tag in the HTML must match `htmlTag`. Valid values: `h1`–`h6`, `p`, `span`,
`div`.

## Single button

```html
<!-- wp:kadence/advancedbtn {"uniqueID":"sn2_wrap","hAlign":"left"} -->
<div class="wp-block-kadence-advancedbtn kb-buttons-wrap kb-btnssn2_wrap"><!-- wp:kadence/singlebtn {"uniqueID":"sn2_btn","text":"Get started","link":"/signup/","inheritStyles":"fill","background":"palette1","color":"palette9"} /--></div>
<!-- /wp:kadence/advancedbtn -->
```

A button always needs the `advancedbtn` wrapper — `singlebtn` is a child block
and cannot stand alone. The wrapper is static, the button is dynamic.

## Spacer

```html
<!-- wp:kadence/spacer {"uniqueID":"sn3_sp","spacerHeight":40,"dividerEnable":false} -->
<div class="wp-block-kadence-spacer aligncenter kt-block-spacer-sn3_sp"><div class="kt-block-spacer kt-block-spacer-halign-center"></div></div>
<!-- /wp:kadence/spacer -->
```

## Divider

The same block with the divider left on, which is its default.

```html
<!-- wp:kadence/spacer {"uniqueID":"sn4_div","spacerHeight":50,"dividerStyle":"solid","dividerColor":"palette6","dividerWidth":60} -->
<div class="wp-block-kadence-spacer aligncenter kt-block-spacer-sn4_div"><div class="kt-block-spacer kt-block-spacer-halign-center"><hr class="kt-divider"/></div></div>
<!-- /wp:kadence/spacer -->
```

`dividerWidth` is a percentage by default (`dividerWidthUnits` is `%`). The
`<hr>` must be present when `dividerEnable` is true and absent when it is false.

## Standalone icon

```html
<!-- wp:kadence/icon {"uniqueID":"sn5_ic"} -->
<div class="wp-block-kadence-icon kt-svg-icons kt-svg-iconssn5_ic alignnone"><!-- wp:kadence/single-icon {"uniqueID":"sn5_si","icon":"fe_check","size":32,"color":"palette1"} -->
<div class="wp-block-kadence-single-icon kt-svg-style-default kt-svg-icon-wrap kt-svg-item-sn5_si"><span data-name="fe_check" data-stroke="2" class="kadence-dynamic-icon"></span></div>
<!-- /wp:kadence/single-icon --></div>
<!-- /wp:kadence/icon -->
```

`data-name` must equal `icon`, and `data-stroke` must equal the icon's `width`
attribute (default 2). Icon names are prefixed by set: `fe_` for Feather,
`fas_`/`far_`/`fab_` for Font Awesome solid, regular and brands.

## Checklist

```html
<!-- wp:kadence/iconlist {"uniqueID":"sn6_list","columns":1,"icon":"fe_check","listGap":10} -->
<div class="wp-block-kadence-iconlist kt-svg-icon-list-items kt-svg-icon-list-itemssn6_list kt-svg-icon-list-columns-1 alignnone"><ul class="kt-svg-icon-list"><!-- wp:kadence/listitem {"uniqueID":"sn6_i1","text":"First item"} -->
<li class="wp-block-kadence-listitem kt-svg-icon-list-item-wrap kt-svg-icon-list-item-sn6_i1"><span data-name="USE_PARENT_DEFAULT_ICON" data-stroke="USE_PARENT_DEFAULT_WIDTH" data-class="kt-svg-icon-list-single" class="kadence-dynamic-icon"></span><span class="kt-svg-icon-list-text">First item</span></li>
<!-- /wp:kadence/listitem -->

<!-- wp:kadence/listitem {"uniqueID":"sn6_i2","text":"Second item"} -->
<li class="wp-block-kadence-listitem kt-svg-icon-list-item-wrap kt-svg-icon-list-item-sn6_i2"><span data-name="USE_PARENT_DEFAULT_ICON" data-stroke="USE_PARENT_DEFAULT_WIDTH" data-class="kt-svg-icon-list-single" class="kadence-dynamic-icon"></span><span class="kt-svg-icon-list-text">Second item</span></li>
<!-- /wp:kadence/listitem --></ul></div>
<!-- /wp:kadence/iconlist -->
```

## Post grid

Dynamic, so it is one line. This is the block for "latest from the blog".

```html
<!-- wp:kadence/posts {"uniqueID":"sn7_posts","postType":"post","postsToShow":3,"columns":3,"orderBy":"date","order":"desc","image":true} /-->
```

Filter by taxonomy with `categories` (an array of term IDs) and page with
`offsetQuery`. `postType` accepts any registered post type, so this doubles as
a case-study or team grid against a custom post type.

## Collapsible overflow

For long content you want to truncate with a "show more" control.

**This block has a required inner structure.** It does not clamp whatever you
put inside it — the generated CSS targets a direct child `kadence/column`
carrying the class `kb-show-more-content`, and the toggle is a
`kadence/advancedbtn` with **exactly two** `singlebtn` children, shown and
hidden by CSS. Put bare paragraphs inside and the block validates, renders, and
silently clamps nothing.

```html
<!-- wp:kadence/show-more {"uniqueID":"sn8_more","heightDesktop":320,"heightMobile":220,"heightType":"px","enableFadeOut":true,"fadeOutSize":70,"showHideMore":true} -->
<div class="wp-block-kadence-show-more kb-block-show-more-container kb-block-show-more-containersn8_more"><div class="kb-show-more-sr-excerpt" aria-live="polite" aria-atomic="true"></div><!-- wp:kadence/column {"uniqueID":"sn8_col","className":"kb-show-more-content","kbVersion":2} -->
<div class="wp-block-kadence-column kadence-columnsn8_col kb-show-more-content"><div class="kt-inside-inner-col"><!-- wp:kadence/advancedheading {"uniqueID":"sn8_p","htmlTag":"p","size":16,"margin":[0,0,0,0]} -->
<p class="kt-adv-headingsn8_p wp-block-kadence-advancedheading" data-kb-block="kb-adv-headingsn8_p">The long content that gets clamped.</p>
<!-- /wp:kadence/advancedheading --></div></div>
<!-- /wp:kadence/column -->

<!-- wp:kadence/advancedbtn {"uniqueID":"sn8_btns","hAlign":"left","lockBtnCount":true,"className":"kb-show-more-buttons"} -->
<div class="wp-block-kadence-advancedbtn kb-buttons-wrap kb-btnssn8_btns kb-show-more-buttons"><!-- wp:kadence/singlebtn {"uniqueID":"sn8_b1","text":"Show More","hideLink":true,"sizePreset":"small","noCustomDefaults":true} /-->

<!-- wp:kadence/singlebtn {"uniqueID":"sn8_b2","text":"Show Less","hideLink":true,"sizePreset":"small","noCustomDefaults":true} /--></div>
<!-- /wp:kadence/advancedbtn --></div>
<!-- /wp:kadence/show-more -->
```

Four things are load-bearing:

- The content column needs `"className":"kb-show-more-content"` **and** that
  class in its HTML, after the generated `kadence-column{ID}`.
- The button wrapper needs `"className":"kb-show-more-buttons"`, again in both
  places.
- There must be exactly two buttons. Kadence hides the second with
  `:nth-child(2)` / `:last-of-type` rules and swaps them on click. One button
  gives you a toggle that never changes label; three breaks the CSS.
- Both buttons take `"hideLink":true` — they are toggles, not links.

The `kb-show-more-sr-excerpt` div is a screen-reader live region and is empty in
saved markup. Leave it exactly as it is, first inside the wrapper.

`heightDesktop`, `heightTablet` and `heightMobile` are separate numbers with a
shared `heightType`. Set at least the desktop one, or there is nothing to clamp
against.

## Empty section shell

The starting point for anything new. One full-width row, one column, nothing
inside.

```html
<!-- wp:kadence/rowlayout {"uniqueID":"sn9_row","columns":1,"colLayout":"equal","align":"full","inheritMaxWidth":true,"topPadding":80,"bottomPadding":80,"topPaddingM":48,"bottomPaddingM":48,"kbVersion":2} -->
<!-- wp:kadence/column {"uniqueID":"sn9_col","kbVersion":2} -->
<div class="wp-block-kadence-column kadence-columnsn9_col"><div class="kt-inside-inner-col"></div></div>
<!-- /wp:kadence/column -->
<!-- /wp:kadence/rowlayout -->
```

Everything you add goes inside `kt-inside-inner-col`.

## Two-column shell

```html
<!-- wp:kadence/rowlayout {"uniqueID":"sn10_row","columns":2,"colLayout":"equal","align":"full","inheritMaxWidth":true,"topPadding":72,"bottomPadding":72,"verticalAlignment":"middle","collapseOrder":"left-to-right","kbVersion":2} -->
<!-- wp:kadence/column {"uniqueID":"sn10_c1","verticalAlignment":"middle","kbVersion":2} -->
<div class="wp-block-kadence-column kadence-columnsn10_c1"><div class="kt-inside-inner-col"></div></div>
<!-- /wp:kadence/column -->

<!-- wp:kadence/column {"uniqueID":"sn10_c2","verticalAlignment":"middle","kbVersion":2} -->
<div class="wp-block-kadence-column kadence-columnsn10_c2"><div class="kt-inside-inner-col"></div></div>
<!-- /wp:kadence/column -->
<!-- /wp:kadence/rowlayout -->
```

The number of `kadence/column` children must equal the row's `columns`.

## Card column

A column styled as a card, for feature and pricing rows.

```html
<!-- wp:kadence/column {"uniqueID":"sn11_card","background":"#ffffff","borderRadius":[12,12,12,12],"padding":[32,28,32,28],"kbVersion":2} -->
<div class="wp-block-kadence-column kadence-columnsn11_card"><div class="kt-inside-inner-col"></div></div>
<!-- /wp:kadence/column -->
```

Card styling lives on the **column**, not on a wrapper inside it. The saved
HTML is identical to a plain column — only the JSON changes — which is why
restyling cards never risks breaking validation.

## Quick reference: what breaks

| Symptom | Cause |
|---|---|
| "Unexpected or invalid content" on a row | You wrapped `rowlayout` in divs. It saves nothing. |
| Doubled classes like `kadence-columnABC kadence-column-ABC` | Recovery ran after a bad paste |
| Attribute set but nothing changes | Wrong name or wrong type — run the linter |
| Two sections restyle together | Shared `uniqueID` |
| List text renders empty | `text` only in JSON, not in the `<span>` |
| Icon does not match | `data-name` and `icon` disagree |
