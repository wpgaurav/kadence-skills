# Kadence Blocks Skills

LLM-optimized skill documentation for creating WordPress Gutenberg templates with Kadence Blocks. Enables AI assistants to generate production-ready block markup.

## Documentation Files

| File | Purpose |
|------|---------|
| `SKILL.md` | Core block reference, attributes, and markup format |
| `kadence-hero.md` | Hero/welcome section templates |
| `kadence-features.md` | Feature grids and info box layouts |
| `kadence-testimonials.md` | Testimonial sections and carousels |
| `kadence-cta.md` | Call-to-action sections |
| `kadence-table.md` | Data tables and comparison tables |
| `kadence-forms.md` | Contact forms and advanced form fields |
| `kadence-snippets.md` | Reusable block snippets |

## Usage

### Claude Code (CLI)

Open the folder and run `claude`. The `CLAUDE.md` file provides automatic context.

```bash
cd kadence-skills
claude
```

### VS Code Extensions (Cline, Roo, etc.)

Open the folder in VS Code. Keep skill files open as tabs for reference.

### Web-based AI (Claude, ChatGPT, Gemini)

Copy the content from `SKILL.md` and paste into your chat. Add section-specific files as needed.

### AI IDEs (Cursor, Windsurf)

Open the folder. The IDE reads `CLAUDE.md` for context automatically.

## Output Format

Templates output as WordPress Gutenberg block markup:

```html
<!-- wp:kadence/rowlayout {"uniqueID":"kt-layout-abc123","columns":2} -->
<div class="wp-block-kadence-rowlayout alignnone kt-row-layout-inner kt-layout-id-abc123">
  <div class="kt-row-column-wrap kt-has-2-columns">
    <!-- wp:kadence/column {"id":1,"uniqueID":"kt-col-def456"} -->
    <div class="wp-block-kadence-column kadence-column-abc123">
      <div class="kt-inside-inner-col">
        <!-- Content blocks -->
      </div>
    </div>
    <!-- /wp:kadence/column -->
  </div>
</div>
<!-- /wp:kadence/rowlayout -->
```

Paste directly into the WordPress Block Editor.

## Responsive Breakpoints

Kadence uses 3-value arrays for responsive values: `[desktop, tablet, mobile]`

```json
"padding": [40, 30, 20]
"fontSize": [48, 36, 28]
"columns": [3, 2, 1]
```

## Core Blocks

**Layout**: `kadence/rowlayout`, `kadence/column`

**Content**: `kadence/advancedheading`, `kadence/advancedbtn`, `kadence/singlebtn`, `kadence/infobox`, `kadence/iconlist`, `kadence/icon`, `kadence/image`, `kadence/spacer`

**Complex**: `kadence/accordion`, `kadence/tabs`, `kadence/testimonials`, `kadence/posts`, `kadence/countdown`, `kadence/countup`, `kadence/table`, `kadence/advanced-form`

## License

MIT for documentation. Kadence Blocks is a separate product by Kadence WP.
