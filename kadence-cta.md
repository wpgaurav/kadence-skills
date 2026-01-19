# Kadence CTA Section Skill

**Activation**: Creating call-to-action sections, conversion blocks, sign-up prompts, download banners with Kadence Blocks.

## CTA Section Patterns

### Pattern 1: Simple Centered CTA

Clean, focused call-to-action with headline and button.

```html
<!-- wp:kadence/rowlayout {"uniqueID":"kt-layout-cta001","columns":1,"colLayout":"equal","inheritMaxWidth":true,"align":"full","padding":["xl","lg","xl","lg"],"tabletPadding":["lg","md","lg","md"],"mobilePadding":["md","sm","md","sm"],"bgColor":"palette1"} -->
<div class="wp-block-kadence-rowlayout alignfull kt-row-layout-inner kt-layout-id-cta001">
<div class="kt-row-column-wrap kt-has-1-columns">

<!-- wp:kadence/column {"id":1,"uniqueID":"kt-col-cta001"} -->
<div class="wp-block-kadence-column kadence-column-cta001"><div class="kt-inside-inner-col">

<!-- wp:kadence/advancedheading {"uniqueID":"kt-adv-heading-cta001","align":"center","color":"#ffffff","htmlTag":"h2","fontSize":["36","32","26"],"lineHeight":["1.25","1.3","1.35"],"fontWeight":"700","margin":["","","16",""]} -->
<h2 class="kt-adv-heading-cta001 wp-block-kadence-advancedheading" data-kb-block="kb-adv-heading-cta001">Ready to Get Started?</h2>
<!-- /wp:kadence/advancedheading -->

<!-- wp:kadence/advancedheading {"uniqueID":"kt-adv-heading-cta002","align":"center","color":"rgba(255,255,255,0.9)","htmlTag":"p","fontSize":["18","17","16"],"lineHeight":["1.6","1.6","1.5"],"maxWidth":600,"margin":["","","28",""]} -->
<p class="kt-adv-heading-cta002 wp-block-kadence-advancedheading" data-kb-block="kb-adv-heading-cta002">Join thousands of satisfied customers and transform your workflow today.</p>
<!-- /wp:kadence/advancedheading -->

<!-- wp:kadence/advancedbtn {"uniqueID":"kt-btn-cta001","hAlign":"center"} -->
<div class="wp-block-kadence-advancedbtn kt-btn-wrap-cta001">
<!-- wp:kadence/singlebtn {"uniqueID":"kt-btn-cta001a","text":"Start Free Trial","sizePreset":"large","color":"palette1","background":"#ffffff","backgroundHover":"#f1f5f9","borderRadius":[6,6,6,6],"padding":["16","32","16","32"]} -->
<div class="wp-block-kadence-singlebtn kt-btn-wrap-cta001a"><a class="kt-button button kt-btn-cta001a-action kt-btn-size-large kt-btn-style-basic" href="#">Start Free Trial</a></div>
<!-- /wp:kadence/singlebtn -->
</div>
<!-- /wp:kadence/advancedbtn -->

</div></div>
<!-- /wp:kadence/column -->

</div>
</div>
<!-- /wp:kadence/rowlayout -->
```

### Pattern 2: Split CTA with Image

Two-column CTA with visual element.

```html
<!-- wp:kadence/rowlayout {"uniqueID":"kt-layout-cta002","columns":2,"colLayout":"left-golden","inheritMaxWidth":true,"align":"full","padding":["xl","lg","xl","lg"],"tabletPadding":["lg","md","lg","md"],"mobilePadding":["md","sm","md","sm"],"bgColor":"palette3","columnGutter":"wider","verticalAlignment":"middle"} -->
<div class="wp-block-kadence-rowlayout alignfull kt-row-layout-inner kt-layout-id-cta002">
<div class="kt-row-column-wrap kt-has-2-columns kt-gutter-wider kt-v-gutter-default kt-row-valign-middle">

<!-- wp:kadence/column {"id":1,"uniqueID":"kt-col-cta002a"} -->
<div class="wp-block-kadence-column kadence-column-cta002a"><div class="kt-inside-inner-col">

<!-- wp:kadence/advancedheading {"uniqueID":"kt-adv-heading-cta003","color":"#ffffff","htmlTag":"h2","fontSize":["40","34","28"],"lineHeight":["1.2","1.25","1.3"],"fontWeight":"700","margin":["","","16",""]} -->
<h2 class="kt-adv-heading-cta003 wp-block-kadence-advancedheading" data-kb-block="kb-adv-heading-cta003">Take Your Business to the Next Level</h2>
<!-- /wp:kadence/advancedheading -->

<!-- wp:kadence/advancedheading {"uniqueID":"kt-adv-heading-cta004","color":"rgba(255,255,255,0.85)","htmlTag":"p","fontSize":["18","17","16"],"lineHeight":["1.6","1.6","1.5"],"margin":["","","24",""]} -->
<p class="kt-adv-heading-cta004 wp-block-kadence-advancedheading" data-kb-block="kb-adv-heading-cta004">Get access to premium features and dedicated support. No commitment, cancel anytime.</p>
<!-- /wp:kadence/advancedheading -->

<!-- wp:kadence/advancedbtn {"uniqueID":"kt-btn-cta002","hAlign":"left","gap":[12,12,10]} -->
<div class="wp-block-kadence-advancedbtn kt-btn-wrap-cta002">
<!-- wp:kadence/singlebtn {"uniqueID":"kt-btn-cta002a","text":"Get Started Free","sizePreset":"large","color":"palette3","background":"#ffffff","backgroundHover":"#f8fafc","borderRadius":[6,6,6,6]} -->
<div class="wp-block-kadence-singlebtn kt-btn-wrap-cta002a"><a class="kt-button button kt-btn-cta002a-action kt-btn-size-large kt-btn-style-basic" href="#">Get Started Free</a></div>
<!-- /wp:kadence/singlebtn -->
<!-- wp:kadence/singlebtn {"uniqueID":"kt-btn-cta002b","text":"Talk to Sales","sizePreset":"large","style":"outline","color":"#ffffff","borderColor":"rgba(255,255,255,0.5)","colorHover":"#ffffff","borderHover":"#ffffff","borderRadius":[6,6,6,6]} -->
<div class="wp-block-kadence-singlebtn kt-btn-wrap-cta002b"><a class="kt-button button kt-btn-cta002b-action kt-btn-size-large kt-btn-style-outline" href="#">Talk to Sales</a></div>
<!-- /wp:kadence/singlebtn -->
</div>
<!-- /wp:kadence/advancedbtn -->

</div></div>
<!-- /wp:kadence/column -->

<!-- wp:kadence/column {"id":2,"uniqueID":"kt-col-cta002b"} -->
<div class="wp-block-kadence-column kadence-column-cta002b"><div class="kt-inside-inner-col">

<!-- wp:kadence/image {"uniqueID":"kt-image-cta001","borderRadius":[12,12,12,12],"boxShadow":[true,"#000000",0.2,0,20,40,0,false]} -->
<figure class="wp-block-kadence-image kb-image-cta001"><img src="https://placehold.co/480x360/e2e8f0/64748b?text=CTA+Image" alt="CTA visual" class="kb-img wp-image-"/></figure>
<!-- /wp:kadence/image -->

</div></div>
<!-- /wp:kadence/column -->

</div>
</div>
<!-- /wp:kadence/rowlayout -->
```

### Pattern 3: Gradient CTA Banner

Eye-catching gradient background CTA.

```html
<!-- wp:kadence/rowlayout {"uniqueID":"kt-layout-cta003","columns":1,"colLayout":"equal","inheritMaxWidth":true,"align":"full","padding":["xxl","lg","xxl","lg"],"tabletPadding":["xl","md","xl","md"],"mobilePadding":["lg","sm","lg","sm"],"gradient":"linear-gradient(135deg, palette1 0%, palette2 100%)"} -->
<div class="wp-block-kadence-rowlayout alignfull kt-row-layout-inner kt-layout-id-cta003">
<div class="kt-row-column-wrap kt-has-1-columns">

<!-- wp:kadence/column {"id":1,"uniqueID":"kt-col-cta003"} -->
<div class="wp-block-kadence-column kadence-column-cta003"><div class="kt-inside-inner-col">

<!-- wp:kadence/advancedheading {"uniqueID":"kt-adv-heading-cta005","align":"center","color":"#ffffff","htmlTag":"h2","fontSize":["44","36","28"],"lineHeight":["1.2","1.25","1.3"],"fontWeight":"700","margin":["","","20",""]} -->
<h2 class="kt-adv-heading-cta005 wp-block-kadence-advancedheading" data-kb-block="kb-adv-heading-cta005">Start Building Amazing Things</h2>
<!-- /wp:kadence/advancedheading -->

<!-- wp:kadence/advancedheading {"uniqueID":"kt-adv-heading-cta006","align":"center","color":"rgba(255,255,255,0.9)","htmlTag":"p","fontSize":["20","18","16"],"lineHeight":["1.6","1.6","1.5"],"maxWidth":650,"margin":["","","32",""]} -->
<p class="kt-adv-heading-cta006 wp-block-kadence-advancedheading" data-kb-block="kb-adv-heading-cta006">Everything you need to succeed is just one click away. No credit card required to start.</p>
<!-- /wp:kadence/advancedheading -->

<!-- wp:kadence/advancedbtn {"uniqueID":"kt-btn-cta003","hAlign":"center","gap":[16,16,12]} -->
<div class="wp-block-kadence-advancedbtn kt-btn-wrap-cta003">
<!-- wp:kadence/singlebtn {"uniqueID":"kt-btn-cta003a","text":"Create Free Account","sizePreset":"large","color":"palette1","background":"#ffffff","backgroundHover":"#f8fafc","borderRadius":[50,50,50,50],"padding":["18","36","18","36"],"boxShadow":[true,"#000000",0.15,0,8,20,0,false]} -->
<div class="wp-block-kadence-singlebtn kt-btn-wrap-cta003a"><a class="kt-button button kt-btn-cta003a-action kt-btn-size-large kt-btn-style-basic" href="#">Create Free Account</a></div>
<!-- /wp:kadence/singlebtn -->
</div>
<!-- /wp:kadence/advancedbtn -->

<!-- wp:kadence/advancedheading {"uniqueID":"kt-adv-heading-cta007","align":"center","color":"rgba(255,255,255,0.7)","htmlTag":"p","fontSize":["14","14","13"],"margin":["20","","",""]} -->
<p class="kt-adv-heading-cta007 wp-block-kadence-advancedheading" data-kb-block="kb-adv-heading-cta007">Free 14-day trial • No credit card needed • Cancel anytime</p>
<!-- /wp:kadence/advancedheading -->

</div></div>
<!-- /wp:kadence/column -->

</div>
</div>
<!-- /wp:kadence/rowlayout -->
```

### Pattern 4: Newsletter Signup CTA

Email capture focused CTA with inline form styling.

```html
<!-- wp:kadence/rowlayout {"uniqueID":"kt-layout-cta004","columns":1,"colLayout":"equal","inheritMaxWidth":true,"align":"full","padding":["lg","lg","lg","lg"],"tabletPadding":["md","md","md","md"],"mobilePadding":["sm","sm","sm","sm"],"bgColor":"palette8","borderRadius":[16,16,16,16],"maxWidth":900,"margin":["xl","auto","xl","auto"]} -->
<div class="wp-block-kadence-rowlayout kt-row-layout-inner kt-layout-id-cta004">
<div class="kt-row-column-wrap kt-has-1-columns">

<!-- wp:kadence/column {"id":1,"uniqueID":"kt-col-cta004"} -->
<div class="wp-block-kadence-column kadence-column-cta004"><div class="kt-inside-inner-col">

<!-- wp:kadence/rowlayout {"uniqueID":"kt-layout-cta004a","columns":2,"colLayout":"left-golden","verticalAlignment":"middle","columnGutter":"default"} -->
<div class="wp-block-kadence-rowlayout kt-row-layout-inner kt-layout-id-cta004a">
<div class="kt-row-column-wrap kt-has-2-columns kt-gutter-default kt-row-valign-middle">

<!-- wp:kadence/column {"id":1,"uniqueID":"kt-col-cta004a"} -->
<div class="wp-block-kadence-column kadence-column-cta004a"><div class="kt-inside-inner-col">

<!-- wp:kadence/advancedheading {"uniqueID":"kt-adv-heading-cta008","color":"palette3","htmlTag":"h3","fontSize":["24","22","20"],"fontWeight":"700","margin":["","","8",""]} -->
<h3 class="kt-adv-heading-cta008 wp-block-kadence-advancedheading" data-kb-block="kb-adv-heading-cta008">Stay in the Loop</h3>
<!-- /wp:kadence/advancedheading -->

<!-- wp:kadence/advancedheading {"uniqueID":"kt-adv-heading-cta009","color":"palette4","htmlTag":"p","fontSize":["16","15","14"],"lineHeight":["1.5","1.5","1.5"]} -->
<p class="kt-adv-heading-cta009 wp-block-kadence-advancedheading" data-kb-block="kb-adv-heading-cta009">Get weekly tips, insights, and exclusive content delivered to your inbox.</p>
<!-- /wp:kadence/advancedheading -->

</div></div>
<!-- /wp:kadence/column -->

<!-- wp:kadence/column {"id":2,"uniqueID":"kt-col-cta004b"} -->
<div class="wp-block-kadence-column kadence-column-cta004b"><div class="kt-inside-inner-col">

<!-- wp:kadence/advancedbtn {"uniqueID":"kt-btn-cta004","hAlign":"right","thAlign":"left","mhAlign":"center"} -->
<div class="wp-block-kadence-advancedbtn kt-btn-wrap-cta004">
<!-- wp:kadence/singlebtn {"uniqueID":"kt-btn-cta004a","text":"Subscribe Now","sizePreset":"medium","color":"#ffffff","background":"palette1","backgroundHover":"palette2","borderRadius":[6,6,6,6],"icon":"fe_mail","iconSide":"left"} -->
<div class="wp-block-kadence-singlebtn kt-btn-wrap-cta004a"><a class="kt-button button kt-btn-cta004a-action kt-btn-size-medium kt-btn-style-basic kt-btn-has-icon kt-btn-icon-side-left" href="#"><span class="kt-btn-icon kt-btn-svg-icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"></path><polyline points="22,6 12,13 2,6"></polyline></svg></span>Subscribe Now</a></div>
<!-- /wp:kadence/singlebtn -->
</div>
<!-- /wp:kadence/advancedbtn -->

</div></div>
<!-- /wp:kadence/column -->

</div>
</div>
<!-- /wp:kadence/rowlayout -->

</div></div>
<!-- /wp:kadence/column -->

</div>
</div>
<!-- /wp:kadence/rowlayout -->
```

### Pattern 5: Stats + CTA Combo

CTA with social proof numbers.

```html
<!-- wp:kadence/rowlayout {"uniqueID":"kt-layout-cta005","columns":1,"colLayout":"equal","inheritMaxWidth":true,"align":"full","padding":["xl","lg","xl","lg"],"bgColor":"palette9"} -->
<div class="wp-block-kadence-rowlayout alignfull kt-row-layout-inner kt-layout-id-cta005">
<div class="kt-row-column-wrap kt-has-1-columns">

<!-- wp:kadence/column {"id":1,"uniqueID":"kt-col-cta005"} -->
<div class="wp-block-kadence-column kadence-column-cta005"><div class="kt-inside-inner-col">

<!-- wp:kadence/advancedheading {"uniqueID":"kt-adv-heading-cta010","align":"center","color":"palette3","htmlTag":"h2","fontSize":["38","32","26"],"lineHeight":["1.25","1.3","1.35"],"fontWeight":"700","margin":["","","16",""]} -->
<h2 class="kt-adv-heading-cta010 wp-block-kadence-advancedheading" data-kb-block="kb-adv-heading-cta010">Trusted by Industry Leaders</h2>
<!-- /wp:kadence/advancedheading -->

<!-- wp:kadence/advancedheading {"uniqueID":"kt-adv-heading-cta011","align":"center","color":"palette4","htmlTag":"p","fontSize":["18","17","16"],"lineHeight":["1.6","1.6","1.5"],"maxWidth":600,"margin":["","","40",""]} -->
<p class="kt-adv-heading-cta011 wp-block-kadence-advancedheading" data-kb-block="kb-adv-heading-cta011">Join the companies that are already seeing incredible results.</p>
<!-- /wp:kadence/advancedheading -->

</div></div>
<!-- /wp:kadence/column -->

</div>
</div>
<!-- /wp:kadence/rowlayout -->

<!-- Stats Row -->
<!-- wp:kadence/rowlayout {"uniqueID":"kt-layout-cta006","columns":4,"colLayout":"equal","inheritMaxWidth":true,"align":"full","padding":["","lg","lg","lg"],"tabletPadding":["","md","md","md"],"bgColor":"palette9","tabletLayout":"two-equal","mobileLayout":"row"} -->
<div class="wp-block-kadence-rowlayout alignfull kt-row-layout-inner kt-layout-id-cta006">
<div class="kt-row-column-wrap kt-has-4-columns">

<!-- wp:kadence/column {"id":1,"uniqueID":"kt-col-cta006a","textAlign":"center"} -->
<div class="wp-block-kadence-column kadence-column-cta006a has-text-align-center"><div class="kt-inside-inner-col">
<!-- wp:kadence/advancedheading {"uniqueID":"kt-adv-heading-cta012","align":"center","color":"palette1","htmlTag":"p","fontSize":["48","40","32"],"fontWeight":"700","margin":["","","4",""]} -->
<p class="kt-adv-heading-cta012 wp-block-kadence-advancedheading" data-kb-block="kb-adv-heading-cta012">10K+</p>
<!-- /wp:kadence/advancedheading -->
<!-- wp:kadence/advancedheading {"uniqueID":"kt-adv-heading-cta013","align":"center","color":"palette4","htmlTag":"p","fontSize":["15","14","14"]} -->
<p class="kt-adv-heading-cta013 wp-block-kadence-advancedheading" data-kb-block="kb-adv-heading-cta013">Active Users</p>
<!-- /wp:kadence/advancedheading -->
</div></div>
<!-- /wp:kadence/column -->

<!-- wp:kadence/column {"id":2,"uniqueID":"kt-col-cta006b","textAlign":"center"} -->
<div class="wp-block-kadence-column kadence-column-cta006b has-text-align-center"><div class="kt-inside-inner-col">
<!-- wp:kadence/advancedheading {"uniqueID":"kt-adv-heading-cta014","align":"center","color":"palette1","htmlTag":"p","fontSize":["48","40","32"],"fontWeight":"700","margin":["","","4",""]} -->
<p class="kt-adv-heading-cta014 wp-block-kadence-advancedheading" data-kb-block="kb-adv-heading-cta014">99%</p>
<!-- /wp:kadence/advancedheading -->
<!-- wp:kadence/advancedheading {"uniqueID":"kt-adv-heading-cta015","align":"center","color":"palette4","htmlTag":"p","fontSize":["15","14","14"]} -->
<p class="kt-adv-heading-cta015 wp-block-kadence-advancedheading" data-kb-block="kb-adv-heading-cta015">Satisfaction</p>
<!-- /wp:kadence/advancedheading -->
</div></div>
<!-- /wp:kadence/column -->

<!-- wp:kadence/column {"id":3,"uniqueID":"kt-col-cta006c","textAlign":"center"} -->
<div class="wp-block-kadence-column kadence-column-cta006c has-text-align-center"><div class="kt-inside-inner-col">
<!-- wp:kadence/advancedheading {"uniqueID":"kt-adv-heading-cta016","align":"center","color":"palette1","htmlTag":"p","fontSize":["48","40","32"],"fontWeight":"700","margin":["","","4",""]} -->
<p class="kt-adv-heading-cta016 wp-block-kadence-advancedheading" data-kb-block="kb-adv-heading-cta016">50M+</p>
<!-- /wp:kadence/advancedheading -->
<!-- wp:kadence/advancedheading {"uniqueID":"kt-adv-heading-cta017","align":"center","color":"palette4","htmlTag":"p","fontSize":["15","14","14"]} -->
<p class="kt-adv-heading-cta017 wp-block-kadence-advancedheading" data-kb-block="kb-adv-heading-cta017">Tasks Completed</p>
<!-- /wp:kadence/advancedheading -->
</div></div>
<!-- /wp:kadence/column -->

<!-- wp:kadence/column {"id":4,"uniqueID":"kt-col-cta006d","textAlign":"center"} -->
<div class="wp-block-kadence-column kadence-column-cta006d has-text-align-center"><div class="kt-inside-inner-col">
<!-- wp:kadence/advancedheading {"uniqueID":"kt-adv-heading-cta018","align":"center","color":"palette1","htmlTag":"p","fontSize":["48","40","32"],"fontWeight":"700","margin":["","","4",""]} -->
<p class="kt-adv-heading-cta018 wp-block-kadence-advancedheading" data-kb-block="kb-adv-heading-cta018">24/7</p>
<!-- /wp:kadence/advancedheading -->
<!-- wp:kadence/advancedheading {"uniqueID":"kt-adv-heading-cta019","align":"center","color":"palette4","htmlTag":"p","fontSize":["15","14","14"]} -->
<p class="kt-adv-heading-cta019 wp-block-kadence-advancedheading" data-kb-block="kb-adv-heading-cta019">Support</p>
<!-- /wp:kadence/advancedheading -->
</div></div>
<!-- /wp:kadence/column -->

</div>
</div>
<!-- /wp:kadence/rowlayout -->

<!-- CTA Button Row -->
<!-- wp:kadence/rowlayout {"uniqueID":"kt-layout-cta007","columns":1,"colLayout":"equal","inheritMaxWidth":true,"align":"full","padding":["lg","lg","xl","lg"],"bgColor":"palette9"} -->
<div class="wp-block-kadence-rowlayout alignfull kt-row-layout-inner kt-layout-id-cta007">
<div class="kt-row-column-wrap kt-has-1-columns">

<!-- wp:kadence/column {"id":1,"uniqueID":"kt-col-cta007"} -->
<div class="wp-block-kadence-column kadence-column-cta007"><div class="kt-inside-inner-col">

<!-- wp:kadence/advancedbtn {"uniqueID":"kt-btn-cta005","hAlign":"center"} -->
<div class="wp-block-kadence-advancedbtn kt-btn-wrap-cta005">
<!-- wp:kadence/singlebtn {"uniqueID":"kt-btn-cta005a","text":"Join Them Today","sizePreset":"large","color":"#ffffff","background":"palette1","backgroundHover":"palette2","borderRadius":[6,6,6,6],"padding":["16","40","16","40"],"icon":"fe_arrowRight","iconSide":"right"} -->
<div class="wp-block-kadence-singlebtn kt-btn-wrap-cta005a"><a class="kt-button button kt-btn-cta005a-action kt-btn-size-large kt-btn-style-basic kt-btn-has-icon kt-btn-icon-side-right" href="#">Join Them Today<span class="kt-btn-icon kt-btn-svg-icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="5" y1="12" x2="19" y2="12"></line><polyline points="12 5 19 12 12 19"></polyline></svg></span></a></div>
<!-- /wp:kadence/singlebtn -->
</div>
<!-- /wp:kadence/advancedbtn -->

</div></div>
<!-- /wp:kadence/column -->

</div>
</div>
<!-- /wp:kadence/rowlayout -->
```

## CTA Button Styles

### Primary (Solid)
```json
{
  "style": "basic",
  "color": "#ffffff",
  "background": "palette1",
  "backgroundHover": "palette2"
}
```

### Secondary (Outline)
```json
{
  "style": "outline",
  "color": "palette1",
  "borderColor": "palette1",
  "colorHover": "#ffffff",
  "backgroundHover": "palette1"
}
```

### Ghost (Transparent)
```json
{
  "style": "basic",
  "color": "palette1",
  "background": "transparent",
  "backgroundHover": "palette8"
}
```

## Best Practices

1. **Single focus**: One primary CTA per section
2. **Urgency words**: "Now", "Today", "Free", "Limited"
3. **Value proposition**: Clear benefit statement
4. **Visual hierarchy**: Button stands out from background
5. **Trust elements**: Stats, testimonials, guarantees nearby
6. **Responsive**: Buttons stack nicely on mobile
7. **Contrast**: Ensure WCAG AA contrast ratios
