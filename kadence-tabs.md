# Kadence Tabs

Tabbed panels. This is the most intricate save markup in the plugin: the
wrapper carries a full `<ul>` of tab titles that has to stay in sync with the
`titles` attribute *and* the child blocks. Copy, then edit carefully.

## What has to agree

| Thing | Where |
|---|---|
| `tabCount` | Tabs JSON |
| Length of the `titles` array | Tabs JSON |
| `kt-tabs-has-N-tabs` | Wrapper class |
| One `<li>` per title | Wrapper `<ul>` |
| One `kadence/tab` child per title | Structure |
| Each tab's `id` (1, 2, 3, …) | Tab JSON **and** its `kt-inner-tab-N` class |

## The anchor trap

**The `<li id>` and `<a href>` are derived from the title text**, not from the
tab index. The transformation is not the slugify you expect — it **deletes**
disallowed characters rather than replacing them with hyphens:

```
"tab-" + text.toLowerCase().replace(/[^a-z0-9-]/g, "")
```

Lowercase, keep `a-z`, `0-9` and existing hyphens, drop everything else. Spaces
vanish without a separator. Verified:

| Title | Anchor |
|---|---|
| `Monthly` | `tab-monthly` |
| `Cost per drop` | `tab-costperdrop` |
| `Time / Round` | `tab-timeround` |
| `Plan A & B` | `tab-planab` |
| `24-hour SLA` | `tab-24-hoursla` |
| `Café Ünicode` | `tab-cafnicode` |
| `Tab 1` | `tab-tab1` |

`Cost per drop` becomes `tab-costperdrop`, **not** `tab-cost-per-drop`. Writing
the hyphenated form is the single easiest way to fail validation on a tabs
block, and it is what you get if you reach for a normal slug helper.

Set a title object's `anchor` to pin a slug you control instead — worth doing
for any title with punctuation, and required for non-Latin titles, which
otherwise reduce to a handful of surviving ASCII characters or nothing at all.

`python3 tools/lint-attributes.py` checks these for you.

Each `titles` entry is a full object. Partial objects are dropped:

```
{"text":"Monthly","icon":"","iconSide":"right","onlyIcon":false,"subText":"","anchor":""}
```

Two more details that look like typos but are not: `class="kt-tab-title
kt-tab-title-1 "` has a **trailing space**, and so does
`kt-tab-alignment-left `. Both are in the plugin's own output. Reproduce them.

## Pattern 1 — Two tabs

```html
<!-- wp:kadence/rowlayout {"uniqueID":"tabs1_row","columns":1,"colLayout":"equal","align":"full","inheritMaxWidth":true,"topPadding":72,"bottomPadding":72,"topPaddingM":44,"bottomPaddingM":44,"kbVersion":2} -->
<!-- wp:kadence/column {"uniqueID":"tabs1_col","kbVersion":2} -->
<div class="wp-block-kadence-column kadence-columntabs1_col"><div class="kt-inside-inner-col"><!-- wp:kadence/tabs {"uniqueID":"tabs1_set","tabCount":2,"titles":[{"text":"Monthly","icon":"","iconSide":"right","onlyIcon":false,"subText":"","anchor":""},{"text":"Yearly","icon":"","iconSide":"right","onlyIcon":false,"subText":"","anchor":""}]} -->
<div class="wp-block-kadence-tabs alignnone"><div class="kt-tabs-wrap kt-tabs-idtabs1_set kt-tabs-has-2-tabs kt-active-tab-1 kt-tabs-layout-tabs kt-tabs-tablet-layout-inherit kt-tabs-mobile-layout-inherit kt-tab-alignment-left "><ul class="kt-tabs-title-list"><li id="tab-monthly" class="kt-title-item kt-title-item-1 kt-tabs-svg-show-always kt-tabs-icon-side-right kt-tab-title-active"><a href="#tab-monthly" data-tab="1" class="kt-tab-title kt-tab-title-1 "><span class="kt-title-text">Monthly</span></a></li><li id="tab-yearly" class="kt-title-item kt-title-item-2 kt-tabs-svg-show-always kt-tabs-icon-side-right kt-tab-title-inactive"><a href="#tab-yearly" data-tab="2" class="kt-tab-title kt-tab-title-2 "><span class="kt-title-text">Yearly</span></a></li></ul><div class="kt-tabs-content-wrap"><!-- wp:kadence/tab {"id":1,"uniqueID":"tabs1_t1"} -->
<div class="wp-block-kadence-tab kt-tab-inner-content kt-inner-tab-1 kt-inner-tabtabs1_t1"><div class="kt-tab-inner-content-inner"><!-- wp:kadence/advancedheading {"uniqueID":"tabs1_c1","htmlTag":"p","size":17,"color":"palette4","margin":[0,0,0,0]} -->
<p class="kt-adv-headingtabs1_c1 wp-block-kadence-advancedheading" data-kb-block="kb-adv-headingtabs1_c1">Billed on the first of each month. Cancel from the account screen and the current month runs to its end.</p>
<!-- /wp:kadence/advancedheading --></div></div>
<!-- /wp:kadence/tab -->

<!-- wp:kadence/tab {"id":2,"uniqueID":"tabs1_t2"} -->
<div class="wp-block-kadence-tab kt-tab-inner-content kt-inner-tab-2 kt-inner-tabtabs1_t2"><div class="kt-tab-inner-content-inner"><!-- wp:kadence/advancedheading {"uniqueID":"tabs1_c2","htmlTag":"p","size":17,"color":"palette4","margin":[0,0,0,0]} -->
<p class="kt-adv-headingtabs1_c2 wp-block-kadence-advancedheading" data-kb-block="kb-adv-headingtabs1_c2">Two months free against the monthly rate. Same terms otherwise, and we refund the unused remainder if you leave mid-year.</p>
<!-- /wp:kadence/advancedheading --></div></div>
<!-- /wp:kadence/tab --></div></div></div>
<!-- /wp:kadence/tabs --></div></div>
<!-- /wp:kadence/column -->
<!-- /wp:kadence/rowlayout -->
```

**Payoff:** everything inside `kt-tab-inner-content-inner` is an ordinary inner
block list, so a tab can hold a whole section.

## Pattern 2 — Three tabs with vertical layout

`layout:"vtabs"` puts the titles down the left side. Better than horizontal
tabs when titles are long enough to wrap.

```html
<!-- wp:kadence/rowlayout {"uniqueID":"tabs2_row","columns":1,"colLayout":"equal","align":"full","inheritMaxWidth":true,"topPadding":72,"bottomPadding":72,"kbVersion":2} -->
<!-- wp:kadence/column {"uniqueID":"tabs2_col","kbVersion":2} -->
<div class="wp-block-kadence-column kadence-columntabs2_col"><div class="kt-inside-inner-col"><!-- wp:kadence/tabs {"uniqueID":"tabs2_set","tabCount":3,"layout":"vtabs","mobileLayout":"accordion","titles":[{"text":"Import","icon":"","iconSide":"right","onlyIcon":false,"subText":"","anchor":""},{"text":"Transform","icon":"","iconSide":"right","onlyIcon":false,"subText":"","anchor":""},{"text":"Export","icon":"","iconSide":"right","onlyIcon":false,"subText":"","anchor":""}]} -->
<div class="wp-block-kadence-tabs alignnone"><div class="kt-tabs-wrap kt-tabs-idtabs2_set kt-tabs-has-3-tabs kt-active-tab-1 kt-tabs-layout-vtabs kt-tabs-tablet-layout-inherit kt-tabs-mobile-layout-accordion kt-tab-alignment-left kt-create-accordion"><ul class="kt-tabs-title-list"><li id="tab-import" class="kt-title-item kt-title-item-1 kt-tabs-svg-show-always kt-tabs-icon-side-right kt-tab-title-active"><a href="#tab-import" data-tab="1" class="kt-tab-title kt-tab-title-1 "><span class="kt-title-text">Import</span></a></li><li id="tab-transform" class="kt-title-item kt-title-item-2 kt-tabs-svg-show-always kt-tabs-icon-side-right kt-tab-title-inactive"><a href="#tab-transform" data-tab="2" class="kt-tab-title kt-tab-title-2 "><span class="kt-title-text">Transform</span></a></li><li id="tab-export" class="kt-title-item kt-title-item-3 kt-tabs-svg-show-always kt-tabs-icon-side-right kt-tab-title-inactive"><a href="#tab-export" data-tab="3" class="kt-tab-title kt-tab-title-3 "><span class="kt-title-text">Export</span></a></li></ul><div class="kt-tabs-content-wrap"><!-- wp:kadence/tab {"id":1,"uniqueID":"tabs2_t1"} -->
<div class="wp-block-kadence-tab kt-tab-inner-content kt-inner-tab-1 kt-inner-tabtabs2_t1"><div class="kt-tab-inner-content-inner"><!-- wp:kadence/advancedheading {"uniqueID":"tabs2_c1","htmlTag":"p","size":17,"color":"palette4","margin":[0,0,0,0]} -->
<p class="kt-adv-headingtabs2_c1 wp-block-kadence-advancedheading" data-kb-block="kb-adv-headingtabs2_c1">Point us at a CSV, a Postgres replica, or one of eleven APIs. Schema is inferred on the first run and pinned after that.</p>
<!-- /wp:kadence/advancedheading --></div></div>
<!-- /wp:kadence/tab -->

<!-- wp:kadence/tab {"id":2,"uniqueID":"tabs2_t2"} -->
<div class="wp-block-kadence-tab kt-tab-inner-content kt-inner-tab-2 kt-inner-tabtabs2_t2"><div class="kt-tab-inner-content-inner"><!-- wp:kadence/advancedheading {"uniqueID":"tabs2_c2","htmlTag":"p","size":17,"color":"palette4","margin":[0,0,0,0]} -->
<p class="kt-adv-headingtabs2_c2 wp-block-kadence-advancedheading" data-kb-block="kb-adv-headingtabs2_c2">Rules are SQL, versioned in the app, and testable against last night's snapshot before you promote them.</p>
<!-- /wp:kadence/advancedheading --></div></div>
<!-- /wp:kadence/tab -->

<!-- wp:kadence/tab {"id":3,"uniqueID":"tabs2_t3"} -->
<div class="wp-block-kadence-tab kt-tab-inner-content kt-inner-tab-3 kt-inner-tabtabs2_t3"><div class="kt-tab-inner-content-inner"><!-- wp:kadence/advancedheading {"uniqueID":"tabs2_c3","htmlTag":"p","size":17,"color":"palette4","margin":[0,0,0,0]} -->
<p class="kt-adv-headingtabs2_c3 wp-block-kadence-advancedheading" data-kb-block="kb-adv-headingtabs2_c3">Scheduled to S3, SFTP or a warehouse table, with a manifest that records exactly which rows went out.</p>
<!-- /wp:kadence/advancedheading --></div></div>
<!-- /wp:kadence/tab --></div></div></div>
<!-- /wp:kadence/tabs --></div></div>
<!-- /wp:kadence/column -->
<!-- /wp:kadence/rowlayout -->
```

**Payoff:** `mobileLayout:"accordion"` turns the tabs into an accordion on
phones, which is the only tab pattern that survives a 390px screen.

Layout values are reflected in the wrapper class:

| Attribute | Class |
|---|---|
| `layout:"tabs"` | `kt-tabs-layout-tabs` |
| `layout:"vtabs"` | `kt-tabs-layout-vtabs` |
| `tabletLayout:"inherit"` | `kt-tabs-tablet-layout-inherit` |
| `mobileLayout:"accordion"` | `kt-tabs-mobile-layout-accordion` **and** `kt-create-accordion` |

Change the attribute, change the class. They are written independently and
nothing reconciles them for you.

Note the last row carefully: setting `mobileLayout` or `tabletLayout` to
`"accordion"` adds a **second** class, `kt-create-accordion`, at the very end of
the wrapper's class list — after `kt-tab-alignment-left `. It is easy to add the
obvious `kt-tabs-mobile-layout-accordion` and miss this one, and the block then
fails validation.

## Adding a tab

Six edits. Work through them in order or you will miss one:

1. `tabCount` + 1.
2. Append a full title object to `titles`.
3. `kt-tabs-has-N-tabs` + 1.
4. Append an `<li>` with `kt-title-item-N`, `kt-tab-title-inactive`, the
   slugified `id`/`href`, and `data-tab="N"`.
5. Append a `kadence/tab` child with `"id":N` and `kt-inner-tab-N`.
6. Give the new tab and its content blocks fresh `uniqueID`s.

If that sounds fragile, it is. For anything beyond four tabs, add the block in
the editor and copy the markup out, rather than hand-writing it.

## Tabs versus accordion

Tabs work when the options are parallel and the reader picks one — pricing
periods, plan tiers, platform-specific instructions. They fail when content is
long, because only one panel is ever visible and nothing can be searched with
ctrl-F or printed.

Accordions work when most readers want none of it. Tabs work when every reader
wants exactly one.

Neither works when readers need to compare panels side by side. That is a
table.
