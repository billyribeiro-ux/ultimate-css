# CSS Platform Coverage Audit — June 9, 2026

**Scope:** every module, every lesson (298 lessons + 12 challenges across 28 modules), audited end-to-end against the complete CSS platform as shipped through June 9, 2026.
**Method:** full inventory of every lesson's headings and topics, cross-referenced against a master checklist built from the CSS specifications, Interop 2024–2026 focus areas, and the browser release notes through June 2026.
**Result:** 16 coverage gaps found and closed with 16 new full lessons. All module TOCs, lesson navigation, home-page counts, and the browser support matrix updated. Stale lesson counts corrected.

---

## 1. Verdict by domain

| Domain | Verdict | Where |
|---|---|---|
| Cascade, specificity, `!important`, source order | Complete | M1 |
| `@layer` (order, sub-layers, imports, frameworks) | Complete | M2, M3, M13.21, M22.6 |
| Design tokens, OKLCH, `@property`, `light-dark()` | Complete | M4, M6.7 |
| Resets and base styles | Complete | M5, M6 |
| Typography (fluid, tokens, `text-wrap`, `text-box-trim`) | Complete | M4.5, M6, M13.14, M21.1 |
| **Variable fonts, OpenType features, color fonts** | **Gap → closed** | **M6.9 (new)** |
| **International typography (CJK, ruby, `initial-letter`)** | **Gap → closed** | **M6.10 (new)** |
| Layout primitives, container/style queries | Complete | M7, M21.4 |
| **Multi-column layout** | **Gap → closed** | **M7.9 (new)** |
| Grid (full), subgrid, masonry/grid-lanes | Complete | M26, M7.8, M13.15 |
| Flexbox (full) | Complete | M27 |
| `@scope`, `:has()`, anchor positioning, base-select | Complete | M8, M28 |
| Scroll-driven animations, view transitions, `@starting-style` | Complete | M9, M13.8 |
| **Motion paths (`offset-path`, `ray()`)** | **Gap → closed** | **M9.9 (new)** |
| **`animation-composition`, individual transforms, `allow-discrete`** | **Gap → closed** | **M9.10 (new)** |
| Logic functions (`if()`, `@function`, typed `attr()`) | Complete | M10 |
| Math: `round()`, `mod()`, `rem()`, `sign()`, `abs()` + `round()`+`clamp()` | Complete | M13.4, M21.15 |
| **Trigonometric & exponential math (`sin()`…`pow()`)** | **Gap → closed** | **M10.7 (new)** |
| No-JS UI patterns (popover, details, carousels) | Complete | M11 |
| Color (relative color, `color-mix()`, P3, `contrast-color()`) | Complete | M13 |
| **`corner-shape` / `superellipse()` squircles** | **Gap → closed** | **M13.22 (new)** |
| **`shape()` responsive clip paths** | **Gap → closed** | **M13.23 (new)** |
| **Gap decorations (grid/flex `column-rule`/`row-rule`)** | **Gap → closed** | **M13.24 (new)** |
| **Houdini Paint API & Typed OM** | **Gap → closed** | **M13.25 (new)** |
| Industry patterns (Apple, MD3, Fluent, Stripe…) | Complete | M14 |
| Filters, gradients, 3D, glassmorphism | Complete | M14, M15 |
| **Blend modes (`mix-blend-mode`, `isolation`)** | **Gap → closed** | **M15.16 (new)** |
| **Masking (`mask-image`, `mask-composite`)** | **Gap → closed** | **M15.17 (new)** |
| Real-world layouts, micro-interactions, CSS art | Complete | M16–M18 |
| Accessibility (focus, contrast, forced-colors, ARIA) | Complete | M19 |
| **Complete preference media queries (`prefers-contrast`, `update`, `scripting`, `display-mode`…)** | **Gap → closed** | **M19.12 (new)** |
| Performance (pipeline, containment, critical CSS, CSS-vs-JS animation) | Complete | M20 |
| Responsive (fluid everything, viewport units, foldables) | Complete | M21 |
| **The scroll surface (`scrollbar-gutter`, `overscroll-behavior`, `scroll-padding`, `overflow: clip`)** | **Gap → closed** | **M21.16 (new)** |
| CSS at scale (naming, governance, testing, linting) | Complete | M22 |
| **Web component styling (`::part()`, `::slotted()`, `:state()`, `adoptedStyleSheets`)** | **Gap → closed** | **M22.10 (new)** |
| Print & email CSS | Complete | M23 |
| Custom properties (space toggle, IACVT, state machines) | Complete | M25 |
| Selectors (every family, `nth` formulas, 20 `:has()` patterns) | Complete | M28 |
| **Highlight pseudos & Custom Highlight API (`::highlight()`, `::target-text`)** | **Gap → closed** | **M28.11 (new)** |

## 2. The 16 new lessons

| # | Lesson | Tier |
|---|---|---|
| 1 | 6.9 — Variable Fonts, Font Features & Color Fonts | Production |
| 2 | 6.10 — International Typography: CJK, Ruby & Text Polish | Mixed (gated) |
| 3 | 7.9 — The Columns Primitive: CSS Multi-Column | Production |
| 4 | 9.9 — Motion Paths: offset-path, ray() & Orbital Animation | Production |
| 5 | 9.10 — animation-composition, Individual Transforms & Discrete Transitions | Production |
| 6 | 10.7 — Trigonometry & Advanced Math: sin(), cos(), atan2() & pow() | Production |
| 7 | 13.22 — corner-shape & superellipse(): Native Squircles | Progressive |
| 8 | 13.23 — shape(): Responsive Curved Clip Paths | Progressive |
| 9 | 13.24 — Gap Decorations: Rules Between Grid & Flex Tracks | Beta (Jun 2026) |
| 10 | 13.25 — CSS Houdini: The Paint API & Typed OM | Experimental |
| 11 | 15.16 — Blend Modes: mix-blend-mode, background-blend-mode & isolation | Production |
| 12 | 15.17 — CSS Masking Mastery: mask-image, mask-composite & Gradient Masks | Production |
| 13 | 19.12 — Every User Preference: The Complete Media Query Set | Mixed (gated) |
| 14 | 21.16 — The Scroll Surface: Scrollbars, Overscroll & Scroll Margins | Mixed (gated) |
| 15 | 22.10 — Styling Web Components: ::part(), ::slotted() & :state() | Production |
| 16 | 28.11 — Highlight Pseudo-Elements & the Custom Highlight API | Production |

Every new lesson follows the house format: problem-first explanation, precise mechanics, production guidance with explicit support tier, live demo, interactive editor, and a mini-exercise.

## 3. Corrections made during the audit

- **Stale lesson counts** on the course home page fixed: Module 14 said "25 lessons" (has 28), Module 22 said "8 lessons" (had 9, now 10). All updated counts now match the actual files.
- **COURSE.md architecture block** listed only modules 1–24; modules 25–28 added. Totals updated to 310 (298 lessons + 12 challenges).
- **Dates refreshed** across the home page (meta description, hero, support-matrix heading, footer): May 29, 2026 → June 9, 2026.
- **Browser support matrix extended** with 12 rows: trigonometric/exponential functions, individual transforms, `animation-composition`, motion paths, a new "Shapes & visual effects" section (masking, blend modes, `corner-shape`, `shape()`, Houdini Paint), `font-palette`, `text-spacing-trim`, `initial-letter`, `::highlight()`, `:state()`, and scrollbar styling.

## 4. Deliberate exclusions (audited, judged out of scope)

- **SVG presentation attributes & SMIL** — SVG-specific authoring; CSS-side styling of SVG (`fill`, `stroke`, `currentColor`) is covered as an aside in 15.17.
- **MathML styling** — niche; no mainstream production demand.
- **Non-CSS platform APIs** (speculation rules, web animations JS API details beyond 20.11, `CustomStateSet` JS internals beyond what 22.10 needs) — JS-platform topics; touched only where CSS meets them.
- **Deprecated/removed syntax** (`@scroll-timeline` block syntax, `-webkit-mask` longhand teaching, CSS toggles proposal) — never shipped or superseded; noted inline where students may meet them in legacy code.

## 5. Maintenance protocol

Re-run this audit when a new Chrome/Firefox/Safari stable release ships features at Baseline. The procedure: (1) regenerate the lesson inventory (`grep` h1/h2 across `module-*/lesson-*.html`), (2) diff against the release notes, (3) add lessons to the thematically correct module, (4) update the matrix, counts, and this file.
