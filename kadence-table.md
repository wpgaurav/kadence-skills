# Kadence Tables

Data and comparison tables. `kadence/table`, `kadence/table-row` and
`kadence/table-data` are all **dynamic** blocks — comment-only, no saved HTML.
Cells hold ordinary inner blocks.

## Structure

```
kadence/table            columns: N
  kadence/table-row      row: 0, 1, 2, …
    kadence/table-data   column: 0, 1, 2, …
      core/paragraph     the actual cell content
```

There is **no `rows` attribute**. Row count comes from the number of
`table-row` children. And there is **no `content` attribute on `table-data`** —
a cell that looks empty in the rendered table usually has its text in the JSON
where nothing reads it.

`row` and `column` are zero-indexed and should match the child's real position.
Kadence uses them for per-column styling, so a mismatch shows up as the wrong
column getting the wrong background.

## Pattern 1 — Comparison table

```html
<!-- wp:kadence/rowlayout {"uniqueID":"tbl1_row","columns":1,"colLayout":"equal","align":"full","inheritMaxWidth":true,"topPadding":72,"bottomPadding":72,"topPaddingM":44,"bottomPaddingM":44,"kbVersion":2} -->
<!-- wp:kadence/column {"uniqueID":"tbl1_col","kbVersion":2} -->
<div class="wp-block-kadence-column kadence-columntbl1_col"><div class="kt-inside-inner-col"><!-- wp:kadence/advancedheading {"uniqueID":"tbl1_h","htmlTag":"h2","align":"center","size":32,"mobileSize":25,"fontWeight":"700","margin":[0,0,28,0]} -->
<h2 class="kt-adv-headingtbl1_h wp-block-kadence-advancedheading" data-kb-block="kb-adv-headingtbl1_h">What each plan actually includes</h2>
<!-- /wp:kadence/advancedheading -->

<!-- wp:kadence/table {"uniqueID":"tbl1_tab","columns":4,"isFirstRowHeader":true,"isFirstColumnHeader":true,"evenOddBackground":true,"backgroundColorOdd":"palette9","overflowXScroll":true,"cellPadding":[12,16,12,16]} -->
<!-- wp:kadence/table-row {"uniqueID":"tbl1_r0","row":0} -->
<!-- wp:kadence/table-data {"uniqueID":"tbl1_c00","column":0} -->
<!-- wp:paragraph --><p>Capability</p><!-- /wp:paragraph -->
<!-- /wp:kadence/table-data -->

<!-- wp:kadence/table-data {"uniqueID":"tbl1_c01","column":1} -->
<!-- wp:paragraph --><p>Starter</p><!-- /wp:paragraph -->
<!-- /wp:kadence/table-data -->

<!-- wp:kadence/table-data {"uniqueID":"tbl1_c02","column":2} -->
<!-- wp:paragraph --><p>Team</p><!-- /wp:paragraph -->
<!-- /wp:kadence/table-data -->

<!-- wp:kadence/table-data {"uniqueID":"tbl1_c03","column":3} -->
<!-- wp:paragraph --><p>Enterprise</p><!-- /wp:paragraph -->
<!-- /wp:kadence/table-data -->
<!-- /wp:kadence/table-row -->

<!-- wp:kadence/table-row {"uniqueID":"tbl1_r1","row":1} -->
<!-- wp:kadence/table-data {"uniqueID":"tbl1_c10","column":0} -->
<!-- wp:paragraph --><p>Scheduled exports</p><!-- /wp:paragraph -->
<!-- /wp:kadence/table-data -->

<!-- wp:kadence/table-data {"uniqueID":"tbl1_c11","column":1} -->
<!-- wp:paragraph --><p>Daily</p><!-- /wp:paragraph -->
<!-- /wp:kadence/table-data -->

<!-- wp:kadence/table-data {"uniqueID":"tbl1_c12","column":2} -->
<!-- wp:paragraph --><p>Hourly</p><!-- /wp:paragraph -->
<!-- /wp:kadence/table-data -->

<!-- wp:kadence/table-data {"uniqueID":"tbl1_c13","column":3} -->
<!-- wp:paragraph --><p>Every 5 minutes</p><!-- /wp:paragraph -->
<!-- /wp:kadence/table-data -->
<!-- /wp:kadence/table-row -->

<!-- wp:kadence/table-row {"uniqueID":"tbl1_r2","row":2} -->
<!-- wp:kadence/table-data {"uniqueID":"tbl1_c20","column":0} -->
<!-- wp:paragraph --><p>Row limit</p><!-- /wp:paragraph -->
<!-- /wp:kadence/table-data -->

<!-- wp:kadence/table-data {"uniqueID":"tbl1_c21","column":1} -->
<!-- wp:paragraph --><p>1 million</p><!-- /wp:paragraph -->
<!-- /wp:kadence/table-data -->

<!-- wp:kadence/table-data {"uniqueID":"tbl1_c22","column":2} -->
<!-- wp:paragraph --><p>50 million</p><!-- /wp:paragraph -->
<!-- /wp:kadence/table-data -->

<!-- wp:kadence/table-data {"uniqueID":"tbl1_c23","column":3} -->
<!-- wp:paragraph --><p>Unmetered</p><!-- /wp:paragraph -->
<!-- /wp:kadence/table-data -->
<!-- /wp:kadence/table-row -->

<!-- wp:kadence/table-row {"uniqueID":"tbl1_r3","row":3} -->
<!-- wp:kadence/table-data {"uniqueID":"tbl1_c30","column":0} -->
<!-- wp:paragraph --><p>Support response</p><!-- /wp:paragraph -->
<!-- /wp:kadence/table-data -->

<!-- wp:kadence/table-data {"uniqueID":"tbl1_c31","column":1} -->
<!-- wp:paragraph --><p>2 business days</p><!-- /wp:paragraph -->
<!-- /wp:kadence/table-data -->

<!-- wp:kadence/table-data {"uniqueID":"tbl1_c32","column":2} -->
<!-- wp:paragraph --><p>4 hours</p><!-- /wp:paragraph -->
<!-- /wp:kadence/table-data -->

<!-- wp:kadence/table-data {"uniqueID":"tbl1_c33","column":3} -->
<!-- wp:paragraph --><p>1 hour, 24/7</p><!-- /wp:paragraph -->
<!-- /wp:kadence/table-data -->
<!-- /wp:kadence/table-row -->
<!-- /wp:kadence/table --></div></div>
<!-- /wp:kadence/column -->
<!-- /wp:kadence/rowlayout -->
```

**Payoff:** `overflowXScroll:true` is the single attribute that keeps a
four-column table usable on a phone — without it the table either squeezes into
unreadable columns or pushes the page sideways.

Three attributes do most of the styling work:

- `isFirstRowHeader` renders row 0 as `<th>`. Set it whenever the first row is
  labels, so screen readers announce column headers.
- `isFirstColumnHeader` does the same down the left edge. In a comparison
  table you usually want both.
- `evenOddBackground` plus `backgroundColorOdd` gives zebra striping. Striping
  earns its keep past about four rows and adds noise below that.

## Pattern 2 — Compact spec table

Two columns, no striping, for specifications or plan details.

```html
<!-- wp:kadence/table {"uniqueID":"tbl2_tab","columns":2,"isFirstColumnHeader":true,"cellPadding":[10,14,10,14],"maxWidth":[640,"",""],"maxWidthUnit":"px"} -->
<!-- wp:kadence/table-row {"uniqueID":"tbl2_r0","row":0} -->
<!-- wp:kadence/table-data {"uniqueID":"tbl2_c00","column":0} -->
<!-- wp:paragraph --><p>Latency, p95</p><!-- /wp:paragraph -->
<!-- /wp:kadence/table-data -->

<!-- wp:kadence/table-data {"uniqueID":"tbl2_c01","column":1} -->
<!-- wp:paragraph --><p>340&nbsp;ms on a 10&nbsp;million row table</p><!-- /wp:paragraph -->
<!-- /wp:kadence/table-data -->
<!-- /wp:kadence/table-row -->

<!-- wp:kadence/table-row {"uniqueID":"tbl2_r1","row":1} -->
<!-- wp:kadence/table-data {"uniqueID":"tbl2_c10","column":0} -->
<!-- wp:paragraph --><p>Retention</p><!-- /wp:paragraph -->
<!-- /wp:kadence/table-data -->

<!-- wp:kadence/table-data {"uniqueID":"tbl2_c11","column":1} -->
<!-- wp:paragraph --><p>30 days after cancellation, then deleted</p><!-- /wp:paragraph -->
<!-- /wp:kadence/table-data -->
<!-- /wp:kadence/table-row -->
<!-- /wp:kadence/table -->
```

**Payoff:** `maxWidth` keeps a two-column table from stretching to full page
width, where the gap between label and value becomes unreadable.

`maxWidth` here is a **three-value array** `[desktop, tablet, mobile]`, unlike
the row block's plain number. Same attribute name, different shape, different
block.

## Cells can hold anything

Because cells take inner blocks, a comparison table can hold buttons, icons or
images rather than text:

```html
<!-- wp:kadence/table-data {"uniqueID":"tbl3_cell","column":2} -->
<!-- wp:kadence/icon {"uniqueID":"tbl3_ic"} -->
<div class="wp-block-kadence-icon kt-svg-icons kt-svg-iconstbl3_ic alignnone"><!-- wp:kadence/single-icon {"uniqueID":"tbl3_si","icon":"fe_check","color":"palette1","size":20} -->
<div class="wp-block-kadence-single-icon kt-svg-style-default kt-svg-icon-wrap kt-svg-item-tbl3_si"><span data-name="fe_check" data-stroke="2" class="kadence-dynamic-icon"></span></div>
<!-- /wp:kadence/single-icon --></div>
<!-- /wp:kadence/icon -->
<!-- /wp:kadence/table-data -->
```

**Payoff:** a tick icon reads faster than the word "Yes" across a wide row, and
it stays legible when the column is narrow.

Give every icon a distinct `uniqueID`. Twenty ticks with the same ID means one
CSS rule fighting twenty elements.

## Accessibility and honesty

Set `isFirstRowHeader` on any table whose first row is labels. Without it every
cell is a `<td>` and a screen reader reads a wall of values with no context.

Use `enableCaption` with `caption` for tables that need a source or a
qualifier. A comparison table with a date on it ages honestly; one without
looks current forever.

Comparison tables that only list the axes where you win are the most common
form of quiet dishonesty in SaaS marketing. Include at least one row where a
competitor is better, or drop the competitor columns and just describe your own
tiers.

## Limits

There is no column-span or row-span. Every row must have the same number of
`table-data` children as `columns`.

There is no sorting, filtering or pagination. For anything interactive, use a
dedicated table plugin — this block renders static markup.

Because all three blocks are dynamic, **the editor will not catch a structural
error**. A row with three cells in a four-column table validates fine and
renders wrong. Count cells per row before shipping.
