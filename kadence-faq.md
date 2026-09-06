# Kadence FAQ Sections

Accordion FAQs. `kadence/accordion` and its `kadence/pane` children are
**static** blocks with long, precise save markup — the most error-prone
combination in the plugin. Copy the patterns rather than composing from memory.

## The four things that must agree

| Thing | Where |
|---|---|
| `paneCount` | Accordion JSON |
| `kt-accordion-has-N-panes` | Accordion wrapper class |
| Number of `kadence/pane` children | Structure |
| Each pane's `id` (1, 2, 3, …) | Pane JSON **and** its `kt-accordion-pane-N` class |

That last row is the one people miss. A pane's number comes from its **`id`
attribute**, which defaults to `1`. Omit `id` on panes two and three and all
three render as `kt-accordion-pane-1` — no validation error, just three panes
sharing one set of styles.

The question text lives in
`<span class="kt-blocks-accordion-title">`, not in the block JSON. It is a
`source: children` attribute, so the HTML is authoritative.

And two class names in the wrapper are **misspelled in the plugin**:
`kt-accodion-icon-style-basic` and `kt-accodion-icon-side-right` (missing the
second `r`). Reproduce the typos exactly or the block will not validate.

## Pattern 1 — Standard FAQ

```html
<!-- wp:kadence/rowlayout {"uniqueID":"faq1_row","columns":1,"colLayout":"equal","align":"full","inheritMaxWidth":true,"topPadding":80,"bottomPadding":80,"topPaddingM":48,"bottomPaddingM":48,"kbVersion":2} -->
<!-- wp:kadence/column {"uniqueID":"faq1_col","kbVersion":2} -->
<div class="wp-block-kadence-column kadence-columnfaq1_col"><div class="kt-inside-inner-col"><!-- wp:kadence/advancedheading {"uniqueID":"faq1_h","htmlTag":"h2","align":"center","size":34,"mobileSize":26,"fontWeight":"700","margin":[0,0,32,0]} -->
<h2 class="kt-adv-headingfaq1_h wp-block-kadence-advancedheading" data-kb-block="kb-adv-headingfaq1_h">Questions we get before the first call</h2>
<!-- /wp:kadence/advancedheading -->

<!-- wp:kadence/accordion {"uniqueID":"faq1_acc","paneCount":3} -->
<div class="wp-block-kadence-accordion alignnone"><div class="kt-accordion-wrap kt-accordion-idfaq1_acc kt-accordion-has-3-panes kt-active-pane-0 kt-accordion-block kt-pane-header-alignment-left kt-accodion-icon-style-basic kt-accodion-icon-side-right" style="max-width:none"><div class="kt-accordion-inner-wrap" data-allow-multiple-open="false" data-start-open="0"><!-- wp:kadence/pane {"id":1,"uniqueID":"faq1_p1"} -->
<div class="wp-block-kadence-pane kt-accordion-pane kt-accordion-pane-1 kt-panefaq1_p1"><div class="kt-accordion-header-wrap"><button class="kt-blocks-accordion-header kt-acccordion-button-label-show" type="button"><span class="kt-blocks-accordion-title-wrap"><span class="kt-blocks-accordion-title">How long does migration actually take?</span></span><span class="kt-blocks-accordion-icon-trigger"></span></button></div><div class="kt-accordion-panel"><div class="kt-accordion-panel-inner"><!-- wp:kadence/advancedheading {"uniqueID":"faq1_a1","htmlTag":"p","size":16,"color":"palette4","margin":[0,0,0,0]} -->
<p class="kt-adv-headingfaq1_a1 wp-block-kadence-advancedheading" data-kb-block="kb-adv-headingfaq1_a1">Two to three weeks for a typical mid-size finance stack, most of which is us waiting on read access rather than moving data. The record is four days. The worst case we have shipped was eleven weeks, and that was a bespoke ERP with no export API.</p>
<!-- /wp:kadence/advancedheading --></div></div></div>
<!-- /wp:kadence/pane -->

<!-- wp:kadence/pane {"id":2,"uniqueID":"faq1_p2"} -->
<div class="wp-block-kadence-pane kt-accordion-pane kt-accordion-pane-2 kt-panefaq1_p2"><div class="kt-accordion-header-wrap"><button class="kt-blocks-accordion-header kt-acccordion-button-label-show" type="button"><span class="kt-blocks-accordion-title-wrap"><span class="kt-blocks-accordion-title">What happens to our data if we leave?</span></span><span class="kt-blocks-accordion-icon-trigger"></span></button></div><div class="kt-accordion-panel"><div class="kt-accordion-panel-inner"><!-- wp:kadence/advancedheading {"uniqueID":"faq1_a2","htmlTag":"p","size":16,"color":"palette4","margin":[0,0,0,0]} -->
<p class="kt-adv-headingfaq1_a2 wp-block-kadence-advancedheading" data-kb-block="kb-adv-headingfaq1_a2">You export everything as CSV or Parquet from the account screen, without asking us. We keep backups for 30 days after cancellation and then delete them. There is no retention clause and no exit fee.</p>
<!-- /wp:kadence/advancedheading --></div></div></div>
<!-- /wp:kadence/pane -->

<!-- wp:kadence/pane {"id":3,"uniqueID":"faq1_p3"} -->
<div class="wp-block-kadence-pane kt-accordion-pane kt-accordion-pane-3 kt-panefaq1_p3"><div class="kt-accordion-header-wrap"><button class="kt-blocks-accordion-header kt-acccordion-button-label-show" type="button"><span class="kt-blocks-accordion-title-wrap"><span class="kt-blocks-accordion-title">Do you support our ERP?</span></span><span class="kt-blocks-accordion-icon-trigger"></span></button></div><div class="kt-accordion-panel"><div class="kt-accordion-panel-inner"><!-- wp:kadence/advancedheading {"uniqueID":"faq1_a3","htmlTag":"p","size":16,"color":"palette4","margin":[0,0,0,0]} -->
<p class="kt-adv-headingfaq1_a3 wp-block-kadence-advancedheading" data-kb-block="kb-adv-headingfaq1_a3">Directly, for the eleven listed on the integrations page. For anything else we read from a nightly database replica or an SFTP drop, which covers most of what we meet in practice.</p>
<!-- /wp:kadence/advancedheading --></div></div></div>
<!-- /wp:kadence/pane --></div></div></div>
<!-- /wp:kadence/accordion --></div></div>
<!-- /wp:kadence/column -->
<!-- /wp:kadence/rowlayout -->
```

**Payoff:** answers are ordinary `advancedheading` blocks, so anything you can
put in a page — lists, buttons, images — can go inside a pane.

## Behavior attributes

Three JSON attributes drive the wrapper's data attributes and one of its
classes. All three mappings are verified against the editor:

| JSON | Wrapper output | Meaning |
|---|---|---|
| *(defaults)* | `data-start-open="0"` + `kt-active-pane-0` | First pane open |
| `"startCollapsed":true` | `data-start-open="none"` | Everything closed on load |
| `"openPane":2` | `data-start-open="2"` + `kt-active-pane-2` | Second pane open |
| `"linkPaneCollapse":false` | `data-allow-multiple-open="true"` | Several open at once |

`linkPaneCollapse` reads backwards from what it does. It defaults to `true`,
meaning panes are linked so opening one closes the others. Set it to `false` to
let readers open several — the data attribute then flips to `true`. There is no
`allowMultipleOpen` attribute, despite the data attribute's name.

## Adding a fourth question

Three edits, all of which must land together:

1. `"paneCount":3` becomes `"paneCount":4`.
2. `kt-accordion-has-3-panes` becomes `kt-accordion-has-4-panes`.
3. The new pane gets `"id":4` and `kt-accordion-pane-4`, plus its own
   `uniqueID`.

Miss step 3 and you get a silent styling collision. Miss steps 1 or 2 and the
grid math is wrong.

## FAQ schema

Kadence does not emit FAQPage structured data from the accordion block. If you
want rich results, add the JSON-LD separately — through your SEO plugin's FAQ
module, or a `core/html` block in the page containing a `<script
type="application/ld+json">` payload whose questions and answers match the
accordion text exactly.

Do not mark up an accordion whose answers are truncated or whose questions
differ from the visible text. Mismatched FAQ schema is a manual-action risk,
not just a missed opportunity.

## When not to use an accordion

Collapsing content hides it from readers who skim and, historically, weights it
lower for search. Use an accordion when the list is genuinely long and each
answer is genuinely optional.

For three short answers, plain headings and paragraphs read better and cost
less markup. For a comparison of options, use a table. An accordion is for
questions a minority of readers will have.
