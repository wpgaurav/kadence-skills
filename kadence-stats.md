# Kadence Stats and Counters

Numbers that move: count-ups, progress bars and countdowns. Three blocks, three
different families, which matters because two of them save HTML and one does
not.

| Block | Family | Use for |
|---|---|---|
| `kadence/countup` | Static | A number that animates into view |
| `kadence/progress-bar` | Dynamic | A proportion, a skill level, a capacity |
| `kadence/countdown` | Static | A deadline |

## Count-up

The number lives in **data attributes on the saved HTML**, not just the JSON.
Six of them, and each mirrors an attribute:

```
data-start data-end data-prefix data-suffix data-duration data-separator
```

Change `end` in the JSON without changing `data-end` and the animation counts
to the old number. The JSON value is what the editor shows you; the data
attribute is what the browser animates.

```html
<!-- wp:kadence/rowlayout {"uniqueID":"stat1_row","columns":3,"colLayout":"equal","align":"full","inheritMaxWidth":true,"topPadding":64,"bottomPadding":64,"topPaddingM":40,"bottomPaddingM":40,"bgColor":"palette9","kbVersion":2} -->
<!-- wp:kadence/column {"uniqueID":"stat1_c1","kbVersion":2} -->
<div class="wp-block-kadence-column kadence-columnstat1_c1"><div class="kt-inside-inner-col"><!-- wp:kadence/countup {"uniqueID":"stat1_n1","start":0,"end":340,"suffix":"ms","duration":2,"title":"Median query time","separator":","} -->
<div class="wp-block-kadence-countup kb-count-up-stat1_n1 kb-count-up" data-start="0" data-end="340" data-prefix="" data-suffix="ms" data-duration="2" data-separator=","><div class="kb-count-up-process kb-count-up-number"></div><div class="kb-count-up-title">Median query time</div></div>
<!-- /wp:kadence/countup --></div></div>
<!-- /wp:kadence/column -->

<!-- wp:kadence/column {"uniqueID":"stat1_c2","kbVersion":2} -->
<div class="wp-block-kadence-column kadence-columnstat1_c2"><div class="kt-inside-inner-col"><!-- wp:kadence/countup {"uniqueID":"stat1_n2","start":0,"end":11,"duration":2,"title":"Native integrations","separator":""} -->
<div class="wp-block-kadence-countup kb-count-up-stat1_n2 kb-count-up" data-start="0" data-end="11" data-prefix="" data-suffix="" data-duration="2" data-separator=""><div class="kb-count-up-process kb-count-up-number"></div><div class="kb-count-up-title">Native integrations</div></div>
<!-- /wp:kadence/countup --></div></div>
<!-- /wp:kadence/column -->

<!-- wp:kadence/column {"uniqueID":"stat1_c3","kbVersion":2} -->
<div class="wp-block-kadence-column kadence-columnstat1_c3"><div class="kt-inside-inner-col"><!-- wp:kadence/countup {"uniqueID":"stat1_n3","start":0,"end":99,"suffix":".95%","duration":2,"title":"Uptime, trailing 12 months","separator":""} -->
<div class="wp-block-kadence-countup kb-count-up-stat1_n3 kb-count-up" data-start="0" data-end="99" data-prefix="" data-suffix=".95%" data-duration="2" data-separator=""><div class="kb-count-up-process kb-count-up-number"></div><div class="kb-count-up-title">Uptime, trailing 12 months</div></div>
<!-- /wp:kadence/countup --></div></div>
<!-- /wp:kadence/column -->
<!-- /wp:kadence/rowlayout -->
```

**Payoff:** `suffix` carries the unit, so the animation counts the number and
the unit stays put instead of scrambling.

The `<div class="kb-count-up-process kb-count-up-number">` is **empty in the
saved HTML**. That is correct — the script fills it. Putting the number in
there by hand breaks validation.

The `title` attribute is the opposite case: it adds a second sibling div,
`<div class="kb-count-up-title">…</div>`, **after** the number div, holding the
label text. Set `title` in the JSON and forget that div and the block fails to
validate. Omit `title` entirely and the div must not be there either.

`separator:","` gives 1,250,000. Leave it empty for years and version numbers,
where a thousands separator is wrong.

## Progress bar

Dynamic, so no HTML to keep in sync.

```html
<!-- wp:kadence/progress-bar {"uniqueID":"stat2_p1","barType":"line","progressAmount":72,"progressMax":100,"label":"Migration complete","labelPosition":"above","displayPercent":true,"delayUntilInView":true,"duration":1500} /-->
```

`barType` accepts exactly four values: `line`, `circle`, `semicircle`,
`line-mask`. Anything else silently falls back.

`delayUntilInView:true` holds the animation until the bar scrolls into view. Set
it, or the bar finishes animating above the fold and everyone below it sees a
static bar.

**Expect these to read zero in screenshots.** Both `progress-bar` and `countup`
animate from their start value when an intersection observer fires. A full-page
screenshot tool, a PDF export, or a print stylesheet renders the page without
ever scrolling it, so every bar shows 0% and every counter shows its `start`
value. The HTML is correct — the server outputs `81%` in the label — it is the
animation that has not run.

If a page needs to survive being captured or printed, set
`delayUntilInView:false`, or use plain text for the number and keep the animated
version for decoration only.

## Countdown

Static, with a required child.

```html
<!-- wp:kadence/countdown {"uniqueID":"stat3_cd","countdownType":"date","date":"2026-12-31T23:59:59","timezone":"UTC","preLabel":"Early pricing ends in","expireAction":"none"} -->
<div class="wp-block-kadence-countdown kb-countdown-container kb-countdown-container-stat3_cd kb-countdown-timer-layout-block kb-countdown-has-timer" data-id="stat3_cd"><!-- wp:kadence/countdown-inner {"uniqueID":"stat3_cdi"} -->
<div class="wp-block-kadence-countdown-inner kb-countdown-inner kb-countdown-inner-undefined kb-countdown-inner-stat3_cdi"></div>
<!-- /wp:kadence/countdown-inner --></div>
<!-- /wp:kadence/countdown -->
```

**Payoff:** the timer itself is rendered by script into the empty inner div, so
the markup does not change when you move the deadline.

`kb-countdown-inner-undefined` is not a mistake in this document. Kadence emits
the literal string `undefined` there when the countdown's own `id` attribute is
unset. Reproduce it exactly or the block fails validation.

`countdownType` is `date` or `evergreen`. Evergreen restarts per visitor, which
is a dark pattern when dressed up as a real deadline. If the deadline is real,
use `date` and let it expire.

`expireAction` accepts `none`, `hide` and `redirect`. `hide` is the honest
choice — an expired countdown showing zeros looks broken.

## Choosing a number to show

A stat row is only as good as its weakest number. Three specific figures beat
five where two are vague:

| Weak | Better |
|---|---|
| "Thousands of users" | "1,240 teams" |
| "Fast queries" | "340 ms median" |
| "Highly available" | "99.95% over 12 months" |

Every number should be one someone could ask you to prove. If you would not put
a date and a method next to it, leave it out.

## Limits

None of these blocks pull live data. The numbers are typed in and go stale
silently. If a figure needs to stay current, either add a "measured in
&lt;month&gt;" line next to it or use a dynamic source.

Count-ups animate on every scroll into view in some themes, which reads as
noise on a page with three stat rows. One animated row per page.

Progress bars carry no accessible value by default — set `ariaLabel` so a
screen reader announces something more useful than a decorative div.
