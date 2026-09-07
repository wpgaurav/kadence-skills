# Kadence Blocks Attribute Reference (v3.7.10)

Generated from the plugin's own `block.json` manifests by `tools/extract-schema.py`.
Do not hand-edit. Attributes not listed here do not exist and are silently
dropped by the editor on save.

**62 blocks.**

## Index

- [`kadence/accordion`](#kadenceaccordion) — Accordion (50 attributes)
- [`kadence/advanced-form`](#kadenceadvancedform) — Advanced Form (3 attributes)
- [`kadence/advanced-form-accept`](#kadenceadvancedformaccept) —  (18 attributes)
- [`kadence/advanced-form-captcha`](#kadenceadvancedformcaptcha) — Captcha (21 attributes)
- [`kadence/advanced-form-checkbox`](#kadenceadvancedformcheckbox) —  (19 attributes)
- [`kadence/advanced-form-date`](#kadenceadvancedformdate) —  (19 attributes)
- [`kadence/advanced-form-email`](#kadenceadvancedformemail) —  (20 attributes)
- [`kadence/advanced-form-file`](#kadenceadvancedformfile) —  (18 attributes)
- [`kadence/advanced-form-hidden`](#kadenceadvancedformhidden) —  (7 attributes)
- [`kadence/advanced-form-number`](#kadenceadvancedformnumber) —  (23 attributes)
- [`kadence/advanced-form-radio`](#kadenceadvancedformradio) —  (21 attributes)
- [`kadence/advanced-form-select`](#kadenceadvancedformselect) —  (20 attributes)
- [`kadence/advanced-form-submit`](#kadenceadvancedformsubmit) — Submit Button (63 attributes)
- [`kadence/advanced-form-telephone`](#kadenceadvancedformtelephone) —  (20 attributes)
- [`kadence/advanced-form-text`](#kadenceadvancedformtext) —  (20 attributes)
- [`kadence/advanced-form-textarea`](#kadenceadvancedformtextarea) —  (21 attributes)
- [`kadence/advanced-form-time`](#kadenceadvancedformtime) —  (19 attributes)
- [`kadence/advancedbtn`](#kadenceadvancedbtn) — Advanced Button (34 attributes)
- [`kadence/advancedgallery`](#kadenceadvancedgallery) — Advanced Gallery (82 attributes)
- [`kadence/advancedheading`](#kadenceadvancedheading) — Advanced Text (145 attributes)
- [`kadence/column`](#kadencecolumn) — Section (132 attributes)
- [`kadence/countdown`](#kadencecountdown) — Countdown (67 attributes)
- [`kadence/countdown-inner`](#kadencecountdowninner) — Countdown Content (2 attributes)
- [`kadence/countdown-timer`](#kadencecountdowntimer) — Countdown Timer (1 attributes)
- [`kadence/countup`](#kadencecountup) — Count Up (39 attributes)
- [`kadence/form`](#kadenceform) — Form (25 attributes)
- [`kadence/googlemaps`](#kadencegooglemaps) — Google Maps (30 attributes)
- [`kadence/header`](#kadenceheader) — Header (Adv) (2 attributes)
- [`kadence/header-column`](#kadenceheadercolumn) — Header Column (2 attributes)
- [`kadence/header-container-desktop`](#kadenceheadercontainerdesktop) — Desktop Header (1 attributes)
- [`kadence/header-container-tablet`](#kadenceheadercontainertablet) — Tablet Header (1 attributes)
- [`kadence/header-row`](#kadenceheaderrow) — Header Row (39 attributes)
- [`kadence/header-section`](#kadenceheadersection) — Header Section (2 attributes)
- [`kadence/icon`](#kadenceicon) — Icon (12 attributes)
- [`kadence/iconlist`](#kadenceiconlist) — Icon List (37 attributes)
- [`kadence/identity`](#kadenceidentity) — Site identity (24 attributes)
- [`kadence/image`](#kadenceimage) — Advanced Image (82 attributes)
- [`kadence/infobox`](#kadenceinfobox) — Info Box (89 attributes)
- [`kadence/listitem`](#kadencelistitem) — List item (62 attributes)
- [`kadence/lottie`](#kadencelottie) — Lottie Animations (30 attributes)
- [`kadence/navigation`](#kadencenavigation) — Navigation (Adv) (4 attributes)
- [`kadence/navigation-link`](#kadencenavigationlink) — Kadence Navigation Link (304 attributes)
- [`kadence/off-canvas`](#kadenceoffcanvas) —  (74 attributes)
- [`kadence/off-canvas-trigger`](#kadenceoffcanvastrigger) —  (37 attributes)
- [`kadence/posts`](#kadenceposts) — Posts (49 attributes)
- [`kadence/progress-bar`](#kadenceprogressbar) — Progress Bar (49 attributes)
- [`kadence/rowlayout`](#kadencerowlayout) — Row Layout (170 attributes)
- [`kadence/search`](#kadencesearch) — Search (Adv) (49 attributes)
- [`kadence/show-more`](#kadenceshowmore) — Show More (22 attributes)
- [`kadence/single-icon`](#kadencesingleicon) — Single Icon (31 attributes)
- [`kadence/singlebtn`](#kadencesinglebtn) — Single Button (130 attributes)
- [`kadence/spacer`](#kadencespacer) — Spacer / Divider (26 attributes)
- [`kadence/tab`](#kadencetab) — Tab (2 attributes)
- [`kadence/table`](#kadencetable) — Table (Adv) (51 attributes)
- [`kadence/table-data`](#kadencetabledata) — Table Data (6 attributes)
- [`kadence/table-row`](#kadencetablerow) — Table (Adv) (8 attributes)
- [`kadence/tableofcontents`](#kadencetableofcontents) — Table of Contents (86 attributes)
- [`kadence/tabs`](#kadencetabs) — Tabs (89 attributes)
- [`kadence/testimonial`](#kadencetestimonial) — Testimonial (25 attributes)
- [`kadence/testimonials`](#kadencetestimonials) — Testimonials (116 attributes)
- [`kadence/vector`](#kadencevector) — Vector SVG (14 attributes)
- [`kadence/videopopup`](#kadencevideopopup) — Video Popup (41 attributes)

## kadence/accordion

**Accordion** · category `kadence-blocks` · apiVersion 3

- Supports: `{"anchor": true, "kbMetadata": true}`

| Attribute | Type | Default |
|---|---|---|
| `align` | string | `"none"` |
| `blockAlignment` | string | `"none"` |
| `columnGap` | array | `["md", "", ""]` |
| `columnGapUnit` | string | `"px"` |
| `columnLayout` | array | `["row", "", "row"]` |
| `contentBgColor` | string | `""` |
| `contentBorder` | array | `["", "", "", ""]` |
| `contentBorderColor` | string | `""` |
| `contentBorderRadius` | array | `["", "", "", ""]` |
| `contentBorderRadiusUnit` | string | `"px"` |
| `contentBorderStyle` | array | `[{"top": ["", "", ""], "right": ["", "", ""], "bottom": ["", "", ""], "left": ["", "", ""], "unit": "px"}]` |
| `contentMobilePadding` | array | `["", "", "", ""]` |
| `contentPadding` | array | `["sm", "sm", "sm", "sm"]` |
| `contentPaddingType` | string | `"px"` |
| `contentTabletPadding` | array | `["", "", "", ""]` |
| `faqSchema` | boolean | `false` |
| `iconColor` | object | `{"standard": "", "active": "", "hover": ""}` |
| `iconSide` | string | `"right"` |
| `iconStyle` | string | `"basic"` |
| `linkColor` | string | `""` |
| `linkHoverColor` | string | `""` |
| `linkPaneCollapse` | boolean | `true` |
| `maxWidth` | number | `""` |
| `minHeight` | number | `""` |
| `mobileContentBorderRadius` | array | `["", "", "", ""]` |
| `mobileContentBorderStyle` | array | `[{"top": ["", "", ""], "right": ["", "", ""], "bottom": ["", "", ""], "left": ["", "", ""], "unit": ""}]` |
| `mobileTitleBorder` | array | `[{"top": ["", "", ""], "right": ["", "", ""], "bottom": ["", "", ""], "left": ["", "", ""], "unit": ""}]` |
| `mobileTitleBorderActive` | array | `[{"top": ["", "", ""], "right": ["", "", ""], "bottom": ["", "", ""], "left": ["", "", ""], "unit": ""}]` |
| `mobileTitleBorderHover` | array | `[{"top": ["", "", ""], "right": ["", "", ""], "bottom": ["", "", ""], "left": ["", "", ""], "unit": ""}]` |
| `mobileTitleBorderRadius` | array | `["", "", "", ""]` |
| `openPane` | number | `0` |
| `paneCount` | number | `2` |
| `showIcon` | boolean | `true` |
| `showPresets` | boolean | `true` |
| `startCollapsed` | boolean | `false` |
| `tabletContentBorderRadius` | array | `["", "", "", ""]` |
| `tabletContentBorderStyle` | array | `[{"top": ["", "", ""], "right": ["", "", ""], "bottom": ["", "", ""], "left": ["", "", ""], "unit": ""}]` |
| `tabletTitleBorder` | array | `[{"top": ["", "", ""], "right": ["", "", ""], "bottom": ["", "", ""], "left": ["", "", ""], "unit": ""}]` |
| `tabletTitleBorderActive` | array | `[{"top": ["", "", ""], "right": ["", "", ""], "bottom": ["", "", ""], "left": ["", "", ""], "unit": ""}]` |
| `tabletTitleBorderHover` | array | `[{"top": ["", "", ""], "right": ["", "", ""], "bottom": ["", "", ""], "left": ["", "", ""], "unit": ""}]` |
| `tabletTitleBorderRadius` | array | `["", "", "", ""]` |
| `textColor` | string | `""` |
| `titleAlignment` | string | `"left"` |
| `titleBorder` | array | `[{"top": ["", "", ""], "right": ["", "", ""], "bottom": ["", "", ""], "left": ["", "", ""], "unit": "px"}]` |
| `titleBorderActive` | array | `[{"top": ["", "", ""], "right": ["", "", ""], "bottom": ["", "", ""], "left": ["", "", ""], "unit": "px"}]` |
| `titleBorderHover` | array | `[{"top": ["", "", ""], "right": ["", "", ""], "bottom": ["", "", ""], "left": ["", "", ""], "unit": "px"}]` |
| `titleBorderRadius` | array | `["", "", "", ""]` |
| `titleBorderRadiusUnit` | string | `"px"` |
| `titleStyles` | array | `[{"size": ["", "", ""], "sizeType": "px", "lineHeight": ["", "", ""], "lineType": "", "letterSpacing": "", "family": "", "google": "", "style": "", "weight": "", "variant": "", "subset": "", "loadGoogle": true, "padding": ["xxs", "xs", "xxs", "xs"], "marginTop": 8, "color": "", "background": "", "border": ["", "", "", ""], "borderRadius": ["", "", "", ""], "borderWidth": ["", "", "", ""], "colorHover": "", "backgroundHover": "", "borderHover": ["", "", "", ""], "colorActive": "", "backgroundActive": "", "borderActive": ["", "", "", ""], "textTransform": "", "paddingTablet": ["", "", "", ""], "paddingMobile": ["", "", "", ""], "paddingType": "px"}]` |
| `uniqueID` | string | `""` |

## kadence/advanced-form

**Advanced Form** · category `kadence-blocks` · apiVersion 3

- Supports: `{"html": false, "customClassName": false, "reusable": false, "lock": false, "kbMetadata": true}`

| Attribute | Type | Default |
|---|---|---|
| `id` | integer | `0` |
| `legacyMigration` | object | `null` |
| `uniqueID` | string |  |

## kadence/advanced-form-accept

**** · category `kadence-blocks` · apiVersion 3

- Parent-only: must be a direct child of `kadence/advanced-form`, `kadence/column`
- Supports: `{"anchor": true, "html": false, "ktfieldconditional": true, "reusable": false, "kbMetadata": true, "ktdynamic": true, "kbContentLabel": "label"}`

| Attribute | Type | Default |
|---|---|---|
| `anchor` | string |  |
| `ariaDescription` | string | `""` |
| `defaultParameter` | string |  |
| `defaultValue` | string |  |
| `description` | string | `""` |
| `formID` | string |  |
| `helpText` | string | `""` |
| `inputName` | string |  |
| `isChecked` | boolean | `false` |
| `label` | string | `""` |
| `maxWidth` | array | `["", "", ""]` |
| `maxWidthUnit` | string | `"%"` |
| `minWidth` | array | `["", "", ""]` |
| `minWidthUnit` | string | `"px"` |
| `required` | boolean | `false` |
| `requiredMessage` | string |  |
| `showLabel` | boolean | `true` |
| `uniqueID` | string |  |

## kadence/advanced-form-captcha

**Captcha** · category `kadence-blocks` · apiVersion 3

- Parent-only: must be a direct child of `kadence/advanced-form`, `kadence/column`
- Supports: `{"html": false, "reusable": false, "kbMetadata": true}`

| Attribute | Type | Default |
|---|---|---|
| `formID` | string |  |
| `hCaptchaSecretKey` | string | `""` |
| `hCaptchaSiteKey` | string | `"-"` |
| `hideRecaptcha` | boolean | `false` |
| `maxWidth` | array | `["", "", ""]` |
| `maxWidthUnit` | string | `"%"` |
| `minWidth` | array | `["", "", ""]` |
| `minWidthUnit` | string | `"px"` |
| `recaptchaLanguage` | string | `""` |
| `recaptchaNotice` | string | `""` |
| `recaptchaSecretKey` | string | `""` |
| `recaptchaSiteKey` | string | `"-"` |
| `showRecaptchaNotice` | boolean | `false` |
| `size` | string | `"normal"` |
| `theme` | string | `"light"` |
| `turnstileSecretKey` | string | `""` |
| `turnstileSiteKey` | string | `"-"` |
| `type` | string | `"googlev2"` |
| `uniqueID` | string | `""` |
| `useKbSettings` | boolean | `true` |
| `useKcSettings` | boolean | `false` |

## kadence/advanced-form-checkbox

**** · category `kadence-blocks` · apiVersion 3

- Parent-only: must be a direct child of `kadence/advanced-form`, `kadence/column`
- Supports: `{"anchor": true, "html": false, "ktfieldconditional": true, "ktdynamic": true, "reusable": false, "kbMetadata": true, "kbContentLabel": "label"}`

| Attribute | Type | Default |
|---|---|---|
| `anchor` | string |  |
| `ariaDescription` | string | `""` |
| `defaultParameter` | string |  |
| `defaultValue` | string |  |
| `errorMessage` | string |  |
| `formID` | string |  |
| `helpText` | string | `""` |
| `inline` | boolean | `false` |
| `inputName` | string |  |
| `label` | string | `""` |
| `maxWidth` | array | `["", "", ""]` |
| `maxWidthUnit` | string | `"%"` |
| `minWidth` | array | `["", "", ""]` |
| `minWidthUnit` | string | `"px"` |
| `options` | array | `[{"value": "", "label": "", "selected": false}]` |
| `required` | boolean | `false` |
| `requiredMessage` | string |  |
| `showLabel` | boolean | `true` |
| `uniqueID` | string |  |

## kadence/advanced-form-date

**** · category `kadence-blocks` · apiVersion 3

- Parent-only: must be a direct child of `kadence/advanced-form`, `kadence/column`
- Supports: `{"anchor": true, "html": false, "ktdynamic": true, "ktfieldconditional": true, "reusable": false, "kbMetadata": true, "kbContentLabel": "label"}`

| Attribute | Type | Default |
|---|---|---|
| `anchor` | string |  |
| `ariaDescription` | string | `""` |
| `auto` | string |  |
| `autoCustom` | string |  |
| `defaultParameter` | string |  |
| `defaultValue` | string |  |
| `errorMessage` | string |  |
| `formID` | string |  |
| `helpText` | string |  |
| `inputName` | string |  |
| `label` | string | `""` |
| `maxWidth` | array | `["", "", ""]` |
| `maxWidthUnit` | string | `"%"` |
| `minWidth` | array | `["", "", ""]` |
| `minWidthUnit` | string | `"px"` |
| `required` | boolean | `false` |
| `requiredMessage` | string |  |
| `showLabel` | boolean | `true` |
| `uniqueID` | string |  |

## kadence/advanced-form-email

**** · category `kadence-blocks` · apiVersion 3

- Parent-only: must be a direct child of `kadence/advanced-form`, `kadence/column`
- Supports: `{"anchor": true, "html": false, "ktdynamic": true, "ktfieldconditional": true, "reusable": false, "kbMetadata": true, "kbContentLabel": "label"}`

| Attribute | Type | Default |
|---|---|---|
| `anchor` | string |  |
| `ariaDescription` | string | `""` |
| `auto` | string |  |
| `autoCustom` | string |  |
| `defaultParameter` | string |  |
| `defaultValue` | string |  |
| `errorMessage` | string |  |
| `formID` | string |  |
| `helpText` | string | `""` |
| `inputName` | string |  |
| `label` | string | `""` |
| `maxWidth` | array | `["", "", ""]` |
| `maxWidthUnit` | string | `"%"` |
| `minWidth` | array | `["", "", ""]` |
| `minWidthUnit` | string | `"px"` |
| `placeholder` | string | `""` |
| `required` | boolean | `false` |
| `requiredMessage` | string |  |
| `showLabel` | boolean | `true` |
| `uniqueID` | string |  |

## kadence/advanced-form-file

**** · category `kadence-blocks` · apiVersion 3

- Parent-only: must be a direct child of `kadence/advanced-form`
- Supports: `{"ktfieldconditional": true}`

| Attribute | Type | Default |
|---|---|---|
| `allowedTypes` | array | `["image"]` |
| `anchor` | string |  |
| `ariaDescription` | string | `""` |
| `formID` | string |  |
| `helpText` | string | `""` |
| `inputName` | string |  |
| `label` | string | `""` |
| `maxSizeMb` | number | `10` |
| `maxWidth` | array | `["", "", ""]` |
| `maxWidthUnit` | string | `"%"` |
| `minWidth` | array | `["", "", ""]` |
| `minWidthUnit` | string | `"px"` |
| `multiple` | boolean | `false` |
| `multipleLimit` | number | `5` |
| `required` | boolean | `false` |
| `requiredMessage` | string |  |
| `showLabel` | boolean | `true` |
| `uniqueID` | string |  |

## kadence/advanced-form-hidden

**** · category `kadence-blocks` · apiVersion 3

- Parent-only: must be a direct child of `kadence/advanced-form`, `kadence/column`
- Supports: `{"anchor": true, "html": false, "reusable": false, "ktdynamic": true, "ktfieldconditional": true, "kbMetadata": true, "kbContentLabel": "label"}`

| Attribute | Type | Default |
|---|---|---|
| `anchor` | string |  |
| `defaultParameter` | string |  |
| `defaultValue` | string |  |
| `formID` | string |  |
| `inputName` | string |  |
| `label` | string | `""` |
| `uniqueID` | string |  |

## kadence/advanced-form-number

**** · category `kadence-blocks` · apiVersion 3

- Parent-only: must be a direct child of `kadence/advanced-form`, `kadence/column`
- Supports: `{"anchor": true, "html": false, "ktdynamic": true, "ktfieldconditional": true, "reusable": false, "kbMetadata": true, "kbContentLabel": "label"}`

| Attribute | Type | Default |
|---|---|---|
| `allowDecimals` | boolean | `false` |
| `anchor` | string |  |
| `ariaDescription` | string | `""` |
| `auto` | string |  |
| `autoCustom` | string |  |
| `defaultParameter` | string |  |
| `defaultValue` | string |  |
| `errorMessage` | string |  |
| `formID` | string |  |
| `helpText` | string | `""` |
| `inputName` | string |  |
| `label` | string | `""` |
| `maxValue` | number | `""` |
| `maxWidth` | array | `["", "", ""]` |
| `maxWidthUnit` | string | `"%"` |
| `minValue` | number | `""` |
| `minWidth` | array | `["", "", ""]` |
| `minWidthUnit` | string | `"px"` |
| `placeholder` | string | `""` |
| `required` | boolean | `false` |
| `requiredMessage` | string |  |
| `showLabel` | boolean | `true` |
| `uniqueID` | string |  |

## kadence/advanced-form-radio

**** · category `kadence-blocks` · apiVersion 3

- Parent-only: must be a direct child of `kadence/advanced-form`
- Supports: `{"anchor": true, "html": false, "ktfieldconditional": true, "reusable": false, "kbMetadata": true, "ktdynamic": true, "kbContentLabel": "label"}`

| Attribute | Type | Default |
|---|---|---|
| `anchor` | string |  |
| `ariaDescription` | string | `""` |
| `auto` | string |  |
| `autoCustom` | string |  |
| `defaultParameter` | string |  |
| `defaultValue` | string |  |
| `formID` | string |  |
| `helpText` | string | `""` |
| `inline` | boolean | `false` |
| `inputName` | string |  |
| `label` | string | `""` |
| `maxWidth` | array | `["", "", ""]` |
| `maxWidthUnit` | string | `"%"` |
| `minWidth` | array | `["", "", ""]` |
| `minWidthUnit` | string | `"px"` |
| `options` | array | `[{"value": "", "label": "", "selected": false}]` |
| `placeholder` | string | `""` |
| `required` | boolean | `false` |
| `requiredMessage` | string |  |
| `showLabel` | boolean | `true` |
| `uniqueID` | string |  |

## kadence/advanced-form-select

**** · category `kadence-blocks` · apiVersion 3

- Parent-only: must be a direct child of `kadence/advanced-form`, `kadence/column`
- Supports: `{"anchor": true, "html": false, "ktdynamic": true, "ktfieldconditional": true, "reusable": false, "kbMetadata": true, "kbContentLabel": "label"}`

| Attribute | Type | Default |
|---|---|---|
| `anchor` | string |  |
| `ariaDescription` | string | `""` |
| `defaultParameter` | string |  |
| `defaultValue` | string |  |
| `errorMessage` | string |  |
| `formID` | string |  |
| `helpText` | string | `""` |
| `inputName` | string |  |
| `label` | string | `""` |
| `maxWidth` | array | `["", "", ""]` |
| `maxWidthUnit` | string | `"%"` |
| `minWidth` | array | `["", "", ""]` |
| `minWidthUnit` | string | `"px"` |
| `multiSelect` | boolean | `false` |
| `options` | array | `[{"value": "", "label": ""}]` |
| `placeholder` | string |  |
| `required` | boolean | `false` |
| `requiredMessage` | string |  |
| `showLabel` | boolean | `true` |
| `uniqueID` | string |  |

## kadence/advanced-form-submit

**Submit Button** · category `kadence-blocks` · apiVersion 3

- Parent-only: must be a direct child of `kadence/advanced-form`, `kadence/column`
- Supports: `{"anchor": true, "html": false, "reusable": false, "kbMetadata": true, "kbContentLabel": "text"}`

| Attribute | Type | Default |
|---|---|---|
| `anchor` | string |  |
| `background` | string | `""` |
| `backgroundHover` | string | `""` |
| `backgroundHoverType` | string | `"normal"` |
| `backgroundType` | string | `"normal"` |
| `borderHoverRadius` | array | `["", "", "", ""]` |
| `borderHoverRadiusUnit` | string | `"px"` |
| `borderHoverStyle` | array | `[{"top": ["", "", ""], "right": ["", "", ""], "bottom": ["", "", ""], "left": ["", "", ""], "unit": "px"}]` |
| `borderRadius` | array | `["", "", "", ""]` |
| `borderRadiusUnit` | string | `"px"` |
| `borderStyle` | array | `[{"top": ["", "", ""], "right": ["", "", ""], "bottom": ["", "", ""], "left": ["", "", ""], "unit": "px"}]` |
| `color` | string | `""` |
| `colorHover` | string | `""` |
| `displayHoverShadow` | boolean | `false` |
| `displayShadow` | boolean | `false` |
| `formID` | string |  |
| `gap` | array | `["", "", ""]` |
| `gradient` | string | `""` |
| `gradientHover` | string | `""` |
| `hAlign` | string | `"left"` |
| `icon` | string | `""` |
| `iconColor` | string | `""` |
| `iconColorHover` | string | `""` |
| `iconHover` | boolean | `false` |
| `iconPadding` | array | `["", "", "", ""]` |
| `iconPaddingUnit` | string | `"px"` |
| `iconSide` | string | `"right"` |
| `iconSize` | array | `["", "", ""]` |
| `iconSizeUnit` | string | `"px"` |
| `inheritStyles` | string | `"fill"` |
| `label` | string | `""` |
| `margin` | array | `["", "", "", ""]` |
| `marginUnit` | string | `"px"` |
| `mhAlign` | string | `""` |
| `mobileBorderHoverRadius` | array | `["", "", "", ""]` |
| `mobileBorderHoverStyle` | array | `[{"top": ["", "", ""], "right": ["", "", ""], "bottom": ["", "", ""], "left": ["", "", ""], "unit": "px"}]` |
| `mobileBorderRadius` | array | `["", "", "", ""]` |
| `mobileBorderStyle` | array | `[{"top": ["", "", ""], "right": ["", "", ""], "bottom": ["", "", ""], "left": ["", "", ""], "unit": "px"}]` |
| `mobileIconPadding` | array | `["", "", "", ""]` |
| `mobileMargin` | array | `["", "", "", ""]` |
| `mobilePadding` | array | `["", "", "", ""]` |
| `noCustomDefaults` | boolean | `false` |
| `onlyIcon` | array | `[false, "", ""]` |
| `padding` | array | `["", "", "", ""]` |
| `paddingUnit` | string | `"px"` |
| `shadow` | array | `[{"color": "#000000", "opacity": 0.2, "spread": 0, "blur": 2, "hOffset": 1, "vOffset": 1, "inset": false}]` |
| `shadowHover` | array | `[{"color": "#000000", "opacity": 0.4, "spread": 0, "blur": 3, "hOffset": 2, "vOffset": 2, "inset": false}]` |
| `sizePreset` | string | `"standard"` |
| `style` | string | `"basic"` |
| `tablePadding` | array | `["", "", "", ""]` |
| `tabletBorderHoverRadius` | array | `["", "", "", ""]` |
| `tabletBorderHoverStyle` | array | `[{"top": ["", "", ""], "right": ["", "", ""], "bottom": ["", "", ""], "left": ["", "", ""], "unit": "px"}]` |
| `tabletBorderRadius` | array | `["", "", "", ""]` |
| `tabletBorderStyle` | array | `[{"top": ["", "", ""], "right": ["", "", ""], "bottom": ["", "", ""], "left": ["", "", ""], "unit": "px"}]` |
| `tabletIconPadding` | array | `["", "", "", ""]` |
| `tabletMargin` | array | `["", "", "", ""]` |
| `text` | string | `""` |
| `thAlign` | string | `""` |
| `typography` | array | `[{"size": ["", "", ""], "sizeType": "px", "lineHeight": ["", "", ""], "lineType": "", "letterSpacing": ["", "", ""], "letterType": "px", "textTransform": "", "family": "", "google": "", "style": "", "weight": "", "variant": "", "subset": "", "loadGoogle": true}]` |
| `uniqueID` | string | `""` |
| `width` | array | `["", "", ""]` |
| `widthType` | string | `"auto"` |
| `widthUnit` | string | `"px"` |

## kadence/advanced-form-telephone

**** · category `kadence-blocks` · apiVersion 3

- Parent-only: must be a direct child of `kadence/advanced-form`, `kadence/column`
- Supports: `{"anchor": true, "html": false, "ktdynamic": true, "ktfieldconditional": true, "reusable": false, "kbMetadata": true, "kbContentLabel": "label"}`

| Attribute | Type | Default |
|---|---|---|
| `anchor` | string |  |
| `ariaDescription` | string | `""` |
| `auto` | string |  |
| `autoCustom` | string |  |
| `defaultParameter` | string |  |
| `defaultValue` | string |  |
| `errorMessage` | string |  |
| `formID` | string |  |
| `helpText` | string | `""` |
| `inputName` | string |  |
| `label` | string | `""` |
| `maxWidth` | array | `["", "", ""]` |
| `maxWidthUnit` | string | `"%"` |
| `minWidth` | array | `["", "", ""]` |
| `minWidthUnit` | string | `"px"` |
| `placeholder` | string | `""` |
| `required` | boolean | `false` |
| `requiredMessage` | string |  |
| `showLabel` | boolean | `true` |
| `uniqueID` | string |  |

## kadence/advanced-form-text

**** · category `kadence-blocks` · apiVersion 3

- Parent-only: must be a direct child of `kadence/advanced-form`, `kadence/column`
- Supports: `{"anchor": true, "html": false, "ktdynamic": true, "ktfieldconditional": true, "reusable": false, "kbMetadata": true, "kbContentLabel": "label"}`

| Attribute | Type | Default |
|---|---|---|
| `anchor` | string |  |
| `ariaDescription` | string |  |
| `auto` | string |  |
| `autoCustom` | string |  |
| `defaultParameter` | string |  |
| `defaultValue` | string |  |
| `errorMessage` | string |  |
| `formID` | string |  |
| `helpText` | string |  |
| `inputName` | string |  |
| `label` | string |  |
| `maxWidth` | array | `["", "", ""]` |
| `maxWidthUnit` | string | `"%"` |
| `minWidth` | array | `["", "", ""]` |
| `minWidthUnit` | string | `"px"` |
| `placeholder` | string |  |
| `required` | boolean | `false` |
| `requiredMessage` | string |  |
| `showLabel` | boolean | `true` |
| `uniqueID` | string |  |

## kadence/advanced-form-textarea

**** · category `kadence-blocks` · apiVersion 3

- Parent-only: must be a direct child of `kadence/advanced-form`, `kadence/column`
- Supports: `{"anchor": true, "html": false, "ktfieldconditional": true, "reusable": false, "kbMetadata": true, "ktdynamic": true, "kbContentLabel": "label"}`

| Attribute | Type | Default |
|---|---|---|
| `anchor` | string |  |
| `ariaDescription` | string | `""` |
| `auto` | string |  |
| `autoCustom` | string |  |
| `defaultParameter` | string |  |
| `defaultValue` | string |  |
| `errorMessage` | string |  |
| `formID` | string |  |
| `helpText` | string | `""` |
| `inputName` | string |  |
| `label` | string | `""` |
| `maxWidth` | array | `["", "", ""]` |
| `maxWidthUnit` | string | `"%"` |
| `minWidth` | array | `["", "", ""]` |
| `minWidthUnit` | string | `"px"` |
| `placeholder` | string | `""` |
| `required` | boolean | `false` |
| `requiredMessage` | string |  |
| `rows` | number | `3` |
| `showLabel` | boolean | `true` |
| `uniqueID` | string |  |

## kadence/advanced-form-time

**** · category `kadence-blocks` · apiVersion 3

- Parent-only: must be a direct child of `kadence/advanced-form`, `kadence/column`
- Supports: `{"anchor": true, "html": false, "ktdynamic": true, "ktfieldconditional": true, "reusable": false, "kbMetadata": true, "kbContentLabel": "label"}`

| Attribute | Type | Default |
|---|---|---|
| `anchor` | string |  |
| `ariaDescription` | string | `""` |
| `auto` | string |  |
| `autoCustom` | string |  |
| `defaultParameter` | string |  |
| `defaultValue` | string |  |
| `errorMessage` | string |  |
| `formID` | string |  |
| `helpText` | string | `""` |
| `inputName` | string |  |
| `label` | string | `""` |
| `maxWidth` | array | `["", "", ""]` |
| `maxWidthUnit` | string | `"%"` |
| `minWidth` | array | `["", "", ""]` |
| `minWidthUnit` | string | `"px"` |
| `required` | boolean | `false` |
| `requiredMessage` | string |  |
| `showLabel` | boolean | `true` |
| `uniqueID` | string |  |

## kadence/advancedbtn

**Advanced Button** · category `kadence-blocks` · apiVersion 3

- Supports: `{"anchor": true, "kbMetadata": true}`

| Attribute | Type | Default |
|---|---|---|
| `btnCount` | number | `1` |
| `btns` | array | `[{"text": "", "link": "", "target": "_self", "size": "", "paddingBT": "", "paddingLR": "", "color": "#555555", "background": "", "border": "#555555", "backgroundOpacity": 1, "borderOpacity": 1, "borderRadius": "", "borderWidth": "", "colorHover": "#ffffff", "backgroundHover": "#444444", "borderHover": "#444444", "backgroundHoverOpacity": 1, "borderHoverOpacity": 1, "icon": "", "iconSide": "right", "iconHover": false, "cssClass": "", "noFollow": false, "gap": 5, "responsiveSize": ["", ""], "gradient": ["#999999", 1, 0, 100, "linear", 180, "center center"], "gradientHover": ["#777777", 1, 0, 100, "linear", 180, "center center"], "btnStyle": "basic", "btnSize": "standard", "backgroundType": "solid", "backgroundHoverType": "solid", "width": ["", "", ""], "responsivePaddingBT": ["", ""], "responsivePaddingLR": ["", ""], "boxShadow": [false, "#000000", 0.2, 1, 1, 2, 0, false], "boxShadowHover": [false, "#000000", 0.4, 2, 2, 3, 0, false], "sponsored": false, "download": false, "tabletGap": "", "mobileGap": "", "inheritStyles": "", "iconSize": ["", "", ""], "iconPadding": ["", "", "", ""], "iconTabletPadding": ["", "", "", ""], "iconMobilePadding": ["", "", "", ""], "onlyIcon": [false, "", ""], "iconColor": "", "iconColorHover": "", "sizeType": "px", "iconSizeType": "px", "label": "", "marginUnit": "px", "margin": ["", "", "", ""], "tabletMargin": ["", "", "", ""], "mobileMargin": ["", "", "", ""], "anchor": "", "borderStyle": ""}]` |
| `collapseFullwidth` | boolean | `false` |
| `fontStyle` | string | `"normal"` |
| `fontSubset` | string | `""` |
| `fontVariant` | string | `""` |
| `fontWeight` | string | `"regular"` |
| `forceFullwidth` | boolean | `false` |
| `gap` | array | `["xs", "", ""]` |
| `gapUnit` | string | `"px"` |
| `googleFont` | boolean | `false` |
| `hAlign` | string | `"center"` |
| `hideLink` | boolean | `false` |
| `inQueryBlock` | boolean | `false` |
| `letterSpacing` | number |  |
| `loadGoogleFont` | boolean | `true` |
| `lockBtnCount` | boolean | `false` |
| `margin` | array | `[{"desk": ["", "", "", ""], "tablet": ["", "", "", ""], "mobile": ["", "", "", ""]}]` |
| `marginUnit` | string | `"px"` |
| `mhAlign` | string | `""` |
| `mobilePadding` | array | `["", "", "", ""]` |
| `mvAlign` | string | `""` |
| `orientation` | array | `["", "", ""]` |
| `padding` | array | `["", "", "", ""]` |
| `paddingUnit` | string | `"px"` |
| `tabletPadding` | array | `["", "", "", ""]` |
| `textTransform` | string | `""` |
| `thAlign` | string | `""` |
| `tvAlign` | string | `""` |
| `typography` | string | `""` |
| `uniqueID` | string | `""` |
| `vAlign` | string | `"center"` |
| `widthType` | string | `"auto"` |
| `widthUnit` | string | `"px"` |

## kadence/advancedgallery

**Advanced Gallery** · category `kadence-blocks` · apiVersion 3

- Supports: `{"anchor": true, "align": ["wide", "full", "left", "right"], "html": false, "ktdynamic": true, "kbMetadata": true}`

| Attribute | Type | Default |
|---|---|---|
| `anchor` | string |  |
| `arrowCustomBorderWidth` | number |  |
| `arrowCustomColor` | string | `""` |
| `arrowCustomColorActive` | string | `""` |
| `arrowCustomColorBackground` | string | `""` |
| `arrowCustomColorBackgroundActive` | string | `""` |
| `arrowCustomColorBackgroundHover` | string | `""` |
| `arrowCustomColorBorder` | string | `""` |
| `arrowCustomColorBorderActive` | string | `""` |
| `arrowCustomColorBorderHover` | string | `""` |
| `arrowCustomColorHover` | string | `""` |
| `arrowMargin` | array | `["", "", "", ""]` |
| `arrowMarginUnit` | string | `"px"` |
| `arrowPosition` | string | `"center"` |
| `arrowSize` | array | `["", "", ""]` |
| `arrowSizeUnit` | string | `"px"` |
| `arrowStyle` | string | `"whiteondark"` |
| `autoPlay` | boolean | `false` |
| `autoSpeed` | number | `7000` |
| `captionAlignment` | string | `"center"` |
| `captionStyle` | string | `"bottom-hover"` |
| `captionStyles` | array | `[{"size": ["", "", ""], "sizeType": "px", "lineHeight": ["", "", ""], "lineType": "px", "letterSpacing": "", "textTransform": "", "family": "", "google": false, "style": "", "weight": "", "variant": "", "subset": "", "loadGoogle": true, "color": "", "background": "#000000", "backgroundOpacity": 0.8}]` |
| `carouselAlign` | boolean | `true` |
| `carouselHeight` | array | `[300, "", ""]` |
| `columnControl` | string | `"linked"` |
| `columns` | array | `[3, 3, 3, 2, 1, 1]` |
| `displayShadow` | boolean | `false` |
| `dotCustomBorderWidth` | number |  |
| `dotCustomColor` | string | `""` |
| `dotCustomColorActive` | string | `""` |
| `dotCustomColorBorder` | string | `""` |
| `dotCustomColorBorderActive` | string | `""` |
| `dotCustomColorBorderHover` | string | `""` |
| `dotCustomColorHover` | string | `""` |
| `dotStyle` | string | `"dark"` |
| `gap` | array | `["", "", ""]` |
| `gutter` | array | `[10, "", ""]` |
| `gutterUnit` | string | `"px"` |
| `hoverStyle` | string | `"dark"` |
| `ids` | array |  |
| `imageFilter` | string | `"none"` |
| `imageRadius` | array | `[0, 0, 0, 0]` |
| `imageRadiusUnit` | string | `"px"` |
| `imageRatio` | string | `"land32"` |
| `images` | array | `[]` |
| `imagesData` | array | `[{"url": "", "thumbUrl": "", "lightUrl": "", "link": "", "customLink": "", "linkTarget": "", "width": "", "height": "", "alt": "", "id": "", "caption": "", "linkSponsored": ""}]` |
| `imagesDynamic` | array | `[]` |
| `inQueryBlock` | boolean | `false` |
| `kbVersion` | number | `""` |
| `lazyLoad` | boolean | `false` |
| `lightSize` | string | `"full"` |
| `lightbox` | string | `"none"` |
| `lightboxCaption` | boolean | `true` |
| `linkTo` | string | `"none"` |
| `margin` | array | `[{"desk": ["", "", "", ""], "tablet": ["", "", "", ""], "mobile": ["", "", "", ""]}]` |
| `marginUnit` | string | `"px"` |
| `mobileArrowMargin` | array | `["", "", "", ""]` |
| `mobileForceHover` | boolean | `false` |
| `mobileImageRadius` | array | `["", "", "", ""]` |
| `mobilePadding` | array | `["", "", "", ""]` |
| `mosaicRowHeight` | array | `[150, "", ""]` |
| `mosaicRowHeightUnit` | string | `"px"` |
| `mosaicType` | string | `"first"` |
| `overflow` | boolean | `false` |
| `padding` | array | `["", "", "", ""]` |
| `paddingUnit` | string | `"px"` |
| `shadow` | array | `[{"color": "#000000", "opacity": 0.2, "spread": 0, "blur": 14, "hOffset": 4, "vOffset": 2}]` |
| `shadowHover` | array | `[{"color": "#000000", "opacity": 0.2, "spread": 0, "blur": 14, "hOffset": 4, "vOffset": 2}]` |
| `showCaption` | boolean | `false` |
| `showPauseButton` | boolean | `false` |
| `slideType` | string | `"fade"` |
| `slidesScroll` | string | `"1"` |
| `tabletArrowMargin` | array | `["", "", "", ""]` |
| `tabletImageRadius` | array | `["", "", "", ""]` |
| `tabletPadding` | array | `["", "", "", ""]` |
| `thumbSize` | string | `"large"` |
| `thumbnailColumns` | array | `[4, 4, 4, 4, 4, 4]` |
| `thumbnailControl` | string | `"linked"` |
| `thumbnailRatio` | string | `"land32"` |
| `transSpeed` | number | `400` |
| `type` | string | `"masonry"` |
| `uniqueID` | string |  |

## kadence/advancedheading

**Advanced Text** · category `kadence-blocks` · apiVersion 3

- Supports: `{"ktanimate": true, "ktanimatereveal": true, "ktanimatepreview": true, "ktdynamic": true, "kbMetadata": true, "kbContentLabel": "content"}`

| Attribute | Type | Default |
|---|---|---|
| `align` | string |  |
| `altTitle` | string | `""` |
| `anchor` | string |  |
| `background` | string |  |
| `backgroundColorClass` | string |  |
| `borderRadius` | array | `["", "", "", ""]` |
| `borderRadiusUnit` | string | `"px"` |
| `borderStyle` | array | `[{"top": ["", "", ""], "right": ["", "", ""], "bottom": ["", "", ""], "left": ["", "", ""], "unit": "px"}]` |
| `bottomMargin` | number | `""` |
| `color` | string |  |
| `colorClass` | string |  |
| `content` | string |  |
| `enableMarkBackgroundGradient` | boolean | `false` |
| `enableMarkGradient` | boolean | `false` |
| `enableTextGradient` | boolean | `false` |
| `enableTextShadow` | boolean | `false` |
| `fontHeight` | array | `["", "", ""]` |
| `fontHeightType` | string | `""` |
| `fontSize` | array | `["", "", ""]` |
| `fontStyle` | string | `"normal"` |
| `fontSubset` | string | `""` |
| `fontVariant` | string | `""` |
| `fontWeight` | string | `""` |
| `googleFont` | boolean | `false` |
| `htmlTag` | string | `"heading"` |
| `icon` | string | `""` |
| `iconColor` | string | `""` |
| `iconColorHover` | string | `""` |
| `iconHover` | boolean | `false` |
| `iconPadding` | array | `["", "", "", ""]` |
| `iconPaddingUnit` | string | `"px"` |
| `iconSide` | string | `"left"` |
| `iconSize` | array | `["", "", ""]` |
| `iconSizeUnit` | string | `"px"` |
| `iconTitle` | string | `""` |
| `iconTooltip` | string | `""` |
| `iconTooltipDash` | boolean | `false` |
| `iconTooltipPlacement` | string | `""` |
| `iconVerticalAlign` | string | `"center"` |
| `inQueryBlock` | boolean | `false` |
| `inlineImageBorderRadius` | array | `["", "", "", ""]` |
| `inlineImageBorderRadiusUnit` | string | `"px"` |
| `inlineImageBorderStyles` | array | `[{"top": ["", "", ""], "right": ["", "", ""], "bottom": ["", "", ""], "left": ["", "", ""], "unit": "px"}]` |
| `inlineImageVerticalAlign` | string | `"baseline"` |
| `inlineImageWidth` | array | `[150, "", ""]` |
| `leftMargin` | number | `""` |
| `letterSpacing` | number |  |
| `letterSpacingType` | string | `"px"` |
| `level` | number | `2` |
| `lineHeight` | number |  |
| `lineType` | string | `"px"` |
| `link` | string |  |
| `linkColor` | string |  |
| `linkHoverColor` | string |  |
| `linkNoFollow` | boolean | `false` |
| `linkSponsored` | boolean | `false` |
| `linkStyle` | string |  |
| `linkTarget` | boolean | `false` |
| `loadGoogleFont` | boolean | `true` |
| `loadItalic` | boolean | `false` |
| `margin` | array | `["", "", "", ""]` |
| `marginType` | string | `"px"` |
| `markBG` | string |  |
| `markBGOpacity` | number | `1` |
| `markBackgroundGradient` | string | `""` |
| `markBorder` | string |  |
| `markBorderOpacity` | number | `1` |
| `markBorderRadius` | array | `["", "", "", ""]` |
| `markBorderRadiusUnit` | string | `"px"` |
| `markBorderStyle` | string | `"solid"` |
| `markBorderStyles` | array | `[{"top": ["", "", ""], "right": ["", "", ""], "bottom": ["", "", ""], "left": ["", "", ""], "unit": "px"}]` |
| `markBorderWidth` | number | `0` |
| `markColor` | string | `"#f76a0c"` |
| `markFontStyle` | string | `"normal"` |
| `markFontSubset` | string | `""` |
| `markFontVariant` | string | `""` |
| `markFontWeight` | string | `""` |
| `markGoogleFont` | boolean | `false` |
| `markGradient` | string | `""` |
| `markLetterSpacing` | number |  |
| `markLetterSpacingType` | string | `"px"` |
| `markLineHeight` | array | `["", "", ""]` |
| `markLineType` | string | `"px"` |
| `markLoadGoogleFont` | boolean | `true` |
| `markMobilePadding` | array | `["", "", "", ""]` |
| `markPadding` | array | `[0, 0, 0, 0]` |
| `markPaddingControl` | string | `"linked"` |
| `markPaddingType` | string | `"px"` |
| `markSize` | array | `["", "", ""]` |
| `markSizeType` | string | `"px"` |
| `markTabPadding` | array | `["", "", "", ""]` |
| `markTextTransform` | string | `""` |
| `markTypography` | string | `""` |
| `maxHeight` | array | `["", "", ""]` |
| `maxHeightType` | string | `"px"` |
| `maxWidth` | array | `["", "", ""]` |
| `maxWidthType` | string | `"px"` |
| `mobileAlign` | string |  |
| `mobileBorderRadius` | array | `["", "", "", ""]` |
| `mobileBorderStyle` | array | `[{"top": ["", "", ""], "right": ["", "", ""], "bottom": ["", "", ""], "left": ["", "", ""], "unit": "px"}]` |
| `mobileIconPadding` | array | `["", "", "", ""]` |
| `mobileInlineImageBorderRadius` | array | `["", "", "", ""]` |
| `mobileInlineImageBorderStyles` | array | `[{"top": ["", "", ""], "right": ["", "", ""], "bottom": ["", "", ""], "left": ["", "", ""], "unit": "px"}]` |
| `mobileLetterSpacing` | number |  |
| `mobileLineHeight` | number |  |
| `mobileMargin` | array | `["", "", "", ""]` |
| `mobileMarginType` | string | `"px"` |
| `mobileMarkBorderRadius` | array | `["", "", "", ""]` |
| `mobileMarkBorderStyles` | array | `[{"top": ["", "", ""], "right": ["", "", ""], "bottom": ["", "", ""], "left": ["", "", ""], "unit": "px"}]` |
| `mobileMarkLetterSpacing` | number |  |
| `mobilePadding` | array | `["", "", "", ""]` |
| `mobileSize` | number |  |
| `mobileTextOrientation` | string |  |
| `padding` | array | `["", "", "", ""]` |
| `paddingType` | string | `"px"` |
| `ratio` | string | `""` |
| `rightMargin` | number | `""` |
| `size` | number |  |
| `sizeType` | string | `"px"` |
| `tabLineHeight` | number |  |
| `tabSize` | number |  |
| `tabletAlign` | string |  |
| `tabletBorderRadius` | array | `["", "", "", ""]` |
| `tabletBorderStyle` | array | `[{"top": ["", "", ""], "right": ["", "", ""], "bottom": ["", "", ""], "left": ["", "", ""], "unit": "px"}]` |
| `tabletIconPadding` | array | `["", "", "", ""]` |
| `tabletInlineImageBorderRadius` | array | `["", "", "", ""]` |
| `tabletInlineImageBorderStyles` | array | `[{"top": ["", "", ""], "right": ["", "", ""], "bottom": ["", "", ""], "left": ["", "", ""], "unit": "px"}]` |
| `tabletLetterSpacing` | number |  |
| `tabletMargin` | array | `["", "", "", ""]` |
| `tabletMarginType` | string | `"px"` |
| `tabletMarkBorderRadius` | array | `["", "", "", ""]` |
| `tabletMarkBorderStyles` | array | `[{"top": ["", "", ""], "right": ["", "", ""], "bottom": ["", "", ""], "left": ["", "", ""], "unit": "px"}]` |
| `tabletMarkLetterSpacing` | number |  |
| `tabletPadding` | array | `["", "", "", ""]` |
| `tabletTextOrientation` | string |  |
| `textGradient` | string | `""` |
| `textOrientation` | string |  |
| `textShadow` | array | `[{"enable": false, "color": "#000000", "opacity": 0.2, "blur": 1, "hOffset": 1, "vOffset": 1}]` |
| `textShadowMobile` | array | `[{"enable": false, "color": "", "opacity": "", "blur": "", "hOffset": "", "vOffset": ""}]` |
| `textShadowTablet` | array | `[{"enable": false, "color": "", "opacity": "", "blur": "", "hOffset": "", "vOffset": ""}]` |
| `textTransform` | string | `""` |
| `topMargin` | number | `""` |
| `typography` | string | `""` |
| `uniqueID` | string |  |
| `useRatio` | boolean | `false` |

## kadence/column

**Section** · category `kadence-blocks` · apiVersion 3

- Supports: `{"anchor": true, "ktanimate": true, "ktanimateadd": true, "ktanimatepreview": true, "ktanimateswipe": true, "ktdynamic": true, "kbcss": true, "kbMetadata": true}`

| Attribute | Type | Default |
|---|---|---|
| `align` | string | `""` |
| `background` | string | `""` |
| `backgroundHover` | string | `""` |
| `backgroundHoverType` | string | `"normal"` |
| `backgroundImg` | array | `[{"bgImg": "", "bgImgID": "", "bgImgSize": "cover", "bgImgPosition": "center center", "bgImgAttachment": "scroll", "bgImgRepeat": "no-repeat"}]` |
| `backgroundImgHover` | array | `[{"bgImg": "", "bgImgID": "", "bgImgSize": "cover", "bgImgPosition": "center center", "bgImgAttachment": "scroll", "bgImgRepeat": "no-repeat"}]` |
| `backgroundOpacity` | number | `1` |
| `backgroundType` | string | `"normal"` |
| `bgColorClass` | string | `""` |
| `border` | string | `""` |
| `borderHover` | string | `""` |
| `borderHoverRadius` | array | `["", "", "", ""]` |
| `borderHoverRadiusUnit` | string | `"px"` |
| `borderHoverStyle` | array | `[{"top": ["", "", ""], "right": ["", "", ""], "bottom": ["", "", ""], "left": ["", "", ""], "unit": "px"}]` |
| `borderHoverWidth` | array | `["", "", "", ""]` |
| `borderOpacity` | number | `1` |
| `borderRadius` | array | `[0, 0, 0, 0]` |
| `borderRadiusUnit` | string | `"px"` |
| `borderStyle` | array | `[{"top": ["", "", ""], "right": ["", "", ""], "bottom": ["", "", ""], "left": ["", "", ""], "unit": "px"}]` |
| `borderWidth` | array | `[0, 0, 0, 0]` |
| `bottomMargin` | number | `""` |
| `bottomMarginM` | number | `""` |
| `bottomMarginT` | number | `""` |
| `bottomPadding` | number | `""` |
| `bottomPaddingM` | number | `""` |
| `bottomPaddingT` | number | `""` |
| `collapseOrder` | number |  |
| `direction` | array | `["", "", ""]` |
| `displayHoverShadow` | boolean | `false` |
| `displayShadow` | boolean | `false` |
| `flexBasis` | array | `["", "", ""]` |
| `flexBasisUnit` | string | `"px"` |
| `flexGrow` | array | `["", "", ""]` |
| `gradient` | string | `""` |
| `gradientHover` | string | `""` |
| `gridArea` | string | `""` |
| `gutter` | array | `["", "", ""]` |
| `gutterUnit` | string | `"px"` |
| `gutterVariable` | array | `["", "", ""]` |
| `height` | array | `["", "", ""]` |
| `heightUnit` | string | `"px"` |
| `hoverOverlayBlendMode` | string |  |
| `htmlTag` | string | `"div"` |
| `id` | number | `1` |
| `inQueryBlock` | boolean | `false` |
| `justifyContent` | array | `["", "", ""]` |
| `kadenceFieldConditional` | object |  |
| `kbVersion` | number | `""` |
| `leftMargin` | number | `""` |
| `leftMarginM` | number | `""` |
| `leftMarginT` | number | `""` |
| `leftPadding` | number | `""` |
| `leftPaddingM` | number | `""` |
| `leftPaddingT` | number | `""` |
| `link` | string | `""` |
| `linkColor` | string | `""` |
| `linkColorHover` | string | `""` |
| `linkHoverColor` | string | `""` |
| `linkHoverColorHover` | string | `""` |
| `linkNoFollow` | boolean | `false` |
| `linkSponsored` | boolean | `false` |
| `linkTarget` | boolean | `false` |
| `linkTitle` | string | `""` |
| `margin` | array | `["", "", "", ""]` |
| `marginType` | string | `"px"` |
| `maxWidth` | array | `["", "", ""]` |
| `maxWidthMobileUnit` | string | `""` |
| `maxWidthTabletUnit` | string | `""` |
| `maxWidthUnit` | string | `"px"` |
| `mobileBorderHoverRadius` | array | `["", "", "", ""]` |
| `mobileBorderHoverStyle` | array | `[{"top": ["", "", ""], "right": ["", "", ""], "bottom": ["", "", ""], "left": ["", "", ""], "unit": "px"}]` |
| `mobileBorderHoverWidth` | array | `["", "", "", ""]` |
| `mobileBorderRadius` | array | `["", "", "", ""]` |
| `mobileBorderStyle` | array | `[{"top": ["", "", ""], "right": ["", "", ""], "bottom": ["", "", ""], "left": ["", "", ""], "unit": "px"}]` |
| `mobileBorderWidth` | array | `["", "", "", ""]` |
| `mobileMargin` | array | `["", "", "", ""]` |
| `mobilePadding` | array | `["", "", "", ""]` |
| `noCustomDefaults` | boolean | `false` |
| `overlay` | string | `""` |
| `overlayBlendMode` | string |  |
| `overlayGradient` | string | `""` |
| `overlayGradientHover` | string | `""` |
| `overlayHover` | string | `""` |
| `overlayHoverOpacity` | number | `""` |
| `overlayHoverType` | string | `"normal"` |
| `overlayImg` | array | `[{"bgImg": "", "bgImgID": "", "bgImgSize": "cover", "bgImgPosition": "center center", "bgImgAttachment": "scroll", "bgImgRepeat": "no-repeat"}]` |
| `overlayImgHover` | array | `[{"bgImg": "", "bgImgID": "", "bgImgSize": "cover", "bgImgPosition": "center center", "bgImgAttachment": "scroll", "bgImgRepeat": "no-repeat"}]` |
| `overlayOpacity` | number | `0.3` |
| `overlayType` | string | `"normal"` |
| `padding` | array | `["", "", "", ""]` |
| `paddingType` | string | `"px"` |
| `rightMargin` | number | `""` |
| `rightMarginM` | number | `""` |
| `rightMarginT` | number | `""` |
| `rightPadding` | number | `""` |
| `rightPaddingM` | number | `""` |
| `rightPaddingT` | number | `""` |
| `rowGap` | array | `["", "", ""]` |
| `rowGapUnit` | string | `"px"` |
| `rowGapVariable` | array | `["", "", ""]` |
| `shadow` | array | `[{"color": "#000000", "opacity": 0.2, "spread": 0, "blur": 14, "hOffset": 0, "vOffset": 0, "inset": false}]` |
| `shadowHover` | array | `[{"color": "#000000", "opacity": 0.2, "spread": 0, "blur": 14, "hOffset": 0, "vOffset": 0, "inset": false}]` |
| `sticky` | boolean | `false` |
| `stickyOffset` | array | `["", "", ""]` |
| `stickyOffsetUnit` | string | `"px"` |
| `tabletBorderHoverRadius` | array | `["", "", "", ""]` |
| `tabletBorderHoverStyle` | array | `[{"top": ["", "", ""], "right": ["", "", ""], "bottom": ["", "", ""], "left": ["", "", ""], "unit": "px"}]` |
| `tabletBorderHoverWidth` | array | `["", "", "", ""]` |
| `tabletBorderRadius` | array | `["", "", "", ""]` |
| `tabletBorderStyle` | array | `[{"top": ["", "", ""], "right": ["", "", ""], "bottom": ["", "", ""], "left": ["", "", ""], "unit": "px"}]` |
| `tabletBorderWidth` | array | `["", "", "", ""]` |
| `tabletMargin` | array | `["", "", "", ""]` |
| `tabletPadding` | array | `["", "", "", ""]` |
| `templateLock` | string \| boolean |  |
| `textAlign` | array | `["", "", ""]` |
| `textColor` | string | `""` |
| `textColorHover` | string | `""` |
| `topMargin` | number | `""` |
| `topMarginM` | number | `""` |
| `topMarginT` | number | `""` |
| `topPadding` | number | `""` |
| `topPaddingM` | number | `""` |
| `topPaddingT` | number | `""` |
| `uniqueID` | string | `""` |
| `verticalAlignment` | string |  |
| `verticalAlignmentMobile` | string |  |
| `verticalAlignmentTablet` | string |  |
| `vsdesk` | boolean | `false` |
| `vsmobile` | boolean | `false` |
| `vstablet` | boolean | `false` |
| `wrapContent` | array | `["", "", ""]` |
| `zIndex` | number | `""` |

## kadence/countdown

**Countdown** · category `kadence-blocks` · apiVersion 3

- Supports: `{"anchor": true, "align": ["wide", "full"], "reusable": false, "html": false, "kbMetadata": true}`

| Attribute | Type | Default |
|---|---|---|
| `background` | string | `""` |
| `border` | string | `""` |
| `borderRadius` | array | `[0, 0, 0, 0]` |
| `borderWidth` | array | `[0, 0, 0, 0]` |
| `campaignID` | string |  |
| `containerMargin` | array | `["", "", "", ""]` |
| `containerMobileMargin` | array | `["", "", "", ""]` |
| `containerMobilePadding` | array | `["", "", "", ""]` |
| `containerPadding` | array | `["", "", "", ""]` |
| `containerTabletMargin` | array | `["", "", "", ""]` |
| `containerTabletPadding` | array | `["", "", "", ""]` |
| `countdownDivider` | boolean | `false` |
| `countdownType` | string | `"date"` |
| `counterAlign` | array | `["", "", ""]` |
| `date` | string | `""` |
| `daysLabel` | string | `""` |
| `enablePauseButton` | boolean | `false` |
| `enableTimer` | boolean | `true` |
| `endDate` | string | `""` |
| `evergreenHours` | number | `0` |
| `evergreenMinutes` | number | `0` |
| `evergreenReset` | number | `30` |
| `evergreenStrict` | boolean | `false` |
| `expireAction` | string | `"none"` |
| `frequency` | string | `"daily"` |
| `hoursLabel` | string | `""` |
| `itemBackground` | string | `""` |
| `itemBorder` | string | `""` |
| `itemBorderRadius` | array | `[0, 0, 0, 0]` |
| `itemBorderWidth` | array | `["", "", "", ""]` |
| `itemMobileBorderWidth` | array | `["", "", "", ""]` |
| `itemMobilePadding` | array | `["", "", "", ""]` |
| `itemPadding` | array | `["", "", "", ""]` |
| `itemPaddingType` | string | `"px"` |
| `itemTabletBorderWidth` | array | `["", "", "", ""]` |
| `itemTabletPadding` | array | `["", "", "", ""]` |
| `labelColor` | string |  |
| `labelFont` | array | `[{"size": ["", "", ""], "sizeType": "px", "lineHeight": ["", "", ""], "lineType": "px", "letterSpacing": ["", "", ""], "letterType": "px", "textTransform": "", "family": "", "google": false, "style": "", "weight": "", "variant": "", "subset": "", "loadGoogle": true}]` |
| `marginType` | string | `"px"` |
| `minutesLabel` | string | `""` |
| `mobileBorderWidth` | array | `["", "", "", ""]` |
| `numberColor` | string |  |
| `numberFont` | array | `[{"size": ["", "", ""], "sizeType": "px", "lineHeight": ["", "", ""], "lineType": "px", "letterSpacing": ["", "", ""], "letterType": "px", "textTransform": "", "family": "", "google": false, "style": "", "weight": "", "variant": "", "subset": "", "loadGoogle": true}]` |
| `paddingType` | string | `"px"` |
| `pauseButtonPosition` | string | `"top-right"` |
| `postLabel` | string | `""` |
| `postLabelColor` | string |  |
| `postLabelFont` | array | `[{"size": ["", "", ""], "sizeType": "px", "lineHeight": ["", "", ""], "lineType": "px", "letterSpacing": ["", "", ""], "letterType": "px", "textTransform": "", "family": "", "google": false, "style": "", "weight": "", "variant": "", "subset": "", "loadGoogle": true}]` |
| `preLabel` | string | `""` |
| `preLabelColor` | string |  |
| `preLabelFont` | array | `[{"size": ["", "", ""], "sizeType": "px", "lineHeight": ["", "", ""], "lineType": "px", "letterSpacing": ["", "", ""], "letterType": "px", "textTransform": "", "family": "", "google": false, "style": "", "weight": "", "variant": "", "subset": "", "loadGoogle": true}]` |
| `redirectURL` | string | `""` |
| `repeat` | boolean | `false` |
| `revealOnLoad` | boolean | `false` |
| `secondsLabel` | string | `""` |
| `stopRepeating` | boolean | `false` |
| `tabletBorderWidth` | array | `["", "", "", ""]` |
| `timeNumbers` | boolean | `false` |
| `timeOffset` | number | `""` |
| `timerLayout` | string | `"block"` |
| `timestamp` | number | `""` |
| `timezone` | string | `""` |
| `uniqueID` | string | `""` |
| `units` | array | `[{"days": true, "hours": true, "minutes": true, "seconds": true}]` |
| `vsdesk` | boolean | `false` |
| `vsmobile` | boolean | `false` |
| `vstablet` | boolean | `false` |

## kadence/countdown-inner

**Countdown Content** · category `kadence-blocks` · apiVersion 3

- Parent-only: must be a direct child of `kadence/countdown`
- Supports: `{"inserter": false, "reusable": false, "html": false, "kbMetadata": true}`

| Attribute | Type | Default |
|---|---|---|
| `location` | string |  |
| `uniqueID` | string |  |

## kadence/countdown-timer

**Countdown Timer** · category `kadence-blocks` · apiVersion 3

- Parent-only: must be a direct child of `kadence/countdown`
- Supports: `{"inserter": false, "reusable": false, "html": false, "kbMetadata": true}`

| Attribute | Type | Default |
|---|---|---|
| `uniqueID` | string |  |

## kadence/countup

**Count Up** · category `kadence-blocks` · apiVersion 3

- Supports: `{"kbMetadata": true}`

| Attribute | Type | Default |
|---|---|---|
| `decimal` | string | `""` |
| `decimalSpaces` | number | `2` |
| `displayTitle` | boolean | `true` |
| `duration` | number | `2.5` |
| `end` | number | `100` |
| `endDecimal` | string |  |
| `numberAlign` | array | `["", "", ""]` |
| `numberColor` | string | `""` |
| `numberFont` | array | `[{"size": ["50", "", ""], "sizeType": "px", "lineHeight": ["", "", ""], "lineType": "px", "letterSpacing": "", "textTransform": "", "family": "", "google": false, "style": "", "weight": "", "variant": "", "subset": "", "loadGoogle": true}]` |
| `numberHoverColor` | string | `""` |
| `numberMargin` | array | `["", "", "", ""]` |
| `numberMarginType` | string | `"px"` |
| `numberMinHeight` | array | `["", "", ""]` |
| `numberMobileMargin` | array | `["", "", "", ""]` |
| `numberMobilePadding` | array | `["", "", "", ""]` |
| `numberPadding` | array | `["", "", "", ""]` |
| `numberPaddingType` | string | `"px"` |
| `numberTabletMargin` | array | `["", "", "", ""]` |
| `numberTabletPadding` | array | `["", "", "", ""]` |
| `prefix` | string | `""` |
| `separator` | string | `""` |
| `start` | number | `0` |
| `startDecimal` | string |  |
| `suffix` | string | `""` |
| `title` | string | `""` |
| `titleAlign` | array | `["", "", ""]` |
| `titleColor` | string | `""` |
| `titleFont` | array | `[{"level": 4, "htmlTag": "div", "size": ["", "", ""], "sizeType": "px", "lineHeight": ["", "", ""], "lineType": "", "letterSpacing": "", "textTransform": "", "family": "", "google": false, "style": "", "weight": "", "variant": "", "subset": "", "loadGoogle": true}]` |
| `titleHoverColor` | string | `""` |
| `titleMargin` | array | `["", "", "", ""]` |
| `titleMarginType` | string | `"px"` |
| `titleMinHeight` | array | `["", "", ""]` |
| `titleMobileMargin` | array | `["", "", "", ""]` |
| `titleMobilePadding` | array | `["", "", "", ""]` |
| `titlePadding` | array | `["", "", "", ""]` |
| `titlePaddingType` | string | `"px"` |
| `titleTabletMargin` | array | `["", "", "", ""]` |
| `titleTabletPadding` | array | `["", "", "", ""]` |
| `uniqueID` | string | `""` |

## kadence/form

**Form** · category `kadence-blocks` · apiVersion 3

- Supports: `{"anchor": true, "align": ["wide", "full"], "ktanimate": true, "ktanimateadd": true, "ktanimatepreview": true, "ktanimateswipe": true, "kbMetadata": true, "inserter": false}`

| Attribute | Type | Default |
|---|---|---|
| `actions` | array | `["email"]` |
| `containerMargin` | array | `["", "", "", ""]` |
| `containerMarginType` | string | `"px"` |
| `email` | array | `[{"emailTo": "", "subject": "", "fromEmail": "", "fromName": "", "replyTo": "email_field", "cc": "", "bcc": "", "html": true}]` |
| `fields` | array | `[{"label": "Name", "showLabel": true, "placeholder": "", "default": "", "description": "", "rows": 4, "options": [{"value": "", "label": ""}], "multiSelect": false, "inline": false, "showLink": false, "min": "", "max": "", "type": "text", "required": false, "width": ["100", "", ""], "auto": "", "errorMessage": "", "requiredMessage": "", "slug": "", "ariaLabel": ""}, {"label": "Email", "showLabel": true, "placeholder": "", "default": "", "description": "", "rows": 4, "options": [{"value": "", "label": ""}], "multiSelect": false, "inline": false, "showLink": false, "min": "", "max": "", "type": "email", "required": true, "width": ["100", "", ""], "auto": "", "errorMessage": "", "requiredMessage": "", "slug": "", "ariaLabel": ""}, {"label": "Message", "showLabel": true, "placeholder": "", "default": "", "description": "", "rows": 4, "options": [{"value": "", "label": ""}], "multiSelect": false, "inline": false, "showLink": false, "min": "", "max": "", "type": "textarea", "required": true, "width": ["100", "", ""], "auto": "", "errorMessage": "", "requiredMessage": "", "slug": "", "ariaLabel": ""}]` |
| `fluentcrm` | array | `[{"lists": [], "tags": [], "map": [], "doubleOptin": false}]` |
| `hAlign` | string | `""` |
| `hAlignFormFeilds` | boolean | `false` |
| `honeyPot` | boolean | `true` |
| `labelFont` | array | `[{"color": "", "size": ["", "", ""], "sizeType": "px", "lineHeight": ["", "", ""], "lineType": "px", "letterSpacing": "", "textTransform": "", "family": "", "google": "", "style": "", "weight": "", "variant": "", "subset": "", "loadGoogle": true, "padding": ["", "", "", ""], "margin": ["", "", "", ""]}]` |
| `mailerlite` | array | `[{"group": [], "map": []}]` |
| `messageFont` | array | `[{"colorSuccess": "", "colorError": "", "borderSuccess": "", "borderError": "", "backgroundSuccess": "", "backgroundSuccessOpacity": 1, "backgroundError": "", "backgroundErrorOpacity": 1, "borderWidth": ["", "", "", ""], "borderRadius": "", "size": ["", "", ""], "sizeType": "px", "lineHeight": ["", "", ""], "lineType": "px", "letterSpacing": "", "textTransform": "", "family": "", "google": "", "style": "", "weight": "", "variant": "", "subset": "", "loadGoogle": true, "padding": ["", "", "", ""], "margin": ["", "", "", ""]}]` |
| `messages` | array | `[{"success": "", "error": "", "required": "", "invalid": "", "recaptchaerror": "", "preError": ""}]` |
| `mobileContainerMargin` | array | `["", "", "", ""]` |
| `postID` | string | `""` |
| `recaptcha` | boolean | `false` |
| `recaptchaVersion` | string | `"v3"` |
| `redirect` | string | `""` |
| `style` | array | `[{"showRequired": true, "size": "standard", "deskPadding": ["", "", "", ""], "tabletPadding": ["", "", "", ""], "mobilePadding": ["", "", "", ""], "color": "", "requiredColor": "", "background": "", "border": "", "backgroundOpacity": 1, "borderOpacity": 1, "borderRadius": "", "borderWidth": ["", "", "", ""], "colorActive": "", "backgroundActive": "", "borderActive": "", "backgroundActiveOpacity": 1, "borderActiveOpacity": 1, "gradient": ["#999999", 1, 0, 100, "linear", 180, "center center"], "gradientActive": ["#777777", 1, 0, 100, "linear", 180, "center center"], "backgroundType": "solid", "backgroundActiveType": "solid", "boxShadow": [false, "#000000", 0.2, 1, 1, 2, 0, false], "boxShadowActive": [false, "#000000", 0.4, 2, 2, 3, 0, false], "fontSize": ["", "", ""], "fontSizeType": "px", "lineHeight": ["", "", ""], "lineType": "px", "rowGap": "", "rowGapType": "px", "gutter": "", "gutterType": "px", "tabletRowGap": "", "mobileRowGap": "", "tabletGutter": "", "mobileGutter": ""}]` |
| `submit` | array | `[{"label": "", "width": ["100", "", ""], "size": "standard", "widthType": "auto", "fixedWidth": ["", "", ""], "align": ["", "", ""], "deskPadding": ["", "", "", ""], "tabletPadding": ["", "", "", ""], "mobilePadding": ["", "", "", ""], "color": "", "background": "", "border": "", "backgroundOpacity": 1, "borderOpacity": 1, "borderRadius": "", "borderWidth": ["", "", "", ""], "colorHover": "", "backgroundHover": "", "borderHover": "", "backgroundHoverOpacity": 1, "borderHoverOpacity": 1, "icon": "", "iconSide": "right", "iconHover": false, "cssClass": "", "gradient": ["#999999", 1, 0, 100, "linear", 180, "center center"], "gradientHover": ["#777777", 1, 0, 100, "linear", 180, "center center"], "btnStyle": "basic", "btnSize": "standard", "backgroundType": "solid", "backgroundHoverType": "solid", "boxShadow": [false, "#000000", 0.2, 1, 1, 2, 0, false], "boxShadowHover": [false, "#000000", 0.4, 2, 2, 3, 0, false]}]` |
| `submitFont` | array | `[{"size": ["", "", ""], "sizeType": "px", "lineHeight": ["", "", ""], "lineType": "px", "letterSpacing": "", "textTransform": "", "family": "", "google": "", "style": "", "weight": "", "variant": "", "subset": "", "loadGoogle": true}]` |
| `submitLabel` | string | `""` |
| `submitMargin` | array | `[{"desk": ["", "", "", ""], "tablet": ["", "", "", ""], "mobile": ["", "", "", ""], "unit": "px", "control": "linked"}]` |
| `tabletContainerMargin` | array | `["", "", "", ""]` |
| `uniqueID` | string | `""` |

## kadence/googlemaps

**Google Maps** · category `kadence-blocks` · apiVersion 3

- Supports: `{"kbMetadata": true, "ktdynamic": true}`

| Attribute | Type | Default |
|---|---|---|
| `apiType` | string | `"embed"` |
| `customSnazzy` | string | `""` |
| `heightDesktop` | number | `450` |
| `heightMobile` | number | `""` |
| `heightTablet` | number | `""` |
| `kbVersion` | number | `""` |
| `lat` | string | `""` |
| `lng` | string | `""` |
| `location` | string | `"Golden Gate Bridge"` |
| `mapFilter` | string | `"standard"` |
| `mapFilterAmount` | number | `50` |
| `mapStyle` | string | `"standard"` |
| `mapType` | string | `"roadmap"` |
| `marginDesktop` | array | `["", "", "", ""]` |
| `marginMobile` | array | `["", "", "", ""]` |
| `marginTablet` | array | `["", "", "", ""]` |
| `marginUnit` | string | `"px"` |
| `paddingDesktop` | array | `["", "", "", ""]` |
| `paddingMobile` | array | `["", "", "", ""]` |
| `paddingTablet` | array | `["", "", "", ""]` |
| `paddingUnit` | string | `"px"` |
| `showControls` | boolean | `true` |
| `showMarker` | boolean | `true` |
| `textAlign` | array | `["", "", ""]` |
| `uniqueID` | string |  |
| `width` | number | `""` |
| `widthDesktop` | number | `""` |
| `widthMobile` | number | `""` |
| `widthTablet` | number | `""` |
| `zoom` | number | `"11"` |

## kadence/header

**Header (Adv)** · category `kadence-blocks` · apiVersion 3

- Supports: `{"html": false, "customClassName": false, "reusable": false, "lock": false, "kbMetadata": true, "ktdynamic": true}`

| Attribute | Type | Default |
|---|---|---|
| `id` | integer | `0` |
| `uniqueID` | string |  |

## kadence/header-column

**Header Column** · category `kadence-blocks` · apiVersion 3

- Parent-only: must be a direct child of `kadence/header`
- Supports: `{"inserter": true}`

| Attribute | Type | Default |
|---|---|---|
| `location` | string |  |
| `uniqueID` | string |  |

## kadence/header-container-desktop

**Desktop Header** · category `design` · apiVersion 3

- Parent-only: must be a direct child of `kadence/header`
- Supports: `{"inserter": true}`

| Attribute | Type | Default |
|---|---|---|
| `uniqueID` | string | `"default-uniqueID"` |

## kadence/header-container-tablet

**Tablet Header** · category `design` · apiVersion 3

- Parent-only: must be a direct child of `kadence/header`
- Supports: `{"inserter": true}`

| Attribute | Type | Default |
|---|---|---|
| `uniqueID` | string | `"default-uniqueID"` |

## kadence/header-row

**Header Row** · category `design` · apiVersion 3

- Parent-only: must be a direct child of `kadence/header`
- Supports: `{"inserter": true, "ktdynamic": true, "kbcss": true}`

| Attribute | Type | Default |
|---|---|---|
| `background` | object | `{"color": "", "image": "", "imageID": "", "position": "center center", "size": "cover", "repeat": "no-repeat", "attachment": "scroll", "type": "normal", "gradient": ""}` |
| `backgroundTransparent` | object | `{"color": "transparent", "image": "", "imageID": "", "position": "center center", "size": "cover", "repeat": "no-repeat", "attachment": "scroll", "type": "normal", "gradient": ""}` |
| `border` | array | `[{"top": ["", "", ""], "right": ["", "", ""], "bottom": ["", "", ""], "left": ["", "", ""], "unit": "px"}]` |
| `borderMobile` | array | `[{"top": ["", "", ""], "right": ["", "", ""], "bottom": ["", "", ""], "left": ["", "", ""], "unit": "px"}]` |
| `borderRadius` | array | `["", "", "", ""]` |
| `borderRadiusMobile` | array | `["", "", "", ""]` |
| `borderRadiusTablet` | array | `["", "", "", ""]` |
| `borderRadiusUnit` | string | `"px"` |
| `borderTablet` | array | `[{"top": ["", "", ""], "right": ["", "", ""], "bottom": ["", "", ""], "left": ["", "", ""], "unit": "px"}]` |
| `itemGap` | string | `"xs"` |
| `itemGapMobile` | string | `""` |
| `itemGapTablet` | string | `""` |
| `itemGapUnit` | string | `"px"` |
| `layout` | string | `""` |
| `layoutConfig` | string | `""` |
| `location` | string |  |
| `margin` | array | `["", "", "", ""]` |
| `marginMobile` | array | `["", "", "", ""]` |
| `marginTablet` | array | `["", "", "", ""]` |
| `marginUnit` | string | `"px"` |
| `maxWidth` | number | `null` |
| `maxWidthMobile` | number | `null` |
| `maxWidthTablet` | number | `null` |
| `maxWidthUnit` | string | `"px"` |
| `minHeight` | number | `null` |
| `minHeightMobile` | number | `null` |
| `minHeightTablet` | number | `null` |
| `minHeightUnit` | string | `"px"` |
| `padding` | array | `["", "", "", ""]` |
| `paddingMobile` | array | `["", "", "", ""]` |
| `paddingTablet` | array | `["", "", "", ""]` |
| `paddingUnit` | string | `"px"` |
| `sectionPriority` | string | `""` |
| `sectionPriorityMobile` | string | `""` |
| `sectionPriorityTablet` | string | `""` |
| `uniqueID` | string |  |
| `vAlign` | string | `""` |
| `vAlignMobile` | string | `""` |
| `vAlignTablet` | string | `""` |

## kadence/header-section

**Header Section** · category `design` · apiVersion 3

- Parent-only: must be a direct child of `kadence/header`
- Supports: `{"inserter": true}`

| Attribute | Type | Default |
|---|---|---|
| `location` | string |  |
| `uniqueID` | string |  |

## kadence/icon

**Icon** · category `kadence-blocks` · apiVersion 3

- Supports: `{"ktdynamic": true, "kbMetadata": true}`

| Attribute | Type | Default |
|---|---|---|
| `blockAlignment` | string | `""` |
| `gap` | array | `["", "", ""]` |
| `gapUnit` | string | `"px"` |
| `iconCount` | number | `1` |
| `icons` | array | `[{"icon": "fe_aperture", "link": "", "target": "_self", "size": 50, "width": 2, "title": "", "color": "palette4", "background": "transparent", "border": "palette4", "borderRadius": 0, "borderWidth": 2, "padding": [20, 20, 20, 20], "paddingUnit": "px", "style": "default", "margin": ["", "", "", ""], "marginUnit": "px", "hColor": "", "hBackground": "", "hBorder": "", "linkTitle": "", "tabletSize": "", "mobileSize": "", "tabletMargin": ["", "", "", ""], "mobileMargin": ["", "", "", ""], "tabletPadding": ["", "", "", ""], "mobilePadding": ["", "", "", ""]}]` |
| `inQueryBlock` | boolean | `false` |
| `mobileTextAlignment` | string |  |
| `tabletTextAlignment` | string |  |
| `textAlignment` | string | `"center"` |
| `uniqueID` | string | `""` |
| `verticalAlignment` | string |  |
| `wrapIcons` | boolean | `false` |

## kadence/iconlist

**Icon List** · category `kadence-blocks` · apiVersion 3

- Supports: `{"ktdynamic": true, "kbMetadata": true}`

| Attribute | Type | Default |
|---|---|---|
| `background` | string | `""` |
| `blockAlignment` | string | `"none"` |
| `border` | string | `""` |
| `borderRadius` | number | `""` |
| `borderWidth` | number | `""` |
| `color` | string | `""` |
| `columnGap` | number | `0` |
| `columns` | number | `1` |
| `icon` | string | `"fe_checkCircle"` |
| `iconAlign` | string | `"middle"` |
| `iconSize` | array | `["", "", ""]` |
| `items` | array | `[{"icon": "fe_checkCircle", "link": "", "target": "_self", "size": 20, "width": 2, "text": "", "color": "", "background": "", "border": "", "borderRadius": 0, "padding": 5, "borderWidth": 1, "style": "default", "level": 0}]` |
| `linkColor` | string | `""` |
| `linkHoverColor` | string | `""` |
| `linkUnderline` | string | `"inherit"` |
| `listCount` | number | `1` |
| `listGap` | number | `5` |
| `listLabelGap` | number | `10` |
| `listMargin` | array | `["0", "0", "sm", "0"]` |
| `listMarginType` | string | `"px"` |
| `listPadding` | array | `["", "", "", ""]` |
| `listPaddingType` | string | `"px"` |
| `listStyles` | array | `[{"size": ["", "", ""], "sizeType": "px", "lineHeight": ["", "", ""], "lineType": "px", "letterSpacing": "", "family": "", "google": false, "style": "", "weight": "", "variant": "", "subset": "", "loadGoogle": true, "color": "", "textTransform": ""}]` |
| `mobileColumnGap` | number | `""` |
| `mobileColumns` | number | `""` |
| `mobileListGap` | number | `""` |
| `mobileListMargin` | array | `["", "", "", ""]` |
| `mobileListPadding` | array | `["", "", "", ""]` |
| `padding` | number | `""` |
| `style` | string | `"default"` |
| `tabletColumnGap` | number | `""` |
| `tabletColumns` | number | `""` |
| `tabletListGap` | number | `""` |
| `tabletListMargin` | array | `["", "", "", ""]` |
| `tabletListPadding` | array | `["", "", "", ""]` |
| `uniqueID` | string | `""` |
| `width` | number | `2` |

## kadence/identity

**Site identity** · category `kadence-blocks` · apiVersion 3

- Supports: `{"anchor": true, "kbMetadata": true}`

| Attribute | Type | Default |
|---|---|---|
| `align` | string |  |
| `idSticky` | number |  |
| `idTransparent` | number |  |
| `layout` | string | `"logo-left"` |
| `link` | string | `""` |
| `linkToHomepage` | boolean | `true` |
| `margin` | array | `["", "", "", ""]` |
| `marginType` | string | `"px"` |
| `mobileMargin` | array | `["", "", "", ""]` |
| `mobilePadding` | array | `["", "", "", ""]` |
| `padding` | array | `["", "", "", ""]` |
| `paddingType` | string | `"px"` |
| `showSiteTagline` | boolean | `false` |
| `showSiteTitle` | boolean | `true` |
| `sizeSlugSticky` | string |  |
| `sizeSlugTransparent` | string |  |
| `tabletMargin` | array | `["", "", "", ""]` |
| `tabletPadding` | array | `["", "", "", ""]` |
| `taglineTypography` | array | `[{"size": ["", "", ""], "sizeType": "px", "lineHeight": ["", "", ""], "lineType": "px", "letterSpacing": ["", "", ""], "letterType": "px", "textTransform": "", "family": "", "google": false, "style": "", "weight": "", "variant": "", "subset": "", "loadGoogle": true}]` |
| `textVerticalAlign` | string | `"center"` |
| `titleTypography` | array | `[{"size": ["", "", ""], "sizeType": "px", "lineHeight": ["", "", ""], "lineType": "px", "letterSpacing": ["", "", ""], "letterType": "px", "textTransform": "", "family": "", "google": false, "style": "", "weight": "", "variant": "", "subset": "", "loadGoogle": true}]` |
| `uniqueID` | string |  |
| `urlSticky` | string | `""` |
| `urlTransparent` | string | `""` |

## kadence/image

**Advanced Image** · category `kadence-blocks` · apiVersion 3

- Supports: `{"anchor": true, "ktanimate": true, "ktanimateadd": true, "ktanimatepreview": true, "ktdynamic": true, "kbMetadata": true}`

| Attribute | Type | Default |
|---|---|---|
| `align` | string |  |
| `alt` | string | `""` |
| `altSticky` | string |  |
| `altTransparent` | string |  |
| `backgroundColor` | string | `""` |
| `borderColor` | string | `""` |
| `borderRadius` | array | `["", "", "", ""]` |
| `borderRadiusUnit` | string | `"px"` |
| `borderStyle` | array | `[{"top": ["", "", ""], "right": ["", "", ""], "bottom": ["", "", ""], "left": ["", "", ""], "unit": "px"}]` |
| `borderWidthDesktop` | array | `["", "", "", ""]` |
| `borderWidthMobile` | array | `["", "", "", ""]` |
| `borderWidthTablet` | array | `["", "", "", ""]` |
| `borderWidthUnit` | string | `"px"` |
| `boxShadow` | array | `[{"color": "#000000", "opacity": 0.2, "spread": 0, "blur": 14, "hOffset": 0, "vOffset": 0, "inset": false}]` |
| `caption` | string |  |
| `captionStyles` | array | `[{"size": ["", "", ""], "sizeType": "px", "lineHeight": ["", "", ""], "lineType": "px", "letterSpacing": ["", "", ""], "textTransform": "", "family": "", "google": false, "style": "", "weight": "", "variant": "", "subset": "", "loadGoogle": true, "color": "", "background": ""}]` |
| `displayBoxShadow` | boolean | `false` |
| `displayDropShadow` | boolean | `false` |
| `dropShadow` | array | `[{"color": "#000000", "opacity": 0.2, "blur": 14, "hOffset": 0, "vOffset": 0}]` |
| `globalAlt` | boolean | `false` |
| `height` | number |  |
| `heightSticky` | number |  |
| `heightTransparent` | number |  |
| `id` | number |  |
| `idSticky` | number |  |
| `idTransparent` | number |  |
| `imageFilter` | string | `"none"` |
| `imagePosition` | string | `""` |
| `imgMaxWidth` | number |  |
| `imgMaxWidthMobile` | number |  |
| `imgMaxWidthTablet` | number |  |
| `inQueryBlock` | boolean | `false` |
| `link` | string |  |
| `linkClass` | string |  |
| `linkDestination` | string |  |
| `linkNoFollow` | boolean | `false` |
| `linkSponsored` | boolean | `false` |
| `linkTarget` | boolean | `false` |
| `linkTitle` | string |  |
| `marginDesktop` | array | `["", "", "", ""]` |
| `marginMobile` | array | `["", "", "", ""]` |
| `marginTablet` | array | `["", "", "", ""]` |
| `marginUnit` | string | `"px"` |
| `maskPosition` | string | `"center center"` |
| `maskRepeat` | string | `"no-repeat"` |
| `maskSize` | string | `"auto"` |
| `maskSvg` | string | `"none"` |
| `maskUrl` | string |  |
| `mobileBorderRadius` | array | `["", "", "", ""]` |
| `mobileBorderStyle` | array | `[{"top": ["", "", ""], "right": ["", "", ""], "bottom": ["", "", ""], "left": ["", "", ""], "unit": "px"}]` |
| `overlay` | string | `""` |
| `overlayBlendMode` | string |  |
| `overlayGradient` | string | `""` |
| `overlayOpacity` | number | `0.3` |
| `overlayType` | string | `"normal"` |
| `paddingDesktop` | array | `["", "", "", ""]` |
| `paddingMobile` | array | `["", "", "", ""]` |
| `paddingTablet` | array | `["", "", "", ""]` |
| `paddingUnit` | string | `"px"` |
| `preventLazyLoad` | boolean | `false` |
| `ratio` | string |  |
| `showCaption` | boolean | `true` |
| `sizeSlug` | string |  |
| `sizeSlugSticky` | string |  |
| `sizeSlugTransparent` | string |  |
| `tabletBorderRadius` | array | `["", "", "", ""]` |
| `tabletBorderStyle` | array | `[{"top": ["", "", ""], "right": ["", "", ""], "bottom": ["", "", ""], "left": ["", "", ""], "unit": "px"}]` |
| `title` | string |  |
| `titleSticky` | string |  |
| `titleTransparent` | string |  |
| `tooltip` | string |  |
| `tooltipDash` | boolean | `false` |
| `tooltipPlacement` | string | `""` |
| `uniqueID` | string |  |
| `url` | string |  |
| `urlSticky` | string |  |
| `urlTransparent` | string |  |
| `useRatio` | boolean | `false` |
| `width` | number |  |
| `widthSticky` | number |  |
| `widthTransparent` | number |  |
| `zIndex` | number |  |

## kadence/infobox

**Info Box** · category `kadence-blocks` · apiVersion 3

- Supports: `{"ktdynamic": true, "kbMetadata": true}`

| Attribute | Type | Default |
|---|---|---|
| `borderHoverRadius` | array | `["", "", "", ""]` |
| `borderHoverRadiusUnit` | string | `"px"` |
| `borderHoverStyle` | array | `[{"top": ["", "", ""], "right": ["", "", ""], "bottom": ["", "", ""], "left": ["", "", ""], "unit": "px"}]` |
| `borderRadius` | array | `["", "", "", ""]` |
| `borderRadiusUnit` | string | `"px"` |
| `borderStyle` | array | `[{"top": ["", "", ""], "right": ["", "", ""], "bottom": ["", "", ""], "left": ["", "", ""], "unit": "px"}]` |
| `containerBackground` | string | `""` |
| `containerBackgroundOpacity` | number | `""` |
| `containerBorder` | string | `""` |
| `containerBorderOpacity` | number | `1` |
| `containerBorderRadius` | number | `""` |
| `containerBorderWidth` | array | `["", "", "", ""]` |
| `containerHoverBackground` | string | `""` |
| `containerHoverBackgroundOpacity` | number | `""` |
| `containerHoverBorder` | string | `""` |
| `containerHoverBorderOpacity` | number | `1` |
| `containerMargin` | array | `["", "", "", ""]` |
| `containerMarginUnit` | string | `"px"` |
| `containerMobilePadding` | array | `["", "", "", ""]` |
| `containerPadding` | array | `["xs", "xs", "xs", "xs"]` |
| `containerPaddingType` | string | `"px"` |
| `containerTabletPadding` | array | `["", "", "", ""]` |
| `contentText` | rich-text | `"Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean diam dolor, accumsan sed rutrum vel, dapibus et leo."` |
| `displayLearnMore` | boolean | `false` |
| `displayShadow` | boolean | `false` |
| `displayText` | boolean | `true` |
| `displayTitle` | boolean | `true` |
| `fullHeight` | boolean | `false` |
| `hAlign` | string | `"center"` |
| `hAlignMobile` | string | `""` |
| `hAlignTablet` | string | `""` |
| `imageRatio` | string | `"inherit"` |
| `inQueryBlock` | boolean | `false` |
| `kbVersion` | number | `""` |
| `learnMore` | rich-text | `"Learn More"` |
| `learnMoreStyles` | array | `[{"size": ["", "", ""], "sizeType": "px", "lineHeight": ["", "", ""], "lineType": "px", "letterSpacing": "", "family": "", "google": "", "style": "", "weight": "", "variant": "", "subset": "", "loadGoogle": true, "padding": [4, 8, 4, 8], "paddingControl": "individual", "margin": [10, 0, 10, 0], "marginControl": "individual", "color": "", "background": "transparent", "border": "", "borderRadius": 0, "borderWidth": [0, 0, 0, 0], "borderControl": "linked", "colorHover": "", "backgroundHover": "", "borderHover": "", "hoverEffect": "revealBorder", "paddingTablet": ["", "", "", ""], "paddingMobile": ["", "", "", ""], "paddingType": "px", "textTransform": ""}]` |
| `link` | string |  |
| `linkNoFollow` | boolean | `false` |
| `linkProperty` | string | `"box"` |
| `linkSponsored` | boolean | `false` |
| `linkTitle` | string | `""` |
| `maxWidth` | number | `""` |
| `maxWidthMobileUnit` | string | `""` |
| `maxWidthTabletUnit` | string | `""` |
| `maxWidthUnit` | string | `"px"` |
| `mediaAlign` | string | `"top"` |
| `mediaAlignMobile` | string | `""` |
| `mediaAlignTablet` | string | `""` |
| `mediaIcon` | array | `[{"icon": "fe_aperture", "size": 50, "unit": "px", "width": 2, "title": "", "color": "", "hoverColor": "", "hoverAnimation": "none", "flipIcon": "", "tabletSize": "", "mobileSize": ""}]` |
| `mediaImage` | array | `[{"url": "", "id": "", "alt": "", "width": "", "height": "", "maxWidth": "", "hoverAnimation": "none", "flipUrl": "", "flipId": "", "flipAlt": "", "flipWidth": "", "flipHeight": "", "subtype": "", "flipSubtype": ""}]` |
| `mediaNumber` | array | `[{"family": "", "google": false, "hoverAnimation": "none", "style": "", "weight": "", "variant": "", "subset": "", "loadGoogle": true}]` |
| `mediaStyle` | array | `[{"background": "", "hoverBackground": "", "border": "", "hoverBorder": "", "borderRadius": 0, "borderRadiusUnit": "px", "borderWidth": [0, 0, 0, 0], "borderWidthUnit": "px", "padding": [10, 10, 10, 10], "paddingUnit": "px", "margin": [0, 15, 0, 15], "marginUnit": "px"}]` |
| `mediaType` | string | `"icon"` |
| `mediaVAlign` | string | `"middle"` |
| `mobileBorderHoverRadius` | array | `["", "", "", ""]` |
| `mobileBorderHoverStyle` | array | `[{"top": ["", "", ""], "right": ["", "", ""], "bottom": ["", "", ""], "left": ["", "", ""], "unit": "px"}]` |
| `mobileBorderRadius` | array | `["", "", "", ""]` |
| `mobileBorderStyle` | array | `[{"top": ["", "", ""], "right": ["", "", ""], "bottom": ["", "", ""], "left": ["", "", ""], "unit": "px"}]` |
| `mobileContainerMargin` | array | `["", "", "", ""]` |
| `mobileMaxWidth` | number | `""` |
| `mobileShadow` | array | `[{"color": "", "opacity": "", "spread": "", "blur": "", "hOffset": "", "vOffset": "", "inset": ""}]` |
| `mobileShadowHover` | array | `[{"color": "", "opacity": "", "spread": "", "blur": "", "hOffset": "", "vOffset": "", "inset": ""}]` |
| `number` | rich-text | `""` |
| `shadow` | array | `[{"color": "#000000", "opacity": 0, "spread": 0, "blur": 0, "hOffset": 0, "vOffset": 0, "inset": false}]` |
| `shadowHover` | array | `[{"color": "#000000", "opacity": 0.2, "spread": 0, "blur": 14, "hOffset": 0, "vOffset": 0, "inset": false}]` |
| `showPresets` | boolean | `true` |
| `tabletBorderHoverRadius` | array | `["", "", "", ""]` |
| `tabletBorderHoverStyle` | array | `[{"top": ["", "", ""], "right": ["", "", ""], "bottom": ["", "", ""], "left": ["", "", ""], "unit": "px"}]` |
| `tabletBorderRadius` | array | `["", "", "", ""]` |
| `tabletBorderStyle` | array | `[{"top": ["", "", ""], "right": ["", "", ""], "bottom": ["", "", ""], "left": ["", "", ""], "unit": "px"}]` |
| `tabletContainerMargin` | array | `["", "", "", ""]` |
| `tabletMaxWidth` | number | `""` |
| `tabletShadow` | array | `[{"color": "", "opacity": "", "spread": "", "blur": "", "hOffset": "", "vOffset": "", "inset": ""}]` |
| `tabletShadowHover` | array | `[{"color": "", "opacity": "", "spread": "", "blur": "", "hOffset": "", "vOffset": "", "inset": ""}]` |
| `target` | string | `"_self"` |
| `textColor` | string | `""` |
| `textFont` | array | `[{"size": ["", "", ""], "sizeType": "px", "lineHeight": ["", "", ""], "lineType": "px", "letterSpacing": "", "family": "", "google": "", "style": "", "weight": "", "variant": "", "subset": "", "loadGoogle": true, "textTransform": ""}]` |
| `textHoverColor` | string | `""` |
| `textMinHeight` | array | `["", "", ""]` |
| `textMinHeightUnit` | string | `"px"` |
| `textSpacing` | array | `[{"padding": ["", "", "", ""], "paddingControl": "linked", "margin": ["", "", "", ""], "marginControl": "linked"}]` |
| `title` | rich-text | `"Title"` |
| `titleColor` | string | `""` |
| `titleFont` | array | `[{"level": 2, "size": ["", "", ""], "sizeType": "px", "lineHeight": ["", "", ""], "lineType": "px", "letterSpacing": "", "textTransform": "", "family": "", "google": false, "style": "", "weight": "", "variant": "", "subset": "", "loadGoogle": true, "padding": ["", "", "", ""], "paddingControl": "linked", "margin": ["", "", "", ""], "marginControl": "individual", "paddingUnit": "px", "marginUnit": "px"}]` |
| `titleHoverColor` | string | `""` |
| `titleMinHeight` | array | `["", "", ""]` |
| `titleMinHeightUnit` | string | `"px"` |
| `titleTagType` | string | `"heading"` |
| `uniqueID` | string | `""` |

## kadence/listitem

**List item** · category `kadence-blocks` · apiVersion 3

- Parent-only: must be a direct child of `kadence/iconlist`
- Supports: `{"ktdynamic": true, "html": false, "reusable": false, "kbMetadata": true, "kbContentLabel": "text"}`

| Attribute | Type | Default |
|---|---|---|
| `background` | string | `""` |
| `border` | string | `""` |
| `borderRadius` | number | `""` |
| `borderWidth` | number | `""` |
| `color` | string | `""` |
| `enableMarkBackgroundGradient` | boolean | `false` |
| `enableMarkGradient` | boolean | `false` |
| `icon` | string | `""` |
| `iconTitle` | string | `""` |
| `level` | number | `0` |
| `link` | string | `""` |
| `linkNoFollow` | boolean | `false` |
| `linkSponsored` | boolean | `false` |
| `markBG` | string |  |
| `markBGOpacity` | number | `1` |
| `markBackgroundGradient` | string | `""` |
| `markBorder` | string |  |
| `markBorderOpacity` | number | `1` |
| `markBorderRadius` | array | `["", "", "", ""]` |
| `markBorderRadiusUnit` | string | `"px"` |
| `markBorderStyle` | string | `"solid"` |
| `markBorderStyles` | array | `[{"top": ["", "", ""], "right": ["", "", ""], "bottom": ["", "", ""], "left": ["", "", ""], "unit": "px"}]` |
| `markBorderWidth` | number | `0` |
| `markColor` | string | `"#f76a0c"` |
| `markFontStyle` | string | `"normal"` |
| `markFontSubset` | string | `""` |
| `markFontVariant` | string | `""` |
| `markFontWeight` | string | `""` |
| `markGoogleFont` | boolean | `false` |
| `markGradient` | string | `""` |
| `markLetterSpacing` | number |  |
| `markLetterSpacingType` | string | `"px"` |
| `markLineHeight` | array | `["", "", ""]` |
| `markLineType` | string | `"px"` |
| `markLoadGoogleFont` | boolean | `true` |
| `markMobilePadding` | array | `["", "", "", ""]` |
| `markPadding` | array | `[0, 0, 0, 0]` |
| `markPaddingControl` | string | `"linked"` |
| `markPaddingType` | string | `"px"` |
| `markSize` | array | `["", "", ""]` |
| `markSizeType` | string | `"px"` |
| `markTabPadding` | array | `["", "", "", ""]` |
| `markTextTransform` | string | `""` |
| `markTypography` | string | `""` |
| `mobileMarkBorderRadius` | array | `["", "", "", ""]` |
| `mobileMarkBorderStyles` | array | `[{"top": ["", "", ""], "right": ["", "", ""], "bottom": ["", "", ""], "left": ["", "", ""], "unit": "px"}]` |
| `mobileMarkLetterSpacing` | number |  |
| `padding` | number | `""` |
| `showIcon` | boolean | `true` |
| `size` | number | `""` |
| `style` | string | `""` |
| `tabletMarkBorderRadius` | array | `["", "", "", ""]` |
| `tabletMarkBorderStyles` | array | `[{"top": ["", "", ""], "right": ["", "", ""], "bottom": ["", "", ""], "left": ["", "", ""], "unit": "px"}]` |
| `tabletMarkLetterSpacing` | number |  |
| `target` | string | `"_self"` |
| `text` | string |  |
| `tooltip` | string |  |
| `tooltipDash` | boolean | `true` |
| `tooltipPlacement` | string | `""` |
| `tooltipSelection` | string | `"both"` |
| `uniqueID` | string | `""` |
| `width` | number | `""` |

## kadence/lottie

**Lottie Animations** · category `kadence-blocks` · apiVersion 3

- Supports: `{"kbMetadata": true}`

| Attribute | Type | Default |
|---|---|---|
| `align` | string |  |
| `autoplay` | boolean | `true` |
| `bouncePlayback` | boolean | `false` |
| `delay` | number | `0` |
| `endFrame` | number | `"100"` |
| `fileSrc` | string | `"url"` |
| `fileUrl` | string | `"https://assets10.lottiefiles.com/packages/lf20_rqcjx8hr.json"` |
| `id` | number |  |
| `label` | string | `""` |
| `localFile` | array | `[]` |
| `loop` | boolean | `true` |
| `loopLimit` | number | `0` |
| `marginDesktop` | array | `["", "", "", ""]` |
| `marginMobile` | array | `["", "", "", ""]` |
| `marginTablet` | array | `["", "", "", ""]` |
| `marginUnit` | string | `"px"` |
| `onlyPlayOnHover` | boolean | `false` |
| `onlyPlayOnScroll` | boolean | `false` |
| `paddingDesktop` | array | `["", "", "", ""]` |
| `paddingMobile` | array | `["", "", "", ""]` |
| `paddingTablet` | array | `["", "", "", ""]` |
| `paddingUnit` | string | `"px"` |
| `playbackSpeed` | number | `1` |
| `ratio` | number | `100` |
| `showControls` | boolean | `false` |
| `startFrame` | number | `"0"` |
| `uniqueID` | string |  |
| `useRatio` | boolean | `false` |
| `waitUntilInView` | boolean | `false` |
| `width` | number | `"0"` |

## kadence/navigation

**Navigation (Adv)** · category `kadence-blocks` · apiVersion 3

- Supports: `{"align": ["wide", "full"], "reusable": false, "ariaLabel": true, "html": false, "customClassName": false}`

| Attribute | Type | Default |
|---|---|---|
| `id` | integer | `0` |
| `makePost` | boolean | `false` |
| `templateKey` | string | `""` |
| `uniqueID` | string |  |

## kadence/navigation-link

**Kadence Navigation Link** · category `kadence-blocks` · apiVersion 3

- Allowed children: `kadence/navigation-link`, `core/navigation-link`, `kadence/rowlayout`, `core/page-list`
- Supports: `{"html": false, "className": true, "reusable": false, "anchor": true, "kbMetadata": true, "kbContentLabel": "label", "renaming": false, "ktdynamic": true, "interactivity": {"clientNavigation": true}}`

| Attribute | Type | Default |
|---|---|---|
| `align` | string | `""` |
| `alignMobile` | string | `""` |
| `alignTablet` | string | `""` |
| `anchor` | string |  |
| `background` | string | `""` |
| `backgroundActive` | string | `""` |
| `backgroundActiveMobile` | string | `""` |
| `backgroundActiveTablet` | string | `""` |
| `backgroundDropdown` | string | `""` |
| `backgroundDropdownActive` | string | `""` |
| `backgroundDropdownActiveMobile` | string | `""` |
| `backgroundDropdownActiveTablet` | string | `""` |
| `backgroundDropdownHover` | string | `""` |
| `backgroundDropdownHoverMobile` | string | `""` |
| `backgroundDropdownHoverTablet` | string | `""` |
| `backgroundDropdownMobile` | string | `""` |
| `backgroundDropdownTablet` | string | `""` |
| `backgroundGradient` | string | `""` |
| `backgroundGradientActive` | string | `""` |
| `backgroundGradientHover` | string | `""` |
| `backgroundHover` | string | `""` |
| `backgroundHoverMobile` | string | `""` |
| `backgroundHoverTablet` | string | `""` |
| `backgroundMobile` | string | `""` |
| `backgroundSticky` | string | `""` |
| `backgroundStickyActive` | string | `""` |
| `backgroundStickyActiveMobile` | string | `""` |
| `backgroundStickyActiveTablet` | string | `""` |
| `backgroundStickyHover` | string | `""` |
| `backgroundStickyHoverMobile` | string | `""` |
| `backgroundStickyHoverTablet` | string | `""` |
| `backgroundStickyMobile` | string | `""` |
| `backgroundStickyTablet` | string | `""` |
| `backgroundTablet` | string | `""` |
| `backgroundTransparent` | string | `""` |
| `backgroundTransparentActive` | string | `""` |
| `backgroundTransparentActiveMobile` | string | `""` |
| `backgroundTransparentActiveTablet` | string | `""` |
| `backgroundTransparentHover` | string | `""` |
| `backgroundTransparentHoverMobile` | string | `""` |
| `backgroundTransparentHoverTablet` | string | `""` |
| `backgroundTransparentMobile` | string | `""` |
| `backgroundTransparentTablet` | string | `""` |
| `backgroundType` | string | `"normal"` |
| `backgroundTypeActive` | string | `"normal"` |
| `backgroundTypeHover` | string | `"normal"` |
| `border` | array | `[{"top": ["", "", ""], "right": ["", "", ""], "bottom": ["", "", ""], "left": ["", "", ""], "unit": "px"}]` |
| `borderActive` | array | `[{"top": ["", "", ""], "right": ["", "", ""], "bottom": ["", "", ""], "left": ["", "", ""], "unit": "px"}]` |
| `borderActiveMobile` | array | `[{"top": ["", "", ""], "right": ["", "", ""], "bottom": ["", "", ""], "left": ["", "", ""], "unit": "px"}]` |
| `borderActiveTablet` | array | `[{"top": ["", "", ""], "right": ["", "", ""], "bottom": ["", "", ""], "left": ["", "", ""], "unit": "px"}]` |
| `borderHover` | array | `[{"top": ["", "", ""], "right": ["", "", ""], "bottom": ["", "", ""], "left": ["", "", ""], "unit": "px"}]` |
| `borderHoverMobile` | array | `[{"top": ["", "", ""], "right": ["", "", ""], "bottom": ["", "", ""], "left": ["", "", ""], "unit": "px"}]` |
| `borderHoverTablet` | array | `[{"top": ["", "", ""], "right": ["", "", ""], "bottom": ["", "", ""], "left": ["", "", ""], "unit": "px"}]` |
| `borderMobile` | array | `[{"top": ["", "", ""], "right": ["", "", ""], "bottom": ["", "", ""], "left": ["", "", ""], "unit": "px"}]` |
| `borderRadius` | array | `["", "", "", ""]` |
| `borderRadiusActive` | array | `["", "", "", ""]` |
| `borderRadiusActiveMobile` | array | `["", "", "", ""]` |
| `borderRadiusActiveTablet` | array | `["", "", "", ""]` |
| `borderRadiusHover` | array | `["", "", "", ""]` |
| `borderRadiusHoverMobile` | array | `["", "", "", ""]` |
| `borderRadiusHoverTablet` | array | `["", "", "", ""]` |
| `borderRadiusMobile` | array | `["", "", "", ""]` |
| `borderRadiusTablet` | array | `["", "", "", ""]` |
| `borderRadiusUnit` | string | `"px"` |
| `borderRadiusUnitActive` | string | `"px"` |
| `borderRadiusUnitHover` | string | `"px"` |
| `borderTablet` | array | `[{"top": ["", "", ""], "right": ["", "", ""], "bottom": ["", "", ""], "left": ["", "", ""], "unit": "px"}]` |
| `description` | string | `""` |
| `descriptionColor` | string | `""` |
| `descriptionColorActive` | string | `""` |
| `descriptionColorActiveMobile` | string | `""` |
| `descriptionColorActiveTablet` | string | `""` |
| `descriptionColorHover` | string | `""` |
| `descriptionColorHoverMobile` | string | `""` |
| `descriptionColorHoverTablet` | string | `""` |
| `descriptionColorMobile` | string | `""` |
| `descriptionColorTablet` | string | `""` |
| `descriptionPositioning` | string | `"normal"` |
| `descriptionPositioningMobile` | string | `""` |
| `descriptionPositioningTablet` | string | `""` |
| `descriptionSpacing` | number | `""` |
| `descriptionSpacingMobile` | number | `""` |
| `descriptionSpacingTablet` | number | `""` |
| `descriptionSpacingUnit` | string | `"px"` |
| `descriptionTypography` | array | `[{"size": ["", "", ""], "sizeType": "px", "lineHeight": ["", "", ""], "lineType": "", "letterSpacing": ["", "", ""], "letterType": "px", "textTransform": "", "family": "", "google": "", "style": "", "weight": "", "variant": "", "subset": "", "loadGoogle": true}]` |
| `disableLink` | boolean | `false` |
| `dropdownBorder` | array | `[{"top": ["", "", ""], "right": ["", "", ""], "bottom": ["", "", ""], "left": ["", "", ""], "unit": "px"}]` |
| `dropdownBorderMobile` | array | `[{"top": ["", "", ""], "right": ["", "", ""], "bottom": ["", "", ""], "left": ["", "", ""], "unit": "px"}]` |
| `dropdownBorderRadius` | array | `["", "", "", ""]` |
| `dropdownBorderRadiusMobile` | array | `["", "", "", ""]` |
| `dropdownBorderRadiusTablet` | array | `["", "", "", ""]` |
| `dropdownBorderRadiusUnit` | string | `"px"` |
| `dropdownBorderTablet` | array | `[{"top": ["", "", ""], "right": ["", "", ""], "bottom": ["", "", ""], "left": ["", "", ""], "unit": "px"}]` |
| `dropdownClick` | boolean | `false` |
| `dropdownDescriptionColor` | string | `""` |
| `dropdownDescriptionColorActive` | string | `""` |
| `dropdownDescriptionColorActiveMobile` | string | `""` |
| `dropdownDescriptionColorActiveTablet` | string | `""` |
| `dropdownDescriptionColorHover` | string | `""` |
| `dropdownDescriptionColorHoverMobile` | string | `""` |
| `dropdownDescriptionColorHoverTablet` | string | `""` |
| `dropdownDescriptionColorMobile` | string | `""` |
| `dropdownDescriptionColorTablet` | string | `""` |
| `dropdownDescriptionPositioning` | string | `"normal"` |
| `dropdownDescriptionPositioningMobile` | string | `""` |
| `dropdownDescriptionPositioningTablet` | string | `""` |
| `dropdownDescriptionSpacing` | number | `""` |
| `dropdownDescriptionSpacingMobile` | number | `""` |
| `dropdownDescriptionSpacingTablet` | number | `""` |
| `dropdownDescriptionSpacingUnit` | string | `"px"` |
| `dropdownDescriptionTypography` | array | `[{"size": ["", "", ""], "sizeType": "px", "lineHeight": ["", "", ""], "lineType": "", "letterSpacing": ["", "", ""], "letterType": "px", "textTransform": "", "family": "", "google": "", "style": "", "weight": "", "variant": "", "subset": "", "loadGoogle": true}]` |
| `dropdownDivider` | array | `[{"top": ["", "", ""], "right": ["", "", ""], "bottom": ["", "", ""], "left": ["", "", ""], "unit": "px"}]` |
| `dropdownDividerMobile` | array | `[{"top": ["", "", ""], "right": ["", "", ""], "bottom": ["", "", ""], "left": ["", "", ""], "unit": "px"}]` |
| `dropdownDividerTablet` | array | `[{"top": ["", "", ""], "right": ["", "", ""], "bottom": ["", "", ""], "left": ["", "", ""], "unit": "px"}]` |
| `dropdownHorizontalAlignment` | string | `""` |
| `dropdownHorizontalAlignmentMobile` | string | `""` |
| `dropdownHorizontalAlignmentTablet` | string | `""` |
| `dropdownShadow` | array | `[{"enable": false, "color": "#000000", "opacity": 0.1, "spread": 0, "blur": 13, "hOffset": 0, "vOffset": 2, "inset": false}]` |
| `dropdownTypography` | array | `[{"size": ["", "", ""], "sizeType": "px", "lineHeight": ["", "", ""], "lineType": "", "letterSpacing": ["", "", ""], "letterType": "px", "textTransform": "", "family": "", "google": "", "style": "", "weight": "", "variant": "", "subset": "", "loadGoogle": true}]` |
| `dropdownVerticalSpacing` | number | `""` |
| `dropdownVerticalSpacingMobile` | number | `""` |
| `dropdownVerticalSpacingTablet` | number | `""` |
| `dropdownVerticalSpacingUnit` | string | `"em"` |
| `dropdownWidth` | number | `""` |
| `dropdownWidthMobile` | number | `""` |
| `dropdownWidthTablet` | number | `""` |
| `dropdownWidthUnit` | string | `"px"` |
| `forceOpenInEditor` | boolean | `false` |
| `hideLabel` | boolean | `false` |
| `highlightIcon` | array | `[{"icon": "", "size": "", "sizeTablet": "", "sizeMobile": "", "width": 2, "title": ""}]` |
| `highlightLabel` | string | `""` |
| `highlightPosition` | string | `""` |
| `highlightSide` | string | `"right"` |
| `highlightSideMobile` | string | `""` |
| `highlightSideTablet` | string | `""` |
| `highlightSpacing` | array | `[{"border": "", "tabletBorder": "", "mobileBorder": "", "borderRadius": ["", "", "", ""], "tabletBorderRadius": ["", "", "", ""], "mobileBorderRadius": ["", "", "", ""], "borderWidth": ["", "", "", ""], "gap": ["", "", ""], "textGap": ["", "", ""], "padding": ["", "", "", ""], "tabletPadding": ["", "", "", ""], "mobilePadding": ["", "", "", ""], "margin": ["", "", "", ""], "tabletMargin": ["", "", "", ""], "mobileMargin": ["", "", "", ""]}]` |
| `highlightTypography` | array | `[{"size": ["", "", ""], "sizeType": "px", "lineHeight": ["", "", ""], "lineType": "", "letterSpacing": ["", "", ""], "letterType": "px", "textTransform": "", "family": "", "google": "", "style": "", "weight": "", "variant": "", "subset": "", "loadGoogle": true}]` |
| `iconSide` | string | `"right"` |
| `iconSideMobile` | string | `""` |
| `iconSideTablet` | string | `""` |
| `id` | number |  |
| `imageOverlayBackground` | string | `""` |
| `imageOverlayBackgroundActive` | string | `""` |
| `imageOverlayBackgroundActiveMobile` | string | `""` |
| `imageOverlayBackgroundActiveTablet` | string | `""` |
| `imageOverlayBackgroundHover` | string | `""` |
| `imageOverlayBackgroundHoverMobile` | string | `""` |
| `imageOverlayBackgroundHoverTablet` | string | `""` |
| `imageOverlayBackgroundMobile` | string | `""` |
| `imageOverlayBackgroundTablet` | string | `""` |
| `imageRatio` | string | `"inherit"` |
| `isMegaMenu` | boolean | `false` |
| `isTopLevelLink` | boolean | `false` |
| `kadenceConditional` | object |  |
| `kind` | string | `""` |
| `label` | string | `""` |
| `labelBackground` | string | `""` |
| `labelBackgroundActive` | string | `""` |
| `labelBackgroundActiveMobile` | string | `""` |
| `labelBackgroundActiveTablet` | string | `""` |
| `labelBackgroundHover` | string | `""` |
| `labelBackgroundHoverMobile` | string | `""` |
| `labelBackgroundHoverTablet` | string | `""` |
| `labelBackgroundMobile` | string | `""` |
| `labelBackgroundTablet` | string | `""` |
| `labelColor` | string | `""` |
| `labelColorActive` | string | `""` |
| `labelColorActiveMobile` | string | `""` |
| `labelColorActiveTablet` | string | `""` |
| `labelColorHover` | string | `""` |
| `labelColorHoverMobile` | string | `""` |
| `labelColorHoverTablet` | string | `""` |
| `labelColorMobile` | string | `""` |
| `labelColorTablet` | string | `""` |
| `linkColor` | string | `""` |
| `linkColorActive` | string | `""` |
| `linkColorActiveMobile` | string | `""` |
| `linkColorActiveTablet` | string | `""` |
| `linkColorDropdown` | string | `""` |
| `linkColorDropdownActive` | string | `""` |
| `linkColorDropdownActiveMobile` | string | `""` |
| `linkColorDropdownActiveTablet` | string | `""` |
| `linkColorDropdownHover` | string | `""` |
| `linkColorDropdownHoverMobile` | string | `""` |
| `linkColorDropdownHoverTablet` | string | `""` |
| `linkColorDropdownMobile` | string | `""` |
| `linkColorDropdownTablet` | string | `""` |
| `linkColorHover` | string | `""` |
| `linkColorHoverMobile` | string | `""` |
| `linkColorHoverTablet` | string | `""` |
| `linkColorMobile` | string | `""` |
| `linkColorSticky` | string | `""` |
| `linkColorStickyActive` | string | `""` |
| `linkColorStickyActiveMobile` | string | `""` |
| `linkColorStickyActiveTablet` | string | `""` |
| `linkColorStickyHover` | string | `""` |
| `linkColorStickyHoverMobile` | string | `""` |
| `linkColorStickyHoverTablet` | string | `""` |
| `linkColorStickyMobile` | string | `""` |
| `linkColorStickyTablet` | string | `""` |
| `linkColorTablet` | string | `""` |
| `linkColorTransparent` | string | `""` |
| `linkColorTransparentActive` | string | `""` |
| `linkColorTransparentActiveMobile` | string | `""` |
| `linkColorTransparentActiveTablet` | string | `""` |
| `linkColorTransparentHover` | string | `""` |
| `linkColorTransparentHoverMobile` | string | `""` |
| `linkColorTransparentHoverTablet` | string | `""` |
| `linkColorTransparentMobile` | string | `""` |
| `linkColorTransparentTablet` | string | `""` |
| `margin` | array | `["", "", "", ""]` |
| `marginDropdown` | array | `["", "", "", ""]` |
| `marginDropdownLink` | array | `["", "", "", ""]` |
| `marginDropdownLinkUnit` | string | `"px"` |
| `marginDropdownUnit` | string | `"px"` |
| `marginUnit` | string | `"px"` |
| `mediaAlign` | string | `"left"` |
| `mediaAlignMobile` | string | `""` |
| `mediaAlignTablet` | string | `""` |
| `mediaBackground` | string | `""` |
| `mediaBackgroundActive` | string | `""` |
| `mediaBackgroundActiveMobile` | string | `""` |
| `mediaBackgroundActiveTablet` | string | `""` |
| `mediaBackgroundGradient` | string | `""` |
| `mediaBackgroundGradientActive` | string | `""` |
| `mediaBackgroundGradientHover` | string | `""` |
| `mediaBackgroundHover` | string | `""` |
| `mediaBackgroundHoverMobile` | string | `""` |
| `mediaBackgroundHoverTablet` | string | `""` |
| `mediaBackgroundMobile` | string | `""` |
| `mediaBackgroundTablet` | string | `""` |
| `mediaBackgroundType` | string | `"normal"` |
| `mediaBackgroundTypeActive` | string | `"normal"` |
| `mediaBackgroundTypeHover` | string | `"normal"` |
| `mediaBorder` | array | `[{"top": ["", "", ""], "right": ["", "", ""], "bottom": ["", "", ""], "left": ["", "", ""], "unit": "px"}]` |
| `mediaBorderActive` | array | `[{"top": ["", "", ""], "right": ["", "", ""], "bottom": ["", "", ""], "left": ["", "", ""], "unit": "px"}]` |
| `mediaBorderActiveMobile` | array | `[{"top": ["", "", ""], "right": ["", "", ""], "bottom": ["", "", ""], "left": ["", "", ""], "unit": "px"}]` |
| `mediaBorderActiveTablet` | array | `[{"top": ["", "", ""], "right": ["", "", ""], "bottom": ["", "", ""], "left": ["", "", ""], "unit": "px"}]` |
| `mediaBorderHover` | array | `[{"top": ["", "", ""], "right": ["", "", ""], "bottom": ["", "", ""], "left": ["", "", ""], "unit": "px"}]` |
| `mediaBorderHoverMobile` | array | `[{"top": ["", "", ""], "right": ["", "", ""], "bottom": ["", "", ""], "left": ["", "", ""], "unit": "px"}]` |
| `mediaBorderHoverTablet` | array | `[{"top": ["", "", ""], "right": ["", "", ""], "bottom": ["", "", ""], "left": ["", "", ""], "unit": "px"}]` |
| `mediaBorderMobile` | array | `[{"top": ["", "", ""], "right": ["", "", ""], "bottom": ["", "", ""], "left": ["", "", ""], "unit": "px"}]` |
| `mediaBorderRadius` | array | `["", "", "", ""]` |
| `mediaBorderRadiusActive` | array | `["", "", "", ""]` |
| `mediaBorderRadiusActiveMobile` | array | `["", "", "", ""]` |
| `mediaBorderRadiusActiveTablet` | array | `["", "", "", ""]` |
| `mediaBorderRadiusHover` | array | `["", "", "", ""]` |
| `mediaBorderRadiusHoverMobile` | array | `["", "", "", ""]` |
| `mediaBorderRadiusHoverTablet` | array | `["", "", "", ""]` |
| `mediaBorderRadiusMobile` | array | `["", "", "", ""]` |
| `mediaBorderRadiusTablet` | array | `["", "", "", ""]` |
| `mediaBorderRadiusUnit` | string | `"px"` |
| `mediaBorderRadiusUnitActive` | string | `"px"` |
| `mediaBorderRadiusUnitHover` | string | `"px"` |
| `mediaBorderTablet` | array | `[{"top": ["", "", ""], "right": ["", "", ""], "bottom": ["", "", ""], "left": ["", "", ""], "unit": "px"}]` |
| `mediaColor` | string | `""` |
| `mediaColorActive` | string | `""` |
| `mediaColorActiveMobile` | string | `""` |
| `mediaColorActiveTablet` | string | `""` |
| `mediaColorHover` | string | `""` |
| `mediaColorHoverMobile` | string | `""` |
| `mediaColorHoverTablet` | string | `""` |
| `mediaColorMobile` | string | `""` |
| `mediaColorTablet` | string | `""` |
| `mediaIcon` | array | `[{"icon": "fe_aperture", "size": "", "sizeTablet": "", "sizeMobile": "", "width": 2, "title": ""}]` |
| `mediaImage` | array | `[{"url": "", "id": "", "alt": "", "width": "", "height": "", "maxWidth": ""}]` |
| `mediaStyle` | array | `[{"color": "", "colorTablet": "", "colorMobile": "", "colorHover": "", "colorHoverTablet": "", "colorHoverMobile": "", "colorActive": "", "colorActiveTablet": "", "colorActiveMobile": "", "background": "", "backgroundTablet": "", "backgroundMobile": "", "backgroundHover": "", "backgroundHoverTablet": "", "backgroundHoverMobile": "", "backgroundActive": "", "backgroundActiveTablet": "", "backgroundActiveMobile": "", "border": "", "hoverBorder": "", "borderRadius": "", "borderRadiusTablet": "", "borderRadiusMobile": "", "borderWidth": ["", "", "", ""], "padding": ["", "", "", ""], "paddingTablet": ["", "", "", ""], "paddingMobile": ["", "", "", ""], "paddingType": "px", "margin": ["", "", "", ""], "marginTablet": ["", "", "", ""], "marginMobile": ["", "", "", ""], "marginType": "px"}]` |
| `mediaType` | string | `""` |
| `megaMenuCustomWidth` | number | `400` |
| `megaMenuCustomWidthMobile` | number | `0` |
| `megaMenuCustomWidthTablet` | number | `0` |
| `megaMenuCustomWidthUnit` | string | `"px"` |
| `megaMenuWidth` | string | `""` |
| `megaMenuWidthMobile` | string | `""` |
| `megaMenuWidthTablet` | string | `""` |
| `mobileMargin` | array | `["", "", "", ""]` |
| `mobileMarginDropdown` | array | `["", "", "", ""]` |
| `mobileMarginDropdownLink` | array | `["", "", "", ""]` |
| `mobilePadding` | array | `["", "", "", ""]` |
| `mobilePaddingDropdown` | array | `["", "", "", ""]` |
| `mobilePaddingDropdownLink` | array | `["", "", "", ""]` |
| `opensInNewTab` | boolean | `false` |
| `padding` | array | `["", "", "", ""]` |
| `paddingDropdown` | array | `["", "", "", ""]` |
| `paddingDropdownLink` | array | `["", "", "", ""]` |
| `paddingDropdownLinkUnit` | string | `"px"` |
| `paddingDropdownUnit` | string | `"px"` |
| `paddingUnit` | string | `"px"` |
| `rel` | string | `""` |
| `shadow` | array | `[{"enable": false, "color": "#000000", "opacity": 0.2, "spread": 0, "blur": 2, "hOffset": 1, "vOffset": 1, "inset": false}]` |
| `shadowActive` | array | `[{"enable": false, "color": "#000000", "opacity": 0.2, "spread": 0, "blur": 2, "hOffset": 1, "vOffset": 1, "inset": false}]` |
| `shadowHover` | array | `[{"enable": false, "color": "#000000", "opacity": 0.2, "spread": 0, "blur": 2, "hOffset": 1, "vOffset": 1, "inset": false}]` |
| `tabletMargin` | array | `["", "", "", ""]` |
| `tabletMarginDropdown` | array | `["", "", "", ""]` |
| `tabletMarginDropdownLink` | array | `["", "", "", ""]` |
| `tabletPadding` | array | `["", "", "", ""]` |
| `tabletPaddingDropdown` | array | `["", "", "", ""]` |
| `tabletPaddingDropdownLink` | array | `["", "", "", ""]` |
| `target` | string | `""` |
| `title` | string | `""` |
| `type` | string | `""` |
| `typography` | array | `[{"size": ["", "", ""], "sizeType": "px", "lineHeight": ["", "", ""], "lineType": "", "letterSpacing": ["", "", ""], "letterType": "px", "textTransform": "", "family": "", "google": "", "style": "", "weight": "", "variant": "", "subset": "", "loadGoogle": true}]` |
| `uniqueID` | string |  |
| `url` | string | `""` |

## kadence/off-canvas

**** · category `design` · apiVersion 3

- Parent-only: must be a direct child of `kadence/header`
- Supports: `{"inserter": true, "className": true}`

| Attribute | Type | Default |
|---|---|---|
| `backgroundColor` | string | `""` |
| `backgroundColorMobile` | string | `""` |
| `backgroundColorTablet` | string | `""` |
| `border` | array | `[{"top": ["", "", ""], "right": ["", "", ""], "bottom": ["", "", ""], "left": ["", "", ""], "unit": "px"}]` |
| `borderMobile` | array | `[{"top": ["", "", ""], "right": ["", "", ""], "bottom": ["", "", ""], "left": ["", "", ""], "unit": "px"}]` |
| `borderRadius` | array | `["", "", "", ""]` |
| `borderRadiusMobile` | array | `["", "", "", ""]` |
| `borderRadiusTablet` | array | `["", "", "", ""]` |
| `borderRadiusUnit` | string | `"px"` |
| `borderTablet` | array | `[{"top": ["", "", ""], "right": ["", "", ""], "bottom": ["", "", ""], "left": ["", "", ""], "unit": "px"}]` |
| `closeIcon` | string | `"fe_x"` |
| `closeIconBackgroundColor` | string | `""` |
| `closeIconBackgroundColorHover` | string | `""` |
| `closeIconBackgroundColorHoverMobile` | string | `""` |
| `closeIconBackgroundColorHoverTablet` | string | `""` |
| `closeIconBackgroundColorMobile` | string | `""` |
| `closeIconBackgroundColorTablet` | string | `""` |
| `closeIconBorder` | array | `[{"top": ["", "", ""], "right": ["", "", ""], "bottom": ["", "", ""], "left": ["", "", ""], "unit": "px"}]` |
| `closeIconBorderHover` | array | `[{"top": ["", "", ""], "right": ["", "", ""], "bottom": ["", "", ""], "left": ["", "", ""], "unit": "px"}]` |
| `closeIconBorderHoverMobile` | array | `[{"top": ["", "", ""], "right": ["", "", ""], "bottom": ["", "", ""], "left": ["", "", ""], "unit": "px"}]` |
| `closeIconBorderHoverTablet` | array | `[{"top": ["", "", ""], "right": ["", "", ""], "bottom": ["", "", ""], "left": ["", "", ""], "unit": "px"}]` |
| `closeIconBorderMobile` | array | `[{"top": ["", "", ""], "right": ["", "", ""], "bottom": ["", "", ""], "left": ["", "", ""], "unit": "px"}]` |
| `closeIconBorderRadius` | array | `["", "", "", ""]` |
| `closeIconBorderRadiusMobile` | array | `["", "", "", ""]` |
| `closeIconBorderRadiusTablet` | array | `["", "", "", ""]` |
| `closeIconBorderRadiusUnit` | string | `"px"` |
| `closeIconBorderTablet` | array | `[{"top": ["", "", ""], "right": ["", "", ""], "bottom": ["", "", ""], "left": ["", "", ""], "unit": "px"}]` |
| `closeIconColor` | string | `""` |
| `closeIconColorHover` | string | `""` |
| `closeIconColorHoverMobile` | string | `""` |
| `closeIconColorHoverTablet` | string | `""` |
| `closeIconColorMobile` | string | `""` |
| `closeIconColorTablet` | string | `""` |
| `closeIconMargin` | array | `["", "", "", ""]` |
| `closeIconMarginMobile` | array | `["", "", "", ""]` |
| `closeIconMarginTablet` | array | `["", "", "", ""]` |
| `closeIconMarginUnit` | string | `"px"` |
| `closeIconPadding` | array | `["", "", "", ""]` |
| `closeIconPaddingMobile` | array | `["", "", "", ""]` |
| `closeIconPaddingTablet` | array | `["", "", "", ""]` |
| `closeIconPaddingUnit` | string | `"px"` |
| `closeIconSize` | number | `25` |
| `closeIconSizeMobile` | number |  |
| `closeIconSizeTablet` | number |  |
| `closeLabel` | string | `""` |
| `closeLineWidth` | number | `2` |
| `containerMaxWidth` | number |  |
| `containerMaxWidthMobile` | number |  |
| `containerMaxWidthTablet` | number |  |
| `containerMaxWidthUnit` | string | `"px"` |
| `hAlign` | string | `"left"` |
| `hAlignMobile` | string | `""` |
| `hAlignTablet` | string | `""` |
| `maxWidth` | number | `400` |
| `maxWidthMobile` | number |  |
| `maxWidthTablet` | number |  |
| `maxWidthUnit` | string | `"px"` |
| `padding` | array | `["", "", "", ""]` |
| `paddingMobile` | array | `["", "", "", ""]` |
| `paddingTablet` | array | `["", "", "", ""]` |
| `paddingUnit` | string | `"px"` |
| `pageBackgroundColor` | string | `"rgba(0, 0, 0, 0.6)"` |
| `pageBackgroundColorMobile` | string | `""` |
| `pageBackgroundColorTablet` | string | `""` |
| `slideFrom` | string | `"left"` |
| `slideFromMobile` | string | `""` |
| `slideFromTablet` | string | `""` |
| `uniqueID` | string |  |
| `vAlign` | string | `""` |
| `vAlignMobile` | string | `""` |
| `vAlignTablet` | string | `""` |
| `widthType` | string | `"partial"` |
| `widthTypeMobile` | string | `""` |
| `widthTypeTablet` | string | `""` |

## kadence/off-canvas-trigger

**** · category `design` · apiVersion 3

- Supports: `{"className": true}`

| Attribute | Type | Default |
|---|---|---|
| `border` | array | `[{"top": ["", "", ""], "right": ["", "", ""], "bottom": ["", "", ""], "left": ["", "", ""], "unit": "px"}]` |
| `borderHover` | array | `[{"top": ["", "", ""], "right": ["", "", ""], "bottom": ["", "", ""], "left": ["", "", ""], "unit": "px"}]` |
| `borderHoverMobile` | array | `[{"top": ["", "", ""], "right": ["", "", ""], "bottom": ["", "", ""], "left": ["", "", ""], "unit": "px"}]` |
| `borderHoverTablet` | array | `[{"top": ["", "", ""], "right": ["", "", ""], "bottom": ["", "", ""], "left": ["", "", ""], "unit": "px"}]` |
| `borderMobile` | array | `[{"top": ["", "", ""], "right": ["", "", ""], "bottom": ["", "", ""], "left": ["", "", ""], "unit": "px"}]` |
| `borderRadius` | array | `["", "", "", ""]` |
| `borderRadiusMobile` | array | `["", "", "", ""]` |
| `borderRadiusTablet` | array | `["", "", "", ""]` |
| `borderRadiusUnit` | string | `"px"` |
| `borderTablet` | array | `[{"top": ["", "", ""], "right": ["", "", ""], "bottom": ["", "", ""], "left": ["", "", ""], "unit": "px"}]` |
| `icon` | string | `"fe_menu"` |
| `iconBackgroundColor` | string | `""` |
| `iconBackgroundColorHover` | string | `""` |
| `iconBackgroundColorHoverMobile` | string | `""` |
| `iconBackgroundColorHoverTablet` | string | `""` |
| `iconBackgroundColorMobile` | string | `""` |
| `iconBackgroundColorTablet` | string | `""` |
| `iconColor` | string | `""` |
| `iconColorHover` | string | `""` |
| `iconColorHoverMobile` | string | `""` |
| `iconColorHoverTablet` | string | `""` |
| `iconColorMobile` | string | `""` |
| `iconColorTablet` | string | `""` |
| `iconSize` | number | `25` |
| `iconSizeMobile` | number | `""` |
| `iconSizeTablet` | number | `""` |
| `label` | string | `""` |
| `lineWidth` | number | `2` |
| `margin` | array | `["", "", "", ""]` |
| `marginMobile` | array | `["", "", "", ""]` |
| `marginTablet` | array | `["", "", "", ""]` |
| `marginUnit` | string | `"px"` |
| `padding` | array | `["", "", "", ""]` |
| `paddingMobile` | array | `["", "", "", ""]` |
| `paddingTablet` | array | `["", "", "", ""]` |
| `paddingUnit` | string | `"px"` |
| `uniqueID` | string |  |

## kadence/posts

**Posts** · category `kadence-blocks` · apiVersion 3

- Supports: `{"html": false, "kbMetadata": true}`

| Attribute | Type | Default |
|---|---|---|
| `aboveCategories` | boolean | `true` |
| `alignImage` | string | `"beside"` |
| `allowSticky` | boolean | `false` |
| `author` | boolean | `true` |
| `authorEnabledLabel` | boolean | `true` |
| `authorImage` | boolean | `false` |
| `authorImageSize` | number | `25` |
| `authorLabel` | string | `""` |
| `authorLink` | boolean | `false` |
| `categories` | array | `[]` |
| `categoriesDivider` | string | `"vline"` |
| `categoriesStyle` | string | `"normal"` |
| `columns` | number | `3` |
| `comments` | boolean | `false` |
| `customKadenceArchiveColors` | boolean | `true` |
| `date` | boolean | `true` |
| `dateEnabledLabel` | boolean | `false` |
| `dateLabel` | string | `""` |
| `dateUpdated` | boolean | `false` |
| `dateUpdatedEnabledLabel` | boolean | `false` |
| `dateUpdatedLabel` | string | `""` |
| `excerpt` | boolean | `true` |
| `excerptCustomLength` | boolean | `false` |
| `excerptLength` | number | `40` |
| `excludeTax` | string | `"include"` |
| `image` | boolean | `true` |
| `imageRatio` | string | `"2-3"` |
| `imageSize` | string | `"medium_large"` |
| `loopStyle` | string | `"boxed"` |
| `meta` | boolean | `true` |
| `metaCategories` | boolean | `false` |
| `metaCategoriesEnabledLabel` | boolean | `false` |
| `metaCategoriesLabel` | string | `""` |
| `metaDivider` | string | `"dot"` |
| `mobileColumns` | number |  |
| `offsetQuery` | number | `0` |
| `order` | string | `"desc"` |
| `orderBy` | string | `"date"` |
| `postTax` | boolean | `false` |
| `postType` | string | `"post"` |
| `postsToShow` | number | `6` |
| `readmore` | boolean | `true` |
| `readmoreLabel` | string | `""` |
| `showUnique` | boolean | `false` |
| `tabletColumns` | number |  |
| `tags` | array | `[]` |
| `taxType` | string | `""` |
| `titleFont` | array | `[{"level": 2, "size": ["", "", ""], "sizeType": "px", "lineHeight": ["", "", ""], "lineType": "px", "letterSpacing": ["", "", ""], "letterType": "px", "textTransform": ""}]` |
| `uniqueID` | string |  |

## kadence/progress-bar

**Progress Bar** · category `kadence-blocks` · apiVersion 3


| Attribute | Type | Default |
|---|---|---|
| `align` | string |  |
| `ariaLabel` | string | `""` |
| `barBackground` | string | `""` |
| `barBackgroundOpacity` | number | `1` |
| `barType` | string | `"line"` |
| `containerMaxWidth` | number |  |
| `containerMaxWidthUnits` | string | `"px"` |
| `decimal` | string | `"none"` |
| `delayUntilInView` | boolean | `true` |
| `displayLabel` | boolean | `true` |
| `displayPercent` | boolean | `true` |
| `duration` | number | `2` |
| `easing` | string | `"easeInOut"` |
| `hAlign` | string | `"space-between"` |
| `id` | number |  |
| `label` | string | `""` |
| `labelFont` | object | `{"color": "", "level": 6, "size": ["", "", ""], "sizeType": "px", "lineHeight": ["", "", ""], "lineType": "", "letterSpacing": ["", "", ""], "textTransform": "", "family": "", "google": false, "style": "", "weight": "", "variant": "", "subset": "", "loadGoogle": true, "padding": [0, 0, 0, 0], "margin": [0, 0, 0, 0]}` |
| `labelLayout` | string | `"lp"` |
| `labelPadding` | array | `["", "", "", ""]` |
| `labelPaddingType` | string | `"px"` |
| `labelPosition` | string | `"above"` |
| `margin` | array | `["", "", "", ""]` |
| `marginType` | string | `"px"` |
| `maskIterations` | number | `5` |
| `maskSvg` | string | `"star"` |
| `maskUrl` | string |  |
| `mhAlign` | string | `""` |
| `mobileContainerMaxWidth` | number |  |
| `mobileLabelPadding` | array | `["", "", "", ""]` |
| `mobileMargin` | array | `["", "", "", ""]` |
| `numberFont` | object | `{"color": "", "level": 6, "size": ["", "", ""], "sizeType": "px", "lineHeight": ["", "", ""], "lineType": "", "letterSpacing": ["", "", ""], "textTransform": "", "family": "", "google": false, "style": "", "weight": "", "variant": "", "subset": "", "loadGoogle": true, "padding": [0, 0, 0, 0], "margin": [0, 0, 0, 0]}` |
| `numberIsRelative` | boolean | `false` |
| `numberPrefix` | string | `""` |
| `numberSuffix` | string | `"%"` |
| `progressAmount` | number | `90` |
| `progressBorderRadius` | array | `["", "", ""]` |
| `progressColor` | string | `""` |
| `progressMax` | number | `100` |
| `progressOpacity` | number | `1` |
| `progressWidth` | number | `2` |
| `progressWidthMobile` | number | `""` |
| `progressWidthTablet` | number | `""` |
| `showMaxProgressOnPageLoad` | boolean | `true` |
| `tabletContainerMaxWidth` | number |  |
| `tabletLabelPadding` | array | `["", "", "", ""]` |
| `tabletMargin` | array | `["", "", "", ""]` |
| `thAlign` | string | `""` |
| `uniqueID` | string |  |
| `width` | number | `""` |

## kadence/rowlayout

**Row Layout** · category `kadence-blocks` · apiVersion 3

- Supports: `{"anchor": true, "ktdynamic": true, "kbcss": true, "html": false, "kbMetadata": true}`

| Attribute | Type | Default |
|---|---|---|
| `align` | string | `"none"` |
| `anchor` | string |  |
| `backgroundInline` | boolean | `false` |
| `backgroundSettingTab` | string | `"normal"` |
| `backgroundSlider` | array | `[{"bgColor": "", "bgImg": "", "bgImgID": ""}]` |
| `backgroundSliderCount` | number | `1` |
| `backgroundSliderSettings` | array | `[{"arrowStyle": "none", "dotStyle": "dark", "autoPlay": true, "speed": 7000, "fade": true, "tranSpeed": 400, "showPauseButton": false}]` |
| `backgroundVideo` | array | `[{"youTube": "", "local": "", "localID": "", "vimeo": "", "ratio": "16/9", "btns": false, "loop": true, "mute": true}]` |
| `backgroundVideoType` | string | `"local"` |
| `bgColor` | string | `""` |
| `bgColorClass` | string | `""` |
| `bgImg` | string | `""` |
| `bgImgAttachment` | string | `"scroll"` |
| `bgImgID` | number | `""` |
| `bgImgPosition` | string | `"center center"` |
| `bgImgRepeat` | string | `"no-repeat"` |
| `bgImgSize` | string | `"cover"` |
| `blockAlignment` | string | `"none"` |
| `border` | string | `""` |
| `borderRadius` | array | `["", "", "", ""]` |
| `borderRadiusOverflow` | boolean | `true` |
| `borderRadiusUnit` | string | `"px"` |
| `borderStyle` | array | `[{"top": ["", "", ""], "right": ["", "", ""], "bottom": ["", "", ""], "left": ["", "", ""], "unit": "px"}]` |
| `borderWidth` | array | `["", "", "", ""]` |
| `bottomMargin` | number | `""` |
| `bottomMarginM` | number | `""` |
| `bottomMarginT` | number | `""` |
| `bottomPadding` | number | `""` |
| `bottomPaddingM` | number | `""` |
| `bottomSep` | string | `"none"` |
| `bottomSepColor` | string | `"#ffffff"` |
| `bottomSepFlip` | boolean | `false` |
| `bottomSepHeight` | number | `100` |
| `bottomSepHeightMobile` | number | `""` |
| `bottomSepHeightTab` | number | `""` |
| `bottomSepHeightUnit` | string | `"px"` |
| `bottomSepWidth` | number | `100` |
| `bottomSepWidthMobile` | number | `""` |
| `bottomSepWidthTab` | number | `""` |
| `boxShadow` | array | `[{"color": "#000000", "opacity": 0.2, "spread": 0, "blur": 14, "hOffset": 0, "vOffset": 0, "inset": false}]` |
| `breakoutLeft` | boolean | `false` |
| `breakoutRight` | boolean | `false` |
| `colLayout` | string | `""` |
| `collapseGutter` | string | `"default"` |
| `collapseOrder` | string | `"left-to-right"` |
| `collapseOrderTablet` | string | `""` |
| `columnGutter` | string | `"default"` |
| `columns` | number | `2` |
| `columnsInnerHeight` | boolean | `false` |
| `columnsUnlocked` | boolean | `false` |
| `currentOverlayTab` | string | `"normal"` |
| `currentTab` | string | `"desk"` |
| `customGutter` | array | `["", "", ""]` |
| `customRowGutter` | array | `["", "", ""]` |
| `displayBoxShadow` | boolean | `false` |
| `fifthColumnWidth` | number |  |
| `fifthColumnWidthMobile` | number |  |
| `fifthColumnWidthTablet` | number |  |
| `firstColumnWidth` | number |  |
| `firstColumnWidthMobile` | number |  |
| `firstColumnWidthTablet` | number |  |
| `fourthColumnWidth` | number |  |
| `fourthColumnWidthMobile` | number |  |
| `fourthColumnWidthTablet` | number |  |
| `gradient` | string | `""` |
| `gutterType` | string | `"px"` |
| `htmlTag` | string | `"div"` |
| `inQueryBlock` | boolean | `false` |
| `inheritMaxWidth` | boolean | `false` |
| `isPrebuiltModal` | boolean | `false` |
| `kbVersion` | number | `""` |
| `leftPadding` | number | `""` |
| `leftPaddingM` | number | `""` |
| `linkColor` | string | `""` |
| `linkHoverColor` | string | `""` |
| `loggedIn` | boolean | `false` |
| `loggedInShow` | array |  |
| `loggedInUser` | array |  |
| `loggedOut` | boolean | `false` |
| `margin` | array | `["", "", "", ""]` |
| `marginUnit` | string | `"px"` |
| `maxWidth` | number | `""` |
| `maxWidthUnit` | string | `"px"` |
| `minHeight` | number | `0` |
| `minHeightMobile` | number | `""` |
| `minHeightTablet` | number | `""` |
| `minHeightUnit` | string | `"px"` |
| `mobileBackground` | array | `[{"enable": false, "bgColor": "", "bgImg": "", "bgImgID": "", "bgImgSize": "cover", "bgImgPosition": "center center", "bgImgAttachment": "scroll", "bgImgRepeat": "no-repeat", "forceOverDesk": false}]` |
| `mobileBackgroundType` | string | `"normal"` |
| `mobileBorder` | string | `""` |
| `mobileBorderRadius` | array | `["", "", "", ""]` |
| `mobileBorderStyle` | array | `[{"top": ["", "", ""], "right": ["", "", ""], "bottom": ["", "", ""], "left": ["", "", ""], "unit": "px"}]` |
| `mobileBorderWidth` | array | `["", "", "", ""]` |
| `mobileGutter` | string | `""` |
| `mobileLayout` | string | `"row"` |
| `mobileMargin` | array | `["", "", "", ""]` |
| `mobileOverlay` | array | `[{"enable": false, "currentOverlayTab": "normal", "overlay": "", "overlaySecond": "#00B5E2", "overlayGradLoc": 0, "overlayGradLocSecond": 100, "overlayGradType": "linear", "overlayGradAngle": 180, "overlayBgImg": "", "overlayBgImgID": "", "overlayBgImgSize": "cover", "overlayBgImgPosition": "center center", "overlayBgImgAttachment": "scroll", "overlayBgImgRepeat": "no-repeat", "overlayOpacity": 30, "overlayBlendMod": "none"}]` |
| `mobilePadding` | array | `["", "", "", ""]` |
| `mobileRowGutter` | string | `""` |
| `noCustomDefaults` | boolean | `false` |
| `overlay` | string | `""` |
| `overlayBgImg` | string | `""` |
| `overlayBgImgAttachment` | string | `"scroll"` |
| `overlayBgImgID` | number | `""` |
| `overlayBgImgPosition` | string | `"center center"` |
| `overlayBgImgRepeat` | string | `"no-repeat"` |
| `overlayBgImgSize` | string | `"cover"` |
| `overlayBlendMode` | string | `"none"` |
| `overlayFirstOpacity` | number | `""` |
| `overlayGradAngle` | number | `180` |
| `overlayGradLoc` | number | `0` |
| `overlayGradLocSecond` | number | `100` |
| `overlayGradType` | string | `"linear"` |
| `overlayGradient` | string | `""` |
| `overlayOpacity` | number | `30` |
| `overlaySecond` | string | `"#00B5E2"` |
| `overlaySecondOpacity` | number | `""` |
| `padding` | array | `["sm", "", "sm", ""]` |
| `paddingUnit` | string | `"px"` |
| `rcpAccess` | string | `""` |
| `rcpMembership` | boolean | `false` |
| `rcpMembershipLevel` | array |  |
| `responsiveMaxWidth` | array | `["", ""]` |
| `rightPadding` | number | `""` |
| `rightPaddingM` | number | `""` |
| `rowGutterType` | string | `"px"` |
| `secondColumnWidth` | number |  |
| `secondColumnWidthMobile` | number |  |
| `secondColumnWidthTablet` | number |  |
| `sixthColumnWidth` | number |  |
| `sixthColumnWidthMobile` | number |  |
| `sixthColumnWidthTablet` | number |  |
| `tabletBackground` | array | `[{"enable": false, "bgColor": "", "bgImg": "", "bgImgID": "", "bgImgSize": "cover", "bgImgPosition": "center center", "bgImgAttachment": "scroll", "bgImgRepeat": "no-repeat", "forceOverDesk": false}]` |
| `tabletBackgroundType` | string | `"normal"` |
| `tabletBorder` | string | `""` |
| `tabletBorderRadius` | array | `["", "", "", ""]` |
| `tabletBorderStyle` | array | `[{"top": ["", "", ""], "right": ["", "", ""], "bottom": ["", "", ""], "left": ["", "", ""], "unit": "px"}]` |
| `tabletBorderWidth` | array | `["", "", "", ""]` |
| `tabletGutter` | string | `""` |
| `tabletLayout` | string | `"inherit"` |
| `tabletMargin` | array | `["", "", "", ""]` |
| `tabletOverlay` | array | `[{"enable": false, "currentOverlayTab": "normal", "overlay": "", "overlaySecond": "#00B5E2", "overlayGradLoc": 0, "overlayGradLocSecond": 100, "overlayGradType": "linear", "overlayGradAngle": 180, "overlayBgImg": "", "overlayBgImgID": "", "overlayBgImgSize": "cover", "overlayBgImgPosition": "center center", "overlayBgImgAttachment": "scroll", "overlayBgImgRepeat": "no-repeat", "overlayOpacity": 30, "overlayBlendMod": "none"}]` |
| `tabletPadding` | array | `["", "", "", ""]` |
| `tabletRowGutter` | string | `""` |
| `templateLock` | string \| boolean |  |
| `textColor` | string | `""` |
| `thirdColumnWidth` | number |  |
| `thirdColumnWidthMobile` | number |  |
| `thirdColumnWidthTablet` | number |  |
| `topMargin` | number | `""` |
| `topMarginM` | number | `""` |
| `topMarginT` | number | `""` |
| `topPadding` | number | `""` |
| `topPaddingM` | number | `""` |
| `topSep` | string | `"none"` |
| `topSepColor` | string | `"#ffffff"` |
| `topSepFlip` | boolean | `false` |
| `topSepHeight` | number | `100` |
| `topSepHeightMobile` | number | `""` |
| `topSepHeightTab` | number | `""` |
| `topSepHeightUnit` | string | `"px"` |
| `topSepWidth` | number | `100` |
| `topSepWidthMobile` | number | `""` |
| `topSepWidthTablet` | number | `""` |
| `uniqueID` | string | `""` |
| `verticalAlignment` | string | `"top"` |
| `vsdesk` | boolean | `false` |
| `vsmobile` | boolean | `false` |
| `vstablet` | boolean | `false` |
| `zIndex` | number | `""` |

## kadence/search

**Search (Adv)** · category `kadence-blocks` · apiVersion 3

- Supports: `{"anchor": true, "kbMetadata": true}`

| Attribute | Type | Default |
|---|---|---|
| `buttonSide` | string | `"right"` |
| `closeIcon` | string | `"fe_x"` |
| `closeIconColor` | string | `""` |
| `closeIconHoverColor` | string | `""` |
| `closeIconLineWidth` | number | `2` |
| `closeIconSize` | array | `[50, "", ""]` |
| `displayStyle` | string | `"standard"` |
| `inputBackgroundColor` | string | `""` |
| `inputBackgroundType` | string | `"normal"` |
| `inputBorderRadius` | array | `["", "", "", ""]` |
| `inputBorderRadiusUnit` | string | `"px"` |
| `inputBorderStyles` | array | `[{"top": ["#dee2e6", "", 1], "right": ["#dee2e6", "", 1], "bottom": ["#dee2e6", "", 1], "left": ["#dee2e6", "", 1], "unit": "px"}]` |
| `inputBoxShadow` | array | `[false, "#000000", 0.4, 2, 2, 3, 0, false]` |
| `inputColor` | string | `""` |
| `inputFocusBackgroundColor` | string | `""` |
| `inputFocusBackgroundType` | string | `"normal"` |
| `inputFocusBorderColor` | string | `""` |
| `inputFocusBoxShadowActive` | array | `[false, "#000000", 0.4, 2, 2, 3, 0, false]` |
| `inputFocusGradientActive` | boolean | `false` |
| `inputIcon` | string | `"fe_search"` |
| `inputIconColor` | string | `""` |
| `inputIconHoverColor` | string | `""` |
| `inputIconLineWidth` | number | `2` |
| `inputMargin` | array | `["", "", "", ""]` |
| `inputMarginType` | string | `"px"` |
| `inputMaxWidth` | array | `["", "", ""]` |
| `inputMaxWidthType` | string | `"px"` |
| `inputMinWidth` | array | `["", "", ""]` |
| `inputMinWidthType` | string | `"px"` |
| `inputPadding` | array | `["", "", "", ""]` |
| `inputPaddingType` | string | `"px"` |
| `inputPlaceholder` | string | `""` |
| `inputPlaceholderColor` | string | `""` |
| `inputTypography` | array | `[{"size": ["", "", ""], "sizeType": "px", "lineHeight": ["", "", ""], "lineType": "", "letterSpacing": ["", "", ""], "letterType": "px", "textTransform": "", "family": "", "google": "", "style": "", "weight": "", "variant": "", "subset": "", "loadGoogle": true}]` |
| `label` | string | `""` |
| `mobileInputBorderRadius` | array | `["", "", "", ""]` |
| `mobileInputBorderStyles` | array | `[{"top": ["", "", ""], "right": ["", "", ""], "bottom": ["", "", ""], "left": ["", "", ""], "unit": "px"}]` |
| `mobileInputMargin` | array | `["", "", "", ""]` |
| `mobileInputPadding` | array | `["", "", "", ""]` |
| `modalBackgroundColor` | string | `""` |
| `modalBackgroundType` | string | `"normal"` |
| `modalGradientActive` | string | `""` |
| `searchProductsOnly` | boolean | `false` |
| `showButton` | boolean | `false` |
| `tabletInputBorderRadius` | array | `["", "", "", ""]` |
| `tabletInputBorderStyles` | array | `[{"top": ["", "", ""], "right": ["", "", ""], "bottom": ["", "", ""], "left": ["", "", ""], "unit": "px"}]` |
| `tabletInputMargin` | array | `["", "", "", ""]` |
| `tabletInputPadding` | array | `["", "", "", ""]` |
| `uniqueID` | string |  |

## kadence/show-more

**Show More** · category `kadence-blocks` · apiVersion 3

- Supports: `{"kbMetadata": true}`

| Attribute | Type | Default |
|---|---|---|
| `align` | string |  |
| `defaultExpandedDesktop` | boolean | `false` |
| `defaultExpandedMobile` | boolean | `false` |
| `defaultExpandedTablet` | boolean | `false` |
| `enableFadeOut` | boolean | `false` |
| `fadeOutSize` | number | `50` |
| `heightDesktop` | number | `250` |
| `heightMobile` | number | `""` |
| `heightTablet` | number | `""` |
| `heightType` | string | `"px"` |
| `id` | number |  |
| `inQueryBlock` | boolean | `false` |
| `marginDesktop` | array | `["", "", "", ""]` |
| `marginMobile` | array | `["", "", "", ""]` |
| `marginTablet` | array | `["", "", "", ""]` |
| `marginUnit` | string | `"px"` |
| `paddingDesktop` | array | `["", "", "", ""]` |
| `paddingMobile` | array | `["", "", "", ""]` |
| `paddingTablet` | array | `["", "", "", ""]` |
| `paddingUnit` | string | `"px"` |
| `showHideMore` | boolean | `true` |
| `uniqueID` | string |  |

## kadence/single-icon

**Single Icon** · category `kadence-blocks` · apiVersion 3

- Parent-only: must be a direct child of `kadence/icon`
- Supports: `{"ktdynamic": true, "html": false, "reusable": false, "kbMetadata": true}`

| Attribute | Type | Default |
|---|---|---|
| `background` | string | `"transparent"` |
| `border` | string | `""` |
| `borderRadius` | number | `0` |
| `borderWidth` | number | `2` |
| `color` | string | `""` |
| `hBackground` | string | `""` |
| `hBorder` | string | `""` |
| `hColor` | string | `""` |
| `icon` | string | `"fe_aperture"` |
| `inQueryBlock` | boolean | `false` |
| `link` | string | `""` |
| `linkTitle` | string | `""` |
| `margin` | array | `["", "", "", ""]` |
| `marginUnit` | string | `"px"` |
| `mobileMargin` | array | `["", "", "", ""]` |
| `mobilePadding` | array | `["", "", "", ""]` |
| `mobileSize` | number | `""` |
| `padding` | array | `["xs", "xs", "xs", "xs"]` |
| `paddingUnit` | string | `"px"` |
| `size` | number | `50` |
| `style` | string | `"default"` |
| `tabletMargin` | array | `["", "", "", ""]` |
| `tabletPadding` | array | `["", "", "", ""]` |
| `tabletSize` | number | `""` |
| `target` | string | `"_self"` |
| `title` | string | `""` |
| `tooltip` | string |  |
| `tooltipDash` | boolean | `false` |
| `tooltipPlacement` | string | `""` |
| `uniqueID` | string | `""` |
| `width` | number | `2` |

## kadence/singlebtn

**Single Button** · category `kadence-blocks` · apiVersion 3

- Parent-only: must be a direct child of `kadence/advancedbtn`
- Supports: `{"anchor": true, "ktanimate": true, "ktanimateadd": true, "ktanimatepreview": true, "ktdynamic": true, "html": false, "reusable": false, "kbMetadata": true, "kbContentLabel": "text"}`

| Attribute | Type | Default |
|---|---|---|
| `anchor` | string |  |
| `background` | string | `""` |
| `backgroundHover` | string | `""` |
| `backgroundHoverType` | string | `"normal"` |
| `backgroundSticky` | string | `""` |
| `backgroundStickyHover` | string | `""` |
| `backgroundStickyHoverType` | string | `"normal"` |
| `backgroundStickyType` | string | `"normal"` |
| `backgroundTransparent` | string | `""` |
| `backgroundTransparentHover` | string | `""` |
| `backgroundTransparentHoverType` | string | `"normal"` |
| `backgroundTransparentType` | string | `"normal"` |
| `backgroundType` | string | `"normal"` |
| `borderHoverRadius` | array | `["", "", "", ""]` |
| `borderHoverRadiusUnit` | string | `"px"` |
| `borderHoverStyle` | array | `[{"top": ["", "", ""], "right": ["", "", ""], "bottom": ["", "", ""], "left": ["", "", ""], "unit": "px"}]` |
| `borderRadius` | array | `["", "", "", ""]` |
| `borderRadiusUnit` | string | `"px"` |
| `borderStickyHoverRadius` | array | `["", "", "", ""]` |
| `borderStickyHoverRadiusUnit` | string | `"px"` |
| `borderStickyHoverStyle` | array | `[{"top": ["", "", ""], "right": ["", "", ""], "bottom": ["", "", ""], "left": ["", "", ""], "unit": "px"}]` |
| `borderStickyRadius` | array | `["", "", "", ""]` |
| `borderStickyRadiusUnit` | string | `"px"` |
| `borderStickyStyle` | array | `[{"top": ["", "", ""], "right": ["", "", ""], "bottom": ["", "", ""], "left": ["", "", ""], "unit": "px"}]` |
| `borderStyle` | array | `[{"top": ["", "", ""], "right": ["", "", ""], "bottom": ["", "", ""], "left": ["", "", ""], "unit": "px"}]` |
| `borderTransparentHoverRadius` | array | `["", "", "", ""]` |
| `borderTransparentHoverRadiusUnit` | string | `"px"` |
| `borderTransparentHoverStyle` | array | `[{"top": ["", "", ""], "right": ["", "", ""], "bottom": ["", "", ""], "left": ["", "", ""], "unit": "px"}]` |
| `borderTransparentRadius` | array | `["", "", "", ""]` |
| `borderTransparentRadiusUnit` | string | `"px"` |
| `borderTransparentStyle` | array | `[{"top": ["", "", ""], "right": ["", "", ""], "bottom": ["", "", ""], "left": ["", "", ""], "unit": "px"}]` |
| `buttonRole` | boolean | `false` |
| `color` | string | `""` |
| `colorHover` | string | `""` |
| `colorSticky` | string | `""` |
| `colorStickyHover` | string | `""` |
| `colorTransparent` | string | `""` |
| `colorTransparentHover` | string | `""` |
| `displayHoverShadow` | boolean | `false` |
| `displayHoverShadowSticky` | boolean | `false` |
| `displayHoverShadowTransparent` | boolean | `false` |
| `displayShadow` | boolean | `false` |
| `displayShadowSticky` | boolean | `false` |
| `displayShadowTransparent` | boolean | `false` |
| `download` | boolean | `false` |
| `gap` | array | `["", "", ""]` |
| `gradient` | string | `""` |
| `gradientHover` | string | `""` |
| `gradientSticky` | string | `""` |
| `gradientStickyHover` | string | `""` |
| `gradientTransparent` | string | `""` |
| `gradientTransparentHover` | string | `""` |
| `hideLink` | boolean | `false` |
| `icon` | string | `""` |
| `iconColor` | string | `""` |
| `iconColorHover` | string | `""` |
| `iconHover` | boolean | `false` |
| `iconPadding` | array | `["", "", "", ""]` |
| `iconPaddingUnit` | string | `"px"` |
| `iconReveal` | boolean | `false` |
| `iconSide` | string | `"right"` |
| `iconSize` | array | `["", "", ""]` |
| `iconSizeUnit` | string | `"px"` |
| `iconTitle` | string | `""` |
| `inQueryBlock` | boolean | `false` |
| `inheritStyles` | string | `"fill"` |
| `isSubmit` | boolean | `false` |
| `label` | string | `""` |
| `link` | string | `""` |
| `margin` | array | `["", "", "", ""]` |
| `marginUnit` | string | `"px"` |
| `mobileBorderHoverRadius` | array | `["", "", "", ""]` |
| `mobileBorderHoverStyle` | array | `[{"top": ["", "", ""], "right": ["", "", ""], "bottom": ["", "", ""], "left": ["", "", ""], "unit": "px"}]` |
| `mobileBorderRadius` | array | `["", "", "", ""]` |
| `mobileBorderStickyHoverRadius` | array | `["", "", "", ""]` |
| `mobileBorderStickyHoverStyle` | array | `[{"top": ["", "", ""], "right": ["", "", ""], "bottom": ["", "", ""], "left": ["", "", ""], "unit": "px"}]` |
| `mobileBorderStickyRadius` | array | `["", "", "", ""]` |
| `mobileBorderStickyStyle` | array | `[{"top": ["", "", ""], "right": ["", "", ""], "bottom": ["", "", ""], "left": ["", "", ""], "unit": "px"}]` |
| `mobileBorderStyle` | array | `[{"top": ["", "", ""], "right": ["", "", ""], "bottom": ["", "", ""], "left": ["", "", ""], "unit": "px"}]` |
| `mobileBorderTransparentHoverRadius` | array | `["", "", "", ""]` |
| `mobileBorderTransparentHoverStyle` | array | `[{"top": ["", "", ""], "right": ["", "", ""], "bottom": ["", "", ""], "left": ["", "", ""], "unit": "px"}]` |
| `mobileBorderTransparentRadius` | array | `["", "", "", ""]` |
| `mobileBorderTransparentStyle` | array | `[{"top": ["", "", ""], "right": ["", "", ""], "bottom": ["", "", ""], "left": ["", "", ""], "unit": "px"}]` |
| `mobileIconPadding` | array | `["", "", "", ""]` |
| `mobileMargin` | array | `["", "", "", ""]` |
| `mobilePadding` | array | `["", "", "", ""]` |
| `noCustomDefaults` | boolean | `false` |
| `noFollow` | boolean | `false` |
| `onlyIcon` | array | `[false, "", ""]` |
| `onlyText` | array | `[false, ""]` |
| `padding` | array | `["", "", "", ""]` |
| `paddingUnit` | string | `"px"` |
| `shadow` | array | `[{"color": "#000000", "opacity": 0.2, "spread": 0, "blur": 2, "hOffset": 1, "vOffset": 1, "inset": false}]` |
| `shadowHover` | array | `[{"color": "#000000", "opacity": 0.4, "spread": 0, "blur": 3, "hOffset": 2, "vOffset": 2, "inset": false}]` |
| `shadowSticky` | array | `[{"color": "#000000", "opacity": 0.2, "spread": 0, "blur": 2, "hOffset": 1, "vOffset": 1, "inset": false}]` |
| `shadowStickyHover` | array | `[{"color": "#000000", "opacity": 0.4, "spread": 0, "blur": 3, "hOffset": 2, "vOffset": 2, "inset": false}]` |
| `shadowTransparent` | array | `[{"color": "#000000", "opacity": 0.2, "spread": 0, "blur": 2, "hOffset": 1, "vOffset": 1, "inset": false}]` |
| `shadowTransparentHover` | array | `[{"color": "#000000", "opacity": 0.4, "spread": 0, "blur": 3, "hOffset": 2, "vOffset": 2, "inset": false}]` |
| `sizePreset` | string | `"standard"` |
| `sponsored` | boolean | `false` |
| `style` | string | `"basic"` |
| `tabletBorderHoverRadius` | array | `["", "", "", ""]` |
| `tabletBorderHoverStyle` | array | `[{"top": ["", "", ""], "right": ["", "", ""], "bottom": ["", "", ""], "left": ["", "", ""], "unit": "px"}]` |
| `tabletBorderRadius` | array | `["", "", "", ""]` |
| `tabletBorderStickyHoverRadius` | array | `["", "", "", ""]` |
| `tabletBorderStickyHoverStyle` | array | `[{"top": ["", "", ""], "right": ["", "", ""], "bottom": ["", "", ""], "left": ["", "", ""], "unit": "px"}]` |
| `tabletBorderStickyRadius` | array | `["", "", "", ""]` |
| `tabletBorderStickyStyle` | array | `[{"top": ["", "", ""], "right": ["", "", ""], "bottom": ["", "", ""], "left": ["", "", ""], "unit": "px"}]` |
| `tabletBorderStyle` | array | `[{"top": ["", "", ""], "right": ["", "", ""], "bottom": ["", "", ""], "left": ["", "", ""], "unit": "px"}]` |
| `tabletBorderTransparentHoverRadius` | array | `["", "", "", ""]` |
| `tabletBorderTransparentHoverStyle` | array | `[{"top": ["", "", ""], "right": ["", "", ""], "bottom": ["", "", ""], "left": ["", "", ""], "unit": "px"}]` |
| `tabletBorderTransparentRadius` | array | `["", "", "", ""]` |
| `tabletBorderTransparentStyle` | array | `[{"top": ["", "", ""], "right": ["", "", ""], "bottom": ["", "", ""], "left": ["", "", ""], "unit": "px"}]` |
| `tabletIconPadding` | array | `["", "", "", ""]` |
| `tabletMargin` | array | `["", "", "", ""]` |
| `tabletPadding` | array | `["", "", "", ""]` |
| `target` | string | `"_self"` |
| `text` | string | `""` |
| `textBackgroundHoverType` | string | `"normal"` |
| `textBackgroundType` | string | `"normal"` |
| `textGradient` | string | `""` |
| `textGradientHover` | string | `""` |
| `textUnderline` | string |  |
| `tooltip` | string | `""` |
| `tooltipPlacement` | string | `""` |
| `typography` | array | `[{"size": ["", "", ""], "sizeType": "px", "lineHeight": ["", "", ""], "lineType": "", "letterSpacing": ["", "", ""], "letterType": "px", "textTransform": "", "family": "", "google": "", "style": "", "weight": "", "variant": "", "subset": "", "loadGoogle": true}]` |
| `uniqueID` | string | `""` |
| `width` | array | `["", "", ""]` |
| `widthType` | string | `"auto"` |
| `widthUnit` | string | `"px"` |

## kadence/spacer

**Spacer / Divider** · category `kadence-blocks` · apiVersion 3

- Supports: `{"anchor": true, "kbMetadata": true}`

| Attribute | Type | Default |
|---|---|---|
| `blockAlignment` | string | `"center"` |
| `dividerColor` | string | `"#eee"` |
| `dividerEnable` | boolean | `true` |
| `dividerHeight` | number | `1` |
| `dividerOpacity` | number | `100` |
| `dividerStyle` | string | `"solid"` |
| `dividerWidth` | number | `80` |
| `dividerWidthUnits` | string | `"%"` |
| `hAlign` | string | `"center"` |
| `mobileDividerHeight` | number |  |
| `mobileDividerWidth` | number |  |
| `mobileHAlign` | string | `""` |
| `mobileSpacerHeight` | number | `""` |
| `rotate` | number | `40` |
| `spacerHeight` | number | `60` |
| `spacerHeightUnits` | string | `"px"` |
| `strokeGap` | number | `5` |
| `strokeWidth` | number | `4` |
| `tabletDividerHeight` | number |  |
| `tabletDividerWidth` | number |  |
| `tabletHAlign` | string | `""` |
| `tabletSpacerHeight` | number | `""` |
| `uniqueID` | string | `""` |
| `vsdesk` | boolean | `false` |
| `vsmobile` | boolean | `false` |
| `vstablet` | boolean | `false` |

## kadence/tab

**Tab** · category `kadence-blocks` · apiVersion 3

- Parent-only: must be a direct child of `kadence/tabs`
- Supports: `{"inserter": false, "reusable": false, "html": false, "lock": false, "ktdynamic": true}`

| Attribute | Type | Default |
|---|---|---|
| `id` | number | `1` |
| `uniqueID` | string | `""` |

## kadence/table

**Table (Adv)** · category `kadence-blocks` · apiVersion 3

- Supports: `{"kbMetadata": true}`

| Attribute | Type | Default |
|---|---|---|
| `backgroundColorEven` | string | `""` |
| `backgroundColorOdd` | string | `""` |
| `backgroundHoverColorEven` | string | `""` |
| `backgroundHoverColorOdd` | string | `""` |
| `borderOnRowOnly` | boolean | `false` |
| `borderStyle` | array | `[{"top": ["", "", ""], "right": ["", "", ""], "bottom": ["", "", ""], "left": ["", "", ""], "unit": "px"}]` |
| `caption` | string | `""` |
| `captionAlign` | string | `"center"` |
| `captionAlignMobile` | string | `""` |
| `captionAlignTablet` | string | `""` |
| `captionTypography` | array | `[{"size": ["", "", ""], "sizeType": "px", "lineHeight": ["", "", ""], "lineType": "", "letterSpacing": "", "family": "", "google": "", "style": "", "weight": "", "variant": "", "subset": "", "loadGoogle": true, "padding": ["xxs", "xs", "xxs", "xs"], "marginTop": 8, "color": "", "background": "", "border": ["", "", "", ""], "borderRadius": ["", "", "", ""], "borderWidth": ["", "", "", ""], "colorHover": "", "backgroundHover": "", "borderHover": ["", "", "", ""], "colorActive": "", "backgroundActive": "", "borderActive": ["", "", "", ""], "textTransform": "", "paddingTablet": ["", "", "", ""], "paddingMobile": ["", "", "", ""], "paddingType": "px"}]` |
| `cellPadding` | array | `["xxs", "xxs", "xxs", "xxs"]` |
| `cellPaddingType` | string | `"px"` |
| `columnBackgrounds` | array | `[]` |
| `columnBackgroundsHover` | array | `[]` |
| `columnSettings` | array | `[]` |
| `columns` | number |  |
| `dataTypography` | array | `[{"size": ["", "", ""], "sizeType": "px", "lineHeight": ["", "", ""], "lineType": "", "letterSpacing": "", "family": "", "google": "", "style": "", "weight": "", "variant": "", "subset": "", "loadGoogle": true, "padding": ["xxs", "xs", "xxs", "xs"], "marginTop": 8, "color": "", "background": "", "border": ["", "", "", ""], "borderRadius": ["", "", "", ""], "borderWidth": ["", "", "", ""], "colorHover": "", "backgroundHover": "", "borderHover": ["", "", "", ""], "colorActive": "", "backgroundActive": "", "borderActive": ["", "", "", ""], "textTransform": "", "paddingTablet": ["", "", "", ""], "paddingMobile": ["", "", "", ""], "paddingType": "px"}]` |
| `enableCaption` | boolean | `false` |
| `evenOddBackground` | boolean | `false` |
| `headerAlign` | string | `"center"` |
| `headerAlignMobile` | string | `""` |
| `headerAlignTablet` | string | `""` |
| `headerTypography` | array | `[{"size": ["", "", ""], "sizeType": "px", "lineHeight": ["", "", ""], "lineType": "", "letterSpacing": "", "family": "", "google": "", "style": "", "weight": "", "variant": "", "subset": "", "loadGoogle": true, "padding": ["xxs", "xs", "xxs", "xs"], "marginTop": 8, "color": "", "background": "", "border": ["", "", "", ""], "borderRadius": ["", "", "", ""], "borderWidth": ["", "", "", ""], "colorHover": "", "backgroundHover": "", "borderHover": ["", "", "", ""], "colorActive": "", "backgroundActive": "", "borderActive": ["", "", "", ""], "textTransform": "", "paddingTablet": ["", "", "", ""], "paddingMobile": ["", "", "", ""], "paddingType": "px"}]` |
| `isFirstColumnHeader` | boolean | `false` |
| `isFirstRowHeader` | boolean | `false` |
| `margin` | array | `["", "", "", ""]` |
| `marginType` | string | `"px"` |
| `maxHeight` | array | `["", "", ""]` |
| `maxHeightUnit` | string | `"px"` |
| `maxWidth` | array | `["", "", ""]` |
| `maxWidthUnit` | string | `"%"` |
| `mobileBorderStyle` | array | `[{"top": ["", "", ""], "right": ["", "", ""], "bottom": ["", "", ""], "left": ["", "", ""], "unit": "px"}]` |
| `mobileCellPadding` | array | `["", "", "", ""]` |
| `mobileMargin` | array | `["", "", "", ""]` |
| `mobilePadding` | array | `["", "", "", ""]` |
| `mobileRowMinHeight` | number | `""` |
| `overflowXScroll` | boolean | `false` |
| `padding` | array | `["", "", "", ""]` |
| `paddingType` | string | `"px"` |
| `rowMinHeight` | number | `""` |
| `rowMinHeightType` | string | `"px"` |
| `tabletBorderStyle` | array | `[{"top": ["", "", ""], "right": ["", "", ""], "bottom": ["", "", ""], "left": ["", "", ""], "unit": "px"}]` |
| `tabletCellPadding` | array | `["", "", "", ""]` |
| `tabletMargin` | array | `["", "", "", ""]` |
| `tabletPadding` | array | `["", "", "", ""]` |
| `tabletRowMinHeight` | number | `""` |
| `textAlign` | string | `"left"` |
| `textAlignMobile` | string | `""` |
| `textAlignTablet` | string | `""` |
| `uniqueID` | string |  |

## kadence/table-data

**Table Data** · category `kadence-blocks` · apiVersion 3

- Parent-only: must be a direct child of `kadence/table-row`
- Supports: `{"kbMetadata": true}`

| Attribute | Type | Default |
|---|---|---|
| `column` | number |  |
| `mobilePadding` | array | `["", "", "", ""]` |
| `padding` | array | `["", "", "", ""]` |
| `paddingType` | string | `"px"` |
| `tabletPadding` | array | `["", "", "", ""]` |
| `uniqueID` | string |  |

## kadence/table-row

**Table (Adv)** · category `kadence-blocks` · apiVersion 3

- Parent-only: must be a direct child of `kadence/table`
- Allowed children: `kadence/table-data`
- Supports: `{"kbMetadata": true}`

| Attribute | Type | Default |
|---|---|---|
| `backgroundColor` | string | `""` |
| `backgroundHoverColor` | string | `""` |
| `minHeight` | number | `""` |
| `minHeightMobile` | number | `""` |
| `minHeightTablet` | number | `""` |
| `minHeightType` | string | `"px"` |
| `row` | number |  |
| `uniqueID` | string |  |

## kadence/tableofcontents

**Table of Contents** · category `kadence-blocks` · apiVersion 3

- Supports: `{"html": false, "kbMetadata": true}`

| Attribute | Type | Default |
|---|---|---|
| `allowedHeaders` | array | `[{"h1": true, "h2": true, "h3": true, "h4": true, "h5": true, "h6": true}]` |
| `borderRadius` | array | `["", "", "", ""]` |
| `borderRadiusUnit` | string | `"px"` |
| `borderStyle` | array | `[{"top": ["", "", ""], "right": ["", "", ""], "bottom": ["", "", ""], "left": ["", "", ""], "unit": "px"}]` |
| `columns` | number | `1` |
| `containerBackground` | string | `""` |
| `containerBorder` | array | `["", "", "", ""]` |
| `containerBorderColor` | string | `""` |
| `containerMargin` | array | `["", "", "", ""]` |
| `containerMarginUnit` | string | `"px"` |
| `containerMobileMargin` | array | `["", "", "", ""]` |
| `containerPadding` | array | `["sm", "sm", "sm", "sm"]` |
| `containerPaddingUnit` | string | `"px"` |
| `containerTabletMargin` | array | `["", "", "", ""]` |
| `contentActiveColor` | string |  |
| `contentColor` | string |  |
| `contentFontStyle` | string | `"normal"` |
| `contentFontSubset` | string | `""` |
| `contentFontVariant` | string | `""` |
| `contentFontWeight` | string | `"regular"` |
| `contentGoogleFont` | boolean | `false` |
| `contentHoverColor` | string |  |
| `contentLetterSpacing` | number |  |
| `contentLineHeight` | array | `["", "", ""]` |
| `contentLineType` | string | `"px"` |
| `contentLoadGoogleFont` | boolean | `true` |
| `contentMargin` | array | `["sm", "0", "0", "0"]` |
| `contentMarginType` | string | `"px"` |
| `contentSize` | array | `["", "", ""]` |
| `contentSizeType` | string | `"px"` |
| `contentTextTransform` | string | `""` |
| `contentTypography` | string | `""` |
| `displayShadow` | boolean | `false` |
| `enableDynamicSearch` | boolean | `false` |
| `enableScrollSpy` | boolean | `false` |
| `enableSmoothScroll` | boolean | `false` |
| `enableTemplateSearch` | boolean | `false` |
| `enableTitle` | boolean | `true` |
| `enableTitleToggle` | boolean | `false` |
| `enableToggle` | boolean | `false` |
| `linkStyle` | string | `"underline"` |
| `listGap` | array | `["", "", ""]` |
| `listStyle` | string | `"disc"` |
| `maxWidth` | number | `""` |
| `maxWidthType` | string | `"px"` |
| `mobileBorderRadius` | array | `["", "", "", ""]` |
| `mobileBorderStyle` | array | `[{"top": ["", "", ""], "right": ["", "", ""], "bottom": ["", "", ""], "left": ["", "", ""], "unit": "px"}]` |
| `mobileContainerPadding` | array | `["", "", "", ""]` |
| `mobileContentMargin` | array | `["", "", "", ""]` |
| `mobileMaxWidth` | number | `""` |
| `mobileTitleBorderStyle` | array | `[{"top": ["", "", ""], "right": ["", "", ""], "bottom": ["", "", ""], "left": ["", "", ""], "unit": "px"}]` |
| `mobileTitlePadding` | array | `["", "", "", ""]` |
| `shadow` | array | `[{"color": "#000000", "opacity": 0.2, "spread": 0, "blur": 14, "hOffset": 0, "vOffset": 0, "inset": false}]` |
| `smoothScrollOffset` | number | `40` |
| `startClosed` | boolean | `false` |
| `tabletBorderRadius` | array | `["", "", "", ""]` |
| `tabletBorderStyle` | array | `[{"top": ["", "", ""], "right": ["", "", ""], "bottom": ["", "", ""], "left": ["", "", ""], "unit": "px"}]` |
| `tabletContainerPadding` | array | `["", "", "", ""]` |
| `tabletContentMargin` | array | `["", "", "", ""]` |
| `tabletMaxWidth` | number | `""` |
| `tabletTitleBorderStyle` | array | `[{"top": ["", "", ""], "right": ["", "", ""], "bottom": ["", "", ""], "left": ["", "", ""], "unit": "px"}]` |
| `tabletTitlePadding` | array | `["", "", "", ""]` |
| `title` | string | `"Table of Contents"` |
| `titleAlign` | string |  |
| `titleBorder` | array | `["", "", "", ""]` |
| `titleBorderColor` | string |  |
| `titleBorderStyle` | array | `[{"top": ["", "", ""], "right": ["", "", ""], "bottom": ["", "", ""], "left": ["", "", ""], "unit": "px"}]` |
| `titleCollapseBorderColor` | string |  |
| `titleColor` | string |  |
| `titleFontStyle` | string | `"normal"` |
| `titleFontSubset` | string | `""` |
| `titleFontVariant` | string | `""` |
| `titleFontWeight` | string | `"regular"` |
| `titleGoogleFont` | boolean | `false` |
| `titleLetterSpacing` | number |  |
| `titleLineHeight` | array | `["", "", ""]` |
| `titleLineType` | string | `"px"` |
| `titleLoadGoogleFont` | boolean | `true` |
| `titlePadding` | array | `["0", "0", "0", "0"]` |
| `titlePaddingType` | string | `"px"` |
| `titleSize` | array | `["", "", ""]` |
| `titleSizeType` | string | `"px"` |
| `titleTextTransform` | string | `""` |
| `titleTypography` | string | `""` |
| `toggleIcon` | string | `"arrow"` |
| `uniqueID` | string |  |

## kadence/tabs

**Tabs** · category `kadence-blocks` · apiVersion 3

- Supports: `{"anchor": true, "kbMetadata": true}`

| Attribute | Type | Default |
|---|---|---|
| `blockAlignment` | string | `"none"` |
| `contentBgColor` | string | `""` |
| `contentBorder` | array | `["", "", "", ""]` |
| `contentBorderColor` | string | `""` |
| `contentBorderRadius` | array | `[0, 0, 0, 0]` |
| `contentBorderRadiusUnit` | string | `"px"` |
| `contentBorderStyles` | array | `[{"top": ["#dee2e6", "", 1], "right": ["#dee2e6", "", 1], "bottom": ["#dee2e6", "", 1], "left": ["#dee2e6", "", 1], "unit": "px"}]` |
| `currentTab` | number | `1` |
| `enableSubtitle` | boolean | `false` |
| `fontStyle` | string | `"normal"` |
| `fontSubset` | string | `""` |
| `fontVariant` | string | `""` |
| `fontWeight` | string | `"regular"` |
| `googleFont` | boolean | `false` |
| `gutter` | array | `[10, "", ""]` |
| `iSize` | number | `14` |
| `innerPadding` | array | `["sm", "sm", "sm", "sm"]` |
| `innerPaddingControl` | string | `"linked"` |
| `innerPaddingM` | array |  |
| `innerPaddingType` | string | `"px"` |
| `layout` | string | `"tabs"` |
| `letterSpacing` | number |  |
| `lineHeight` | number |  |
| `lineType` | string | `"px"` |
| `linkPaneCollapse` | boolean | `false` |
| `loadGoogleFont` | boolean | `true` |
| `maxWidth` | number | `""` |
| `minHeight` | number | `""` |
| `mobileContentBorderRadius` | array | `["", "", "", ""]` |
| `mobileContentBorderStyles` | array | `[{"top": ["", "", ""], "right": ["", "", ""], "bottom": ["", "", ""], "left": ["", "", ""], "unit": "px"}]` |
| `mobileISize` | number | `""` |
| `mobileInnerPadding` | array | `["", "", "", ""]` |
| `mobileLayout` | string | `"inherit"` |
| `mobileLineHeight` | number |  |
| `mobileMaxWidth` | number | `""` |
| `mobileMinHeight` | number | `""` |
| `mobileSize` | string |  |
| `mobileTitleBorderRadius` | array | `["", "", "", ""]` |
| `mobileTitleBorderWidth` | array | `["", "", "", ""]` |
| `mobileTitleMargin` | array | `["", "", "", ""]` |
| `mobileTitlePadding` | array | `["", "", "", ""]` |
| `showPresets` | boolean | `true` |
| `size` | string |  |
| `sizeType` | string | `"px"` |
| `startTab` | number | `""` |
| `subtitleColor` | string |  |
| `subtitleColorActive` | string |  |
| `subtitleColorHover` | string |  |
| `subtitleFont` | array | `[{"size": ["", "", ""], "sizeType": "px", "lineHeight": ["", "", ""], "lineType": "px", "letterSpacing": "", "textTransform": "", "family": "", "google": false, "style": "", "weight": "", "variant": "", "subset": "", "loadGoogle": true, "padding": [0, 0, 0, 0], "paddingControl": "linked", "margin": [0, 0, 0, 0], "marginControl": "linked"}]` |
| `tabAlignment` | string | `"left"` |
| `tabCount` | number | `3` |
| `tabLineHeight` | number |  |
| `tabSize` | string |  |
| `tabWidth` | array | `[4, "", ""]` |
| `tabletContentBorderRadius` | array | `["", "", "", ""]` |
| `tabletContentBorderStyles` | array | `[{"top": ["", "", ""], "right": ["", "", ""], "bottom": ["", "", ""], "left": ["", "", ""], "unit": "px"}]` |
| `tabletISize` | number | `""` |
| `tabletInnerPadding` | array | `["", "", "", ""]` |
| `tabletLayout` | string | `"inherit"` |
| `tabletMaxWidth` | number | `""` |
| `tabletMinHeight` | number | `""` |
| `tabletTitleBorderRadius` | array | `["", "", "", ""]` |
| `tabletTitleBorderWidth` | array | `["", "", "", ""]` |
| `tabletTitleMargin` | array | `["", "", "", ""]` |
| `tabletTitlePadding` | array | `["", "", "", ""]` |
| `textTransform` | string |  |
| `titleBg` | string |  |
| `titleBgActive` | string | `""` |
| `titleBgHover` | string |  |
| `titleBorder` | string |  |
| `titleBorderActive` | string |  |
| `titleBorderHover` | string |  |
| `titleBorderRadius` | array |  |
| `titleBorderRadiusUnit` | string | `"px"` |
| `titleBorderWidth` | array | `["", "", "", ""]` |
| `titleBorderWidthUnit` | string | `"px"` |
| `titleColor` | string |  |
| `titleColorActive` | string |  |
| `titleColorHover` | string |  |
| `titleMargin` | array | `["", "", "", ""]` |
| `titleMarginUnit` | string | `"px"` |
| `titlePadding` | array | `["", "", "", ""]` |
| `titlePaddingUnit` | string | `"px"` |
| `titles` | array | `[{"text": "Tab 1", "icon": "", "iconSide": "right", "onlyIcon": false, "subText": "", "anchor": ""}, {"text": "Tab 2", "icon": "", "iconSide": "right", "onlyIcon": false, "subText": "", "anchor": ""}, {"text": "Tab 3", "icon": "", "iconSide": "right", "onlyIcon": false, "subText": "", "anchor": ""}]` |
| `typography` | string | `""` |
| `uniqueID` | string | `""` |
| `verticalTabWidth` | array | `["30", "", ""]` |
| `verticalTabWidthUnit` | string | `"%"` |
| `widthType` | string | `"normal"` |

## kadence/testimonial

**Testimonial** · category `kadence-blocks` · apiVersion 3

- Parent-only: must be a direct child of `kadence/testimonials`
- Supports: `{"anchor": true, "html": false, "kbMetadata": true, "kbContentLabel": "title", "ktdynamic": true}`

| Attribute | Type | Default |
|---|---|---|
| `alt` | string | `""` |
| `anchor` | string | `""` |
| `color` | string | `""` |
| `content` | string | `""` |
| `height` | number | `""` |
| `icon` | string | `"fas_quote-left"` |
| `id` | number | `""` |
| `inQueryBlock` | boolean | `false` |
| `isize` | number | `50` |
| `istroke` | number | `2` |
| `ititle` | string | `""` |
| `maxWidth` | number | `""` |
| `media` | string | `"image"` |
| `mobileIsize` | number | `""` |
| `name` | string | `""` |
| `occupation` | string | `""` |
| `rating` | number | `5` |
| `sizes` | object | `{}` |
| `subtype` | string | `""` |
| `tabletIsize` | number | `""` |
| `title` | string | `""` |
| `uniqueID` | string | `""` |
| `url` | string | `""` |
| `useBlockQuoteTags` | boolean | `true` |
| `width` | number | `""` |

## kadence/testimonials

**Testimonials** · category `kadence-blocks` · apiVersion 3

- Supports: `{"anchor": true, "html": false, "kbMetadata": true}`

| Attribute | Type | Default |
|---|---|---|
| `anchor` | string | `""` |
| `arrowStyle` | string | `"whiteondark"` |
| `autoPlay` | boolean | `false` |
| `autoSpeed` | number | `7000` |
| `borderStyle` | array | `[{"top": ["", "", ""], "right": ["", "", ""], "bottom": ["", "", ""], "left": ["", "", ""], "unit": "px"}]` |
| `carouselType` | string | `"loop"` |
| `columnControl` | string | `"linked"` |
| `columnGap` | number | `""` |
| `columns` | array | `[1, 1, 1, 1, 1, 1]` |
| `containerBackground` | string | `""` |
| `containerBackgroundOpacity` | number | `1` |
| `containerBorder` | string | `""` |
| `containerBorderOpacity` | number | `1` |
| `containerBorderRadius` | number | `""` |
| `containerBorderRadiusUnit` | string | `"px"` |
| `containerBorderWidth` | array | `["", "", "", ""]` |
| `containerMaxWidth` | number | `500` |
| `containerMinHeight` | array | `["", "", ""]` |
| `containerPadding` | array | `[20, 20, 20, 20]` |
| `containerPaddingType` | string | `"px"` |
| `containerVAlign` | string | `""` |
| `contentFont` | array | `[{"color": "", "size": ["", "", ""], "sizetype": "px", "lineHeight": ["", "", ""], "linetype": "px", "letterSpacing": "", "textTransform": "", "family": "", "google": "", "style": "", "weight": "", "variant": "", "subset": "", "loadGoogle": true}]` |
| `contentMinHeight` | array | `["", "", ""]` |
| `displayContent` | boolean | `true` |
| `displayIcon` | boolean | `false` |
| `displayMedia` | boolean | `true` |
| `displayName` | boolean | `true` |
| `displayOccupation` | boolean | `true` |
| `displayRating` | boolean | `false` |
| `displayShadow` | boolean | `false` |
| `displayTitle` | boolean | `true` |
| `dotStyle` | string | `"dark"` |
| `gap` | array | `["md", "", ""]` |
| `gapUnit` | string | `"px"` |
| `hAlign` | string | `"center"` |
| `iconBorderRadius` | array | `["", "", "", ""]` |
| `iconBorderRadiusUnit` | string | `"px"` |
| `iconBorderStyle` | array | `[{"top": ["", "", ""], "right": ["", "", ""], "bottom": ["", "", ""], "left": ["", "", ""], "unit": "px"}]` |
| `iconMargin` | array | `["", "", "", ""]` |
| `iconMarginUnit` | string | `"px"` |
| `iconPadding` | array | `["", "", "", ""]` |
| `iconPaddingUnit` | string | `"px"` |
| `iconStyles` | array | `[{"size": 30, "margin": ["", "", "", ""], "padding": ["", "", "", ""], "borderWidth": ["", "", "", ""], "borderRadius": "", "border": "", "borderOpacity": 1, "color": "", "background": "", "backgroundOpacity": 1, "title": "", "icon": "fas_quote-left", "stroke": 2}]` |
| `inQueryBlock` | boolean | `false` |
| `itemsCount` | number | `1` |
| `kbVersion` | number | `""` |
| `layout` | string | `"grid"` |
| `mediaBorderRadius` | array | `["", "", "", ""]` |
| `mediaBorderRadiusUnit` | string | `"px"` |
| `mediaBorderStyle` | array | `[{"top": ["", "", ""], "right": ["", "", ""], "bottom": ["", "", ""], "left": ["", "", ""], "unit": "px"}]` |
| `mediaMargin` | array | `["", "", "", ""]` |
| `mediaMarginUnit` | string | `"px"` |
| `mediaPadding` | array | `["", "", "", ""]` |
| `mediaPaddingUnit` | string | `"px"` |
| `mediaStyles` | array | `[{"width": 60, "backgroundSize": "cover", "background": "", "backgroundOpacity": 1, "border": "", "borderRadius": "", "borderWidth": [0, 0, 0, 0], "padding": [0, 0, 0, 0], "margin": ["", "", "", ""], "ratio": ""}]` |
| `mobileBorderStyle` | array | `[{"top": ["", "", ""], "right": ["", "", ""], "bottom": ["", "", ""], "left": ["", "", ""], "unit": "px"}]` |
| `mobileContainerBorderRadius` | array | `["", "", "", ""]` |
| `mobileContainerPadding` | array | `["", "", "", ""]` |
| `mobileIconBorderRadius` | array | `["", "", "", ""]` |
| `mobileIconBorderStyle` | array | `[{"top": ["", "", ""], "right": ["", "", ""], "bottom": ["", "", ""], "left": ["", "", ""], "unit": "px"}]` |
| `mobileIconMargin` | array | `["", "", "", ""]` |
| `mobileIconPadding` | array | `["", "", "", ""]` |
| `mobileMediaBorderRadius` | array | `["", "", "", ""]` |
| `mobileMediaBorderStyle` | array | `[{"top": ["", "", ""], "right": ["", "", ""], "bottom": ["", "", ""], "left": ["", "", ""], "unit": "px"}]` |
| `mobileMediaMargin` | array | `["", "", "", ""]` |
| `mobileMediaPadding` | array | `["", "", "", ""]` |
| `mobileRatingMargin` | array | `["", "", "", ""]` |
| `mobileRatingPadding` | array | `["", "", "", ""]` |
| `mobileTitleMargin` | array | `["", "", "", ""]` |
| `mobileTitlePadding` | array | `["", "", "", ""]` |
| `mobileWrapperMargin` | array | `["", "", "", ""]` |
| `nameFont` | array | `[{"color": "", "size": ["", "", ""], "sizetype": "px", "lineHeight": ["", "", ""], "linetype": "px", "letterSpacing": "", "textTransform": "", "family": "", "google": "", "style": "", "weight": "", "variant": "", "subset": "", "loadGoogle": true}]` |
| `occupationFont` | array | `[{"color": "", "size": [15, "", ""], "sizetype": "px", "lineHeight": ["", "", ""], "linetype": "px", "letterSpacing": "", "textTransform": "", "family": "", "google": "", "style": "", "weight": "", "variant": "", "subset": "", "loadGoogle": true}]` |
| `ratingMargin` | array | `["", "", "", ""]` |
| `ratingMarginUnit` | string | `"px"` |
| `ratingPadding` | array | `["", "", "", ""]` |
| `ratingPaddingUnit` | string | `"px"` |
| `ratingStyles` | array | `[{"color": "#ffd700", "size": 16, "margin": [10, 0, 10, 0], "iconSpacing": "", "icon": "fas_star", "stroke": 2}]` |
| `responsiveContainerBorderRadius` | array | `["", "", "", ""]` |
| `shadow` | array | `[{"color": "#000000", "opacity": 0.2, "spread": 0, "blur": 14, "hOffset": 4, "vOffset": 2}]` |
| `showPauseButton` | boolean | `false` |
| `showPresets` | boolean | `true` |
| `slidesScroll` | string | `"1"` |
| `style` | string | `"basic"` |
| `tabletBorderStyle` | array | `[{"top": ["", "", ""], "right": ["", "", ""], "bottom": ["", "", ""], "left": ["", "", ""], "unit": "px"}]` |
| `tabletContainerBorderRadius` | array | `["", "", "", ""]` |
| `tabletContainerPadding` | array | `["", "", "", ""]` |
| `tabletIconBorderRadius` | array | `["", "", "", ""]` |
| `tabletIconBorderStyle` | array | `[{"top": ["", "", ""], "right": ["", "", ""], "bottom": ["", "", ""], "left": ["", "", ""], "unit": "px"}]` |
| `tabletIconMargin` | array | `["", "", "", ""]` |
| `tabletIconPadding` | array | `["", "", "", ""]` |
| `tabletMediaBorderRadius` | array | `["", "", "", ""]` |
| `tabletMediaBorderStyle` | array | `[{"top": ["", "", ""], "right": ["", "", ""], "bottom": ["", "", ""], "left": ["", "", ""], "unit": "px"}]` |
| `tabletMediaMargin` | array | `["", "", "", ""]` |
| `tabletMediaPadding` | array | `["", "", "", ""]` |
| `tabletRatingMargin` | array | `["", "", "", ""]` |
| `tabletRatingPadding` | array | `["", "", "", ""]` |
| `tabletTitleMargin` | array | `["", "", "", ""]` |
| `tabletTitlePadding` | array | `["", "", "", ""]` |
| `tabletWrapperMargin` | array | `["", "", "", ""]` |
| `testimonials` | array | `[{"url": "", "id": "", "alt": "", "width": "", "height": "", "maxWidth": "", "subtype": "", "media": "image", "icon": "fas_quote-left", "isize": 50, "istroke": 2, "ititle": "", "color": "", "title": "", "content": "", "name": "", "occupation": "", "rating": 5}]` |
| `titleFont` | array | `[{"color": "", "level": 2, "size": ["", "", ""], "sizetype": "px", "lineHeight": ["", "", ""], "linetype": "px", "letterSpacing": "", "textTransform": "", "family": "", "google": false, "style": "", "weight": "", "variant": "", "subset": "", "loadGoogle": true, "padding": [0, 0, 0, 0], "margin": [0, 0, 15, 0]}]` |
| `titleMargin` | array | `["", "", "", ""]` |
| `titleMarginUnit` | string | `"px"` |
| `titleMinHeight` | array | `["", "", ""]` |
| `titlePadding` | array | `["", "", "", ""]` |
| `titlePaddingUnit` | string | `"px"` |
| `transSpeed` | number | `400` |
| `uniqueID` | string | `""` |
| `useBlockQuoteTags` | boolean | `true` |
| `wrapperMargin` | array | `["", "", "", ""]` |
| `wrapperMarginUnit` | string | `"px"` |
| `wrapperMobilePadding` | array | `["", "", "", ""]` |
| `wrapperPadding` | array | `["", "", "", ""]` |
| `wrapperPaddingType` | string | `"px"` |
| `wrapperTabletPadding` | array | `["", "", "", ""]` |

## kadence/vector

**Vector SVG** · category `kadence-blocks` · apiVersion 3

- Supports: `{"anchor": true, "html": false, "align": ["left", "right"]}`

| Attribute | Type | Default |
|---|---|---|
| `align` | string |  |
| `anchor` | string |  |
| `id` | number |  |
| `margin` | array | `["", "", "", ""]` |
| `marginUnit` | string | `"px"` |
| `maxWidth` | array | `["150", "", ""]` |
| `maxWidthUnit` | string | `"px"` |
| `mobileMargin` | array | `["", "", "", ""]` |
| `mobilePadding` | array | `["", "", "", ""]` |
| `padding` | array | `["", "", "", ""]` |
| `paddingUnit` | string | `"px"` |
| `tabletMargin` | array | `["", "", "", ""]` |
| `tabletPadding` | array | `["", "", "", ""]` |
| `uniqueID` | string |  |

## kadence/videopopup

**Video Popup** · category `kadence-blocks` · apiVersion 3

- Supports: `{"anchor": true, "ktanimate": true, "ktanimateadd": true, "ktanimatepreview": true, "ktanimateswipe": true, "ktdynamic": true, "align": ["wide", "full"], "kbMetadata": true}`

| Attribute | Type | Default |
|---|---|---|
| `anchor` | string |  |
| `ariaLabel` | string |  |
| `autoPlay` | boolean | `true` |
| `background` | array | `[{"color": "", "colorOpacity": 1, "img": "", "imgID": "", "imgAlt": "", "imgWidth": "", "imageHeight": "", "bgSize": "cover", "bgPosition": "center center", "bgAttachment": "scroll", "bgRepeat": "no-repeat"}]` |
| `backgroundOverlay` | array | `[{"type": "solid", "fill": "#000000", "fillOpacity": 1, "secondFill": "", "secondFillOpacity": 1, "gradLoc": 0, "gradLocSecond": 100, "gradType": "linear", "gradAngle": 180, "gradPosition": "center center", "opacity": 0.3, "opacityHover": 0.5, "blendMode": "none"}]` |
| `borderColor` | string |  |
| `borderOpacity` | number |  |
| `borderRadius` | array | `["", "", "", ""]` |
| `borderRadiusUnit` | string | `"px"` |
| `borderStyle` | array | `[{"top": ["rgba(255,255,255,0.8)", "solid", "2"], "right": ["rgba(255,255,255,0.8)", "solid", "2"], "bottom": ["rgba(255,255,255,0.8)", "solid", "2"], "left": ["rgba(255,255,255,0.8)", "solid", "2"], "unit": "px"}]` |
| `borderWidth` | array | `["", "", "", ""]` |
| `displayShadow` | boolean | `false` |
| `inQueryBlock` | boolean | `false` |
| `isVimeoPrivate` | boolean | `false` |
| `margin` | array | `[{"desk": ["", "", "", ""], "tablet": ["", "", "", ""], "mobile": ["", "", "", ""]}]` |
| `marginUnit` | string | `"px"` |
| `maxWidth` | number |  |
| `maxWidthUnit` | string |  |
| `media` | array | `[{"url": "", "id": "", "width": "", "height": "", "alt": "", "subtype": ""}]` |
| `mediaMobile` | array | `[{"url": "", "id": "", "width": "", "height": "", "alt": "", "subtype": ""}]` |
| `mediaPoster` | array | `[{"url": "", "id": "", "width": "", "height": "", "alt": "", "subtype": ""}]` |
| `mediaRatio` | string |  |
| `mediaRatioMobile` | string |  |
| `mediaUseMobile` | boolean | `false` |
| `mobileBorderRadius` | array | `["", "", "", ""]` |
| `mobileBorderStyle` | array | `[{"top": ["", "", ""], "right": ["", "", ""], "bottom": ["", "", ""], "left": ["", "", ""], "unit": "px"}]` |
| `padding` | array | `[{"desk": ["", "", "", ""], "tablet": ["", "", "", ""], "mobile": ["", "", "", ""]}]` |
| `paddingUnit` | string | `"px"` |
| `playBtn` | array | `[{"icon": "", "size": "", "width": 2, "title": "Play", "color": "#ffffff", "opacity": 1, "background": "#000000", "backgroundOpacity": 0.7, "border": "", "borderOpacity": 1, "borderRadius": ["", "", "", ""], "borderWidth": ["", "", "", ""], "padding": "", "style": "default", "animation": "none", "colorHover": "", "opacityHover": 1, "backgroundHover": "", "backgroundOpacityHover": 1, "borderHover": "", "borderOpacityHover": 1}]` |
| `popup` | array | `[{"background": "#000000", "backgroundOpacity": 0.8, "closeBackground": "", "closeColor": "#ffffff", "maxWidth": 900, "maxWidthTablet": "", "maxWidthMobile": "", "maxWidthUnit": "px", "animation": "none"}]` |
| `posterType` | string | `""` |
| `ratio` | string |  |
| `shadow` | array | `[{"color": "#000000", "opacity": 0.2, "spread": 0, "blur": 14, "hOffset": 4, "vOffset": 2}]` |
| `shadowHover` | array | `[{"color": "#000000", "opacity": 0.2, "spread": 0, "blur": 14, "hOffset": 4, "vOffset": 2}]` |
| `tabletBorderRadius` | array | `["", "", "", ""]` |
| `tabletBorderStyle` | array | `[{"top": ["", "", ""], "right": ["", "", ""], "bottom": ["", "", ""], "left": ["", "", ""], "unit": "px"}]` |
| `type` | string | `"iframe"` |
| `uniqueID` | string | `""` |
| `url` | string |  |
| `urlMobile` | string |  |
| `youtubeCookies` | boolean | `true` |
