# Kadence Hero Section Skill

**Activation**: Creating hero sections, welcome sections, above-the-fold content, page headers with Kadence Blocks.

## Hero Section Patterns

### Pattern 1: Centered Hero (Single Column)

Full-width section with centered text and CTA buttons.

```html
<!-- wp:kadence/rowlayout {"uniqueID":"kt-layout-hero001","columns":1,"colLayout":"equal","inheritMaxWidth":true,"align":"full","padding":["xl","md","xl","md"],"tabletPadding":["lg","sm","lg","sm"],"mobilePadding":["md","xs","md","xs"],"bgColor":"palette9","bgColorClass":"theme-palette9"} -->
<div class="wp-block-kadence-rowlayout alignfull kt-row-layout-inner kt-layout-id-hero001">
<div class="kt-row-column-wrap kt-has-1-columns">

<!-- wp:kadence/column {"id":1,"uniqueID":"kt-col-hero001"} -->
<div class="wp-block-kadence-column kadence-column-hero001"><div class="kt-inside-inner-col">

<!-- wp:kadence/advancedheading {"uniqueID":"kt-adv-heading-hero001","align":"center","color":"palette1","htmlTag":"h1","fontSize":["60","48","36"],"lineHeight":["1.1","1.2","1.3"],"fontWeight":"700","margin":["","","20",""]} -->
<h1 class="kt-adv-heading-hero001 wp-block-kadence-advancedheading" data-kb-block="kb-adv-heading-hero001">Your Compelling Headline Goes Here</h1>
<!-- /wp:kadence/advancedheading -->

<!-- wp:kadence/advancedheading {"uniqueID":"kt-adv-heading-hero002","align":"center","color":"palette4","htmlTag":"p","fontSize":["22","20","18"],"lineHeight":["1.6","1.6","1.5"],"maxWidth":800,"margin":["","","30",""]} -->
<p class="kt-adv-heading-hero002 wp-block-kadence-advancedheading" data-kb-block="kb-adv-heading-hero002">Supporting text that explains your value proposition. Keep it concise but compelling enough to encourage action.</p>
<!-- /wp:kadence/advancedheading -->

<!-- wp:kadence/advancedbtn {"uniqueID":"kt-btn-hero001","hAlign":"center","gap":[16,16,12]} -->
<div class="wp-block-kadence-advancedbtn kt-btn-wrap-hero001">
<!-- wp:kadence/singlebtn {"uniqueID":"kt-btn-hero001a","text":"Get Started","sizePreset":"large","color":"palette9","background":"palette1","borderRadius":[4,4,4,4]} -->
<div class="wp-block-kadence-singlebtn kt-btn-wrap-hero001a"><a class="kt-button button kt-btn-hero001a-action kt-btn-size-large kt-btn-style-basic" href="#">Get Started</a></div>
<!-- /wp:kadence/singlebtn -->
<!-- wp:kadence/singlebtn {"uniqueID":"kt-btn-hero001b","text":"Learn More","sizePreset":"large","style":"outline","color":"palette1","borderColor":"palette1","borderRadius":[4,4,4,4]} -->
<div class="wp-block-kadence-singlebtn kt-btn-wrap-hero001b"><a class="kt-button button kt-btn-hero001b-action kt-btn-size-large kt-btn-style-outline" href="#">Learn More</a></div>
<!-- /wp:kadence/singlebtn -->
</div>
<!-- /wp:kadence/advancedbtn -->

</div></div>
<!-- /wp:kadence/column -->

</div>
</div>
<!-- /wp:kadence/rowlayout -->
```

### Pattern 2: Split Hero (Text + Image)

Two-column layout with text on one side, image on the other.

```html
<!-- wp:kadence/rowlayout {"uniqueID":"kt-layout-hero002","columns":2,"colLayout":"equal","inheritMaxWidth":true,"align":"full","padding":["xl","lg","xl","lg"],"tabletPadding":["lg","md","lg","md"],"mobilePadding":["md","sm","md","sm"],"columnGutter":"wider","mobileLayout":"row","verticalAlignment":"middle"} -->
<div class="wp-block-kadence-rowlayout alignfull kt-row-layout-inner kt-layout-id-hero002">
<div class="kt-row-column-wrap kt-has-2-columns kt-gutter-wider kt-v-gutter-default kt-row-valign-middle">

<!-- wp:kadence/column {"id":1,"uniqueID":"kt-col-hero002a"} -->
<div class="wp-block-kadence-column kadence-column-hero002a"><div class="kt-inside-inner-col">

<!-- wp:kadence/advancedheading {"uniqueID":"kt-adv-heading-hero003","color":"palette3","htmlTag":"h1","fontSize":["52","42","32"],"lineHeight":["1.15","1.2","1.25"],"fontWeight":"700","margin":["","","16",""]} -->
<h1 class="kt-adv-heading-hero003 wp-block-kadence-advancedheading" data-kb-block="kb-adv-heading-hero003">Build Something Amazing Today</h1>
<!-- /wp:kadence/advancedheading -->

<!-- wp:kadence/advancedheading {"uniqueID":"kt-adv-heading-hero004","color":"palette4","htmlTag":"p","fontSize":["20","18","16"],"lineHeight":["1.6","1.6","1.5"],"margin":["","","24",""]} -->
<p class="kt-adv-heading-hero004 wp-block-kadence-advancedheading" data-kb-block="kb-adv-heading-hero004">A clear description of what you offer and why visitors should care. Focus on benefits, not just features.</p>
<!-- /wp:kadence/advancedheading -->

<!-- wp:kadence/advancedbtn {"uniqueID":"kt-btn-hero002","hAlign":"left","gap":[12,12,10]} -->
<div class="wp-block-kadence-advancedbtn kt-btn-wrap-hero002">
<!-- wp:kadence/singlebtn {"uniqueID":"kt-btn-hero002a","text":"Start Free Trial","sizePreset":"large","color":"palette9","background":"palette1","borderRadius":[6,6,6,6]} -->
<div class="wp-block-kadence-singlebtn kt-btn-wrap-hero002a"><a class="kt-button button kt-btn-hero002a-action kt-btn-size-large kt-btn-style-basic" href="#">Start Free Trial</a></div>
<!-- /wp:kadence/singlebtn -->
</div>
<!-- /wp:kadence/advancedbtn -->

<!-- wp:kadence/iconlist {"uniqueID":"kt-iconlist-hero001","items":[{"icon":"fe_checkCircle","link":"","target":"_self","size":20,"width":2,"text":"No credit card required","color":"palette2","background":"","border":"","borderRadius":0,"padding":5,"borderWidth":1,"style":"default","level":0},{"icon":"fe_checkCircle","link":"","target":"_self","size":20,"width":2,"text":"14-day free trial","color":"palette2","background":"","border":"","borderRadius":0,"padding":5,"borderWidth":1,"style":"default","level":0},{"icon":"fe_checkCircle","link":"","target":"_self","size":20,"width":2,"text":"Cancel anytime","color":"palette2","background":"","border":"","borderRadius":0,"padding":5,"borderWidth":1,"style":"default","level":0}],"listCount":3,"listGap":8,"listStyles":[{"size":["16","",""],"sizeType":"px","lineHeight":["","",""],"lineType":"px","letterSpacing":"","family":"","google":false,"style":"","weight":"","variant":"","subset":"","loadGoogle":true,"color":"palette4","textTransform":""}],"margin":["24","","",""]} -->
<ul class="wp-block-kadence-iconlist kt-svg-icon-list-items kt-svg-icon-list-items-hero001 kt-svg-icon-list-columns-1"><li class="wp-block-kadence-listitem kt-svg-icon-list-item-wrap kt-svg-icon-list-item-0 kt-svg-icon-list-level-0"><span class="kt-svg-icon-list-single kt-svg-icon-fe_checkCircle"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" xmlns="http://www.w3.org/2000/svg" aria-hidden="true"><path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"></path><polyline points="22 4 12 14.01 9 11.01"></polyline></svg></span><span class="kt-svg-icon-list-text">No credit card required</span></li><li class="wp-block-kadence-listitem kt-svg-icon-list-item-wrap kt-svg-icon-list-item-1 kt-svg-icon-list-level-0"><span class="kt-svg-icon-list-single kt-svg-icon-fe_checkCircle"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" xmlns="http://www.w3.org/2000/svg" aria-hidden="true"><path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"></path><polyline points="22 4 12 14.01 9 11.01"></polyline></svg></span><span class="kt-svg-icon-list-text">14-day free trial</span></li><li class="wp-block-kadence-listitem kt-svg-icon-list-item-wrap kt-svg-icon-list-item-2 kt-svg-icon-list-level-0"><span class="kt-svg-icon-list-single kt-svg-icon-fe_checkCircle"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" xmlns="http://www.w3.org/2000/svg" aria-hidden="true"><path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"></path><polyline points="22 4 12 14.01 9 11.01"></polyline></svg></span><span class="kt-svg-icon-list-text">Cancel anytime</span></li></ul>
<!-- /wp:kadence/iconlist -->

</div></div>
<!-- /wp:kadence/column -->

<!-- wp:kadence/column {"id":2,"uniqueID":"kt-col-hero002b"} -->
<div class="wp-block-kadence-column kadence-column-hero002b"><div class="kt-inside-inner-col">

<!-- wp:kadence/image {"uniqueID":"kt-image-hero001","imgMaxWidth":600,"borderRadius":[12,12,12,12],"boxShadow":[true,"#000000",0.12,0,20,40,0,false]} -->
<figure class="wp-block-kadence-image kb-image-hero001"><img src="https://placehold.co/600x450/e2e8f0/64748b?text=Hero+Image" alt="Hero image" class="kb-img wp-image-"/></figure>
<!-- /wp:kadence/image -->

</div></div>
<!-- /wp:kadence/column -->

</div>
</div>
<!-- /wp:kadence/rowlayout -->
```

### Pattern 3: Hero with Background Image

Full-width hero with background image and overlay.

```html
<!-- wp:kadence/rowlayout {"uniqueID":"kt-layout-hero003","columns":1,"colLayout":"equal","inheritMaxWidth":true,"align":"full","padding":["xxl","lg","xxl","lg"],"tabletPadding":["xl","md","xl","md"],"mobilePadding":["lg","sm","lg","sm"],"minHeight":500,"bgImg":"https://placehold.co/1920x800/1a1a2e/1a1a2e","bgImgSize":"cover","bgImgPosition":"center center","overlay":"#000000","overlayOpacity":0.6} -->
<div class="wp-block-kadence-rowlayout alignfull kt-row-layout-inner kt-layout-id-hero003">
<div class="kt-row-column-wrap kt-has-1-columns">

<!-- wp:kadence/column {"id":1,"uniqueID":"kt-col-hero003"} -->
<div class="wp-block-kadence-column kadence-column-hero003"><div class="kt-inside-inner-col">

<!-- wp:kadence/advancedheading {"uniqueID":"kt-adv-heading-hero005","align":"center","color":"#ffffff","htmlTag":"h1","fontSize":["56","44","34"],"lineHeight":["1.15","1.2","1.25"],"fontWeight":"700","margin":["","","16",""],"textShadow":[{"enable":true,"color":"rgba(0,0,0,0.3)","hOffset":0,"vOffset":2,"blur":8}]} -->
<h1 class="kt-adv-heading-hero005 wp-block-kadence-advancedheading" data-kb-block="kb-adv-heading-hero005">Transform Your Business</h1>
<!-- /wp:kadence/advancedheading -->

<!-- wp:kadence/advancedheading {"uniqueID":"kt-adv-heading-hero006","align":"center","color":"rgba(255,255,255,0.9)","htmlTag":"p","fontSize":["22","20","18"],"lineHeight":["1.6","1.6","1.5"],"maxWidth":700,"margin":["","","32",""]} -->
<p class="kt-adv-heading-hero006 wp-block-kadence-advancedheading" data-kb-block="kb-adv-heading-hero006">Discover the tools and strategies that will help you achieve your goals faster than ever before.</p>
<!-- /wp:kadence/advancedheading -->

<!-- wp:kadence/advancedbtn {"uniqueID":"kt-btn-hero003","hAlign":"center","gap":[16,16,12]} -->
<div class="wp-block-kadence-advancedbtn kt-btn-wrap-hero003">
<!-- wp:kadence/singlebtn {"uniqueID":"kt-btn-hero003a","text":"Get Started Now","sizePreset":"large","color":"#1a1a2e","background":"#ffffff","backgroundHover":"#f1f5f9","borderRadius":[6,6,6,6]} -->
<div class="wp-block-kadence-singlebtn kt-btn-wrap-hero003a"><a class="kt-button button kt-btn-hero003a-action kt-btn-size-large kt-btn-style-basic" href="#">Get Started Now</a></div>
<!-- /wp:kadence/singlebtn -->
<!-- wp:kadence/singlebtn {"uniqueID":"kt-btn-hero003b","text":"Watch Demo","sizePreset":"large","style":"outline","color":"#ffffff","borderColor":"#ffffff","borderRadius":[6,6,6,6],"icon":"fe_playCircle","iconSide":"left"} -->
<div class="wp-block-kadence-singlebtn kt-btn-wrap-hero003b"><a class="kt-button button kt-btn-hero003b-action kt-btn-size-large kt-btn-style-outline kt-btn-has-icon kt-btn-icon-side-left" href="#"><span class="kt-btn-icon kt-btn-svg-icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" xmlns="http://www.w3.org/2000/svg"><circle cx="12" cy="12" r="10"></circle><polygon points="10 8 16 12 10 16 10 8"></polygon></svg></span>Watch Demo</a></div>
<!-- /wp:kadence/singlebtn -->
</div>
<!-- /wp:kadence/advancedbtn -->

</div></div>
<!-- /wp:kadence/column -->

</div>
</div>
<!-- /wp:kadence/rowlayout -->
```

### Pattern 4: Video Hero

Hero with embedded video background.

```html
<!-- wp:kadence/rowlayout {"uniqueID":"kt-layout-hero004","columns":1,"colLayout":"equal","inheritMaxWidth":true,"align":"full","padding":["xxl","lg","xxl","lg"],"minHeight":600,"backgroundSettingTab":"video","backgroundVideo":[{"youTube":"","local":"","localID":"","popup":false,"ratio":"16/9","btns":true,"mute":true,"loop":true}],"overlay":"#000000","overlayOpacity":0.5} -->
<div class="wp-block-kadence-rowlayout alignfull kt-row-layout-inner kt-layout-id-hero004">
<div class="kt-row-column-wrap kt-has-1-columns">

<!-- wp:kadence/column {"id":1,"uniqueID":"kt-col-hero004"} -->
<div class="wp-block-kadence-column kadence-column-hero004"><div class="kt-inside-inner-col">

<!-- wp:kadence/advancedheading {"uniqueID":"kt-adv-heading-hero007","align":"center","color":"#ffffff","htmlTag":"h1","fontSize":["64","50","38"],"lineHeight":["1.1","1.15","1.2"],"fontWeight":"800","letterSpacing":-1} -->
<h1 class="kt-adv-heading-hero007 wp-block-kadence-advancedheading" data-kb-block="kb-adv-heading-hero007">Experience Excellence</h1>
<!-- /wp:kadence/advancedheading -->

<!-- wp:kadence/advancedheading {"uniqueID":"kt-adv-heading-hero008","align":"center","color":"rgba(255,255,255,0.85)","htmlTag":"p","fontSize":["24","22","18"],"lineHeight":["1.5","1.5","1.5"],"maxWidth":650,"margin":["20","","40",""]} -->
<p class="kt-adv-heading-hero008 wp-block-kadence-advancedheading" data-kb-block="kb-adv-heading-hero008">Where innovation meets execution. Join thousands who have transformed their workflow.</p>
<!-- /wp:kadence/advancedheading -->

<!-- wp:kadence/advancedbtn {"uniqueID":"kt-btn-hero004","hAlign":"center"} -->
<div class="wp-block-kadence-advancedbtn kt-btn-wrap-hero004">
<!-- wp:kadence/singlebtn {"uniqueID":"kt-btn-hero004a","text":"Start Your Journey","sizePreset":"large","color":"palette9","background":"palette1","borderRadius":[50,50,50,50],"padding":["18","40","18","40"]} -->
<div class="wp-block-kadence-singlebtn kt-btn-wrap-hero004a"><a class="kt-button button kt-btn-hero004a-action kt-btn-size-large kt-btn-style-basic" href="#">Start Your Journey</a></div>
<!-- /wp:kadence/singlebtn -->
</div>
<!-- /wp:kadence/advancedbtn -->

</div></div>
<!-- /wp:kadence/column -->

</div>
</div>
<!-- /wp:kadence/rowlayout -->
```

## Customization Parameters

### Key Attributes to Modify

| Attribute | Location | Purpose |
|-----------|----------|---------|
| `padding` | rowlayout | Section spacing |
| `bgColor` | rowlayout | Background color |
| `bgImg` | rowlayout | Background image URL |
| `overlay` | rowlayout | Overlay color |
| `overlayOpacity` | rowlayout | Overlay transparency (0-1) |
| `minHeight` | rowlayout | Minimum section height |
| `fontSize` | advancedheading | Text size [desktop, tablet, mobile] |
| `color` | advancedheading | Text color |
| `maxWidth` | advancedheading | Max width for text container |

### Common Modifications

**Dark Mode Hero:**
```json
"bgColor": "palette3"  // Dark background
"color": "#ffffff"     // Light text
```

**Light Mode Hero:**
```json
"bgColor": "palette9"  // Light background
"color": "palette3"    // Dark text
```

**Gradient Background:**
```json
"gradient": "linear-gradient(135deg, palette1 0%, palette2 100%)"
```

## Best Practices

1. **Responsive Design**: Always set tablet and mobile values
2. **Contrast**: Ensure text is readable against backgrounds
3. **CTA Prominence**: Primary button should stand out
4. **Whitespace**: Use generous padding for hero sections
5. **Image Optimization**: Use appropriate image sizes
6. **Loading Speed**: Consider lazy loading for background images
