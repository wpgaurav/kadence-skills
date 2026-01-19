# Kadence Features Section Skill

**Activation**: Creating feature sections, benefits grids, services displays, info box layouts with Kadence Blocks.

## Feature Section Patterns

### Pattern 1: 3-Column Icon Features

Classic feature grid with icons, titles, and descriptions.

```html
<!-- wp:kadence/rowlayout {"uniqueID":"kt-layout-feat001","columns":1,"colLayout":"equal","inheritMaxWidth":true,"align":"full","padding":["xl","lg","xl","lg"],"tabletPadding":["lg","md","lg","md"],"mobilePadding":["md","sm","md","sm"],"bgColor":"palette9"} -->
<div class="wp-block-kadence-rowlayout alignfull kt-row-layout-inner kt-layout-id-feat001">
<div class="kt-row-column-wrap kt-has-1-columns">

<!-- wp:kadence/column {"id":1,"uniqueID":"kt-col-feat001"} -->
<div class="wp-block-kadence-column kadence-column-feat001"><div class="kt-inside-inner-col">

<!-- Section Header -->
<!-- wp:kadence/advancedheading {"uniqueID":"kt-adv-heading-feat001","align":"center","color":"palette1","htmlTag":"p","fontSize":["14","14","13"],"fontWeight":"600","letterSpacing":2,"textTransform":"uppercase","margin":["","","8",""]} -->
<p class="kt-adv-heading-feat001 wp-block-kadence-advancedheading" data-kb-block="kb-adv-heading-feat001">Why Choose Us</p>
<!-- /wp:kadence/advancedheading -->

<!-- wp:kadence/advancedheading {"uniqueID":"kt-adv-heading-feat002","align":"center","color":"palette3","htmlTag":"h2","fontSize":["42","36","28"],"lineHeight":["1.2","1.25","1.3"],"fontWeight":"700","margin":["","","16",""]} -->
<h2 class="kt-adv-heading-feat002 wp-block-kadence-advancedheading" data-kb-block="kb-adv-heading-feat002">Features That Set Us Apart</h2>
<!-- /wp:kadence/advancedheading -->

<!-- wp:kadence/advancedheading {"uniqueID":"kt-adv-heading-feat003","align":"center","color":"palette4","htmlTag":"p","fontSize":["18","17","16"],"lineHeight":["1.6","1.6","1.5"],"maxWidth":700,"margin":["","","48",""]} -->
<p class="kt-adv-heading-feat003 wp-block-kadence-advancedheading" data-kb-block="kb-adv-heading-feat003">Discover the powerful features that make our solution the best choice for your needs.</p>
<!-- /wp:kadence/advancedheading -->

</div></div>
<!-- /wp:kadence/column -->

</div>
</div>
<!-- /wp:kadence/rowlayout -->

<!-- Features Grid -->
<!-- wp:kadence/rowlayout {"uniqueID":"kt-layout-feat002","columns":3,"colLayout":"equal","inheritMaxWidth":true,"align":"full","padding":["","lg","xl","lg"],"tabletPadding":["","md","lg","md"],"mobilePadding":["","sm","md","sm"],"bgColor":"palette9","columnGutter":"wider"} -->
<div class="wp-block-kadence-rowlayout alignfull kt-row-layout-inner kt-layout-id-feat002">
<div class="kt-row-column-wrap kt-has-3-columns kt-gutter-wider">

<!-- Feature 1 -->
<!-- wp:kadence/column {"id":1,"uniqueID":"kt-col-feat002a"} -->
<div class="wp-block-kadence-column kadence-column-feat002a"><div class="kt-inside-inner-col">

<!-- wp:kadence/infobox {"uniqueID":"kt-info-feat001","containerBackground":"#ffffff","containerPadding":["lg","lg","lg","lg"],"containerBorderRadius":12,"containerBorderWidth":[0,0,0,0],"mediaType":"icon","mediaAlign":"top","mediaIcon":[{"icon":"fe_zap","size":40,"width":2,"title":"","color":"palette1","hoverColor":"","hoverAnimation":"none"}],"mediaStyle":[{"background":"palette8","hoverBackground":"","border":"","hoverBorder":"","borderRadius":50,"padding":[20,20,20,20]}],"title":"Lightning Fast","titleFont":[{"level":3,"size":["22","20","18"],"lineHeight":["1.3","1.3","1.3"],"letterSpacing":"","family":"","weight":"600","color":"palette3"}],"titleMinHeight":[0,0,0],"titlePadding":["16","","",""]} -->
<div class="wp-block-kadence-infobox"><div class="kt-blocks-info-box-link-wrap kt-blocks-info-box-media-align-top kt-info-halign-center"><div class="kt-blocks-info-box-media-container kt-info-media-animate-none"><div class="kt-blocks-info-box-media kt-info-media-animate-none"><div class="kt-info-svg-icon-container kt-info-svg-icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" xmlns="http://www.w3.org/2000/svg"><polygon points="13 2 3 14 12 14 11 22 21 10 12 10 13 2"></polygon></svg></div></div></div><div class="kt-infobox-textcontent"><h3 class="kt-blocks-info-box-title">Lightning Fast</h3><p class="kt-blocks-info-box-text">Optimized performance ensures your pages load instantly, keeping visitors engaged.</p></div></div></div>
<!-- /wp:kadence/infobox -->

</div></div>
<!-- /wp:kadence/column -->

<!-- Feature 2 -->
<!-- wp:kadence/column {"id":2,"uniqueID":"kt-col-feat002b"} -->
<div class="wp-block-kadence-column kadence-column-feat002b"><div class="kt-inside-inner-col">

<!-- wp:kadence/infobox {"uniqueID":"kt-info-feat002","containerBackground":"#ffffff","containerPadding":["lg","lg","lg","lg"],"containerBorderRadius":12,"containerBorderWidth":[0,0,0,0],"mediaType":"icon","mediaAlign":"top","mediaIcon":[{"icon":"fe_shield","size":40,"width":2,"title":"","color":"palette1","hoverColor":"","hoverAnimation":"none"}],"mediaStyle":[{"background":"palette8","hoverBackground":"","border":"","hoverBorder":"","borderRadius":50,"padding":[20,20,20,20]}],"title":"Secure by Default","titleFont":[{"level":3,"size":["22","20","18"],"lineHeight":["1.3","1.3","1.3"],"letterSpacing":"","family":"","weight":"600","color":"palette3"}],"titleMinHeight":[0,0,0],"titlePadding":["16","","",""]} -->
<div class="wp-block-kadence-infobox"><div class="kt-blocks-info-box-link-wrap kt-blocks-info-box-media-align-top kt-info-halign-center"><div class="kt-blocks-info-box-media-container kt-info-media-animate-none"><div class="kt-blocks-info-box-media kt-info-media-animate-none"><div class="kt-info-svg-icon-container kt-info-svg-icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" xmlns="http://www.w3.org/2000/svg"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"></path></svg></div></div></div><div class="kt-infobox-textcontent"><h3 class="kt-blocks-info-box-title">Secure by Default</h3><p class="kt-blocks-info-box-text">Enterprise-grade security protects your data with industry-leading encryption.</p></div></div></div>
<!-- /wp:kadence/infobox -->

</div></div>
<!-- /wp:kadence/column -->

<!-- Feature 3 -->
<!-- wp:kadence/column {"id":3,"uniqueID":"kt-col-feat002c"} -->
<div class="wp-block-kadence-column kadence-column-feat002c"><div class="kt-inside-inner-col">

<!-- wp:kadence/infobox {"uniqueID":"kt-info-feat003","containerBackground":"#ffffff","containerPadding":["lg","lg","lg","lg"],"containerBorderRadius":12,"containerBorderWidth":[0,0,0,0],"mediaType":"icon","mediaAlign":"top","mediaIcon":[{"icon":"fe_refreshCw","size":40,"width":2,"title":"","color":"palette1","hoverColor":"","hoverAnimation":"none"}],"mediaStyle":[{"background":"palette8","hoverBackground":"","border":"","hoverBorder":"","borderRadius":50,"padding":[20,20,20,20]}],"title":"Always Updated","titleFont":[{"level":3,"size":["22","20","18"],"lineHeight":["1.3","1.3","1.3"],"letterSpacing":"","family":"","weight":"600","color":"palette3"}],"titleMinHeight":[0,0,0],"titlePadding":["16","","",""]} -->
<div class="wp-block-kadence-infobox"><div class="kt-blocks-info-box-link-wrap kt-blocks-info-box-media-align-top kt-info-halign-center"><div class="kt-blocks-info-box-media-container kt-info-media-animate-none"><div class="kt-blocks-info-box-media kt-info-media-animate-none"><div class="kt-info-svg-icon-container kt-info-svg-icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" xmlns="http://www.w3.org/2000/svg"><polyline points="23 4 23 10 17 10"></polyline><polyline points="1 20 1 14 7 14"></polyline><path d="M3.51 9a9 9 0 0 1 14.85-3.36L23 10M1 14l4.64 4.36A9 9 0 0 0 20.49 15"></path></svg></div></div></div><div class="kt-infobox-textcontent"><h3 class="kt-blocks-info-box-title">Always Updated</h3><p class="kt-blocks-info-box-text">Automatic updates ensure you always have the latest features and improvements.</p></div></div></div>
<!-- /wp:kadence/infobox -->

</div></div>
<!-- /wp:kadence/column -->

</div>
</div>
<!-- /wp:kadence/rowlayout -->
```

### Pattern 2: Alternating Feature Rows

Left-right alternating layout with images and text.

```html
<!-- Feature Row 1: Image Left -->
<!-- wp:kadence/rowlayout {"uniqueID":"kt-layout-feat003","columns":2,"colLayout":"equal","inheritMaxWidth":true,"align":"full","padding":["xl","lg","xl","lg"],"columnGutter":"wider","verticalAlignment":"middle"} -->
<div class="wp-block-kadence-rowlayout alignfull kt-row-layout-inner kt-layout-id-feat003">
<div class="kt-row-column-wrap kt-has-2-columns kt-gutter-wider kt-v-gutter-default kt-row-valign-middle">

<!-- wp:kadence/column {"id":1,"uniqueID":"kt-col-feat003a"} -->
<div class="wp-block-kadence-column kadence-column-feat003a"><div class="kt-inside-inner-col">

<!-- wp:kadence/image {"uniqueID":"kt-image-feat001","borderRadius":[12,12,12,12],"boxShadow":[true,"#000000",0.1,0,15,30,0,false]} -->
<figure class="wp-block-kadence-image kb-image-feat001"><img src="https://placehold.co/580x420/e2e8f0/64748b?text=Feature+1" alt="Feature image" class="kb-img wp-image-"/></figure>
<!-- /wp:kadence/image -->

</div></div>
<!-- /wp:kadence/column -->

<!-- wp:kadence/column {"id":2,"uniqueID":"kt-col-feat003b"} -->
<div class="wp-block-kadence-column kadence-column-feat003b"><div class="kt-inside-inner-col">

<!-- wp:kadence/advancedheading {"uniqueID":"kt-adv-heading-feat004","color":"palette3","htmlTag":"h3","fontSize":["32","28","24"],"lineHeight":["1.25","1.3","1.3"],"fontWeight":"700","margin":["","","16",""]} -->
<h3 class="kt-adv-heading-feat004 wp-block-kadence-advancedheading" data-kb-block="kb-adv-heading-feat004">Intuitive Dashboard</h3>
<!-- /wp:kadence/advancedheading -->

<!-- wp:kadence/advancedheading {"uniqueID":"kt-adv-heading-feat005","color":"palette4","htmlTag":"p","fontSize":["17","16","15"],"lineHeight":["1.7","1.7","1.6"],"margin":["","","24",""]} -->
<p class="kt-adv-heading-feat005 wp-block-kadence-advancedheading" data-kb-block="kb-adv-heading-feat005">Get a clear overview of all your metrics in one place. Our intuitive dashboard makes it easy to track progress and make data-driven decisions.</p>
<!-- /wp:kadence/advancedheading -->

<!-- wp:kadence/iconlist {"uniqueID":"kt-iconlist-feat001","items":[{"icon":"fe_checkCircle","link":"","target":"_self","size":20,"width":2,"text":"Real-time analytics","color":"palette2","background":"","border":"","borderRadius":0,"padding":5,"borderWidth":1,"style":"default","level":0},{"icon":"fe_checkCircle","link":"","target":"_self","size":20,"width":2,"text":"Custom reporting","color":"palette2","background":"","border":"","borderRadius":0,"padding":5,"borderWidth":1,"style":"default","level":0},{"icon":"fe_checkCircle","link":"","target":"_self","size":20,"width":2,"text":"Export to any format","color":"palette2","background":"","border":"","borderRadius":0,"padding":5,"borderWidth":1,"style":"default","level":0}],"listCount":3,"listGap":12} -->
<ul class="wp-block-kadence-iconlist kt-svg-icon-list-items kt-svg-icon-list-items-feat001 kt-svg-icon-list-columns-1"><li class="wp-block-kadence-listitem kt-svg-icon-list-item-wrap kt-svg-icon-list-item-0"><span class="kt-svg-icon-list-single kt-svg-icon-fe_checkCircle"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"></path><polyline points="22 4 12 14.01 9 11.01"></polyline></svg></span><span class="kt-svg-icon-list-text">Real-time analytics</span></li><li class="wp-block-kadence-listitem kt-svg-icon-list-item-wrap kt-svg-icon-list-item-1"><span class="kt-svg-icon-list-single kt-svg-icon-fe_checkCircle"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"></path><polyline points="22 4 12 14.01 9 11.01"></polyline></svg></span><span class="kt-svg-icon-list-text">Custom reporting</span></li><li class="wp-block-kadence-listitem kt-svg-icon-list-item-wrap kt-svg-icon-list-item-2"><span class="kt-svg-icon-list-single kt-svg-icon-fe_checkCircle"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"></path><polyline points="22 4 12 14.01 9 11.01"></polyline></svg></span><span class="kt-svg-icon-list-text">Export to any format</span></li></ul>
<!-- /wp:kadence/iconlist -->

</div></div>
<!-- /wp:kadence/column -->

</div>
</div>
<!-- /wp:kadence/rowlayout -->

<!-- Feature Row 2: Image Right -->
<!-- wp:kadence/rowlayout {"uniqueID":"kt-layout-feat004","columns":2,"colLayout":"equal","inheritMaxWidth":true,"align":"full","padding":["xl","lg","xl","lg"],"bgColor":"palette9","columnGutter":"wider","verticalAlignment":"middle","collapseOrder":"right-to-left"} -->
<div class="wp-block-kadence-rowlayout alignfull kt-row-layout-inner kt-layout-id-feat004">
<div class="kt-row-column-wrap kt-has-2-columns kt-gutter-wider kt-v-gutter-default kt-row-valign-middle">

<!-- wp:kadence/column {"id":1,"uniqueID":"kt-col-feat004a"} -->
<div class="wp-block-kadence-column kadence-column-feat004a"><div class="kt-inside-inner-col">

<!-- wp:kadence/advancedheading {"uniqueID":"kt-adv-heading-feat006","color":"palette3","htmlTag":"h3","fontSize":["32","28","24"],"lineHeight":["1.25","1.3","1.3"],"fontWeight":"700","margin":["","","16",""]} -->
<h3 class="kt-adv-heading-feat006 wp-block-kadence-advancedheading" data-kb-block="kb-adv-heading-feat006">Powerful Automation</h3>
<!-- /wp:kadence/advancedheading -->

<!-- wp:kadence/advancedheading {"uniqueID":"kt-adv-heading-feat007","color":"palette4","htmlTag":"p","fontSize":["17","16","15"],"lineHeight":["1.7","1.7","1.6"],"margin":["","","24",""]} -->
<p class="kt-adv-heading-feat007 wp-block-kadence-advancedheading" data-kb-block="kb-adv-heading-feat007">Automate repetitive tasks and focus on what matters most. Our smart automation saves hours of manual work every week.</p>
<!-- /wp:kadence/advancedheading -->

<!-- wp:kadence/iconlist {"uniqueID":"kt-iconlist-feat002","items":[{"icon":"fe_checkCircle","link":"","target":"_self","size":20,"width":2,"text":"Workflow automation","color":"palette2","background":"","border":"","borderRadius":0,"padding":5,"borderWidth":1,"style":"default","level":0},{"icon":"fe_checkCircle","link":"","target":"_self","size":20,"width":2,"text":"Smart triggers","color":"palette2","background":"","border":"","borderRadius":0,"padding":5,"borderWidth":1,"style":"default","level":0},{"icon":"fe_checkCircle","link":"","target":"_self","size":20,"width":2,"text":"Integration ready","color":"palette2","background":"","border":"","borderRadius":0,"padding":5,"borderWidth":1,"style":"default","level":0}],"listCount":3,"listGap":12} -->
<ul class="wp-block-kadence-iconlist kt-svg-icon-list-items kt-svg-icon-list-items-feat002 kt-svg-icon-list-columns-1"><li class="wp-block-kadence-listitem kt-svg-icon-list-item-wrap kt-svg-icon-list-item-0"><span class="kt-svg-icon-list-single kt-svg-icon-fe_checkCircle"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"></path><polyline points="22 4 12 14.01 9 11.01"></polyline></svg></span><span class="kt-svg-icon-list-text">Workflow automation</span></li><li class="wp-block-kadence-listitem kt-svg-icon-list-item-wrap kt-svg-icon-list-item-1"><span class="kt-svg-icon-list-single kt-svg-icon-fe_checkCircle"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"></path><polyline points="22 4 12 14.01 9 11.01"></polyline></svg></span><span class="kt-svg-icon-list-text">Smart triggers</span></li><li class="wp-block-kadence-listitem kt-svg-icon-list-item-wrap kt-svg-icon-list-item-2"><span class="kt-svg-icon-list-single kt-svg-icon-fe_checkCircle"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"></path><polyline points="22 4 12 14.01 9 11.01"></polyline></svg></span><span class="kt-svg-icon-list-text">Integration ready</span></li></ul>
<!-- /wp:kadence/iconlist -->

</div></div>
<!-- /wp:kadence/column -->

<!-- wp:kadence/column {"id":2,"uniqueID":"kt-col-feat004b"} -->
<div class="wp-block-kadence-column kadence-column-feat004b"><div class="kt-inside-inner-col">

<!-- wp:kadence/image {"uniqueID":"kt-image-feat002","borderRadius":[12,12,12,12],"boxShadow":[true,"#000000",0.1,0,15,30,0,false]} -->
<figure class="wp-block-kadence-image kb-image-feat002"><img src="https://placehold.co/580x420/e2e8f0/64748b?text=Feature+2" alt="Feature image" class="kb-img wp-image-"/></figure>
<!-- /wp:kadence/image -->

</div></div>
<!-- /wp:kadence/column -->

</div>
</div>
<!-- /wp:kadence/rowlayout -->
```

### Pattern 3: 4-Column Icon Grid

Compact feature grid for more items.

```html
<!-- wp:kadence/rowlayout {"uniqueID":"kt-layout-feat005","columns":4,"colLayout":"equal","inheritMaxWidth":true,"align":"full","padding":["xl","lg","xl","lg"],"tabletPadding":["lg","md","lg","md"],"mobilePadding":["md","sm","md","sm"],"tabletLayout":"two-equal","mobileLayout":"row","columnGutter":"default"} -->
<div class="wp-block-kadence-rowlayout alignfull kt-row-layout-inner kt-layout-id-feat005">
<div class="kt-row-column-wrap kt-has-4-columns kt-gutter-default">

<!-- Feature 1 -->
<!-- wp:kadence/column {"id":1,"uniqueID":"kt-col-feat005a","textAlign":"center"} -->
<div class="wp-block-kadence-column kadence-column-feat005a has-text-align-center"><div class="kt-inside-inner-col">

<!-- wp:kadence/icon {"icons":[{"icon":"fe_target","link":"","target":"_self","size":48,"width":2,"title":"","color":"palette1","background":"palette8","border":"","borderRadius":12,"borderWidth":0,"padding":[16,16,16,16],"style":"default","margin":["","","12",""],"hColor":"","hBackground":"","hBorder":""}],"uniqueID":"kt-icon-feat001","textAlignment":"center"} -->
<div class="wp-block-kadence-icon kt-svg-icons kt-svg-icons-feat001 aligncenter"><div class="kt-svg-style-default kt-svg-icon-wrap kt-svg-item-0"><span class="kt-svg-icon kt-svg-icon-fe_target"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"></circle><circle cx="12" cy="12" r="6"></circle><circle cx="12" cy="12" r="2"></circle></svg></span></div></div>
<!-- /wp:kadence/icon -->

<!-- wp:kadence/advancedheading {"uniqueID":"kt-adv-heading-feat008","align":"center","color":"palette3","htmlTag":"h4","fontSize":["18","17","16"],"fontWeight":"600","margin":["","","8",""]} -->
<h4 class="kt-adv-heading-feat008 wp-block-kadence-advancedheading" data-kb-block="kb-adv-heading-feat008">Goal Tracking</h4>
<!-- /wp:kadence/advancedheading -->

<!-- wp:kadence/advancedheading {"uniqueID":"kt-adv-heading-feat009","align":"center","color":"palette4","htmlTag":"p","fontSize":["15","14","14"],"lineHeight":["1.6","1.6","1.5"]} -->
<p class="kt-adv-heading-feat009 wp-block-kadence-advancedheading" data-kb-block="kb-adv-heading-feat009">Set and track goals with ease.</p>
<!-- /wp:kadence/advancedheading -->

</div></div>
<!-- /wp:kadence/column -->

<!-- Feature 2 -->
<!-- wp:kadence/column {"id":2,"uniqueID":"kt-col-feat005b","textAlign":"center"} -->
<div class="wp-block-kadence-column kadence-column-feat005b has-text-align-center"><div class="kt-inside-inner-col">

<!-- wp:kadence/icon {"icons":[{"icon":"fe_users","link":"","target":"_self","size":48,"width":2,"title":"","color":"palette1","background":"palette8","border":"","borderRadius":12,"borderWidth":0,"padding":[16,16,16,16],"style":"default","margin":["","","12",""],"hColor":"","hBackground":"","hBorder":""}],"uniqueID":"kt-icon-feat002","textAlignment":"center"} -->
<div class="wp-block-kadence-icon kt-svg-icons kt-svg-icons-feat002 aligncenter"><div class="kt-svg-style-default kt-svg-icon-wrap kt-svg-item-0"><span class="kt-svg-icon kt-svg-icon-fe_users"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"></path><circle cx="9" cy="7" r="4"></circle><path d="M23 21v-2a4 4 0 0 0-3-3.87"></path><path d="M16 3.13a4 4 0 0 1 0 7.75"></path></svg></span></div></div>
<!-- /wp:kadence/icon -->

<!-- wp:kadence/advancedheading {"uniqueID":"kt-adv-heading-feat010","align":"center","color":"palette3","htmlTag":"h4","fontSize":["18","17","16"],"fontWeight":"600","margin":["","","8",""]} -->
<h4 class="kt-adv-heading-feat010 wp-block-kadence-advancedheading" data-kb-block="kb-adv-heading-feat010">Team Collaboration</h4>
<!-- /wp:kadence/advancedheading -->

<!-- wp:kadence/advancedheading {"uniqueID":"kt-adv-heading-feat011","align":"center","color":"palette4","htmlTag":"p","fontSize":["15","14","14"],"lineHeight":["1.6","1.6","1.5"]} -->
<p class="kt-adv-heading-feat011 wp-block-kadence-advancedheading" data-kb-block="kb-adv-heading-feat011">Work together seamlessly.</p>
<!-- /wp:kadence/advancedheading -->

</div></div>
<!-- /wp:kadence/column -->

<!-- Feature 3 -->
<!-- wp:kadence/column {"id":3,"uniqueID":"kt-col-feat005c","textAlign":"center"} -->
<div class="wp-block-kadence-column kadence-column-feat005c has-text-align-center"><div class="kt-inside-inner-col">

<!-- wp:kadence/icon {"icons":[{"icon":"fe_barChart2","link":"","target":"_self","size":48,"width":2,"title":"","color":"palette1","background":"palette8","border":"","borderRadius":12,"borderWidth":0,"padding":[16,16,16,16],"style":"default","margin":["","","12",""],"hColor":"","hBackground":"","hBorder":""}],"uniqueID":"kt-icon-feat003","textAlignment":"center"} -->
<div class="wp-block-kadence-icon kt-svg-icons kt-svg-icons-feat003 aligncenter"><div class="kt-svg-style-default kt-svg-icon-wrap kt-svg-item-0"><span class="kt-svg-icon kt-svg-icon-fe_barChart2"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="18" y1="20" x2="18" y2="10"></line><line x1="12" y1="20" x2="12" y2="4"></line><line x1="6" y1="20" x2="6" y2="14"></line></svg></span></div></div>
<!-- /wp:kadence/icon -->

<!-- wp:kadence/advancedheading {"uniqueID":"kt-adv-heading-feat012","align":"center","color":"palette3","htmlTag":"h4","fontSize":["18","17","16"],"fontWeight":"600","margin":["","","8",""]} -->
<h4 class="kt-adv-heading-feat012 wp-block-kadence-advancedheading" data-kb-block="kb-adv-heading-feat012">Analytics</h4>
<!-- /wp:kadence/advancedheading -->

<!-- wp:kadence/advancedheading {"uniqueID":"kt-adv-heading-feat013","align":"center","color":"palette4","htmlTag":"p","fontSize":["15","14","14"],"lineHeight":["1.6","1.6","1.5"]} -->
<p class="kt-adv-heading-feat013 wp-block-kadence-advancedheading" data-kb-block="kb-adv-heading-feat013">Data-driven insights.</p>
<!-- /wp:kadence/advancedheading -->

</div></div>
<!-- /wp:kadence/column -->

<!-- Feature 4 -->
<!-- wp:kadence/column {"id":4,"uniqueID":"kt-col-feat005d","textAlign":"center"} -->
<div class="wp-block-kadence-column kadence-column-feat005d has-text-align-center"><div class="kt-inside-inner-col">

<!-- wp:kadence/icon {"icons":[{"icon":"fe_lock","link":"","target":"_self","size":48,"width":2,"title":"","color":"palette1","background":"palette8","border":"","borderRadius":12,"borderWidth":0,"padding":[16,16,16,16],"style":"default","margin":["","","12",""],"hColor":"","hBackground":"","hBorder":""}],"uniqueID":"kt-icon-feat004","textAlignment":"center"} -->
<div class="wp-block-kadence-icon kt-svg-icons kt-svg-icons-feat004 aligncenter"><div class="kt-svg-style-default kt-svg-icon-wrap kt-svg-item-0"><span class="kt-svg-icon kt-svg-icon-fe_lock"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="11" width="18" height="11" rx="2" ry="2"></rect><path d="M7 11V7a5 5 0 0 1 10 0v4"></path></svg></span></div></div>
<!-- /wp:kadence/icon -->

<!-- wp:kadence/advancedheading {"uniqueID":"kt-adv-heading-feat014","align":"center","color":"palette3","htmlTag":"h4","fontSize":["18","17","16"],"fontWeight":"600","margin":["","","8",""]} -->
<h4 class="kt-adv-heading-feat014 wp-block-kadence-advancedheading" data-kb-block="kb-adv-heading-feat014">Security</h4>
<!-- /wp:kadence/advancedheading -->

<!-- wp:kadence/advancedheading {"uniqueID":"kt-adv-heading-feat015","align":"center","color":"palette4","htmlTag":"p","fontSize":["15","14","14"],"lineHeight":["1.6","1.6","1.5"]} -->
<p class="kt-adv-heading-feat015 wp-block-kadence-advancedheading" data-kb-block="kb-adv-heading-feat015">Enterprise-grade protection.</p>
<!-- /wp:kadence/advancedheading -->

</div></div>
<!-- /wp:kadence/column -->

</div>
</div>
<!-- /wp:kadence/rowlayout -->
```

## InfoBox Attribute Reference

Key `kadence/infobox` attributes:

```json
{
  "uniqueID": "kt-info-xxx",
  "containerBackground": "#ffffff",
  "containerPadding": ["lg","lg","lg","lg"],
  "containerBorderRadius": 12,
  "mediaType": "icon",           // "icon", "image", "number"
  "mediaAlign": "top",           // "top", "left", "right"
  "mediaIcon": [{
    "icon": "fe_zap",
    "size": 40,
    "width": 2,
    "color": "palette1"
  }],
  "mediaStyle": [{
    "background": "palette8",
    "borderRadius": 50,
    "padding": [20,20,20,20]
  }],
  "title": "Feature Title",
  "titleFont": [{
    "level": 3,
    "size": ["22","20","18"],
    "weight": "600",
    "color": "palette3"
  }]
}
```

## Common Icons for Features

| Purpose | Icons |
|---------|-------|
| Speed/Performance | `fe_zap`, `fe_trendingUp`, `fe_clock` |
| Security | `fe_shield`, `fe_lock`, `fe_key` |
| Analytics | `fe_barChart2`, `fe_pieChart`, `fe_activity` |
| Collaboration | `fe_users`, `fe_messageCircle`, `fe_share2` |
| Settings/Config | `fe_settings`, `fe_sliders`, `fe_tool` |
| Success/Check | `fe_checkCircle`, `fe_award`, `fe_thumbsUp` |
| Innovation | `fe_zap`, `fe_star`, `fe_sun` |
| Support | `fe_headphones`, `fe_helpCircle`, `fe_lifeBuoy` |

## Best Practices

1. **Consistent icon style**: Use either line (fe_) or solid icons, not mixed
2. **Visual hierarchy**: Icon → Title → Description flow
3. **Responsive columns**: 4 cols → 2 cols tablet → 1 col mobile
4. **Card styling**: Consistent padding, border radius, shadows
5. **Color contrast**: Ensure icons stand out against backgrounds
