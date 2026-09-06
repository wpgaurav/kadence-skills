# Kadence Pricing Sections

Kadence has no dedicated pricing-table block. You build one from a row of
columns, and that is genuinely the right approach — a pricing card is a
heading, a number, a list and a button, all of which are blocks you already
have.

Two shapes cover almost every case: **cards** when the plans differ in kind,
and a **comparison table** when they differ only in limits. If you need both,
lead with cards and put the table below.

## Pattern 1 — Three-tier cards

```html
<!-- wp:kadence/rowlayout {"uniqueID":"price1_row","columns":3,"colLayout":"equal","align":"full","inheritMaxWidth":true,"topPadding":80,"bottomPadding":80,"topPaddingM":48,"bottomPaddingM":48,"bgColor":"palette9","columnGutter":"default","kbVersion":2} -->
<!-- wp:kadence/column {"uniqueID":"price1_c1","background":"#ffffff","borderRadius":[12,12,12,12],"padding":[32,28,32,28],"kbVersion":2} -->
<div class="wp-block-kadence-column kadence-columnprice1_c1"><div class="kt-inside-inner-col"><!-- wp:kadence/advancedheading {"uniqueID":"price1_t1","htmlTag":"h3","size":20,"fontWeight":"600","color":"palette4","margin":[0,0,6,0]} -->
<h3 class="kt-adv-headingprice1_t1 wp-block-kadence-advancedheading" data-kb-block="kb-adv-headingprice1_t1">Starter</h3>
<!-- /wp:kadence/advancedheading -->

<!-- wp:kadence/advancedheading {"uniqueID":"price1_n1","htmlTag":"p","size":44,"mobileSize":36,"fontWeight":"700","margin":[0,0,4,0]} -->
<p class="kt-adv-headingprice1_n1 wp-block-kadence-advancedheading" data-kb-block="kb-adv-headingprice1_n1">$29</p>
<!-- /wp:kadence/advancedheading -->

<!-- wp:kadence/advancedheading {"uniqueID":"price1_s1","htmlTag":"p","size":14,"color":"palette5","margin":[0,0,22,0]} -->
<p class="kt-adv-headingprice1_s1 wp-block-kadence-advancedheading" data-kb-block="kb-adv-headingprice1_s1">per month, billed monthly</p>
<!-- /wp:kadence/advancedheading -->

<!-- wp:kadence/iconlist {"uniqueID":"price1_l1","columns":1,"icon":"fe_check","listGap":10} -->
<div class="wp-block-kadence-iconlist kt-svg-icon-list-items kt-svg-icon-list-itemsprice1_l1 kt-svg-icon-list-columns-1 alignnone"><ul class="kt-svg-icon-list"><!-- wp:kadence/listitem {"uniqueID":"price1_l1a","text":"1 million rows"} -->
<li class="wp-block-kadence-listitem kt-svg-icon-list-item-wrap kt-svg-icon-list-item-price1_l1a"><span data-name="USE_PARENT_DEFAULT_ICON" data-stroke="USE_PARENT_DEFAULT_WIDTH" data-class="kt-svg-icon-list-single" class="kadence-dynamic-icon"></span><span class="kt-svg-icon-list-text">1 million rows</span></li>
<!-- /wp:kadence/listitem -->

<!-- wp:kadence/listitem {"uniqueID":"price1_l1b","text":"Daily exports"} -->
<li class="wp-block-kadence-listitem kt-svg-icon-list-item-wrap kt-svg-icon-list-item-price1_l1b"><span data-name="USE_PARENT_DEFAULT_ICON" data-stroke="USE_PARENT_DEFAULT_WIDTH" data-class="kt-svg-icon-list-single" class="kadence-dynamic-icon"></span><span class="kt-svg-icon-list-text">Daily exports</span></li>
<!-- /wp:kadence/listitem -->

<!-- wp:kadence/listitem {"uniqueID":"price1_l1c","text":"Email support, 2 business days"} -->
<li class="wp-block-kadence-listitem kt-svg-icon-list-item-wrap kt-svg-icon-list-item-price1_l1c"><span data-name="USE_PARENT_DEFAULT_ICON" data-stroke="USE_PARENT_DEFAULT_WIDTH" data-class="kt-svg-icon-list-single" class="kadence-dynamic-icon"></span><span class="kt-svg-icon-list-text">Email support, 2 business days</span></li>
<!-- /wp:kadence/listitem --></ul></div>
<!-- /wp:kadence/iconlist -->

<!-- wp:kadence/spacer {"uniqueID":"price1_sp1","spacerHeight":20,"dividerEnable":false} -->
<div class="wp-block-kadence-spacer aligncenter kt-block-spacer-price1_sp1"><div class="kt-block-spacer kt-block-spacer-halign-center"></div></div>
<!-- /wp:kadence/spacer -->

<!-- wp:kadence/advancedbtn {"uniqueID":"price1_b1","hAlign":"left"} -->
<div class="wp-block-kadence-advancedbtn kb-buttons-wrap kb-btnsprice1_b1"><!-- wp:kadence/singlebtn {"uniqueID":"price1_b1a","text":"Start on Starter","link":"/signup/?plan=starter","inheritStyles":"outline","color":"palette1","width":["100%","",""]} /--></div>
<!-- /wp:kadence/advancedbtn --></div></div>
<!-- /wp:kadence/column -->

<!-- wp:kadence/column {"uniqueID":"price1_c2","background":"#ffffff","borderRadius":[12,12,12,12],"padding":[32,28,32,28],"borderWidth":[2,2,2,2],"border":"palette1","kbVersion":2} -->
<div class="wp-block-kadence-column kadence-columnprice1_c2"><div class="kt-inside-inner-col"><!-- wp:kadence/advancedheading {"uniqueID":"price1_t2","htmlTag":"h3","size":20,"fontWeight":"600","color":"palette1","margin":[0,0,6,0]} -->
<h3 class="kt-adv-headingprice1_t2 wp-block-kadence-advancedheading" data-kb-block="kb-adv-headingprice1_t2">Team — most chosen</h3>
<!-- /wp:kadence/advancedheading -->

<!-- wp:kadence/advancedheading {"uniqueID":"price1_n2","htmlTag":"p","size":44,"mobileSize":36,"fontWeight":"700","margin":[0,0,4,0]} -->
<p class="kt-adv-headingprice1_n2 wp-block-kadence-advancedheading" data-kb-block="kb-adv-headingprice1_n2">$99</p>
<!-- /wp:kadence/advancedheading -->

<!-- wp:kadence/advancedheading {"uniqueID":"price1_s2","htmlTag":"p","size":14,"color":"palette5","margin":[0,0,22,0]} -->
<p class="kt-adv-headingprice1_s2 wp-block-kadence-advancedheading" data-kb-block="kb-adv-headingprice1_s2">per month, billed monthly</p>
<!-- /wp:kadence/advancedheading -->

<!-- wp:kadence/iconlist {"uniqueID":"price1_l2","columns":1,"icon":"fe_check","listGap":10} -->
<div class="wp-block-kadence-iconlist kt-svg-icon-list-items kt-svg-icon-list-itemsprice1_l2 kt-svg-icon-list-columns-1 alignnone"><ul class="kt-svg-icon-list"><!-- wp:kadence/listitem {"uniqueID":"price1_l2a","text":"50 million rows"} -->
<li class="wp-block-kadence-listitem kt-svg-icon-list-item-wrap kt-svg-icon-list-item-price1_l2a"><span data-name="USE_PARENT_DEFAULT_ICON" data-stroke="USE_PARENT_DEFAULT_WIDTH" data-class="kt-svg-icon-list-single" class="kadence-dynamic-icon"></span><span class="kt-svg-icon-list-text">50 million rows</span></li>
<!-- /wp:kadence/listitem -->

<!-- wp:kadence/listitem {"uniqueID":"price1_l2b","text":"Hourly exports"} -->
<li class="wp-block-kadence-listitem kt-svg-icon-list-item-wrap kt-svg-icon-list-item-price1_l2b"><span data-name="USE_PARENT_DEFAULT_ICON" data-stroke="USE_PARENT_DEFAULT_WIDTH" data-class="kt-svg-icon-list-single" class="kadence-dynamic-icon"></span><span class="kt-svg-icon-list-text">Hourly exports</span></li>
<!-- /wp:kadence/listitem -->

<!-- wp:kadence/listitem {"uniqueID":"price1_l2c","text":"4-hour support response"} -->
<li class="wp-block-kadence-listitem kt-svg-icon-list-item-wrap kt-svg-icon-list-item-price1_l2c"><span data-name="USE_PARENT_DEFAULT_ICON" data-stroke="USE_PARENT_DEFAULT_WIDTH" data-class="kt-svg-icon-list-single" class="kadence-dynamic-icon"></span><span class="kt-svg-icon-list-text">4-hour support response</span></li>
<!-- /wp:kadence/listitem --></ul></div>
<!-- /wp:kadence/iconlist -->

<!-- wp:kadence/spacer {"uniqueID":"price1_sp2","spacerHeight":20,"dividerEnable":false} -->
<div class="wp-block-kadence-spacer aligncenter kt-block-spacer-price1_sp2"><div class="kt-block-spacer kt-block-spacer-halign-center"></div></div>
<!-- /wp:kadence/spacer -->

<!-- wp:kadence/advancedbtn {"uniqueID":"price1_b2","hAlign":"left"} -->
<div class="wp-block-kadence-advancedbtn kb-buttons-wrap kb-btnsprice1_b2"><!-- wp:kadence/singlebtn {"uniqueID":"price1_b2a","text":"Start on Team","link":"/signup/?plan=team","inheritStyles":"fill","background":"palette1","color":"palette9","width":["100%","",""]} /--></div>
<!-- /wp:kadence/advancedbtn --></div></div>
<!-- /wp:kadence/column -->

<!-- wp:kadence/column {"uniqueID":"price1_c3","background":"#ffffff","borderRadius":[12,12,12,12],"padding":[32,28,32,28],"kbVersion":2} -->
<div class="wp-block-kadence-column kadence-columnprice1_c3"><div class="kt-inside-inner-col"><!-- wp:kadence/advancedheading {"uniqueID":"price1_t3","htmlTag":"h3","size":20,"fontWeight":"600","color":"palette4","margin":[0,0,6,0]} -->
<h3 class="kt-adv-headingprice1_t3 wp-block-kadence-advancedheading" data-kb-block="kb-adv-headingprice1_t3">Enterprise</h3>
<!-- /wp:kadence/advancedheading -->

<!-- wp:kadence/advancedheading {"uniqueID":"price1_n3","htmlTag":"p","size":44,"mobileSize":36,"fontWeight":"700","margin":[0,0,4,0]} -->
<p class="kt-adv-headingprice1_n3 wp-block-kadence-advancedheading" data-kb-block="kb-adv-headingprice1_n3">Talk to us</p>
<!-- /wp:kadence/advancedheading -->

<!-- wp:kadence/advancedheading {"uniqueID":"price1_s3","htmlTag":"p","size":14,"color":"palette5","margin":[0,0,22,0]} -->
<p class="kt-adv-headingprice1_s3 wp-block-kadence-advancedheading" data-kb-block="kb-adv-headingprice1_s3">annual, from $1,400 per month</p>
<!-- /wp:kadence/advancedheading -->

<!-- wp:kadence/iconlist {"uniqueID":"price1_l3","columns":1,"icon":"fe_check","listGap":10} -->
<div class="wp-block-kadence-iconlist kt-svg-icon-list-items kt-svg-icon-list-itemsprice1_l3 kt-svg-icon-list-columns-1 alignnone"><ul class="kt-svg-icon-list"><!-- wp:kadence/listitem {"uniqueID":"price1_l3a","text":"Unmetered rows"} -->
<li class="wp-block-kadence-listitem kt-svg-icon-list-item-wrap kt-svg-icon-list-item-price1_l3a"><span data-name="USE_PARENT_DEFAULT_ICON" data-stroke="USE_PARENT_DEFAULT_WIDTH" data-class="kt-svg-icon-list-single" class="kadence-dynamic-icon"></span><span class="kt-svg-icon-list-text">Unmetered rows</span></li>
<!-- /wp:kadence/listitem -->

<!-- wp:kadence/listitem {"uniqueID":"price1_l3b","text":"Five-minute exports"} -->
<li class="wp-block-kadence-listitem kt-svg-icon-list-item-wrap kt-svg-icon-list-item-price1_l3b"><span data-name="USE_PARENT_DEFAULT_ICON" data-stroke="USE_PARENT_DEFAULT_WIDTH" data-class="kt-svg-icon-list-single" class="kadence-dynamic-icon"></span><span class="kt-svg-icon-list-text">Five-minute exports</span></li>
<!-- /wp:kadence/listitem -->

<!-- wp:kadence/listitem {"uniqueID":"price1_l3c","text":"1-hour response, 24/7"} -->
<li class="wp-block-kadence-listitem kt-svg-icon-list-item-wrap kt-svg-icon-list-item-price1_l3c"><span data-name="USE_PARENT_DEFAULT_ICON" data-stroke="USE_PARENT_DEFAULT_WIDTH" data-class="kt-svg-icon-list-single" class="kadence-dynamic-icon"></span><span class="kt-svg-icon-list-text">1-hour response, 24/7</span></li>
<!-- /wp:kadence/listitem --></ul></div>
<!-- /wp:kadence/iconlist -->

<!-- wp:kadence/spacer {"uniqueID":"price1_sp3","spacerHeight":20,"dividerEnable":false} -->
<div class="wp-block-kadence-spacer aligncenter kt-block-spacer-price1_sp3"><div class="kt-block-spacer kt-block-spacer-halign-center"></div></div>
<!-- /wp:kadence/spacer -->

<!-- wp:kadence/advancedbtn {"uniqueID":"price1_b3","hAlign":"left"} -->
<div class="wp-block-kadence-advancedbtn kb-buttons-wrap kb-btnsprice1_b3"><!-- wp:kadence/singlebtn {"uniqueID":"price1_b3a","text":"Book a call","link":"/call/","inheritStyles":"outline","color":"palette1","width":["100%","",""]} /--></div>
<!-- /wp:kadence/advancedbtn --></div></div>
<!-- /wp:kadence/column -->
<!-- /wp:kadence/rowlayout -->
```

**Payoff:** `width:["100%","",""]` on each button makes all three the same
width without any wrapper CSS, which is what makes a card row look designed
rather than assembled.

Highlighting the recommended tier is a border, not a bigger card: `border` and
`borderWidth` on the middle column. Scaling one card up breaks the row's
vertical rhythm and looks broken at tablet widths.

Say what the plan costs in the heading. "Talk to us" with no anchor number is
the single most common reason enterprise cards get skipped — including
"from $1,400" lets people self-select instead of bouncing.

## Pattern 2 — Monthly/yearly toggle

There is no pricing-toggle block. The honest approximation is tabs, which is
what [kadence-tabs.md](kadence-tabs.md) Pattern 1 shows: two tabs, one card row
in each.

That does mean duplicating the cards. The alternative — a JavaScript toggle
swapping prices — needs custom code, and for two price points the duplication
is cheaper to maintain than the script.

## Pattern 3 — Comparison table below the cards

When plans differ only in limits, cards repeat themselves. Put three short
cards on top for the decision and a full table underneath for the detail. See
[kadence-table.md](kadence-table.md) Pattern 1 — set `isFirstRowHeader` and
`isFirstColumnHeader` so the plan names and capability names are real headers.

## What makes a pricing section work

| Do | Instead of |
|---|---|
| Name the constraint that forces an upgrade | Listing every feature per tier |
| Show a number on every tier | "Contact us" with no anchor |
| Repeat the billing period under each price | One "billed annually" note at the bottom |
| Say what happens at the limit | Silence about overages |

The row people actually search for is what happens when they exceed a limit.
Answering it in the FAQ below the table removes more friction than another
feature bullet.

## Limits

Columns do not equalize height. Three cards with different bullet counts end up
different heights unless the theme stretches them, so keep the lists the same
length — which is good discipline anyway.

`columnGutter:"default"` follows the theme's spacing. Use `"skinny"`,
`"narrow"`, `"wide"` or `"wider"` to override; there is no arbitrary pixel gap
without custom CSS.

There is no per-tier structured data. If you want Product/Offer schema, add it
separately and keep the prices in sync — stale price schema is worse than none.
