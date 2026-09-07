# Kadence Testimonials

Social proof sections. `kadence/testimonials` and `kadence/testimonial` are
both **dynamic** blocks — comment-only, no saved HTML. That makes them the
easiest composite in the plugin to write and the hardest to preview from
source, because nothing in the markup shows you the rendered shape.

## The columns attribute

`columns` on `kadence/testimonials` is a **six-value array**, one per
breakpoint, largest first:

```
"columns":[xxl, xl, lg, md, sm, xs]
```

A standard responsive three-up is `[3,3,3,2,1,1]`. The default is
`[1,1,1,1,1,1]`, which is why an untouched testimonials block renders as a
single stacked column no matter how many items it holds.

`itemsCount` must match the number of `kadence/testimonial` children.

## Pattern 1 — Three-column grid

```html
<!-- wp:kadence/rowlayout {"uniqueID":"test1_row","columns":1,"colLayout":"equal","align":"full","inheritMaxWidth":true,"topPadding":80,"bottomPadding":80,"topPaddingM":48,"bottomPaddingM":48,"bgColor":"palette9","kbVersion":2} -->
<!-- wp:kadence/column {"uniqueID":"test1_col","kbVersion":2} -->
<div class="wp-block-kadence-column kadence-columntest1_col"><div class="kt-inside-inner-col"><!-- wp:kadence/advancedheading {"uniqueID":"test1_h","htmlTag":"h2","align":"center","size":34,"mobileSize":26,"fontWeight":"700","margin":[0,0,32,0]} -->
<h2 class="kt-adv-headingtest1_h wp-block-kadence-advancedheading" data-kb-block="kb-adv-headingtest1_h">What teams say after the first quarter</h2>
<!-- /wp:kadence/advancedheading -->

<!-- wp:kadence/testimonials {"uniqueID":"test1_set","layout":"grid","style":"card","columns":[3,3,3,2,1,1],"itemsCount":3,"columnGap":24,"displayTitle":true,"displayMedia":true,"displayName":true,"displayOccupation":true,"containerBackground":"#ffffff","containerBorderRadius":10,"kbVersion":2} -->
<!-- wp:kadence/testimonial {"uniqueID":"test1_t1","title":"Cut close from nine days to two","content":"The reconciliation rules were the whole job. Once those moved over, month-end stopped being a fire drill.","name":"Priya Raman","occupation":"Financial Controller, Halden Group"} /-->

<!-- wp:kadence/testimonial {"uniqueID":"test1_t2","title":"Our auditors stopped asking","content":"Every figure traces back to a source row with a timestamp. That single change removed most of our audit prep.","name":"Tomas Beck","occupation":"Head of Finance, Nordvik"} /-->

<!-- wp:kadence/testimonial {"uniqueID":"test1_t3","title":"Worth it for the exports alone","content":"We rebuilt six years of board reporting in a weekend and the numbers matched the old system to the cent.","name":"Aisha Nwosu","occupation":"CFO, Larksfield"} /-->
<!-- /wp:kadence/testimonials --></div></div>
<!-- /wp:kadence/column -->
<!-- /wp:kadence/rowlayout -->
```

**Payoff:** three items, three comment lines — no HTML to keep in sync, which
is why testimonial sets are the one place bulk-generating markup is genuinely
safe.

`style:"card"` gives each item a background and radius.
`containerBackground` and `containerBorderRadius` live on the **parent**
`testimonials` block, not on each child.

## Pattern 2 — Single large quote

One strong quote beats three weak ones. Use `columns:[1,1,1,1,1,1]` (the
default) and let it run wide.

```html
<!-- wp:kadence/rowlayout {"uniqueID":"test2_row","columns":1,"colLayout":"equal","align":"full","inheritMaxWidth":true,"topPadding":72,"bottomPadding":72,"bgColor":"palette8","kbVersion":2} -->
<!-- wp:kadence/column {"uniqueID":"test2_col","kbVersion":2} -->
<div class="wp-block-kadence-column kadence-columntest2_col"><div class="kt-inside-inner-col"><!-- wp:kadence/testimonials {"uniqueID":"test2_set","layout":"grid","style":"inlineimage","columns":[1,1,1,1,1,1],"itemsCount":1,"displayIcon":true,"displayTitle":false,"displayMedia":true,"kbVersion":2} -->
<!-- wp:kadence/testimonial {"uniqueID":"test2_t1","content":"We ran both systems in parallel for a full quarter because nobody believed the close could actually take two days. It did. We shut the old one off in April and have not looked back.","name":"Priya Raman","occupation":"Financial Controller, Halden Group","icon":"fas_quote-left"} /-->
<!-- /wp:kadence/testimonials --></div></div>
<!-- /wp:kadence/column -->
<!-- /wp:kadence/rowlayout -->
```

**Payoff:** `displayTitle:false` drops the headline field so the quote itself
carries the weight.

`style` accepts `basic`, `card`, `inlineimage` and `bubble`. Switching style
changes the rendered layout, not the markup — another benefit of these blocks
being dynamic.

## Pattern 3 — Carousel

For six or more quotes, where a grid would eat the page.

```html
<!-- wp:kadence/rowlayout {"uniqueID":"test3_row","columns":1,"colLayout":"equal","align":"full","inheritMaxWidth":true,"topPadding":72,"bottomPadding":72,"kbVersion":2} -->
<!-- wp:kadence/column {"uniqueID":"test3_col","kbVersion":2} -->
<div class="wp-block-kadence-column kadence-columntest3_col"><div class="kt-inside-inner-col"><!-- wp:kadence/testimonials {"uniqueID":"test3_set","layout":"carousel","style":"card","columns":[3,3,3,2,1,1],"itemsCount":4,"autoPlay":true,"columnGap":20,"containerBackground":"palette9","containerBorderRadius":10,"kbVersion":2} -->
<!-- wp:kadence/testimonial {"uniqueID":"test3_t1","content":"Support answered on a Sunday, in under an hour, with a working patch.","name":"Devon Park","occupation":"Ops Lead"} /-->

<!-- wp:kadence/testimonial {"uniqueID":"test3_t2","content":"The import tool handled our worst legacy CSV without a single manual fix.","name":"Mira Sandoval","occupation":"Data Analyst"} /-->

<!-- wp:kadence/testimonial {"uniqueID":"test3_t3","content":"Pricing did not change when we tripled seats. That is rarer than it should be.","name":"Ken Oyelaran","occupation":"Director of Finance"} /-->

<!-- wp:kadence/testimonial {"uniqueID":"test3_t4","content":"Three integrations, one afternoon, zero tickets.","name":"Lucia Ferrari","occupation":"Systems Engineer"} /-->
<!-- /wp:kadence/testimonials --></div></div>
<!-- /wp:kadence/column -->
<!-- /wp:kadence/rowlayout -->
```

**Payoff:** flipping `layout` between `"grid"` and `"carousel"` is a one-word
change with no structural edit.

`autoPlay:true` is the default-off option most people want and most users find
irritating. If the quotes matter, leave it false and let people scroll.

## Ratings and photos

`displayRating:true` on the parent turns on stars; each child's `rating`
(default 5) sets its own. `displayMedia:true` plus a child `url` and `id`
shows an avatar:

```
"media":"image","url":"https://example.com/wp-content/uploads/priya.jpg","id":42
```

Leave `displayMedia:false` rather than shipping placeholder avatars. A quote
with a name and a company reads as real; a quote with a stock headshot reads as
invented.

## Limits

The carousel does not pause on hover or focus by default, which is an
accessibility problem for auto-playing content. Prefer `autoPlay:false`.

There is no built-in way to pull testimonials from a custom post type. These
are hand-entered. For a database-backed set you want `kadence/posts` against a
testimonial CPT instead, styled separately.

Because both blocks are dynamic, **the editor cannot tell you when the markup
is wrong** — it validates whatever parses. Mismatched `itemsCount` and child
counts, or a `columns` array of the wrong length, produce a rendering bug with
no editor warning. Count your children.
