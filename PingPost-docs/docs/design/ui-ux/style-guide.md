### UI/UX Style Guide

This guide defines PingPost’s look and feel to keep the interface cohesive and accessible.

#### Theme and colors

- Mode: Dark theme.
- Palette (from `theme.css`):
  - Background: `--pp-bg: #140a14`
  - Surfaces: `--pp-surface: #1e0f1f`, `--pp-surface-2: #2a1830`
  - Text: `--pp-text: #f4f1f6`, Dim text: `--pp-text-dim: #c8bfd0`
  - Accent: `--pp-accent: #7d2b58`, `--pp-accent-2: #9c3b6d`
  - Status: `--pp-danger: #e05252`, `--pp-success: #2bb673`
  - Radius: `--pp-radius: 16px`, Shadow: `--pp-shadow` soft

Usage:

- Backgrounds use `--pp-bg` with subtle radial glows.
- Cards use `--pp-surface`; emphasized elements (composer) use `--pp-surface-2`.
- Primary actions use accent colors; destructive actions use danger.

#### Typography

- Primary font: Poppins (weights 400–700) with system fallbacks.
- Headings: bold, high contrast; `h1` ~2.25rem, `h2` ~1.5rem.
- Body: comfortable line-height; dim text for secondary content via `.pp-muted`.

#### Layout and spacing

- Base layout: `templates/layout.html` with sticky, translucent navbar.
- Page container: `.page-container` keeps content centered with ample padding.
- Grid: `.tweet-grid` uses responsive CSS Grid with `minmax(260px, 1fr)`.
- Radius and shadows: Use theme radius and shadow utilities for depth.

#### Components

- Navbar
  - Brand: `.app-brand` with circular gradient icon and product name.
  - Auth-aware actions: shows Login/Register or Home/Ping/Logout accordingly.

- Buttons
  - Primary accent: `.btn-accent` (solid accent), `.btn-outline-accent` for secondary.
  - Destructive: `.btn-danger` for delete actions.
  - Always include clear labels; avoid icon-only buttons unless accompanied by `aria-label`.

- Cards
  - Base: `.pp-card` for tweet and auth cards; consistent border, radius, and shadow.
  - Tweet card: optional image fills the top; title shows author; actions appear for owner.

- Forms and inputs
  - Auth and tweet forms live in `.auth-card` or `.form` containers.
  - Inputs are dark with clear focus rings; labels use dim text color.
  - Register page uses `.field-with-help` and `.field-help` to surface password guidance above the field.
  - Always include `{% csrf_token %}` and clear submit/cancel actions.

#### Accessibility

- Contrast: Ensure buttons and text meet WCAG AA against dark backgrounds.
- Focus: Keep visible focus rings (accent glow) for keyboard navigation.
- Semantics: Use headings, labels, and landmarks appropriately.
- Icons: Use Bootstrap Icons with descriptive `aria-label` when the icon is interactive.

#### Motion

- Subtle `fadeInUp` animation on headings and form containers; avoid excessive motion.

#### Content guidelines

- Be concise and friendly. Buttons favor verbs (e.g., “Ping”, “Login”, “Delete”).
- Error messages should be specific and next to the relevant field.

#### Examples

- Primary action button:
  - Create: `<button class="btn btn-accent rounded-pill">Ping</button>`
  - Secondary: `<a class="btn btn-outline-accent rounded-pill" href="...">Back</a>`

#### Don’ts

- Don’t introduce new colors without mapping to the palette.
- Don’t remove focus outlines; customize instead if necessary.
- Don’t use icon-only controls without accessible labels.
