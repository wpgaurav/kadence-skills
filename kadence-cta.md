# Kadence Call-to-Action Sections

Conversion bands you drop between content sections or at the end of a page.
All examples validate 100% against Kadence Blocks 3.7.10.

## Pattern 1 — Centered CTA band

The default. Full-bleed color, one headline, one line of copy, one button.

```html
<!-- wp:kadence/rowlayout {"uniqueID":"cta1_row","columns":1,"colLayout":"equal","align":"full","inheritMaxWidth":true,"topPadding":72,"bottomPadding":72,"topPaddingM":48,"bottomPaddingM":48,"bgColor":"palette1","kbVersion":2} -->
<!-- wp:kadence/column {"uniqueID":"cta1_col","kbVersion":2} -->
<div class="wp-block-kadence-column kadence-columncta1_col"><div class="kt-inside-inner-col"><!-- wp:kadence/advancedheading {"uniqueID":"cta1_h","htmlTag":"h2","align":"center","color":"#ffffff","size":36,"mobileSize":27,"fontWeight":"700","margin":[0,0,12,0]} -->
<h2 class="kt-adv-headingcta1_h wp-block-kadence-advancedheading" data-kb-block="kb-adv-headingcta1_h">Start with one report. Keep the whole workspace.</h2>
<!-- /wp:kadence/advancedheading -->

<!-- wp:kadence/advancedheading {"uniqueID":"cta1_p","htmlTag":"p","align":"center","color":"#e8eefc","size":18,"maxWidth":[600,"",""],"maxWidthType":"px","margin":[0,"auto",28,"auto"]} -->
<p class="kt-adv-headingcta1_p wp-block-kadence-advancedheading" data-kb-block="kb-adv-headingcta1_p">Free for 14 days, no card. Export everything on the way out if it is not for you.</p>
<!-- /wp:kadence/advancedheading -->

<!-- wp:kadence/advancedbtn {"uniqueID":"cta1_btns","hAlign":"center"} -->
<div class="wp-block-kadence-advancedbtn kb-buttons-wrap kb-btnscta1_btns"><!-- wp:kadence/singlebtn {"uniqueID":"cta1_b1","text":"Create a workspace","link":"/signup/","sizePreset":"large","inheritStyles":"fill","background":"#ffffff","color":"palette1"} /--></div>
<!-- /wp:kadence/advancedbtn --></div></div>
<!-- /wp:kadence/column -->
<!-- /wp:kadence/rowlayout -->
```

**Payoff:** one row, no nesting — this is the cheapest section in the whole
system to duplicate and re-word.

On a colored band, set text colors explicitly with hex. `palette` slots assume
the page background and will hand you dark-on-dark.

## Pattern 2 — Split CTA, copy left and button right

Reads as a bar rather than a billboard. Good mid-page, where a full billboard
would interrupt.

```html
<!-- wp:kadence/rowlayout {"uniqueID":"cta2_row","columns":2,"colLayout":"left-golden","align":"full","inheritMaxWidth":true,"topPadding":44,"bottomPadding":44,"topPaddingM":32,"bottomPaddingM":32,"bgColor":"palette8","verticalAlignment":"middle","kbVersion":2} -->
<!-- wp:kadence/column {"uniqueID":"cta2_c1","verticalAlignment":"middle","kbVersion":2} -->
<div class="wp-block-kadence-column kadence-columncta2_c1"><div class="kt-inside-inner-col"><!-- wp:kadence/advancedheading {"uniqueID":"cta2_h","htmlTag":"h2","size":26,"mobileSize":22,"fontWeight":"700","margin":[0,0,6,0]} -->
<h2 class="kt-adv-headingcta2_h wp-block-kadence-advancedheading" data-kb-block="kb-adv-headingcta2_h">Still comparing options?</h2>
<!-- /wp:kadence/advancedheading -->

<!-- wp:kadence/advancedheading {"uniqueID":"cta2_p","htmlTag":"p","color":"palette4","size":16,"margin":[0,0,0,0]} -->
<p class="kt-adv-headingcta2_p wp-block-kadence-advancedheading" data-kb-block="kb-adv-headingcta2_p">We keep a side-by-side against the four tools people usually shortlist with us.</p>
<!-- /wp:kadence/advancedheading --></div></div>
<!-- /wp:kadence/column -->

<!-- wp:kadence/column {"uniqueID":"cta2_c2","verticalAlignment":"middle","kbVersion":2} -->
<div class="wp-block-kadence-column kadence-columncta2_c2"><div class="kt-inside-inner-col"><!-- wp:kadence/advancedbtn {"uniqueID":"cta2_btns","hAlign":"right","mhAlign":"center"} -->
<div class="wp-block-kadence-advancedbtn kb-buttons-wrap kb-btnscta2_btns"><!-- wp:kadence/singlebtn {"uniqueID":"cta2_b1","text":"See the comparison","link":"/compare/","sizePreset":"standard","inheritStyles":"outline","color":"palette1"} /--></div>
<!-- /wp:kadence/advancedbtn --></div></div>
<!-- /wp:kadence/column -->
<!-- /wp:kadence/rowlayout -->
```

**Payoff:** `colLayout:"left-golden"` gives the copy roughly two thirds and the
button one third without any width attributes.

`mhAlign` centers the button on mobile, where a right-hugging button looks
broken. The breakpoint prefixes on `advancedbtn` are `t` for tablet and `m` for
mobile, giving `hAlign` / `thAlign` / `mhAlign` — not the `…M` suffix that
`rowlayout` uses for `topPaddingM`. Two blocks, two conventions.

Useful `colLayout` values for two-column rows: `equal`, `left-golden`,
`right-golden`, `left-half`, `right-half`.

## Pattern 3 — CTA with a reassurance list

For higher-friction offers, where the button alone is not enough.

```html
<!-- wp:kadence/rowlayout {"uniqueID":"cta3_row","columns":1,"colLayout":"equal","align":"full","inheritMaxWidth":true,"topPadding":72,"bottomPadding":72,"topPaddingM":48,"bottomPaddingM":48,"bgColor":"palette9","kbVersion":2} -->
<!-- wp:kadence/column {"uniqueID":"cta3_col","kbVersion":2} -->
<div class="wp-block-kadence-column kadence-columncta3_col"><div class="kt-inside-inner-col"><!-- wp:kadence/advancedheading {"uniqueID":"cta3_h","htmlTag":"h2","align":"center","size":34,"mobileSize":26,"fontWeight":"700","margin":[0,0,22,0]} -->
<h2 class="kt-adv-headingcta3_h wp-block-kadence-advancedheading" data-kb-block="kb-adv-headingcta3_h">Move your first dataset this week</h2>
<!-- /wp:kadence/advancedheading -->

<!-- wp:kadence/iconlist {"uniqueID":"cta3_list","columns":3,"mobileColumns":1,"icon":"fe_check","listGap":10} -->
<div class="wp-block-kadence-iconlist kt-svg-icon-list-items kt-svg-icon-list-itemscta3_list kt-svg-icon-list-columns-3 alignnone kt-mobile-svg-icon-list-columns-1"><ul class="kt-svg-icon-list"><!-- wp:kadence/listitem {"uniqueID":"cta3_i1","text":"Migration done for you"} -->
<li class="wp-block-kadence-listitem kt-svg-icon-list-item-wrap kt-svg-icon-list-item-cta3_i1"><span data-name="USE_PARENT_DEFAULT_ICON" data-stroke="USE_PARENT_DEFAULT_WIDTH" data-class="kt-svg-icon-list-single" class="kadence-dynamic-icon"></span><span class="kt-svg-icon-list-text">Migration done for you</span></li>
<!-- /wp:kadence/listitem -->

<!-- wp:kadence/listitem {"uniqueID":"cta3_i2","text":"Cancel any time"} -->
<li class="wp-block-kadence-listitem kt-svg-icon-list-item-wrap kt-svg-icon-list-item-cta3_i2"><span data-name="USE_PARENT_DEFAULT_ICON" data-stroke="USE_PARENT_DEFAULT_WIDTH" data-class="kt-svg-icon-list-single" class="kadence-dynamic-icon"></span><span class="kt-svg-icon-list-text">Cancel any time</span></li>
<!-- /wp:kadence/listitem -->

<!-- wp:kadence/listitem {"uniqueID":"cta3_i3","text":"Your data stays yours"} -->
<li class="wp-block-kadence-listitem kt-svg-icon-list-item-wrap kt-svg-icon-list-item-cta3_i3"><span data-name="USE_PARENT_DEFAULT_ICON" data-stroke="USE_PARENT_DEFAULT_WIDTH" data-class="kt-svg-icon-list-single" class="kadence-dynamic-icon"></span><span class="kt-svg-icon-list-text">Your data stays yours</span></li>
<!-- /wp:kadence/listitem --></ul></div>
<!-- /wp:kadence/iconlist -->

<!-- wp:kadence/spacer {"uniqueID":"cta3_sp","spacerHeight":24,"dividerEnable":false} -->
<div class="wp-block-kadence-spacer aligncenter kt-block-spacer-cta3_sp"><div class="kt-block-spacer kt-block-spacer-halign-center"></div></div>
<!-- /wp:kadence/spacer -->

<!-- wp:kadence/advancedbtn {"uniqueID":"cta3_btns","hAlign":"center"} -->
<div class="wp-block-kadence-advancedbtn kb-buttons-wrap kb-btnscta3_btns"><!-- wp:kadence/singlebtn {"uniqueID":"cta3_b1","text":"Book a migration slot","link":"/migrate/","sizePreset":"large","inheritStyles":"fill","background":"palette1","color":"palette9"} /--></div>
<!-- /wp:kadence/advancedbtn --></div></div>
<!-- /wp:kadence/column -->
<!-- /wp:kadence/rowlayout -->
```

**Payoff:** the spacer with `dividerEnable:false` gives clean vertical rhythm
without an empty paragraph block.

A spacer with the divider **on** (the default) emits an extra
`<hr class="kt-divider"/>` inside. Turning it off means removing that `<hr>`
from the HTML too — the two have to agree.

## Pattern 4 — Dark banner with background image

Highest-contrast CTA. Use once per page at most.

```html
<!-- wp:kadence/rowlayout {"uniqueID":"cta4_row","columns":1,"colLayout":"equal","align":"full","inheritMaxWidth":true,"topPadding":96,"bottomPadding":96,"topPaddingM":60,"bottomPaddingM":60,"bgImg":"https://example.com/wp-content/uploads/factory.jpg","bgImgID":0,"bgImgSize":"cover","bgImgPosition":"center center","overlay":"#07101f","overlayOpacity":70,"kbVersion":2} -->
<!-- wp:kadence/column {"uniqueID":"cta4_col","kbVersion":2} -->
<div class="wp-block-kadence-column kadence-columncta4_col"><div class="kt-inside-inner-col"><!-- wp:kadence/advancedheading {"uniqueID":"cta4_h","htmlTag":"h2","align":"center","color":"#ffffff","size":40,"mobileSize":29,"fontWeight":"700","margin":[0,0,14,0]} -->
<h2 class="kt-adv-headingcta4_h wp-block-kadence-advancedheading" data-kb-block="kb-adv-headingcta4_h">Talk to someone who has done this migration</h2>
<!-- /wp:kadence/advancedheading -->

<!-- wp:kadence/advancedheading {"uniqueID":"cta4_p","htmlTag":"p","align":"center","color":"#d7dfec","size":18,"maxWidth":[640,"",""],"maxWidthType":"px","margin":[0,"auto",30,"auto"]} -->
<p class="kt-adv-headingcta4_p wp-block-kadence-advancedheading" data-kb-block="kb-adv-headingcta4_p">Thirty minutes, an engineer not a rep, and a written plan afterwards whether or not you buy.</p>
<!-- /wp:kadence/advancedheading -->

<!-- wp:kadence/advancedbtn {"uniqueID":"cta4_btns","hAlign":"center"} -->
<div class="wp-block-kadence-advancedbtn kb-buttons-wrap kb-btnscta4_btns"><!-- wp:kadence/singlebtn {"uniqueID":"cta4_b1","text":"Book the call","link":"/call/","sizePreset":"large","inheritStyles":"fill","background":"#ffffff","color":"#07101f"} /-->

<!-- wp:kadence/singlebtn {"uniqueID":"cta4_b2","text":"Read the migration guide","link":"/docs/migrate/","sizePreset":"large","inheritStyles":"outline","color":"#ffffff"} /--></div>
<!-- /wp:kadence/advancedbtn --></div></div>
<!-- /wp:kadence/column -->
<!-- /wp:kadence/rowlayout -->
```

**Payoff:** `overlayOpacity:70` is one number to tune when the photo turns out
busier than the mockup.

## Choosing

| Position on the page | Pattern |
|---|---|
| End of a landing page | 1 or 4 |
| Between two content sections | 2 |
| After a pricing table | 3 |
| Anywhere you already used a dark band | Not 4 again |

## Anti-patterns

**Two primary buttons.** Pattern 4 pairs fill with outline for a reason. Two
filled buttons of equal weight measurably split clicks rather than adding them.

**Palette text on a hex background.** `"color":"palette1"` on a `#07101f` band
resolves to whatever the theme's palette1 is — often navy on navy.

**A CTA band with no offer.** "Learn more" pointing at the homepage is a band
that costs scroll depth and returns nothing. If there is no next step, leave the
section out.
