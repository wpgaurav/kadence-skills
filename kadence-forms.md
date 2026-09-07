# Kadence Forms

Kadence ships two form systems. Pick the right one first — they are not
interchangeable and the older one is a trap for new work.

| | Advanced Form | Legacy Form |
|---|---|---|
| Block | `kadence/advanced-form` | `kadence/form` |
| Family | Dynamic (comment-only) | Static (long saved HTML) |
| Fields live in | A `kadence_form` post | The page itself, in one giant attribute |
| Reusable across pages | Yes, by ID | No |
| Status | Current | Deprecated |

**Use Advanced Form for anything new.** The legacy block's saved markup is a
complete rendered `<form>` — every input, label and hidden field — which makes
it both fragile to hand-edit and impossible to reuse. It is documented at the
end only because existing content still contains it.

## How Advanced Form works

The form is a **post**, not a block. `kadence/advanced-form` on a page is just
a pointer:

```html
<!-- wp:kadence/advanced-form {"uniqueID":"af_contact","id":9} /-->
```

`id` is the post ID of a `kadence_form` post. That is the whole block. Nothing
about the fields, styling or delivery lives on the page.

The field blocks go in **that post's content**, and they are all dynamic too:

```html
<!-- wp:kadence/advanced-form-text {"uniqueID":"fld_name","label":"Full name","inputName":"name","required":true,"showLabel":true} /-->

<!-- wp:kadence/advanced-form-email {"uniqueID":"fld_email","label":"Work email","inputName":"email","required":true,"showLabel":true,"placeholder":"you@company.com"} /-->

<!-- wp:kadence/advanced-form-textarea {"uniqueID":"fld_msg","label":"What are you trying to move?","inputName":"message","rows":5,"showLabel":true} /-->

<!-- wp:kadence/advanced-form-submit {"uniqueID":"fld_submit","text":"Send it over","hAlign":"left","sizePreset":"standard"} /-->
```

**The submit button's label is `text`, and it defaults to an empty string.**
Leave it out and the form renders a correctly styled button with no words in
it — no error, no warning, just a small coloured rectangle. This is the most
likely thing to go wrong in a hand-written form, so set `text` first.

**Payoff:** one form post, referenced from a landing page, a pricing page and a
footer — change the fields once and all three update.

Create the post with WP-CLI when scripting:

```bash
wp post create --post_type=kadence_form --post_title="Contact form" --post_status=publish --post_content='<!-- wp:kadence/advanced-form-text {"uniqueID":"fld_name","label":"Full name","inputName":"name","required":true} /-->'
```

The returned post ID is what goes in the block's `id`.

## Field blocks

Every field block is dynamic and self-closing. The common attributes are the
same across types:

| Attribute | Purpose |
|---|---|
| `label` | Visible label |
| `inputName` | The key in the submitted data |
| `required` | Boolean |
| `showLabel` | Set false for placeholder-only fields |
| `placeholder` | Hint text |
| `helpText` | Text below the field |
| `ariaDescription` | Screen-reader-only description |
| `errorMessage` / `requiredMessage` | Validation copy |
| `defaultValue` | Pre-filled value |
| `defaultParameter` | Pre-fill from a URL query parameter |
| `maxWidth` / `minWidth` + their `…Unit` | Field sizing |

Available types: `text`, `email`, `telephone`, `number`, `textarea`, `select`,
`checkbox`, `radio`, `date`, `time`, `file`, `accept`, `captcha`, `hidden`.

Type-specific extras worth knowing: `textarea` takes `rows`; `select` takes
`options` and `multiSelect`; `advanced-form-submit` carries the whole button
style set (`text`, `background`, `color`, `borderRadius`, `hAlign`,
`sizePreset`, `icon`, …) rather than delegating to a button block. Note that
submit uses `text` for its label while every input field uses `label` — the
submit block has a `label` attribute too, and it is not the button text.

`defaultParameter` is the useful one people miss. Set it to a query-string key
and the field pre-fills from the URL, which is how you attribute a demo request
to the campaign that produced it without a hidden-field hack.

## Pattern — Contact section

```html
<!-- wp:kadence/rowlayout {"uniqueID":"form1_row","columns":2,"colLayout":"equal","align":"full","inheritMaxWidth":true,"topPadding":80,"bottomPadding":80,"topPaddingM":48,"bottomPaddingM":48,"bgColor":"palette9","verticalAlignment":"top","kbVersion":2} -->
<!-- wp:kadence/column {"uniqueID":"form1_c1","kbVersion":2} -->
<div class="wp-block-kadence-column kadence-columnform1_c1"><div class="kt-inside-inner-col"><!-- wp:kadence/advancedheading {"uniqueID":"form1_h","htmlTag":"h2","size":32,"mobileSize":25,"fontWeight":"700","margin":[0,0,14,0]} -->
<h2 class="kt-adv-headingform1_h wp-block-kadence-advancedheading" data-kb-block="kb-adv-headingform1_h">Tell us what you are moving</h2>
<!-- /wp:kadence/advancedheading -->

<!-- wp:kadence/advancedheading {"uniqueID":"form1_p","htmlTag":"p","color":"palette4","size":17,"margin":[0,0,22,0]} -->
<p class="kt-adv-headingform1_p wp-block-kadence-advancedheading" data-kb-block="kb-adv-headingform1_p">An engineer reads every one of these. Expect a reply within one business day, and a straight answer if we are the wrong fit.</p>
<!-- /wp:kadence/advancedheading -->

<!-- wp:kadence/iconlist {"uniqueID":"form1_list","columns":1,"icon":"fe_check","listGap":8} -->
<div class="wp-block-kadence-iconlist kt-svg-icon-list-items kt-svg-icon-list-itemsform1_list kt-svg-icon-list-columns-1 alignnone"><ul class="kt-svg-icon-list"><!-- wp:kadence/listitem {"uniqueID":"form1_i1","text":"No sales sequence"} -->
<li class="wp-block-kadence-listitem kt-svg-icon-list-item-wrap kt-svg-icon-list-item-form1_i1"><span data-name="USE_PARENT_DEFAULT_ICON" data-stroke="USE_PARENT_DEFAULT_WIDTH" data-class="kt-svg-icon-list-single" class="kadence-dynamic-icon"></span><span class="kt-svg-icon-list-text">No sales sequence</span></li>
<!-- /wp:kadence/listitem -->

<!-- wp:kadence/listitem {"uniqueID":"form1_i2","text":"We tell you if another tool fits better"} -->
<li class="wp-block-kadence-listitem kt-svg-icon-list-item-wrap kt-svg-icon-list-item-form1_i2"><span data-name="USE_PARENT_DEFAULT_ICON" data-stroke="USE_PARENT_DEFAULT_WIDTH" data-class="kt-svg-icon-list-single" class="kadence-dynamic-icon"></span><span class="kt-svg-icon-list-text">We tell you if another tool fits better</span></li>
<!-- /wp:kadence/listitem --></ul></div>
<!-- /wp:kadence/iconlist --></div></div>
<!-- /wp:kadence/column -->

<!-- wp:kadence/column {"uniqueID":"form1_c2","background":"#ffffff","borderRadius":[10,10,10,10],"padding":[32,32,32,32],"kbVersion":2} -->
<div class="wp-block-kadence-column kadence-columnform1_c2"><div class="kt-inside-inner-col"><!-- wp:kadence/advanced-form {"uniqueID":"form1_af","id":9} /--></div></div>
<!-- /wp:kadence/column -->
<!-- /wp:kadence/rowlayout -->
```

**Payoff:** the form is one line, so restyling the card around it never risks
breaking the form itself.

Replace `id:9` with your own form post's ID. A missing or wrong ID renders an
empty space with no error — check it after any content migration, because post
IDs do not survive an export-import.

## Spam handling

Advanced Form supports a honeypot and reCAPTCHA/Turnstile through the
`advanced-form-captcha` field and the plugin's global settings. Add the captcha
field to the form post, then configure keys in Kadence Blocks settings.

Do not ship a public form with neither. A bare contact form on an indexed page
collects spam within days.

## The legacy form block

`kadence/form` is **static** and saves a complete rendered `<form>` — labels,
inputs, hidden fields, honeypot and submit button — as one long HTML string.
Its fields live in a `fields` array attribute that must agree with every input
in that HTML.

Do not hand-write it. If you have to touch existing legacy forms:

1. Open the page in the editor and edit through the UI, so the block
   regenerates its own HTML.
2. Or replace it with an Advanced Form and delete the legacy block.

Migrating is usually less work than one careful edit. The legacy block also
duplicates its entire field configuration on every page that uses it, so a
label change means editing every copy.

## Accessibility

Keep `showLabel:true`. Placeholder-only fields fail WCAG — the hint vanishes
the moment someone types, and screen readers treat placeholders inconsistently.

Use `helpText` for format requirements ("include the country code") rather than
burying them in the placeholder, and `ariaDescription` for anything a sighted
user infers from layout.

Write `requiredMessage` per field. "This field is required" on a five-field form
tells someone using a screen reader nothing about which one.
