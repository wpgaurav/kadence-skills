# Kadence Advanced Table Skill

**Activation**: Creating data tables, pricing comparison tables, feature matrices, specification tables with Kadence Blocks.

## Table Block Structure

Kadence tables use a nested block structure:
- `kadence/table` - Container with column count and styling
- `kadence/table-row` - Individual rows (can be header or data)
- `kadence/table-data` - Individual cells containing content blocks

## Table Patterns

### Pattern 1: Simple Data Table

Basic table with header row and data rows.

```html
<!-- wp:kadence/table {"uniqueID":"kt-table-001","columns":3,"isFirstRowHeader":true,"cellPadding":["sm","sm","sm","sm"],"borderStyle":[{"top":["palette7","solid","1"],"right":["palette7","solid","1"],"bottom":["palette7","solid","1"],"left":["palette7","solid","1"],"unit":"px"}],"headerTypography":[{"size":["16","15","14"],"weight":"600","color":"palette3","background":"palette8","padding":["sm","sm","sm","sm"]}],"dataTypography":[{"size":["15","14","14"],"color":"palette4","padding":["sm","sm","sm","sm"]}]} -->
<figure class="wp-block-kadence-table kb-table-container-kt-table-001"><table class="kb-table kb-table-kt-table-001">
<tbody>

<!-- wp:kadence/table-row {"uniqueID":"kt-row-001a","row":0} -->
<tr class="kb-table-row kb-table-row-kt-row-001a">
<!-- wp:kadence/table-data {"uniqueID":"kt-data-001a","column":0} -->
<th class="kb-table-data kb-table-data-kt-data-001a">
<!-- wp:kadence/advancedheading {"uniqueID":"kt-adv-th001","htmlTag":"p","fontSize":["16","15","14"],"fontWeight":"600","color":"palette3"} -->
<p class="kt-adv-heading-th001 wp-block-kadence-advancedheading">Feature</p>
<!-- /wp:kadence/advancedheading -->
</th>
<!-- /wp:kadence/table-data -->
<!-- wp:kadence/table-data {"uniqueID":"kt-data-001b","column":1} -->
<th class="kb-table-data kb-table-data-kt-data-001b">
<!-- wp:kadence/advancedheading {"uniqueID":"kt-adv-th002","htmlTag":"p","fontSize":["16","15","14"],"fontWeight":"600","color":"palette3"} -->
<p class="kt-adv-heading-th002 wp-block-kadence-advancedheading">Basic</p>
<!-- /wp:kadence/advancedheading -->
</th>
<!-- /wp:kadence/table-data -->
<!-- wp:kadence/table-data {"uniqueID":"kt-data-001c","column":2} -->
<th class="kb-table-data kb-table-data-kt-data-001c">
<!-- wp:kadence/advancedheading {"uniqueID":"kt-adv-th003","htmlTag":"p","fontSize":["16","15","14"],"fontWeight":"600","color":"palette3"} -->
<p class="kt-adv-heading-th003 wp-block-kadence-advancedheading">Pro</p>
<!-- /wp:kadence/advancedheading -->
</th>
<!-- /wp:kadence/table-data -->
</tr>
<!-- /wp:kadence/table-row -->

<!-- wp:kadence/table-row {"uniqueID":"kt-row-001b","row":1} -->
<tr class="kb-table-row kb-table-row-kt-row-001b">
<!-- wp:kadence/table-data {"uniqueID":"kt-data-002a","column":0} -->
<td class="kb-table-data kb-table-data-kt-data-002a">
<!-- wp:kadence/advancedheading {"uniqueID":"kt-adv-td001","htmlTag":"p","fontSize":["15","14","14"],"color":"palette4"} -->
<p class="kt-adv-heading-td001 wp-block-kadence-advancedheading">Storage</p>
<!-- /wp:kadence/advancedheading -->
</td>
<!-- /wp:kadence/table-data -->
<!-- wp:kadence/table-data {"uniqueID":"kt-data-002b","column":1} -->
<td class="kb-table-data kb-table-data-kt-data-002b">
<!-- wp:kadence/advancedheading {"uniqueID":"kt-adv-td002","htmlTag":"p","fontSize":["15","14","14"],"color":"palette4"} -->
<p class="kt-adv-heading-td002 wp-block-kadence-advancedheading">10 GB</p>
<!-- /wp:kadence/advancedheading -->
</td>
<!-- /wp:kadence/table-data -->
<!-- wp:kadence/table-data {"uniqueID":"kt-data-002c","column":2} -->
<td class="kb-table-data kb-table-data-kt-data-002c">
<!-- wp:kadence/advancedheading {"uniqueID":"kt-adv-td003","htmlTag":"p","fontSize":["15","14","14"],"color":"palette4"} -->
<p class="kt-adv-heading-td003 wp-block-kadence-advancedheading">100 GB</p>
<!-- /wp:kadence/advancedheading -->
</td>
<!-- /wp:kadence/table-data -->
</tr>
<!-- /wp:kadence/table-row -->

<!-- wp:kadence/table-row {"uniqueID":"kt-row-001c","row":2} -->
<tr class="kb-table-row kb-table-row-kt-row-001c">
<!-- wp:kadence/table-data {"uniqueID":"kt-data-003a","column":0} -->
<td class="kb-table-data kb-table-data-kt-data-003a">
<!-- wp:kadence/advancedheading {"uniqueID":"kt-adv-td004","htmlTag":"p","fontSize":["15","14","14"],"color":"palette4"} -->
<p class="kt-adv-heading-td004 wp-block-kadence-advancedheading">Users</p>
<!-- /wp:kadence/advancedheading -->
</td>
<!-- /wp:kadence/table-data -->
<!-- wp:kadence/table-data {"uniqueID":"kt-data-003b","column":1} -->
<td class="kb-table-data kb-table-data-kt-data-003b">
<!-- wp:kadence/advancedheading {"uniqueID":"kt-adv-td005","htmlTag":"p","fontSize":["15","14","14"],"color":"palette4"} -->
<p class="kt-adv-heading-td005 wp-block-kadence-advancedheading">1</p>
<!-- /wp:kadence/advancedheading -->
</td>
<!-- /wp:kadence/table-data -->
<!-- wp:kadence/table-data {"uniqueID":"kt-data-003c","column":2} -->
<td class="kb-table-data kb-table-data-kt-data-003c">
<!-- wp:kadence/advancedheading {"uniqueID":"kt-adv-td006","htmlTag":"p","fontSize":["15","14","14"],"color":"palette4"} -->
<p class="kt-adv-heading-td006 wp-block-kadence-advancedheading">Unlimited</p>
<!-- /wp:kadence/advancedheading -->
</td>
<!-- /wp:kadence/table-data -->
</tr>
<!-- /wp:kadence/table-row -->

</tbody>
</table></figure>
<!-- /wp:kadence/table -->
```

### Pattern 2: Striped Table with Hover

Alternating row colors for better readability.

```html
<!-- wp:kadence/table {"uniqueID":"kt-table-002","columns":4,"isFirstRowHeader":true,"evenOddBackground":true,"backgroundColorEven":"palette9","backgroundColorOdd":"#ffffff","backgroundHoverColorEven":"palette8","backgroundHoverColorOdd":"palette8","cellPadding":["sm","md","sm","md"],"borderStyle":[{"top":["palette7","solid","1"],"right":["","",""],"bottom":["palette7","solid","1"],"left":["","",""],"unit":"px"}],"borderOnRowOnly":true,"headerTypography":[{"size":["16","15","14"],"weight":"700","color":"#ffffff","background":"palette1","padding":["md","md","md","md"]}],"textAlign":"left"} -->
<figure class="wp-block-kadence-table kb-table-container-kt-table-002"><table class="kb-table kb-table-kt-table-002">
<tbody>

<!-- wp:kadence/table-row {"uniqueID":"kt-row-002a","row":0} -->
<tr class="kb-table-row kb-table-row-kt-row-002a">
<!-- wp:kadence/table-data {"uniqueID":"kt-data-s001","column":0} -->
<th class="kb-table-data kb-table-data-kt-data-s001">
<!-- wp:kadence/advancedheading {"uniqueID":"kt-th-s001","htmlTag":"p","fontWeight":"700","color":"#ffffff"} -->
<p class="kt-adv-heading-s001 wp-block-kadence-advancedheading">Name</p>
<!-- /wp:kadence/advancedheading -->
</th>
<!-- /wp:kadence/table-data -->
<!-- wp:kadence/table-data {"uniqueID":"kt-data-s002","column":1} -->
<th class="kb-table-data kb-table-data-kt-data-s002">
<!-- wp:kadence/advancedheading {"uniqueID":"kt-th-s002","htmlTag":"p","fontWeight":"700","color":"#ffffff"} -->
<p class="kt-adv-heading-s002 wp-block-kadence-advancedheading">Role</p>
<!-- /wp:kadence/advancedheading -->
</th>
<!-- /wp:kadence/table-data -->
<!-- wp:kadence/table-data {"uniqueID":"kt-data-s003","column":2} -->
<th class="kb-table-data kb-table-data-kt-data-s003">
<!-- wp:kadence/advancedheading {"uniqueID":"kt-th-s003","htmlTag":"p","fontWeight":"700","color":"#ffffff"} -->
<p class="kt-adv-heading-s003 wp-block-kadence-advancedheading">Department</p>
<!-- /wp:kadence/advancedheading -->
</th>
<!-- /wp:kadence/table-data -->
<!-- wp:kadence/table-data {"uniqueID":"kt-data-s004","column":3} -->
<th class="kb-table-data kb-table-data-kt-data-s004">
<!-- wp:kadence/advancedheading {"uniqueID":"kt-th-s004","htmlTag":"p","fontWeight":"700","color":"#ffffff"} -->
<p class="kt-adv-heading-s004 wp-block-kadence-advancedheading">Status</p>
<!-- /wp:kadence/advancedheading -->
</th>
<!-- /wp:kadence/table-data -->
</tr>
<!-- /wp:kadence/table-row -->

<!-- wp:kadence/table-row {"uniqueID":"kt-row-002b","row":1} -->
<tr class="kb-table-row kb-table-row-kt-row-002b">
<!-- wp:kadence/table-data {"uniqueID":"kt-data-d001","column":0} -->
<td class="kb-table-data kb-table-data-kt-data-d001">
<!-- wp:kadence/advancedheading {"uniqueID":"kt-td-d001","htmlTag":"p","color":"palette3"} -->
<p class="kt-adv-heading-d001 wp-block-kadence-advancedheading">John Smith</p>
<!-- /wp:kadence/advancedheading -->
</td>
<!-- /wp:kadence/table-data -->
<!-- wp:kadence/table-data {"uniqueID":"kt-data-d002","column":1} -->
<td class="kb-table-data kb-table-data-kt-data-d002">
<!-- wp:kadence/advancedheading {"uniqueID":"kt-td-d002","htmlTag":"p","color":"palette4"} -->
<p class="kt-adv-heading-d002 wp-block-kadence-advancedheading">Developer</p>
<!-- /wp:kadence/advancedheading -->
</td>
<!-- /wp:kadence/table-data -->
<!-- wp:kadence/table-data {"uniqueID":"kt-data-d003","column":2} -->
<td class="kb-table-data kb-table-data-kt-data-d003">
<!-- wp:kadence/advancedheading {"uniqueID":"kt-td-d003","htmlTag":"p","color":"palette4"} -->
<p class="kt-adv-heading-d003 wp-block-kadence-advancedheading">Engineering</p>
<!-- /wp:kadence/advancedheading -->
</td>
<!-- /wp:kadence/table-data -->
<!-- wp:kadence/table-data {"uniqueID":"kt-data-d004","column":3} -->
<td class="kb-table-data kb-table-data-kt-data-d004">
<!-- wp:kadence/advancedheading {"uniqueID":"kt-td-d004","htmlTag":"p","color":"palette2"} -->
<p class="kt-adv-heading-d004 wp-block-kadence-advancedheading">Active</p>
<!-- /wp:kadence/advancedheading -->
</td>
<!-- /wp:kadence/table-data -->
</tr>
<!-- /wp:kadence/table-row -->

<!-- wp:kadence/table-row {"uniqueID":"kt-row-002c","row":2} -->
<tr class="kb-table-row kb-table-row-kt-row-002c">
<!-- wp:kadence/table-data {"uniqueID":"kt-data-d005","column":0} -->
<td class="kb-table-data kb-table-data-kt-data-d005">
<!-- wp:kadence/advancedheading {"uniqueID":"kt-td-d005","htmlTag":"p","color":"palette3"} -->
<p class="kt-adv-heading-d005 wp-block-kadence-advancedheading">Jane Doe</p>
<!-- /wp:kadence/advancedheading -->
</td>
<!-- /wp:kadence/table-data -->
<!-- wp:kadence/table-data {"uniqueID":"kt-data-d006","column":1} -->
<td class="kb-table-data kb-table-data-kt-data-d006">
<!-- wp:kadence/advancedheading {"uniqueID":"kt-td-d006","htmlTag":"p","color":"palette4"} -->
<p class="kt-adv-heading-d006 wp-block-kadence-advancedheading">Designer</p>
<!-- /wp:kadence/advancedheading -->
</td>
<!-- /wp:kadence/table-data -->
<!-- wp:kadence/table-data {"uniqueID":"kt-data-d007","column":2} -->
<td class="kb-table-data kb-table-data-kt-data-d007">
<!-- wp:kadence/advancedheading {"uniqueID":"kt-td-d007","htmlTag":"p","color":"palette4"} -->
<p class="kt-adv-heading-d007 wp-block-kadence-advancedheading">Creative</p>
<!-- /wp:kadence/advancedheading -->
</td>
<!-- /wp:kadence/table-data -->
<!-- wp:kadence/table-data {"uniqueID":"kt-data-d008","column":3} -->
<td class="kb-table-data kb-table-data-kt-data-d008">
<!-- wp:kadence/advancedheading {"uniqueID":"kt-td-d008","htmlTag":"p","color":"palette2"} -->
<p class="kt-adv-heading-d008 wp-block-kadence-advancedheading">Active</p>
<!-- /wp:kadence/advancedheading -->
</td>
<!-- /wp:kadence/table-data -->
</tr>
<!-- /wp:kadence/table-row -->

</tbody>
</table></figure>
<!-- /wp:kadence/table -->
```

### Pattern 3: Feature Comparison Table with Icons

Comparison table using icons for visual checkmarks.

```html
<!-- wp:kadence/table {"uniqueID":"kt-table-003","columns":4,"isFirstRowHeader":true,"isFirstColumnHeader":true,"cellPadding":["sm","md","sm","md"],"headerAlign":"center","textAlign":"center","borderStyle":[{"top":["palette7","solid","1"],"right":["palette7","solid","1"],"bottom":["palette7","solid","1"],"left":["palette7","solid","1"],"unit":"px"}],"headerTypography":[{"size":["16","15","14"],"weight":"600","color":"palette3","background":"palette9","padding":["md","md","md","md"]}]} -->
<figure class="wp-block-kadence-table kb-table-container-kt-table-003"><table class="kb-table kb-table-kt-table-003">
<tbody>

<!-- wp:kadence/table-row {"uniqueID":"kt-row-cmp-001","row":0} -->
<tr class="kb-table-row kb-table-row-kt-row-cmp-001">
<!-- wp:kadence/table-data {"uniqueID":"kt-cmp-001a","column":0} -->
<th class="kb-table-data kb-table-data-kt-cmp-001a">
<!-- wp:kadence/advancedheading {"uniqueID":"kt-cmp-h001","htmlTag":"p","fontWeight":"600"} -->
<p class="kt-adv-heading-cmp-h001 wp-block-kadence-advancedheading">Features</p>
<!-- /wp:kadence/advancedheading -->
</th>
<!-- /wp:kadence/table-data -->
<!-- wp:kadence/table-data {"uniqueID":"kt-cmp-001b","column":1} -->
<th class="kb-table-data kb-table-data-kt-cmp-001b">
<!-- wp:kadence/advancedheading {"uniqueID":"kt-cmp-h002","htmlTag":"p","fontWeight":"600","align":"center"} -->
<p class="kt-adv-heading-cmp-h002 wp-block-kadence-advancedheading">Starter</p>
<!-- /wp:kadence/advancedheading -->
</th>
<!-- /wp:kadence/table-data -->
<!-- wp:kadence/table-data {"uniqueID":"kt-cmp-001c","column":2} -->
<th class="kb-table-data kb-table-data-kt-cmp-001c">
<!-- wp:kadence/advancedheading {"uniqueID":"kt-cmp-h003","htmlTag":"p","fontWeight":"600","align":"center"} -->
<p class="kt-adv-heading-cmp-h003 wp-block-kadence-advancedheading">Professional</p>
<!-- /wp:kadence/advancedheading -->
</th>
<!-- /wp:kadence/table-data -->
<!-- wp:kadence/table-data {"uniqueID":"kt-cmp-001d","column":3} -->
<th class="kb-table-data kb-table-data-kt-cmp-001d">
<!-- wp:kadence/advancedheading {"uniqueID":"kt-cmp-h004","htmlTag":"p","fontWeight":"600","align":"center"} -->
<p class="kt-adv-heading-cmp-h004 wp-block-kadence-advancedheading">Enterprise</p>
<!-- /wp:kadence/advancedheading -->
</th>
<!-- /wp:kadence/table-data -->
</tr>
<!-- /wp:kadence/table-row -->

<!-- wp:kadence/table-row {"uniqueID":"kt-row-cmp-002","row":1} -->
<tr class="kb-table-row kb-table-row-kt-row-cmp-002">
<!-- wp:kadence/table-data {"uniqueID":"kt-cmp-002a","column":0} -->
<th class="kb-table-data kb-table-data-kt-cmp-002a">
<!-- wp:kadence/advancedheading {"uniqueID":"kt-cmp-f001","htmlTag":"p","color":"palette3"} -->
<p class="kt-adv-heading-cmp-f001 wp-block-kadence-advancedheading">Email Support</p>
<!-- /wp:kadence/advancedheading -->
</th>
<!-- /wp:kadence/table-data -->
<!-- wp:kadence/table-data {"uniqueID":"kt-cmp-002b","column":1} -->
<td class="kb-table-data kb-table-data-kt-cmp-002b">
<!-- wp:kadence/icon {"icons":[{"icon":"fe_check","size":20,"color":"palette2"}],"uniqueID":"kt-icon-cmp001","textAlignment":"center"} -->
<div class="wp-block-kadence-icon kt-svg-icons kt-svg-icons-cmp001 aligncenter"><div class="kt-svg-style-default kt-svg-icon-wrap kt-svg-item-0"><span class="kt-svg-icon kt-svg-icon-fe_check"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"></polyline></svg></span></div></div>
<!-- /wp:kadence/icon -->
</td>
<!-- /wp:kadence/table-data -->
<!-- wp:kadence/table-data {"uniqueID":"kt-cmp-002c","column":2} -->
<td class="kb-table-data kb-table-data-kt-cmp-002c">
<!-- wp:kadence/icon {"icons":[{"icon":"fe_check","size":20,"color":"palette2"}],"uniqueID":"kt-icon-cmp002","textAlignment":"center"} -->
<div class="wp-block-kadence-icon kt-svg-icons kt-svg-icons-cmp002 aligncenter"><div class="kt-svg-style-default kt-svg-icon-wrap kt-svg-item-0"><span class="kt-svg-icon kt-svg-icon-fe_check"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"></polyline></svg></span></div></div>
<!-- /wp:kadence/icon -->
</td>
<!-- /wp:kadence/table-data -->
<!-- wp:kadence/table-data {"uniqueID":"kt-cmp-002d","column":3} -->
<td class="kb-table-data kb-table-data-kt-cmp-002d">
<!-- wp:kadence/icon {"icons":[{"icon":"fe_check","size":20,"color":"palette2"}],"uniqueID":"kt-icon-cmp003","textAlignment":"center"} -->
<div class="wp-block-kadence-icon kt-svg-icons kt-svg-icons-cmp003 aligncenter"><div class="kt-svg-style-default kt-svg-icon-wrap kt-svg-item-0"><span class="kt-svg-icon kt-svg-icon-fe_check"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"></polyline></svg></span></div></div>
<!-- /wp:kadence/icon -->
</td>
<!-- /wp:kadence/table-data -->
</tr>
<!-- /wp:kadence/table-row -->

<!-- wp:kadence/table-row {"uniqueID":"kt-row-cmp-003","row":2} -->
<tr class="kb-table-row kb-table-row-kt-row-cmp-003">
<!-- wp:kadence/table-data {"uniqueID":"kt-cmp-003a","column":0} -->
<th class="kb-table-data kb-table-data-kt-cmp-003a">
<!-- wp:kadence/advancedheading {"uniqueID":"kt-cmp-f002","htmlTag":"p","color":"palette3"} -->
<p class="kt-adv-heading-cmp-f002 wp-block-kadence-advancedheading">Priority Support</p>
<!-- /wp:kadence/advancedheading -->
</th>
<!-- /wp:kadence/table-data -->
<!-- wp:kadence/table-data {"uniqueID":"kt-cmp-003b","column":1} -->
<td class="kb-table-data kb-table-data-kt-cmp-003b">
<!-- wp:kadence/icon {"icons":[{"icon":"fe_x","size":20,"color":"palette7"}],"uniqueID":"kt-icon-cmp004","textAlignment":"center"} -->
<div class="wp-block-kadence-icon kt-svg-icons kt-svg-icons-cmp004 aligncenter"><div class="kt-svg-style-default kt-svg-icon-wrap kt-svg-item-0"><span class="kt-svg-icon kt-svg-icon-fe_x"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="18" y1="6" x2="6" y2="18"></line><line x1="6" y1="6" x2="18" y2="18"></line></svg></span></div></div>
<!-- /wp:kadence/icon -->
</td>
<!-- /wp:kadence/table-data -->
<!-- wp:kadence/table-data {"uniqueID":"kt-cmp-003c","column":2} -->
<td class="kb-table-data kb-table-data-kt-cmp-003c">
<!-- wp:kadence/icon {"icons":[{"icon":"fe_check","size":20,"color":"palette2"}],"uniqueID":"kt-icon-cmp005","textAlignment":"center"} -->
<div class="wp-block-kadence-icon kt-svg-icons kt-svg-icons-cmp005 aligncenter"><div class="kt-svg-style-default kt-svg-icon-wrap kt-svg-item-0"><span class="kt-svg-icon kt-svg-icon-fe_check"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"></polyline></svg></span></div></div>
<!-- /wp:kadence/icon -->
</td>
<!-- /wp:kadence/table-data -->
<!-- wp:kadence/table-data {"uniqueID":"kt-cmp-003d","column":3} -->
<td class="kb-table-data kb-table-data-kt-cmp-003d">
<!-- wp:kadence/icon {"icons":[{"icon":"fe_check","size":20,"color":"palette2"}],"uniqueID":"kt-icon-cmp006","textAlignment":"center"} -->
<div class="wp-block-kadence-icon kt-svg-icons kt-svg-icons-cmp006 aligncenter"><div class="kt-svg-style-default kt-svg-icon-wrap kt-svg-item-0"><span class="kt-svg-icon kt-svg-icon-fe_check"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"></polyline></svg></span></div></div>
<!-- /wp:kadence/icon -->
</td>
<!-- /wp:kadence/table-data -->
</tr>
<!-- /wp:kadence/table-row -->

<!-- wp:kadence/table-row {"uniqueID":"kt-row-cmp-004","row":3} -->
<tr class="kb-table-row kb-table-row-kt-row-cmp-004">
<!-- wp:kadence/table-data {"uniqueID":"kt-cmp-004a","column":0} -->
<th class="kb-table-data kb-table-data-kt-cmp-004a">
<!-- wp:kadence/advancedheading {"uniqueID":"kt-cmp-f003","htmlTag":"p","color":"palette3"} -->
<p class="kt-adv-heading-cmp-f003 wp-block-kadence-advancedheading">Dedicated Manager</p>
<!-- /wp:kadence/advancedheading -->
</th>
<!-- /wp:kadence/table-data -->
<!-- wp:kadence/table-data {"uniqueID":"kt-cmp-004b","column":1} -->
<td class="kb-table-data kb-table-data-kt-cmp-004b">
<!-- wp:kadence/icon {"icons":[{"icon":"fe_x","size":20,"color":"palette7"}],"uniqueID":"kt-icon-cmp007","textAlignment":"center"} -->
<div class="wp-block-kadence-icon kt-svg-icons kt-svg-icons-cmp007 aligncenter"><div class="kt-svg-style-default kt-svg-icon-wrap kt-svg-item-0"><span class="kt-svg-icon kt-svg-icon-fe_x"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="18" y1="6" x2="6" y2="18"></line><line x1="6" y1="6" x2="18" y2="18"></line></svg></span></div></div>
<!-- /wp:kadence/icon -->
</td>
<!-- /wp:kadence/table-data -->
<!-- wp:kadence/table-data {"uniqueID":"kt-cmp-004c","column":2} -->
<td class="kb-table-data kb-table-data-kt-cmp-004c">
<!-- wp:kadence/icon {"icons":[{"icon":"fe_x","size":20,"color":"palette7"}],"uniqueID":"kt-icon-cmp008","textAlignment":"center"} -->
<div class="wp-block-kadence-icon kt-svg-icons kt-svg-icons-cmp008 aligncenter"><div class="kt-svg-style-default kt-svg-icon-wrap kt-svg-item-0"><span class="kt-svg-icon kt-svg-icon-fe_x"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="18" y1="6" x2="6" y2="18"></line><line x1="6" y1="6" x2="18" y2="18"></line></svg></span></div></div>
<!-- /wp:kadence/icon -->
</td>
<!-- /wp:kadence/table-data -->
<!-- wp:kadence/table-data {"uniqueID":"kt-cmp-004d","column":3} -->
<td class="kb-table-data kb-table-data-kt-cmp-004d">
<!-- wp:kadence/icon {"icons":[{"icon":"fe_check","size":20,"color":"palette2"}],"uniqueID":"kt-icon-cmp009","textAlignment":"center"} -->
<div class="wp-block-kadence-icon kt-svg-icons kt-svg-icons-cmp009 aligncenter"><div class="kt-svg-style-default kt-svg-icon-wrap kt-svg-item-0"><span class="kt-svg-icon kt-svg-icon-fe_check"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"></polyline></svg></span></div></div>
<!-- /wp:kadence/icon -->
</td>
<!-- /wp:kadence/table-data -->
</tr>
<!-- /wp:kadence/table-row -->

</tbody>
</table></figure>
<!-- /wp:kadence/table -->
```

## Table Attribute Reference

### Main Table Block (`kadence/table`)

```json
{
  "uniqueID": "kt-table-xxx",
  "columns": 3,
  "isFirstRowHeader": true,
  "isFirstColumnHeader": false,
  "evenOddBackground": false,
  "backgroundColorEven": "palette9",
  "backgroundColorOdd": "#ffffff",
  "backgroundHoverColorEven": "palette8",
  "backgroundHoverColorOdd": "palette8",
  "cellPadding": ["sm","sm","sm","sm"],
  "tabletCellPadding": ["xs","xs","xs","xs"],
  "mobileCellPadding": ["xxs","xxs","xxs","xxs"],
  "headerAlign": "center",
  "textAlign": "left",
  "borderStyle": [{
    "top": ["palette7","solid","1"],
    "right": ["palette7","solid","1"],
    "bottom": ["palette7","solid","1"],
    "left": ["palette7","solid","1"],
    "unit": "px"
  }],
  "borderOnRowOnly": false,
  "overflowXScroll": false,
  "maxWidth": ["100","",""],
  "maxWidthUnit": "%"
}
```

### Table Row Block (`kadence/table-row`)

```json
{
  "uniqueID": "kt-row-xxx",
  "row": 0,
  "backgroundColor": "",
  "backgroundHoverColor": "",
  "minHeight": ""
}
```

### Table Data Block (`kadence/table-data`)

```json
{
  "uniqueID": "kt-data-xxx",
  "column": 0,
  "padding": ["","","",""]
}
```

## Cell Content Types

Cells can contain any Kadence block:

| Content | Block | Use Case |
|---------|-------|----------|
| Text | `kadence/advancedheading` | Headers, data values |
| Icons | `kadence/icon` | Status indicators, checkmarks |
| Buttons | `kadence/singlebtn` | Action links |
| Images | `kadence/image` | Product photos, logos |

## Common Icon Patterns for Tables

| Status | Icon | Color |
|--------|------|-------|
| Yes/Available | `fe_check` | `palette2` (green) |
| No/Unavailable | `fe_x` | `palette7` (gray) |
| Partial | `fe_minus` | `palette5` (yellow) |
| Info | `fe_info` | `palette1` (blue) |

## Border Style Format

Border arrays use format: `[color, style, width]`

```json
"borderStyle": [{
  "top": ["#e2e8f0", "solid", "1"],
  "right": ["#e2e8f0", "solid", "1"],
  "bottom": ["#e2e8f0", "solid", "1"],
  "left": ["#e2e8f0", "solid", "1"],
  "unit": "px"
}]
```

Available border styles: `solid`, `dashed`, `dotted`, `double`, `none`

## Best Practices

1. **Accessibility**: Use `isFirstRowHeader` for semantic headers
2. **Responsive**: Tables scroll horizontally on mobile with `overflowXScroll`
3. **Readability**: Use striped backgrounds for long tables
4. **Alignment**: Center icons/checkmarks, left-align text
5. **Padding**: Use consistent cell padding throughout
6. **Borders**: Subtle borders improve visual scanning
7. **Typography**: Bold headers, lighter data cells
