# Kadence Media Blocks

Images, galleries, video popups and maps. All four are **static** blocks, and
two of them have save markup complex enough that hand-writing is a bad idea.
This file tells you which is which.

| Block | Hand-writable? |
|---|---|
| `kadence/image` | Yes, easily |
| `kadence/videopopup` | Yes, with care |
| `kadence/googlemaps` | Yes, with care |
| `kadence/advancedgallery` | **No** — build it in the editor |

## Image

```html
<!-- wp:kadence/image {"uniqueID":"med1_img","id":42,"borderRadius":[8,8,8,8]} -->
<figure class="wp-block-kadence-image kb-imagemed1_img"><img src="https://example.com/wp-content/uploads/schedule.png" alt="Schedule editor with three recurring exports configured" class="kb-img wp-image-42"/></figure>
<!-- /wp:kadence/image -->
```

**Payoff:** the simplest static block in the set — one figure, one img, and the
only ID-derived class is `kb-image{uniqueID}`.

Three rules:

- `url` and `alt` are **sourced from the `<img>` tag**. Put them there. A `url`
  in the block JSON alone renders nothing.
- `id` in the JSON and `wp-image-{id}` on the img should match a real
  attachment. Without it WordPress cannot serve responsive sizes.
- Setting `sizeSlug` adds `size-{slug}` to the **figure** class:
  `"sizeSlug":"large"` needs `class="wp-block-kadence-image kb-image{ID} size-large"`.
  Omit the attribute and omit the class.

Write real alt text. "Dashboard screenshot" describes the file; "Reconciliation
dashboard showing 412 matched payments and 3 exceptions" describes the point
you are making with it.

## Video popup

A poster image that opens a lightbox. Better than an autoplaying background
video for performance, bandwidth and consent.

```html
<!-- wp:kadence/videopopup {"uniqueID":"med2_vid","url":"https://www.youtube.com/watch?v=dQw4w9WgXcQ","mediaPoster":[{"url":"https://example.com/wp-content/uploads/poster.jpg","id":42,"alt":"Poster","width":1600,"height":900,"subtype":"jpg"}],"mediaRatio":"56.25","borderRadius":[10,10,10,10],"maxWidth":900,"maxWidthUnit":"px"} -->
<div class="wp-block-kadence-videopopup kadence-video-popupmed2_vid"><div class="kadence-video-popup-wrap kadence-video-noshadow"><div class="kadence-video-intrinsic "><img src="" alt="" width="" height="" class="kadence-video-poster"/><div class="kadence-video-overlay"></div><a class="kadence-video-popup-link kadence-video-type-external" href="https://www.youtube.com/watch?v=dQw4w9WgXcQ" role="button" data-popup-class="kadence-popup-med2_vid" data-effect="none" data-popup-id="kadence-local-video-med2_vid" data-popup-auto="true" data-youtube-cookies="true" data-media-ratio="56.25"><span data-name="fas_play" data-title="Play" data-class="kt-video-svg-icon_kt-video-svg-icon-style-default_kt-video-svg-icon-fas_play_kt-video-play-animation-none_kt-video-svg-icon-size-auto" class="kadence-dynamic-icon"></span></a></div></div></div>
<!-- /wp:kadence/videopopup -->
```

**Payoff:** the page's largest contentful paint stays an image, not an iframe —
worth roughly a second on a slow connection versus an embedded player.

Two things that look wrong but are correct. The poster `<img>` keeps `src=""`
even with `mediaPoster` populated; Kadence paints it at render time. And the
`<a href>` carries the full video URL, not `#`.

`uniqueID` appears in **three** places in that HTML: the wrapper class,
`data-popup-class` and `data-popup-id`. Change one, change all three.

`youtubeCookies:true` (the default) uses youtube-nocookie.com. Leave it on
unless you have a reason and a consent banner.

## Google Maps

```html
<!-- wp:kadence/googlemaps {"uniqueID":"med3_map","location":"1600 Amphitheatre Parkway, Mountain View, CA","zoom":15,"mapType":"roadmap","heightDesktop":420,"showMarker":true,"kbVersion":2} /-->
```

**Payoff:** one line, and Kadence builds a lazy-loaded iframe from the
attributes at render time.

**Google Maps is the one block where `kbVersion` changes its family.** With
`"kbVersion":2` it is dynamic — comment-only, exactly as above. Without it, it
is static and saves a full `<div>` and `<iframe>`:

<!-- skip-validate -->
```html
<!-- wp:kadence/googlemaps {"uniqueID":"legacy_map","location":"1600 Amphitheatre Parkway, Mountain View, CA"} -->
<div class="kb-google-maps-container kb-google-maps-containerlegacy_map" data-mapid="legacy_map"><iframe width="100%" height="100%" style="border:0" loading="lazy" src="https://www.google.com/maps/embed/v1/place?key=KADENCE_GOOGLE_MAPS_KEY&amp;zoom=11&amp;maptype=roadmap&amp;q=1600%20Amphitheatre%20Parkway%2C%20Mountain%20View%2C%20CA"></iframe></div>
<!-- /wp:kadence/googlemaps -->
```

Write the `kbVersion:2` form. The legacy shape is here so you recognise it in
existing content — adding `kbVersion:2` to one of those without also deleting
its HTML breaks the block.

In the legacy markup, the literal `KADENCE_GOOGLE_MAPS_KEY` is correct: Kadence
substitutes a key at render time. Never put a real API key in block markup — it
lands in the post content and in the page source with no referrer restriction.

**Which key it substitutes matters.** If the site has no Google Maps key in
Kadence Blocks settings, the plugin falls back to a shared key bundled with the
plugin and used by every install that has not set its own. In testing here, the
first page load rendered a map and later loads rendered an empty container — no
console error visible in the markup, just blank space where the map was.

Treat a map that renders once and then stops as a missing key, not a broken
block. Add your own key in Kadence Blocks settings, restricted by HTTP referrer,
before shipping a page that depends on the map.

`zoom` is declared as a number, so write `15` not `"15"` — despite the schema's
own default being the string `"11"`.

## Gallery — build this one in the editor

`kadence/advancedgallery` stores each image's data in **HTML attributes on the
`<img>`** (`data-id`, `data-full-image`, `data-link`, `data-light-image`,
`data-custom-link`, …) and wraps every item in four nested elements with
**computed inline styles**:

```html
<!-- wp:kadence/advancedgallery {"uniqueID":"med4_gal","kbVersion":2} -->
<div class="wp-block-kadence-advancedgallery kb-gallery-wrap-id-med4_gal"><ul class="kb-gallery-ul kb-gallery-type-masonry kb-masonry-init kb-gallery-id-med4_gal kb-gallery-caption-style-bottom-hover kb-gallery-filter-none" data-item-selector=".kadence-blocks-gallery-item" data-image-filter="none" data-lightbox-caption="true" data-columns-xxl="3" data-columns-xl="3" data-columns-lg="3" data-columns-md="2" data-columns-sm="1" data-columns-xs="1"><li class="kadence-blocks-gallery-item"><div class="kadence-blocks-gallery-item-inner"><figure class="kb-gallery-figure kadence-blocks-gallery-item-hide-caption"><div class="kb-gal-image-radius" style="max-width:1000px"><div class="kb-gallery-image-contain kadence-blocks-gallery-intrinsic" style="padding-bottom:100%"><img src="https://example.com/wp-content/uploads/shot.png" width="1000" height="1000" alt="Sample" data-full-image="https://example.com/wp-content/uploads/shot.png" data-id="42" class="wp-image-42"/></div></div></figure></div></li></ul></div>
<!-- /wp:kadence/advancedgallery -->
```

That is **one image**. Note `style="max-width:1000px"` and
`style="padding-bottom:100%"` — both computed from the image's real pixel
dimensions, the second as `height / width * 100`. Get a single one wrong across
a twelve-image gallery and the block fails to validate with no useful pointer to
which item broke.

Add galleries through the editor's media picker and copy the markup out if you
need it in a template. That is the one place in this whole system where the UI
is genuinely faster and safer than writing markup.

The `data-columns-*` attributes mirror the six-value `columns` array
`[xxl, xl, lg, md, sm, xs]`, and `kb-gallery-type-{type}` mirrors `type`
(`masonry`, `grid`, `carousel`, `fluidcarousel`, `slider`, `tiles`).

## Performance

Images and galleries are where WordPress pages get heavy. Two habits cover most
of it:

- Upload at the size you will display, not at camera resolution. Kadence serves
  responsive sizes only when `id` and `wp-image-{id}` are set correctly.
- Prefer `videopopup` over an embedded player, and a still over a video where
  the motion adds nothing.

Kadence does not lazy-load the first image on a page, which is correct — lazy
loading an above-the-fold hero delays the largest contentful paint rather than
improving it. Do not add `loading="lazy"` to a hero image by hand.
