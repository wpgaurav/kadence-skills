# Kadence Block Snippets

**Activation**: Quick reference for commonly used Kadence block patterns and components.

## Basic Building Blocks

### Row Layout (Container)

```html
<!-- wp:kadence/rowlayout {"uniqueID":"kt-layout-xxx","columns":2,"colLayout":"equal","inheritMaxWidth":true,"align":"full","padding":["lg","md","lg","md"],"bgColor":"palette9"} -->
<div class="wp-block-kadence-rowlayout alignfull kt-row-layout-inner kt-layout-id-xxx">
<div class="kt-row-column-wrap kt-has-2-columns">
<!-- Columns go here -->
</div>
</div>
<!-- /wp:kadence/rowlayout -->
```

### Section (Column)

```html
<!-- wp:kadence/column {"id":1,"uniqueID":"kt-col-xxx"} -->
<div class="wp-block-kadence-column kadence-column-xxx"><div class="kt-inside-inner-col">
<!-- Content goes here -->
</div></div>
<!-- /wp:kadence/column -->
```

### Advanced Heading

```html
<!-- wp:kadence/advancedheading {"uniqueID":"kt-adv-heading-xxx","align":"center","color":"palette3","htmlTag":"h2","fontSize":["36","30","24"],"lineHeight":["1.25","1.3","1.35"],"fontWeight":"700"} -->
<h2 class="kt-adv-heading-xxx wp-block-kadence-advancedheading" data-kb-block="kb-adv-heading-xxx">Heading Text</h2>
<!-- /wp:kadence/advancedheading -->
```

### Paragraph Text

```html
<!-- wp:kadence/advancedheading {"uniqueID":"kt-adv-heading-xxx","color":"palette4","htmlTag":"p","fontSize":["18","17","16"],"lineHeight":["1.6","1.6","1.5"]} -->
<p class="kt-adv-heading-xxx wp-block-kadence-advancedheading" data-kb-block="kb-adv-heading-xxx">Paragraph text goes here.</p>
<!-- /wp:kadence/advancedheading -->
```

## Buttons

### Single Primary Button

```html
<!-- wp:kadence/advancedbtn {"uniqueID":"kt-btn-xxx","hAlign":"center"} -->
<div class="wp-block-kadence-advancedbtn kt-btn-wrap-xxx">
<!-- wp:kadence/singlebtn {"uniqueID":"kt-btn-xxxa","text":"Button Text","sizePreset":"large","color":"#ffffff","background":"palette1","backgroundHover":"palette2","borderRadius":[6,6,6,6]} -->
<div class="wp-block-kadence-singlebtn kt-btn-wrap-xxxa"><a class="kt-button button kt-btn-xxxa-action kt-btn-size-large kt-btn-style-basic" href="#">Button Text</a></div>
<!-- /wp:kadence/singlebtn -->
</div>
<!-- /wp:kadence/advancedbtn -->
```

### Outline Button

```html
<!-- wp:kadence/singlebtn {"uniqueID":"kt-btn-xxx","text":"Learn More","sizePreset":"medium","style":"outline","color":"palette1","borderColor":"palette1","colorHover":"#ffffff","backgroundHover":"palette1","borderRadius":[6,6,6,6]} -->
<div class="wp-block-kadence-singlebtn kt-btn-wrap-xxx"><a class="kt-button button kt-btn-xxx-action kt-btn-size-medium kt-btn-style-outline" href="#">Learn More</a></div>
<!-- /wp:kadence/singlebtn -->
```

### Button with Icon

```html
<!-- wp:kadence/singlebtn {"uniqueID":"kt-btn-xxx","text":"Get Started","sizePreset":"large","color":"#ffffff","background":"palette1","borderRadius":[6,6,6,6],"icon":"fe_arrowRight","iconSide":"right"} -->
<div class="wp-block-kadence-singlebtn kt-btn-wrap-xxx"><a class="kt-button button kt-btn-xxx-action kt-btn-size-large kt-btn-style-basic kt-btn-has-icon kt-btn-icon-side-right" href="#">Get Started<span class="kt-btn-icon kt-btn-svg-icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="5" y1="12" x2="19" y2="12"></line><polyline points="12 5 19 12 12 19"></polyline></svg></span></a></div>
<!-- /wp:kadence/singlebtn -->
```

### Two Buttons Side by Side

```html
<!-- wp:kadence/advancedbtn {"uniqueID":"kt-btn-xxx","hAlign":"center","gap":[16,16,12]} -->
<div class="wp-block-kadence-advancedbtn kt-btn-wrap-xxx">
<!-- wp:kadence/singlebtn {"uniqueID":"kt-btn-xxxa","text":"Primary Action","sizePreset":"large","color":"#ffffff","background":"palette1","borderRadius":[6,6,6,6]} -->
<div class="wp-block-kadence-singlebtn kt-btn-wrap-xxxa"><a class="kt-button button kt-btn-xxxa-action kt-btn-size-large kt-btn-style-basic" href="#">Primary Action</a></div>
<!-- /wp:kadence/singlebtn -->
<!-- wp:kadence/singlebtn {"uniqueID":"kt-btn-xxxb","text":"Secondary","sizePreset":"large","style":"outline","color":"palette1","borderColor":"palette1","borderRadius":[6,6,6,6]} -->
<div class="wp-block-kadence-singlebtn kt-btn-wrap-xxxb"><a class="kt-button button kt-btn-xxxb-action kt-btn-size-large kt-btn-style-outline" href="#">Secondary</a></div>
<!-- /wp:kadence/singlebtn -->
</div>
<!-- /wp:kadence/advancedbtn -->
```

## Icons

### Single Icon

```html
<!-- wp:kadence/icon {"icons":[{"icon":"fe_checkCircle","link":"","target":"_self","size":48,"width":2,"title":"","color":"palette1","background":"palette8","border":"","borderRadius":50,"borderWidth":0,"padding":[16,16,16,16],"style":"default"}],"uniqueID":"kt-icon-xxx","textAlignment":"center"} -->
<div class="wp-block-kadence-icon kt-svg-icons kt-svg-icons-xxx aligncenter"><div class="kt-svg-style-default kt-svg-icon-wrap kt-svg-item-0"><span class="kt-svg-icon kt-svg-icon-fe_checkCircle"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"></path><polyline points="22 4 12 14.01 9 11.01"></polyline></svg></span></div></div>
<!-- /wp:kadence/icon -->
```

### 5-Star Rating

```html
<!-- wp:kadence/icon {"icons":[{"icon":"fe_star","size":20,"color":"#fbbf24","background":"transparent","padding":[0,2,0,2],"style":"default"}],"iconCount":5,"uniqueID":"kt-stars-xxx","textAlignment":"left"} -->
<div class="wp-block-kadence-icon kt-svg-icons kt-svg-icons-xxx alignleft"><div class="kt-svg-style-default kt-svg-icon-wrap kt-svg-item-0"><span class="kt-svg-icon kt-svg-icon-fe_star" style="color:#fbbf24"><svg viewBox="0 0 24 24" fill="currentColor" stroke="currentColor" stroke-width="2"><polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"></polygon></svg></span></div><div class="kt-svg-style-default kt-svg-icon-wrap kt-svg-item-1"><span class="kt-svg-icon kt-svg-icon-fe_star" style="color:#fbbf24"><svg viewBox="0 0 24 24" fill="currentColor" stroke="currentColor" stroke-width="2"><polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"></polygon></svg></span></div><div class="kt-svg-style-default kt-svg-icon-wrap kt-svg-item-2"><span class="kt-svg-icon kt-svg-icon-fe_star" style="color:#fbbf24"><svg viewBox="0 0 24 24" fill="currentColor" stroke="currentColor" stroke-width="2"><polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"></polygon></svg></span></div><div class="kt-svg-style-default kt-svg-icon-wrap kt-svg-item-3"><span class="kt-svg-icon kt-svg-icon-fe_star" style="color:#fbbf24"><svg viewBox="0 0 24 24" fill="currentColor" stroke="currentColor" stroke-width="2"><polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"></polygon></svg></span></div><div class="kt-svg-style-default kt-svg-icon-wrap kt-svg-item-4"><span class="kt-svg-icon kt-svg-icon-fe_star" style="color:#fbbf24"><svg viewBox="0 0 24 24" fill="currentColor" stroke="currentColor" stroke-width="2"><polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"></polygon></svg></span></div></div>
<!-- /wp:kadence/icon -->
```

## Icon List

```html
<!-- wp:kadence/iconlist {"uniqueID":"kt-iconlist-xxx","items":[{"icon":"fe_checkCircle","text":"First item","color":"palette2"},{"icon":"fe_checkCircle","text":"Second item","color":"palette2"},{"icon":"fe_checkCircle","text":"Third item","color":"palette2"}],"listCount":3,"listGap":10} -->
<ul class="wp-block-kadence-iconlist kt-svg-icon-list-items kt-svg-icon-list-items-xxx kt-svg-icon-list-columns-1">
<li class="wp-block-kadence-listitem kt-svg-icon-list-item-wrap kt-svg-icon-list-item-0"><span class="kt-svg-icon-list-single kt-svg-icon-fe_checkCircle"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"></path><polyline points="22 4 12 14.01 9 11.01"></polyline></svg></span><span class="kt-svg-icon-list-text">First item</span></li>
<li class="wp-block-kadence-listitem kt-svg-icon-list-item-wrap kt-svg-icon-list-item-1"><span class="kt-svg-icon-list-single kt-svg-icon-fe_checkCircle"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"></path><polyline points="22 4 12 14.01 9 11.01"></polyline></svg></span><span class="kt-svg-icon-list-text">Second item</span></li>
<li class="wp-block-kadence-listitem kt-svg-icon-list-item-wrap kt-svg-icon-list-item-2"><span class="kt-svg-icon-list-single kt-svg-icon-fe_checkCircle"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"></path><polyline points="22 4 12 14.01 9 11.01"></polyline></svg></span><span class="kt-svg-icon-list-text">Third item</span></li>
</ul>
<!-- /wp:kadence/iconlist -->
```

## Images

### Basic Image

```html
<!-- wp:kadence/image {"uniqueID":"kt-image-xxx","borderRadius":[12,12,12,12]} -->
<figure class="wp-block-kadence-image kb-image-xxx"><img src="https://placehold.co/600x400" alt="Description" class="kb-img wp-image-"/></figure>
<!-- /wp:kadence/image -->
```

### Image with Shadow

```html
<!-- wp:kadence/image {"uniqueID":"kt-image-xxx","borderRadius":[12,12,12,12],"boxShadow":[true,"#000000",0.12,0,20,40,0,false]} -->
<figure class="wp-block-kadence-image kb-image-xxx"><img src="https://placehold.co/600x400" alt="Description" class="kb-img wp-image-"/></figure>
<!-- /wp:kadence/image -->
```

### Avatar Image

```html
<!-- wp:kadence/image {"uniqueID":"kt-avatar-xxx","imgMaxWidth":64,"borderRadius":[50,50,50,50]} -->
<figure class="wp-block-kadence-image kb-image-xxx"><img src="https://placehold.co/64x64" alt="Name" class="kb-img wp-image-"/></figure>
<!-- /wp:kadence/image -->
```

## Info Box

```html
<!-- wp:kadence/infobox {"uniqueID":"kt-info-xxx","containerBackground":"#ffffff","containerPadding":["lg","lg","lg","lg"],"containerBorderRadius":12,"mediaType":"icon","mediaAlign":"top","mediaIcon":[{"icon":"fe_zap","size":40,"color":"palette1"}],"mediaStyle":[{"background":"palette8","borderRadius":50,"padding":[20,20,20,20]}],"title":"Feature Title","titleFont":[{"level":3,"size":["22","20","18"],"weight":"600","color":"palette3"}]} -->
<div class="wp-block-kadence-infobox"><div class="kt-blocks-info-box-link-wrap kt-blocks-info-box-media-align-top kt-info-halign-center"><div class="kt-blocks-info-box-media-container"><div class="kt-blocks-info-box-media"><div class="kt-info-svg-icon-container kt-info-svg-icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polygon points="13 2 3 14 12 14 11 22 21 10 12 10 13 2"></polygon></svg></div></div></div><div class="kt-infobox-textcontent"><h3 class="kt-blocks-info-box-title">Feature Title</h3><p class="kt-blocks-info-box-text">Feature description goes here.</p></div></div></div>
<!-- /wp:kadence/infobox -->
```

## Spacer

```html
<!-- wp:kadence/spacer {"spacerHeight":40,"tabletSpacerHeight":30,"mobileSpacerHeight":20} /-->
```

## Section Headers

### Centered Section Header

```html
<!-- wp:kadence/advancedheading {"uniqueID":"kt-label-xxx","align":"center","color":"palette1","htmlTag":"p","fontSize":["14","14","13"],"fontWeight":"600","letterSpacing":2,"textTransform":"uppercase","margin":["","","8",""]} -->
<p class="kt-label-xxx wp-block-kadence-advancedheading">Section Label</p>
<!-- /wp:kadence/advancedheading -->

<!-- wp:kadence/advancedheading {"uniqueID":"kt-title-xxx","align":"center","color":"palette3","htmlTag":"h2","fontSize":["42","36","28"],"lineHeight":["1.2","1.25","1.3"],"fontWeight":"700","margin":["","","16",""]} -->
<h2 class="kt-title-xxx wp-block-kadence-advancedheading">Section Title</h2>
<!-- /wp:kadence/advancedheading -->

<!-- wp:kadence/advancedheading {"uniqueID":"kt-desc-xxx","align":"center","color":"palette4","htmlTag":"p","fontSize":["18","17","16"],"lineHeight":["1.6","1.6","1.5"],"maxWidth":600} -->
<p class="kt-desc-xxx wp-block-kadence-advancedheading">Section description text that provides context.</p>
<!-- /wp:kadence/advancedheading -->
```

## Common Attribute Quick Reference

### Font Sizes by Element
| Element | Desktop | Tablet | Mobile |
|---------|---------|--------|--------|
| H1 | 48-60 | 40-48 | 32-36 |
| H2 | 36-42 | 30-36 | 24-28 |
| H3 | 28-32 | 24-28 | 20-24 |
| H4 | 22-24 | 20-22 | 18-20 |
| Body Large | 18-20 | 17-18 | 16-17 |
| Body | 16-17 | 15-16 | 15-16 |
| Small | 14-15 | 13-14 | 13-14 |

### Spacing Presets
| Preset | Approx Value |
|--------|--------------|
| xxs | 4px |
| xs | 8px |
| sm | 16px |
| md | 24px |
| lg | 40px |
| xl | 64px |
| xxl | 96px |

### Border Radius
| Style | Value |
|-------|-------|
| Sharp | 0 |
| Subtle | 4-6 |
| Rounded | 8-12 |
| Pill | 50 |
| Circle | 50% |

### Common Colors
| Name | Usage |
|------|-------|
| palette1 | Primary brand |
| palette2 | Secondary/accent |
| palette3 | Dark text |
| palette4 | Body text |
| palette8 | Light backgrounds |
| palette9 | Lightest backgrounds |
