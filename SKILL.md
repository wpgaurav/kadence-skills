# Kadence Blocks Template Creation Skill

**Activation**: Use when creating WordPress Gutenberg templates using Kadence Blocks. Triggers: "kadence template", "kadence section", "kadence blocks", "create a hero section", "landing page with Kadence", etc.

## Overview

This skill enables creation of production-ready Kadence Blocks templates for WordPress. Templates are output as WordPress Gutenberg block markup that can be directly pasted into the Block Editor.

## Block Markup Format

WordPress blocks are serialized as HTML comments with JSON attributes:

```html
<!-- wp:kadence/rowlayout {"uniqueID":"kt-layout-abc123","columns":2,"colLayout":"equal"} -->
<div class="wp-block-kadence-rowlayout alignnone kt-row-layout-inner kt-layout-id-abc123">
  <div class="kt-row-column-wrap kt-has-2-columns">
    <!-- wp:kadence/column {"id":1,"uniqueID":"kt-col-def456"} -->
    <div class="wp-block-kadence-column kadence-column-abc123"><div class="kt-inside-inner-col">
      <!-- Inner blocks here -->
    </div></div>
    <!-- /wp:kadence/column -->
  </div>
</div>
<!-- /wp:kadence/rowlayout -->
```

## Core Blocks Reference

### Layout Blocks
| Block | Name | Purpose |
|-------|------|---------|
| `kadence/rowlayout` | Row Layout | Container with columns (1-6 columns) |
| `kadence/column` | Section | Column within Row Layout |

### Content Blocks
| Block | Name | Purpose |
|-------|------|---------|
| `kadence/advancedheading` | Advanced Text | Headings and paragraphs with full styling |
| `kadence/advancedbtn` | Advanced Button | Button container (holds singlebtn blocks) |
| `kadence/singlebtn` | Single Button | Individual button with link/styling |
| `kadence/infobox` | Info Box | Icon/image + title + description card |
| `kadence/iconlist` | Icon List | Bulleted list with custom icons |
| `kadence/icon` | Icon | Standalone icon(s) |
| `kadence/image` | Advanced Image | Image with advanced controls |
| `kadence/spacer` | Spacer/Divider | Vertical spacing |

### Complex Blocks
| Block | Name | Purpose |
|-------|------|---------|
| `kadence/accordion` | Accordion | Collapsible FAQ/content panels |
| `kadence/tabs` | Tabs | Tabbed content sections |
| `kadence/testimonials` | Testimonials | Testimonial grid/carousel |
| `kadence/posts` | Posts | Dynamic post grid |
| `kadence/countdown` | Countdown | Timer countdown |
| `kadence/countup` | Count Up | Animated number counter |
| `kadence/table` | Table (Adv) | Data tables with rows/cells |
| `kadence/advanced-form` | Advanced Form | Contact forms with field types |

## Essential Attributes

### uniqueID Pattern
Every block needs a unique ID. Generate as: `kt-{block-short}-{random-alphanumeric-6}`

Examples:
- Row Layout: `kt-layout-abc123`
- Column: `kt-col-def456`
- Heading: `kt-adv-heading-ghi789`
- Button: `kt-btn-jkl012`

### Responsive Arrays
Many attributes use 3-value arrays: `[desktop, tablet, mobile]`

```json
"padding": [40, 30, 20]        // 40px desktop, 30px tablet, 20px mobile
"fontSize": [48, 36, 28]       // Font sizes per device
"columns": [3, 2, 1]           // 3 cols desktop, 2 tablet, 1 mobile
```

### Color System
Use palette references for theme consistency:
- `palette1` through `palette9` - Theme palette colors
- Direct hex values: `#1a1a1a`
- CSS variables: `var(--global-palette1)`

### Spacing Presets
Kadence uses size presets:
- `xxs`, `xs`, `sm`, `md`, `lg`, `xl`, `xxl`
- Or numeric values in px

## Column Layouts

### colLayout Values (kadence/rowlayout)
| Value | Description |
|-------|-------------|
| `equal` | Equal width columns |
| `left-golden` | 2:1 ratio (left larger) |
| `right-golden` | 1:2 ratio (right larger) |
| `left-half` | 2:1:1 ratio (3 cols) |
| `right-half` | 1:1:2 ratio (3 cols) |
| `center-half` | 1:2:1 ratio (3 cols) |
| `center-wide` | 1:3:1 ratio (3 cols) |
| `row` | Stack vertically |
| `first-row` | First column full width |
| `last-row` | Last column full width |

## Common Icon Names

Icons use prefix `fe_` (Feather icons) or `fas_` (Font Awesome solid):

**Feather (Line)**: `fe_check`, `fe_checkCircle`, `fe_arrowRight`, `fe_star`, `fe_heart`, `fe_mail`, `fe_phone`, `fe_mapPin`, `fe_clock`, `fe_user`, `fe_shield`, `fe_zap`, `fe_award`, `fe_target`, `fe_trending-up`

**Font Awesome**: `fas_check`, `fas_star`, `fas_heart`, `fas_rocket`, `fas_bolt`, `fas_gem`, `fas_crown`

## Template Creation Process

1. **Determine section type** - Hero, features, testimonials, CTA, etc.
2. **Plan column structure** - How many columns? Responsive behavior?
3. **Generate unique IDs** - Create IDs for all blocks
4. **Build from outside in** - rowlayout → column → content blocks
5. **Add responsive values** - Ensure tablet/mobile work well
6. **Test markup validity** - Proper opening/closing tags

## Output Format

Output clean block markup that can be directly pasted into WordPress Block Editor:

```html
<!-- wp:kadence/rowlayout {...} -->
...
<!-- /wp:kadence/rowlayout -->
```

**Important**: Do NOT include extra comments like `<!-- SECTION: Name -->` as they interfere with block parsing.

## Related Skills

For specific section types, see:
- `kadence-hero.md` - Hero/welcome sections
- `kadence-features.md` - Feature grids and info boxes
- `kadence-testimonials.md` - Testimonial sections
- `kadence-cta.md` - Call-to-action sections
- `kadence-table.md` - Advanced data tables and comparison tables
- `kadence-forms.md` - Contact forms, surveys, and advanced forms
- `kadence-snippets.md` - Reusable block snippets

## Quality Checklist

- [ ] All blocks have unique IDs
- [ ] Responsive values set appropriately
- [ ] Proper nesting (rowlayout → column → content)
- [ ] Opening and closing tags match
- [ ] Colors use palette or consistent hex values
- [ ] Spacing is consistent across sections
- [ ] Mobile layout makes sense (columns stack properly)
