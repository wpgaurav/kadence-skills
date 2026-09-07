# Kadence Hero Sections

Four verified hero patterns. Every example below validates 100% in the WordPress
editor on Kadence Blocks 3.7.10 and uses only attributes that exist.

Before editing any of these, skim the three rules in [SKILL.md](SKILL.md). The
one that bites hardest here: `kadence/rowlayout` saves no HTML at all. If you
see a `<div class="wp-block-kadence-rowlayout">` in hero markup, it came from an
older doc or a hallucination, and it will break the block.

## Pattern 1 — Centered hero

The default choice. One column, big headline, supporting line, two buttons.
Works for almost any landing page and is the easiest to restyle.

```html
<!-- wp:kadence/rowlayout {"uniqueID":"hero1_row","columns":1,"colLayout":"equal","align":"full","inheritMaxWidth":true,"topPadding":100,"bottomPadding":100,"topPaddingM":60,"bottomPaddingM":60,"bgColor":"palette9","kbVersion":2} -->
<!-- wp:kadence/column {"uniqueID":"hero1_col","kbVersion":2} -->
<div class="wp-block-kadence-column kadence-columnhero1_col"><div class="kt-inside-inner-col"><!-- wp:kadence/advancedheading {"uniqueID":"hero1_h","htmlTag":"h1","align":"center","color":"palette1","size":60,"tabSize":48,"mobileSize":36,"fontWeight":"700","margin":[0,0,20,0]} -->
<h1 class="kt-adv-headinghero1_h wp-block-kadence-advancedheading" data-kb-block="kb-adv-headinghero1_h">Ship your next landing page in an afternoon</h1>
<!-- /wp:kadence/advancedheading -->

<!-- wp:kadence/advancedheading {"uniqueID":"hero1_p","htmlTag":"p","align":"center","color":"palette4","size":20,"mobileSize":17,"maxWidth":[720,"",""],"maxWidthType":"px","margin":[0,"auto",32,"auto"]} -->
<p class="kt-adv-headinghero1_p wp-block-kadence-advancedheading" data-kb-block="kb-adv-headinghero1_p">Build every section from blocks you already have, without a page builder and without touching a line of CSS.</p>
<!-- /wp:kadence/advancedheading -->

<!-- wp:kadence/advancedbtn {"uniqueID":"hero1_btns","hAlign":"center"} -->
<div class="wp-block-kadence-advancedbtn kb-buttons-wrap kb-btnshero1_btns"><!-- wp:kadence/singlebtn {"uniqueID":"hero1_b1","text":"Start free","link":"/signup/","sizePreset":"large","inheritStyles":"fill","background":"palette1","color":"palette9"} /-->

<!-- wp:kadence/singlebtn {"uniqueID":"hero1_b2","text":"See how it works","link":"/tour/","sizePreset":"large","inheritStyles":"outline","color":"palette1"} /--></div>
<!-- /wp:kadence/advancedbtn --></div></div>
<!-- /wp:kadence/column -->
<!-- /wp:kadence/rowlayout -->
```

**Payoff:** one row, one column, four blocks — and because `singlebtn` is
dynamic, changing button labels means editing JSON only, never HTML.

Two details worth copying rather than reinventing:

- `maxWidth` on `advancedheading` is a **three-value array** `[desktop, tablet,
  mobile]`, not a number. `"maxWidth":720` type-checks as wrong and gets
  dropped. The row's `maxWidth` *is* a plain number. They differ.
- `inheritStyles` takes `"fill"`, `"outline"` or `"inherit"`. That is how you
  get a secondary button, not a `style` attribute.

## Pattern 2 — Split hero, text and image

Text left, image right. Use when the product is visual and the screenshot does
persuasive work the headline can't.

```html
<!-- wp:kadence/rowlayout {"uniqueID":"hero2_row","columns":2,"colLayout":"equal","align":"full","inheritMaxWidth":true,"topPadding":90,"bottomPadding":90,"topPaddingM":50,"bottomPaddingM":50,"verticalAlignment":"middle","collapseOrder":"left-to-right","kbVersion":2} -->
<!-- wp:kadence/column {"uniqueID":"hero2_c1","verticalAlignment":"middle","kbVersion":2} -->
<div class="wp-block-kadence-column kadence-columnhero2_c1"><div class="kt-inside-inner-col"><!-- wp:kadence/advancedheading {"uniqueID":"hero2_h","htmlTag":"h1","color":"palette1","size":52,"tabSize":42,"mobileSize":32,"fontWeight":"700","margin":[0,0,18,0]} -->
<h1 class="kt-adv-headinghero2_h wp-block-kadence-advancedheading" data-kb-block="kb-adv-headinghero2_h">Every invoice, reconciled before you open the app</h1>
<!-- /wp:kadence/advancedheading -->

<!-- wp:kadence/advancedheading {"uniqueID":"hero2_p","htmlTag":"p","color":"palette4","size":19,"mobileSize":17,"margin":[0,0,28,0]} -->
<p class="kt-adv-headinghero2_p wp-block-kadence-advancedheading" data-kb-block="kb-adv-headinghero2_p">Connect your bank once. We match payments to invoices overnight and flag only the handful that need a human.</p>
<!-- /wp:kadence/advancedheading -->

<!-- wp:kadence/advancedbtn {"uniqueID":"hero2_btns","hAlign":"left"} -->
<div class="wp-block-kadence-advancedbtn kb-buttons-wrap kb-btnshero2_btns"><!-- wp:kadence/singlebtn {"uniqueID":"hero2_b1","text":"Connect a bank","link":"/signup/","sizePreset":"large","inheritStyles":"fill","background":"palette1","color":"palette9"} /--></div>
<!-- /wp:kadence/advancedbtn --></div></div>
<!-- /wp:kadence/column -->

<!-- wp:kadence/column {"uniqueID":"hero2_c2","verticalAlignment":"middle","kbVersion":2} -->
<div class="wp-block-kadence-column kadence-columnhero2_c2"><div class="kt-inside-inner-col"><!-- wp:kadence/image {"uniqueID":"hero2_img","id":0,"borderRadius":[8,8,8,8]} -->
<figure class="wp-block-kadence-image kb-imagehero2_img"><img src="https://example.com/wp-content/uploads/dashboard.png" alt="Reconciliation dashboard showing matched payments" class="kb-img"/></figure>
<!-- /wp:kadence/image --></div></div>
<!-- /wp:kadence/column -->
<!-- /wp:kadence/rowlayout -->
```

**Payoff:** `verticalAlignment:"middle"` on both the row and the columns keeps
the image centered against the text no matter how the copy grows.

Replace `id:0` and the `src` with a real media-library attachment. The image
block reads `url` and `alt` **from the `<img>` tag**, not from the block JSON —
that is why they appear in the HTML here and not in the comment.

`collapseOrder` controls which column lands on top on mobile.
`"left-to-right"` keeps the text first, which is nearly always what you want.

## Pattern 3 — Background image with overlay

For heroes that need atmosphere. The overlay is what keeps the text readable;
skipping it is the most common accessibility failure in this pattern.

```html
<!-- wp:kadence/rowlayout {"uniqueID":"hero3_row","columns":1,"colLayout":"equal","align":"full","inheritMaxWidth":true,"topPadding":140,"bottomPadding":140,"topPaddingM":80,"bottomPaddingM":80,"bgImg":"https://example.com/wp-content/uploads/workshop.jpg","bgImgID":0,"bgImgSize":"cover","bgImgPosition":"center center","bgImgAttachment":"scroll","overlay":"#0b1220","overlayOpacity":60,"overlayBlendMode":"normal","kbVersion":2} -->
<!-- wp:kadence/column {"uniqueID":"hero3_col","kbVersion":2} -->
<div class="wp-block-kadence-column kadence-columnhero3_col"><div class="kt-inside-inner-col"><!-- wp:kadence/advancedheading {"uniqueID":"hero3_h","htmlTag":"h1","align":"center","color":"#ffffff","size":56,"tabSize":44,"mobileSize":34,"fontWeight":"700","margin":[0,0,18,0]} -->
<h1 class="kt-adv-headinghero3_h wp-block-kadence-advancedheading" data-kb-block="kb-adv-headinghero3_h">Built in a workshop, not a boardroom</h1>
<!-- /wp:kadence/advancedheading -->

<!-- wp:kadence/advancedheading {"uniqueID":"hero3_p","htmlTag":"p","align":"center","color":"#e6eaf2","size":19,"mobileSize":17,"maxWidth":[640,"",""],"maxWidthType":"px","margin":[0,"auto",30,"auto"]} -->
<p class="kt-adv-headinghero3_p wp-block-kadence-advancedheading" data-kb-block="kb-adv-headinghero3_p">Twelve years of field repairs went into the tolerances on this thing. You will feel it the first time you use it.</p>
<!-- /wp:kadence/advancedheading -->

<!-- wp:kadence/advancedbtn {"uniqueID":"hero3_btns","hAlign":"center"} -->
<div class="wp-block-kadence-advancedbtn kb-buttons-wrap kb-btnshero3_btns"><!-- wp:kadence/singlebtn {"uniqueID":"hero3_b1","text":"See the range","link":"/shop/","sizePreset":"large","inheritStyles":"fill","background":"#ffffff","color":"#0b1220"} /--></div>
<!-- /wp:kadence/advancedbtn --></div></div>
<!-- /wp:kadence/column -->
<!-- /wp:kadence/rowlayout -->
```

**Payoff:** `overlayOpacity` is a 0–100 number, so contrast is a single value to
tune rather than a second background layer to manage.

Set `bgImgID` to the real attachment ID when you have one — Kadence uses it to
serve responsive sizes. With `bgImgID:0` the raw URL is used as-is.

Use `bgImgAttachment:"fixed"` for a parallax feel, but test on mobile Safari,
where fixed backgrounds are historically unreliable.

## Pattern 4 — Video popup hero

A poster image that opens a video in a lightbox. Better than an autoplaying
background video for both performance and consent.

```html
<!-- wp:kadence/rowlayout {"uniqueID":"hero4_row","columns":1,"colLayout":"equal","align":"full","inheritMaxWidth":true,"topPadding":90,"bottomPadding":90,"topPaddingM":50,"bottomPaddingM":50,"bgColor":"palette8","kbVersion":2} -->
<!-- wp:kadence/column {"uniqueID":"hero4_col","kbVersion":2} -->
<div class="wp-block-kadence-column kadence-columnhero4_col"><div class="kt-inside-inner-col"><!-- wp:kadence/advancedheading {"uniqueID":"hero4_h","htmlTag":"h1","align":"center","color":"palette1","size":50,"tabSize":40,"mobileSize":32,"fontWeight":"700","margin":[0,0,16,0]} -->
<h1 class="kt-adv-headinghero4_h wp-block-kadence-advancedheading" data-kb-block="kb-adv-headinghero4_h">Watch a full build, start to finish</h1>
<!-- /wp:kadence/advancedheading -->

<!-- wp:kadence/advancedheading {"uniqueID":"hero4_p","htmlTag":"p","align":"center","color":"palette4","size":18,"margin":[0,"auto",30,"auto"],"maxWidth":[600,"",""],"maxWidthType":"px"} -->
<p class="kt-adv-headinghero4_p wp-block-kadence-advancedheading" data-kb-block="kb-adv-headinghero4_p">Nine minutes, no edits, no narration. Just the workflow as it actually runs.</p>
<!-- /wp:kadence/advancedheading -->

<!-- wp:kadence/videopopup {"uniqueID":"hero4_vid","url":"https://www.youtube.com/watch?v=dQw4w9WgXcQ","mediaPoster":[{"url":"https://example.com/wp-content/uploads/poster.jpg","id":7,"alt":"Poster","width":1600,"height":900,"subtype":"jpg"}],"mediaRatio":"56.25","borderRadius":[10,10,10,10],"maxWidth":900,"maxWidthUnit":"px"} -->
<div class="wp-block-kadence-videopopup kadence-video-popuphero4_vid"><div class="kadence-video-popup-wrap kadence-video-noshadow"><div class="kadence-video-intrinsic "><img src="" alt="" width="" height="" class="kadence-video-poster"/><div class="kadence-video-overlay"></div><a class="kadence-video-popup-link kadence-video-type-external" href="https://www.youtube.com/watch?v=dQw4w9WgXcQ" role="button" data-popup-class="kadence-popup-hero4_vid" data-effect="none" data-popup-id="kadence-local-video-hero4_vid" data-popup-auto="true" data-youtube-cookies="true" data-media-ratio="56.25"><span data-name="fas_play" data-title="Play" data-class="kt-video-svg-icon_kt-video-svg-icon-style-default_kt-video-svg-icon-fas_play_kt-video-play-animation-none_kt-video-svg-icon-size-auto" class="kadence-dynamic-icon"></span></a></div></div></div>
<!-- /wp:kadence/videopopup --></div></div>
<!-- /wp:kadence/column -->
<!-- /wp:kadence/rowlayout -->
```

**Payoff:** the poster image is a normal `<img>`, so the page's largest
contentful paint stays an image, not a video player.

`videopopup` is a static block with a long save string. The `data-popup-class`,
`data-popup-id` and the `kt-video-svg-icon_…` bundle all embed the `uniqueID`
or icon settings. When you change the ID, change it in all three places.

Watch the shapes here. The external video address goes in `url`, a plain string
(`type` defaults to `"iframe"`, so you can leave it out). But `media` and
`mediaPoster` are **arrays holding one object** —
`[{"url":…,"id":…,"alt":…,"width":…,"height":…,"subtype":…}]` — not strings.
Passing a string there validates cleanly and then shows nothing.

Two counterintuitive details in the save output, both verified: the poster
`<img>` keeps `src=""` even when `mediaPoster` is populated (Kadence paints the
poster from the attribute at render time), and the `<a href>` carries the video
URL rather than `#`. Copy the block above rather than "fixing" either one.

## Choosing between them

| Situation | Pattern |
|---|---|
| Copy carries the pitch | 1 — Centered |
| The product is visual | 2 — Split |
| Brand and mood matter more than detail | 3 — Background image |
| A demo converts better than a claim | 4 — Video popup |

## Common modifications

**Full-height hero.** Add `"minHeight":600,"minHeightUnit":"px"` to the row and
`"verticalAlignment":"middle"`.

**Tighter mobile padding.** `topPaddingM` and `bottomPaddingM` are separate
number attributes, not array entries.

**Dark section.** Set the row's `bgColor` to `palette2` (or a hex), then set
each heading's `color` explicitly. Text does not inherit a readable color from
the row background.

**Constrain width without full-bleed background.** Drop `"align":"full"` and
set `"maxWidth":1100` on the row instead of `inheritMaxWidth`.

## What not to do

<!-- skip-validate -->
```html
<!-- wp:kadence/rowlayout {"uniqueID":"bad","kbVersion":2} -->
<div class="wp-block-kadence-rowlayout alignfull kt-row-layout-inner kt-layout-id-bad">
<div class="kt-row-column-wrap kt-has-1-columns">
  <!-- column here -->
</div>
</div>
<!-- /wp:kadence/rowlayout -->
```

That wrapper does not exist in saved output. The editor will absorb both divs
into `className`, produce `kadence-columnbad kadence-column-bad`-style doubled
classes on recovery, and drop the styling. `rowlayout` is dynamic — comment in,
columns, comment out, nothing else.
