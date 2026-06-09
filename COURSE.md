# CSS Cascade Architecture — PE7 Complete Course

**Stack:** HTML + CSS. Pure web platform. Zero frameworks, zero preprocessors, zero build steps.
**Standard:** Apple/Microsoft Principal Engineer ICT Level 7+ on every pattern taught.
**Philosophy:** Root-level understanding first. Syntax is the last thing we teach, not the first.

## Course architecture

```
Module 1  — The Problem: Why CSS Breaks at Scale
Module 2  — @layer Fundamentals
Module 3  — The PE7 Layer Architecture
Module 4  — @layer tokens: Design Token Systems with OKLCH
Module 5  — @layer reset: Production Reset Patterns
Module 6  — @layer base: Typography, Logic, and Dark Mode
Module 7  — @layer layout: Structural Primitives and Container Queries
Module 8  — @layer components: Scoped UI Patterns and Modern Selectors
Module 9  — @layer animations: Scroll, Motion, and Transitions
Module 10 — Modern CSS Logic and Functions
Module 11 — No-JS UI Patterns: What CSS Can Do Alone
Module 12 — Capstone: Production Page from Scratch
Module 13 — CSS in 2026: Functions, Colors, and What Just Shipped (May 2026 update)
Module 14 — Industry Patterns: Apple, Netflix, Stripe, MD3, Fluent & Beyond (PE7 Deep Dive)
Module 15 — Spectacular Effects: Pushing CSS to Its Limits (Showstopper)
Module 16 — Real-World Page Layouts: Famous Sites Rebuilt
Module 17 — Micro-Interactions: The Details That Ship Quality
Module 18 — CSS Art & Creative Experiments: Total Platform Mastery
Module 19 — CSS Accessibility: Building for Everyone
Module 20 — CSS Performance: Making It Fast
Module 21 — Advanced Responsive Design: Beyond Breakpoints
Module 22 — CSS at Scale: Architecture for Teams
Module 23 — CSS Beyond the Browser: Print & Email
Module 24 — CSS Challenges: Test Your Mastery (12 challenges)
Module 25 — CSS Custom Properties Mastery
Module 26 — CSS Grid Mastery: Every Pattern, Every Trick
Module 27 — CSS Flexbox Mastery
Module 28 — CSS Selectors: The Complete Reference
```

- **Total modules:** 28
- **Total lessons:** 310 (298 lessons + 12 challenges)
- **Total projects:** 12 (one per module) + 80 mini-exercises
- **Coverage:** the complete CSS platform as shipped through June 9, 2026 — see `AUDIT.md` for the full coverage audit
- **Open** `index.html` in the repo root to start.

## Repository layout

```
/
├── index.html                      # Course home
├── COURSE.md                       # This file
├── assets/
│   ├── css/
│   │   ├── main.css                # @layer order + imports
│   │   ├── reset.css
│   │   ├── tokens.css
│   │   ├── base.css
│   │   ├── layout.css
│   │   ├── components.css
│   │   └── animations.css
│   └── js/
│       └── editor.js               # Live HTML/CSS editor (every lesson)
├── module-01-the-problem/
├── module-02-layer-fundamentals/
├── module-03-pe7-architecture/
├── module-04-tokens/
├── module-05-reset/
├── module-06-base/
├── module-07-layout/
├── module-08-components/
├── module-09-animations/
├── module-10-modern-logic/
├── module-11-no-js-patterns/
└── module-12-capstone/
```

Each module directory contains:
- `index.html` — module overview
- One HTML file per lesson (with a live editor the learner can type into)
- A `project/` directory containing the module project deliverable

## Browser support tiers

- **Production-ready** — ship without `@supports`. All major browsers.
- **Progressive enhancement** — always wrap in `@supports`.
- **Experimental** — learn and watch; not for production.

See the browser support table on `index.html`.

## Layer order (PE7 stack)

```css
@layer reset, tokens, base, layout, components, animations;
```

Each layer's single responsibility:

| Layer | Responsibility |
|---|---|
| `reset` | Neutralize browser defaults. `:where()`-only selectors. |
| `tokens` | Design decisions as CSS custom properties. Never styles elements. |
| `base` | Element selectors only. Uses tokens. Logical properties. |
| `layout` | Structural primitives. No visual styling. |
| `components` | Named UI patterns. `@scope` + scoped custom properties. |
| `animations` | All motion. Highest priority. `prefers-reduced-motion` override. |
